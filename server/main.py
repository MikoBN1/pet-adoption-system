from fastapi import FastAPI
from controllers import user_controller, auth_controller

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(auth_controller.router)
