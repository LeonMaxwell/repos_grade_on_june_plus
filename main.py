import aiohttp
import asyncio
from aiohttp import web
import requests


async def fun1():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://kanban.digital-sector.ru/api/user/", headers={"Content-Type":"text", "Authorization": "Bearer 1270|32fqt7Ba3PGHVsixBdP446atM3uyOiThOOnbugsk"}) as response:
            
            html = response.status
            return web.Response(text=str(html))



async def fun2(request):
    name = request.match_info.get('name', "Anonymous")
    return web.FileResponse('index.html')

app = web.Application()
app.add_routes([web.get('/', fun2), web.get('/next', fun1), web.get('/{name}', fun2)])
app.router.add_static("/", "./")


async def main():
    task1 = asyncio.create_task(fun1())
    task2 = asyncio.create_task(fun1())
    
    print(type(task1))
    print(type(task2.__class__.__bases__))
    
    await task1
    await task2
    
    
if __name__ == "__main__":
    
    
    asyncio.run(main())
    web.run_app(app, host="localhost", port=7000)