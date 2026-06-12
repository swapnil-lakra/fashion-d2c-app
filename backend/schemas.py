from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None
    price: Decimal
    compare_at_price: Optional[Decimal] = None
    category: Optional[str] = None
    image_url: Optional[str] = None
    additional_images: Optional[List[str]] = None
    sizes: Optional[List[str]] = None
    colors: Optional[List[str]] = None
    inventory_count: int = 0
    is_active: bool = True
    is_featured: bool = False
    badge: Optional[str] = None

class ProductResponse(ProductBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # For SQLAlchemy ORM mode (Pydantic v2)
