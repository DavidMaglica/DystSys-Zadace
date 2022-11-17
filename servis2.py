import aiohttp
from aiohttp import web
import asyncio

routes = web.RouteTableDef()

@routes.post("/parseActivities")
async def parse_activities(request):
    try:
        json_data = await request.json()
        
        async with aiohttp.ClientSession() as session:
            if json_data.get("type") == "recreational" or json_data.get("type") == "charity":
                tasks = []
                for i in range(len(json_data)):
                    tasks.append(asyncio.create_task(session.post(
                        "http://localhost:8082/charityAndRecreational",
                        json = json_data
                    )))

                result = await asyncio.gather(*tasks)
                result = [await data.json() for data in result]

            else:
                tasks = []              
                for i in range(len(json_data)):
                    tasks.append(asyncio.create_task(session.post(
                        "http://localhost:8082/otherActivities",
                        json = json_data
                    )))

                result = await asyncio.gather(*tasks)
                result = [await data.json() for data in result]
        
        return web.json_response(result)

    except Exception as e:
        return web.json_response({ "Failed": str(e) }, status = 500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8081)