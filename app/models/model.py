from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, DECIMAL, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base
import uuid
import bcrypt
import secrets
import re
import hashlib
import json
from datetime import datetime


#example

class EG(Base):
    __tablename__ = "egs"
    
    id = Column(Integer, primary_key=True, index=True, default=lambda: int(uuid.uuid4().int))
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, default=lambda: int(uuid.uuid4().int))
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def set_password(self, password: str) -> None:
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def verify_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.hashed_password.encode('utf-8'))
    
    @staticmethod
    def verify_email(email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

# real

from sqlalchemy import Column, Integer, String, Double, Boolean, DateTime, ForeignKey, Enum as SQLEnum, func
from sqlalchemy.orm import relationship
from enum import Enum
import uuid

class OrderStatus(Enum):
    ORDERED = 1
    SUCCESS = 2
    FAIL = 3
    PACKED = 4
    DELIVER = 5
    ARRIVED = 6
    REFUND = 7

class Admin(Base):
    __tablename__ = "admins"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    is_delete = Column(Boolean, nullable=False, default=False)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    is_delete = Column(Boolean, nullable=False, default=False)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    orders = relationship("Order", back_populates="buyer")

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    company_phone = Column(String, nullable=False)
    company_address = Column(String, nullable=False)
    is_delete = Column(Boolean, nullable=False, default=False)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    products = relationship("Product", back_populates="seller")
    orders = relationship("Order", back_populates="seller")

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    is_delete = Column(Boolean, nullable=False, default=False)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    orders = relationship("Order", back_populates="driver")

class Product(Base):
    __tablename__ = "products"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    p_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Double, nullable=False)
    stock = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False)
    seller_id = Column(String, ForeignKey("sellers.id"))
    desc = Column(String, nullable=False)
    type = Column(String, nullable=False)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    seller = relationship("Seller", back_populates="products")
    selled_product = relationship("OrderItem", back_populates="product")

class Order(Base):
    __tablename__ = "orders"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    o_id = Column(String, nullable=False)
    buyer_id = Column(String, ForeignKey("buyers.id"))
    seller_id = Column(String, ForeignKey("sellers.id"))
    driver_id = Column(String, ForeignKey("drivers.id"))
    to_address = Column(String, nullable=False)
    order_status = Column(SQLEnum(OrderStatus), nullable=False)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    buyer = relationship("Buyer", back_populates="orders")
    seller = relationship("Seller", back_populates="orders")
    driver = relationship("Driver", back_populates="orders")
    selled_products = relationship("SelledProduct", back_populates="order")

class SelledProduct(Base):
    __tablename__ = "selled_products"
    
    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    product_id = Column(String, ForeignKey("products.id"))
    name = Column(String, nullable=False)
    price = Column(Double, nullable=False)
    count = Column(Integer, nullable=False)
    order_id = Column(String, ForeignKey("orders.id"))

    product = relationship("Product", back_populates="selled_product")
    order = relationship("Order", back_populates="selled_products")