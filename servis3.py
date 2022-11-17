import aiohttp
from aiohttp import web
import asyncio

routes = web.RouteTableDef()

temp = []

async def get_random_user(se):
    async with se.get("https://randomuser.me/api/") as result:
        json = await result.json()
        json = json ["results"][0]
        return json
        


@routes.post("/charityAndRecreational")
async def charity_recreational(request):
    try:
        json_data = await request.json()

        async with aiohttp.ClientSession() as session:
            user = await get_random_user(session)
            temp.append({
                **user["location"]["coordinates"],
                **json_data
            })
            
        return web.json_response({ "status": "success" })

    except Exception as e:
        return web.json_response({ "Failed": str(e) }, status = 500)

@routes.post("/otherActivities")
async def other_activities(request):
    try:
        json_data = await request.json()

        async with aiohttp.ClientSession() as session:
            user = await get_random_user(session)
            temp.append({
                "ime": user["name"]["first"],
                "prezime": user["name"]["last"],
                "datum_rodenja": user["dob"]["date"],
                **json_data
            })
        
        return web.json_response({ "status": "success" })

    except Exception as e:
        return web.json_response({ "Failed": str(e) }, status = 500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8082)