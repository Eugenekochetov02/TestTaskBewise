from fastapi import FastAPI

from questions.router import router

# Initialization app.
app = FastAPI()

# Add router.
app.include_router(router)
