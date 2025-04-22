from fastapi import FastAPI

from road.openapi import OPENAPI_PARAMETERS

def create_app() -> FastAPI:
    app = FastAPI(
        **OPENAPI_PARAMETERS
    )
    return app

app = create_app()
