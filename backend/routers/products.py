from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db
from models import Product
from schemas import ProductResponse
from typing import List, Optional

router = APIRouter(prefix="/api/products", tags=["products"])

@router.get("/featured", response_model=list[ProductResponse])
async def get_featured_products(
    db: AsyncSession = Depends(get_db),
    limit: int = Query(8, ge=1, le=20)
):
    """Get featured products for homepage"""
    query = select(Product).where(
        Product.is_active == True,
        Product.is_featured == True
    ).limit(limit)
    result = await db.execute(query)
    products = result.scalars().all()
    return products

@router.get("/", response_model=list[ProductResponse])
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
    return result.scalars().all()

# ✅ DYNAMIC ROUTES - baad mein likho
@router.get("/slug/{slug}", response_model=ProductResponse)
async def get_product_by_slug(slug: str, db: AsyncSession = Depends(get_db)):
    """Get product by slug (SEO friendly)"""
    query = select(Product).where(Product.slug == slug, Product.is_active == True)
    result = await db.execute(query)
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product_by_id(product_id: int, db: AsyncSession = Depends(get_db)):
    """Get single product by ID"""
    query = select(Product).where(Product.id == product_id, Product.is_active == True)
    result = await db.execute(query)
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product