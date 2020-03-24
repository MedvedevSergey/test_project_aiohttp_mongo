from aiohttp import web
from models import Product


async def add_product(request: web.Request) -> web.Response:
    data = await request.json()
    product = await Product.create(data)
    return web.json_response(product.dump(), status=201)


async def get_all_product(request: web.Request) -> web.Response:
    products = await Product.get_all()
    return web.json_response([product.dump() async for product in products], status=200)
 

async def get_by_id(request: web.Request) -> web.Response:
    data = await request.json()
    products = await Product.get_by_id(data['id'])
    response_data = [product.dump() async for product in products]
    if not response_data:
        return web.json_response({'error_message': 'Product Not Found' }, status=404)
    return web.json_response(response_data, status=200)


async def get_filtered_data(request: web.Request) -> web.Response:
    data = await request.json()
    products = await Product.filter(data)
    response_data = [product.dump() async for product in products]
    if not response_data:
        return web.json_response({'error_message': 'Products Not Found' }, status=404)
    return web.json_response(response_data, status=200)

