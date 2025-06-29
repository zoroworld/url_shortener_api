from fastapi import FastAPI
from controllers.AuthController import router as auth_router
from controllers.UrlController import router as url_router

app = FastAPI()


app.include_router(auth_router)
app.include_router(url_router)
