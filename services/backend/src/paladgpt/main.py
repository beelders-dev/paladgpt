from fastapi import FastAPI

from paladgpt.api import router

app = FastAPI(
    title="PaladGPT API",
    version="0.1.0",
    description=(
        "An entertainment-focused palm-scanning API "
        "that generates fictional career predictions."
    ),
)

app.include_router(router)
