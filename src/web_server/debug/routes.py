from fastapi import APIRouter, status
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/debug", tags=["debug"])


@router.get("/health")
async def health() -> PlainTextResponse:
    return PlainTextResponse(content="healthy\n", status_code=status.HTTP_200_OK)
