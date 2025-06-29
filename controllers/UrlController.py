from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from models import Url, User, UrlCreate
from models.db import db_urls
from utils.TokenUtil import get_current_user
import string, random

router = APIRouter()


@router.post("/shorten")
async def shorten(url_data: UrlCreate, current_user: User = Depends(get_current_user)):
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    new_url = Url(
        original_url=url_data.original_url,
        short_code=short_code,
        owner=current_user.username,
        created_at=datetime.utcnow(),
        visits=0
    )

    db_urls[short_code] = new_url
    return {"short_code": short_code}

@router.get("/analytics")
async def analytics(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return [{"code": code, "visits": url.visits} for code, url in db_urls.items()]


@router.get("/{code}")
async def redirect(code: str):
    url = db_urls.get(code)
    if not url:
        raise HTTPException(status_code=404, detail="Not found")
    url.visits += 1
    return {"original_url": url.original_url}


