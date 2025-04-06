from fastapi import APIRouter
import httpx

router = APIRouter()


@router.get("/async-request", tags=["GET"], summary="Асинхронный внешний запрос")
async def async_request():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
        return response.json()
