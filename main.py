# main.py
# AnalystPro FastAPI backend for Railway
# ---------------------------------------
# Provides a simple API with CORS configured
# for your GitHub Pages frontend and Teams app.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AnalystPro API",
    description="Backend service for AnalystPro (Teams + GitHub Pages integration)",
    version="1.0.0"
)

# ✅ Allowed origins (no path segments!)
# Use only scheme + host
allowed_origins = [
    "https://gksn-hub.github.io",   # GitHub Pages frontend
    "http://localhost:5173",        # optional for local dev
    "http://localhost:3000"         # optional for local dev
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Health endpoint for Railway monitoring ---
@app.get("/health")
def health():
    """Used by Railway to check that the service is alive."""
    return {"ok": True}

# --- Demo API endpoint ---
@app.get("/api/hello")
def hello():
    """Simple test route for validation."""
    return {"message": "Hello from AnalystPro FastAPI"}

# --- Example: extend this with your app logic ---
# You can add more endpoints later, e.g.:
# @app.post("/api/score")
# def score_idea(idea: dict):
#     # Call your LLM scoring logic here
#     return {"score": 87, "reason": "High impact and low effort"}

# Run with: uvicorn main:app --host 0.0.0.0 --port ${PORT}
# (Railway reads the PORT env variable automatically)
