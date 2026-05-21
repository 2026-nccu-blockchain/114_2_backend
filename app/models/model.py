from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, DECIMAL, Double, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base
from enum import Enum
import uuid
import bcrypt
import secrets
import re
import hashlib
import json
from datetime import datetime

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

    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), nullable=False)
    hash_password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    avatar_url = Column(String(255), nullable=False, default="https://res.cloudinary.com/dg4uvp9rv/image/upload/v1779102740/default_avatar_zzz4vt.png")
    is_first_login = Column(Boolean, nullable=False, default=False)
    is_delete = Column(Boolean, nullable=False, default=False)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    def set_password(self, password: str) -> None:
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def verify_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.hashed_password.encode('utf-8'))
    
    @staticmethod
    def verify_email(email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), nullable=False)
    hash_password = Column(String(255), nullable=False)
    name = Column(String(20), nullable=False)
    phone = Column(String(10), nullable=False)
    address = Column(String(255), nullable=False)
    avatar_url = Column(String(255), nullable=False, default="https://res.cloudinary.com/dg4uvp9rv/image/upload/v1779102740/default_avatar_zzz4vt.png")
    is_first_login = Column(Boolean, nullable=False, default=False)
    is_delete = Column(Boolean, nullable=False, default=False)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    orders = relationship("Order", back_populates="buyer")

    def set_password(self, password: str) -> None:
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def verify_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.hashed_password.encode('utf-8'))
    
    @staticmethod
    def verify_email(email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), nullable=False)
    hash_password = Column(String(255), nullable=False)
    name = Column(String(20), nullable=False)
    phone = Column(String(10), nullable=False)
    avatar_url = Column(String(255), nullable=False, default="https://res.cloudinary.com/dg4uvp9rv/image/upload/v1779102740/default_avatar_zzz4vt.png")
    company_name = Column(String(255), nullable=False)
    company_phone = Column(String(10), nullable=False)
    company_address = Column(String(255), nullable=False)
    is_first_login = Column(Boolean, nullable=False, default=False)
    is_delete = Column(Boolean, nullable=False, default=False)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    products = relationship("Product", back_populates="seller")
    orders = relationship("Order", back_populates="seller")

    def set_password(self, password: str) -> None:
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def verify_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.hashed_password.encode('utf-8'))
    
    @staticmethod
    def verify_email(email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), nullable=False)
    hash_password = Column(String(255), nullable=False)
    name = Column(String(20), nullable=False)
    phone = Column(String(10), nullable=False)
    avatar_url = Column(String(255), nullable=False, default="https://res.cloudinary.com/dg4uvp9rv/image/upload/v1779102740/default_avatar_zzz4vt.png")
    is_first_login = Column(Boolean, nullable=False, default=False)
    is_delete = Column(Boolean, nullable=False, default=False)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    orders = relationship("Order", back_populates="driver")

    def set_password(self, password: str) -> None:
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def verify_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.hashed_password.encode('utf-8'))
    
    @staticmethod
    def verify_email(email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

class Product(Base):
    __tablename__ = "products"

    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))
    pid = Column(String(10), nullable=False)
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False)
    seller_id = Column(String(36), ForeignKey("sellers.id"))
    desc = Column(Text, nullable=False)
    type = Column(String(255), nullable=False)
    product_url = Column(String(255), nullable=False, default="https://res.cloudinary.com/dg4uvp9rv/image/upload/v1779102750/default_product_mmix3v.png")
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    seller = relationship("Seller", back_populates="products")
    selled_product = relationship("SelledProduct", back_populates="product")

class Order(Base):
    __tablename__ = "orders"

    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))
    oid = Column(String(36), nullable=False)
    buyer_id = Column(String(36), ForeignKey("buyers.id"))
    seller_id = Column(String(36), ForeignKey("sellers.id"))
    driver_id = Column(String(36), ForeignKey("drivers.id"))
    to_address = Column(String(255), nullable=False)
    order_status = Column(SQLEnum(OrderStatus), nullable=False)
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    buyer = relationship("Buyer", back_populates="orders")
    seller = relationship("Seller", back_populates="orders")
    driver = relationship("Driver", back_populates="orders")
    selled_products = relationship("SelledProduct", back_populates="order")

class SelledProduct(Base):
    __tablename__ = "selled_products"
    
    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))
    product_id = Column(String(36), ForeignKey("products.id"))
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    count = Column(Integer, nullable=False)
    order_id = Column(String(36), ForeignKey("orders.id"))

    product = relationship("Product", back_populates="selled_product")
    order = relationship("Order", back_populates="selled_products")