from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from starlette.responses import HTMLResponse

from app.api.routes.routes import router as medication_request_router
from app.database.database import create_tables

app = FastAPI()

create_tables()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI</title>
    </head>
    <body>
        <h1>URL List</h1>
        <ul>
            <li><a href="/docs">API Documentation</a></li>
            <li><a href="/redoc">ReDoc Documentation</a></li>
        </ul>
    </body>
    </html>
    """


app.include_router(medication_request_router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI Medication Request API",
        version="1.0.0",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
