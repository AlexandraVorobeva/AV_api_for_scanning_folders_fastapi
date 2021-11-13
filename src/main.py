import uvicorn
from fastapi import FastAPI
from src.routs import router
from dotenv import load_dotenv


load_dotenv(".env")


app = FastAPI(title="API for folders", description="by Aexandra Vorobeva")
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
