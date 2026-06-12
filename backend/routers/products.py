from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from app.database import get_db
from app.models import Product
from app.schemas import ProductResponse

router = APIRouter(prefix="/api/products", tags=["products"])

@router.get("/", response_model=List[ProductResponse])
async def get_all_products(
    db: AsyncSession = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    category: Optional[str] = None,
    featured: Optional[bool] = None,
):
    """Get all active products with filters"""
    query = select(Product).where(Product.is_active == True)
    
    if category:
        query = query.where(Product.category == category)
    if featured is not None:
        query = query.where(Product.is_featured == featured)
    
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    products = result.scalars().all()
    return products

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product_by_id(product_id: int, db: AsyncSession = Depends(get_db)):
    """Get single product by ID"""
    result = await db.execute(select(Product).where(Product.id == product_id, Product.is_active == True))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/slug/{slug}", response_model=ProductResponse)
async def get_product_by_slug(slug: str, db: AsyncSession = Depends(get_db)):
    """Get product by slug (SEO friendly)"""
    result = await db.execute(select(Product).where(Product.slug == slug, Product.is_active == True))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/featured/", response_model=List[ProductResponse])
async def get_featured_products(db: AsyncSession = Depends(get_db), limit: int = 8):
    """Get featured products for homepage"""
    query = select(Product).where(Product.is_active == True, Product.is_featured == True).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()