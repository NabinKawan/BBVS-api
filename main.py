"""APP
FastAPI app definition, initialization and definition of routes
"""

# # Installed # #
from unicodedata import name
from app.settings import api_settings
from imp import reload
from dotenv import load_dotenv
# from Slr import Prediction
from fastapi import FastAPI, WebSocket
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from app.routers import admin, candidates, file, login, voters
from app.db import init_local_db

from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# # Package # #

load_dotenv()
init_local_db()

app = FastAPI(
    title="BBVS api"
)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# creating different application for '/static'
app.mount('/static', StaticFiles(directory='static'))

@app.get("/", name="root", tags=["Root"])
async def root():
    return {"message": f"Welcome to BBVS API {app.version}"}


app.include_router(candidates.router)
app.include_router(voters.router)
app.include_router(admin.router)
app.include_router(file.router)
app.include_router(login.router)





# def run():
#     """Run the API using Uvicorn"""
#     uvicorn.run(
#         'app:app',
#         port=api_settings.port,
#         host=api_settings.host,
#         reload=True,
#     )

if __name__ == "__main__":
    print("running")
    # run()
    # uvicorn.run('app:app', host='localhost', port=8000,reload=True)
