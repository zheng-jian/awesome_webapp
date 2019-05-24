import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='mysql', db='awesome')

    u = User(name='Test', email='test@test.com', passwd='123456789',image='about:blank')

    await u.save()

loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()