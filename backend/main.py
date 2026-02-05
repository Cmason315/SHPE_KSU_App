from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:8081",  # Expo default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Firebase (ensure you have the service account key or rely on default credentials)
# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

@app.get("/")
async def root():
    return {"message": "Hello from SHPE KSU Backend!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
