from fastapi import FastAPI, HTTPException, Header, Depends
from routers.anime import router as anime_router

app = FastAPI()

TOKENS = ["token1", "token2", "token3"]


def authenticate(token: str = Header(...)):
    if token not in TOKENS:
        raise HTTPException(status_code=401, detail="Invalid auth token")


app.include_router(anime_router, prefix="/anime", dependencies=[Depends(authenticate)])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
