import uvicorn

# # Package # #
from app.settings import api_settings

def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        'main:app',
        port=api_settings.port,
        host=api_settings.host,
        reload=True,
    )
if __name__=='__main__':
    run()