#!/usr/bin/env python3

"""Module for SQLalchemy model named user"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for the declarative model
Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for the users table.

    Attributes:
        id: The integer primary key.
        email: The non-nullable email address.
        hashed_password: The non-nullable hashed password.
        session_id: The nullable session ID.
        reset_token: The nullable reset token.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
