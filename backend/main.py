from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import products
from app.database import engine, Base
import asyncio

# Create tables (run once, usually in a startup event)
async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)   # drop first if needed
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(title="D2C Fashion API", version="1.0")

# CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(products.router)

@app.on_event("startup")
async def startup():
    await init_db()
    print("Database tables ready")

@app.get("/")
async def root():
    return {"message": "Welcome to D2C Fashion API"}