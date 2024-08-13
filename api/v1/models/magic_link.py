from sqlalchemy import TIMESTAMP, Column, String, Integer, ForeignKey, Boolean, DateTime, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from api.v1.models.base import Base  # Import Base from the new base.py file



class MagicLink(Base):
    __tablename__ = 'magic_links'
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    token = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

    
    user = relationship("User", back_populates="magic_links")