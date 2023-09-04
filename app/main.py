from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import sentry_sdk
from app.web_pages import router_web_pages
from app.sockets import router_web_socket

sentry_sdk.init(
    dsn="https://5b3180bbfd6ee4e660a01a4211eb1dac@o4505766519701504.ingest.sentry.io/4505766534905856",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)


app = FastAPI(
    title='First our app',
    description='we are not champions',
    version='0.0.1',
    debug=True,
)
app.mount('/app/static', StaticFiles(directory='app/static'), name='static')


app.include_router(router_web_pages.router)
app.include_router(router_web_socket.router)

@app.get('/')
@app.post('/')
async def main_page() -> dict:
    return {'greeting': 'HELLO'}


@app.get('/{user_name}')
@app.get('/{user_name}/{user_nick}')
async def user_page(user_name: str, user_nick: str = '', limit: int = 10, skip: int = 0) -> dict:
    data = [i for i in range(1000)][skip:][:limit]


    return {'user_name': user_name, 'user_nick': user_nick, 'data': data}

