#!/usr/bin/python3
"""This module provides a class `State` which inherits from the
`Base` SQLalchemy class and connects to a MySQL table `states`.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create instance of declarative_base()
Base = declarative_base()


class State(Base):
    """Links to a mysql table
    """
    __tablename__ = 'states'      # Link to the mysql table `states`
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
