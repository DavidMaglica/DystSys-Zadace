import aiohttp
from aiohttp import web
import asyncio
import time

routes = web.RouteTableDef()

@routes.get("/getActivity")
async def get_activity(request):
    try:
        async with aiohttp.ClientSession() as session:
            for x in range(5):
                tasks = []
                for i in range(8):
                    tasks.append(asyncio.create_task(session.get(
                    "https://www.boredapi.com/api/activity"
                    )))
                    
                bored_data = await asyncio.gather(*tasks)
                bored_data = [await data.json() for data in bored_data]

                tasks = []
                for i in range(len(bored_data)):
                    tasks.append(asyncio.create_task(session.post(
                        "http://localhost:8081/parseActivities",
                        json = bored_data[i]
                    )))

                result = await asyncio.gather(*tasks)
                result = [await data.json() for data in result]
        
        return web.json_response(result)

    except Exception as e:
        return web.json_response({ "Failed": str(e) }, status = 500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app)