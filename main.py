from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import httpx

from .config import settings
from .schemas import ChatRequest, ChatResponse
from .llm import generate_reply

app = FastAPI(title=settings.app_name, version="0.1.0", description="Persian legal chatbot API")
STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
async def home():
    return FileResponse(STATIC_DIR / "index.html")

@app.get("/api/health")
async def health():
    return {"status": "ok", "app": settings.app_name, "mode": "demo" if settings.demo_mode else "model"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        reply, mode = await generate_reply([m.model_dump() for m in request.messages])
        return ChatResponse(reply=reply, mode=mode)
    except (httpx.HTTPError, KeyError, IndexError, ValueError) as exc:
        raise HTTPException(status_code=502, detail=f"خطا در ارتباط با سرویس مدل: {type(exc).__name__}") from exc
