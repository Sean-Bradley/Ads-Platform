import uvicorn

from app.config import APP_HOST, APP_PORT, DEBUG

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=APP_HOST,
        port=APP_PORT,
        reload=DEBUG
    )