
from sqlalchemy import Column, String, JSON

from backend.app.database.connection import Base


class ValidationRecord(Base):

    __tablename__ = "validation_records"

    id = Column(String, primary_key=True, index=True)

    timestamp = Column(String, nullable=False)

    report = Column(JSON, nullable=False)
