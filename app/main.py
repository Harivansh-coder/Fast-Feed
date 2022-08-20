from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, users

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# BASE_DIR = Path(__file__).resolve().parent

@app.get("/")
async def root(request: Request):
    cookie_token: str = request.cookies.get("AccessToken")

    if not cookie_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not Authenticated"
        )
    
    return {"message" : "you are logged in"}
    


    
        

# auth routes
app.include_router(auth.router)
# user routes
app.include_router(users.router)



@app.post("/posts/create")
async def create_post():
    return {"message": "feed page"}

