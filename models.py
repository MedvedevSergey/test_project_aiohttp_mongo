import motor.motor_asyncio
from umongo import Document, fields, Instance


db = motor.motor_asyncio.AsyncIOMotorClient()['test']
instance = Instance(db)

@instance.register
class Product(Document):
    # id created automatically
    title = fields.StrField(required=True)
    description = fields.StrField(required=True)
    parameters = fields.DictField(required=False)

    @staticmethod
    async def get_all():
        product = Product.find({})
        return product

    @staticmethod
    async def filter(data):
        title_filter = data.get('title')
        parameters = data.get('parameters')
        parameter_filter = {}
        if parameters is not None:
            for key, value in parameters.items():
                parameter_filter[f'parameters.{key}'] = value
            return Product.find(parameter_filter)
        elif title_filter is not None:
            return Product.find({'title': title_filter})


    @staticmethod
    async def get_by_id(product_id):
        return Product.find({'id': fields.ObjectId(product_id)})

    @staticmethod
    async def create(data):
        product = Product(**data)
        await product.commit()
        return product
