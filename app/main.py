import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import routers, config


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(routers.index.router)
app.include_router(routers.users.router)

if __name__ == '__main__':
    if config.DEBUG:
        print(f'http://127.0.0.1:{config.PORT}/docs')
    uvicorn.run('app.main:app', host=config.HOST, port=config.PORT, reload=config.DEBUG)
