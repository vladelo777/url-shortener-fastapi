from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from app.models import URLRequest
from app.storage import urls

router = APIRouter()


@router.post("/", tags=["POST"], summary="Сократить URL", status_code=201)
async def shorten_url(request: URLRequest):
    short_id = len(urls) + 1
    urls[short_id] = request.url
    return {
        "Success": True,
        "Shortened URL": f"http://127.0.0.1:8080/{short_id}",
        "Shortened URL ID": short_id
    }


@router.get("/{short_url_id}", tags=["GET"], summary="Получить оригинальный URL", status_code=307)
async def redirect_to_url(short_url_id: str):
    try:
        return RedirectResponse(url=urls[int(short_url_id)])
    except (KeyError, ValueError):
        raise HTTPException(status_code=404, detail="URL не найден.")
