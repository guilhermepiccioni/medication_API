from fastapi import FastAPI
from starlette.responses import HTMLResponse

from app.api.routes.routes import router as medication_request_router

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>URLs List</title>
    </head>
    <body>
        <h1>Lista de URLs</h1>
        <ul>
            <li><a href="http://0.0.0.0:8000/medication_requests">Medication Requests</a></li>
        </ul>
    </body>
    </html>
    """


app.include_router(medication_request_router)
