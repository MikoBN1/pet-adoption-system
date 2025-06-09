from fastapi import FastAPI
from controllers import user_controller, auth_controller, pet_controller, shelter_controller, \
    adoption_request_controller
from database import init_models
app = FastAPI()
@app.on_event("startup")
async def on_startup():
    await init_models()
app.include_router(user_controller.router)
app.include_router(auth_controller.router)
app.include_router(pet_controller.router)
app.include_router(shelter_controller.router)
app.include_router(adoption_request_controller.router)