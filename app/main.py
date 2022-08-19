from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "feed home page"}


@app.get("/login")
async def root():
    return {"message": "login page"}

@app.post("/posts/create")
async def root():
    return {"message": "feed page"}

@app.post("/users/create")
async def root():
    return {"message": "users create page"}
    
