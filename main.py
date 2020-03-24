from aiohttp import web
from routes import setup_routes
from motor.aiohttp import AIOHTTPGridFS 
import motor.motor_asyncio
from umongo import Instance


db = motor.motor_asyncio.AsyncIOMotorClient()['test']

instance = Instance(db)

app = web.Application()
app['db'] = db
setup_routes(app)
web.run_app(app)
