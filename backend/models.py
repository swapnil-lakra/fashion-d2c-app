from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, JSON, TIMESTAMP, text
from database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, nullable=False)
    description = Column(String)
    price = Column(DECIMAL(10, 2), nullable=False)
    compare_at_price = Column(DECIMAL(10, 2))
    category = Column(String(100))
    image_url = Column(String(500))
    additional_images = Column(JSON)
    sizes = Column(JSON)
    colors = Column(JSON)
    inventory_count = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    is_featured = Column(Boolean, default=False)
    badge = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")) 