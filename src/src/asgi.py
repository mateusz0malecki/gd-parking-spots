import os

import django
from django.core.asgi import get_asgi_application
from starlette.applications import Starlette
from starlette.routing import Mount

from parkingspots.http_client import aiohttp_client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

django.setup()
django_app  = get_asgi_application()


async def on_startup():
    await aiohttp_client.start()


async def on_shutdown():
    await aiohttp_client.stop()


app = Starlette(
    routes=[Mount("/", app=django_app)],
    on_startup=[on_startup],
    on_shutdown=[on_shutdown],
)
