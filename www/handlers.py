from coroweb import get
import asyncio


@get('/')
async def index(*,request):
    return '<h1>Test</h1>'
