from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UrlCreate(BaseModel):
    original_url: str

class Url(BaseModel):
    original_url: str
    short_code: Optional[str] = None
    owner: str
    visits: int = 0
    created_at: datetime = datetime.utcnow()
