from db import Base
from sqlalchemy import Column, Integer
from sqlalchemy.ext.associationproxy import association_proxy


class Parent(Base):
    __tablename__ = 'parent_table'
    parent_id = Column(Integer, primary_key=True)
    children = association_proxy('parent_children', 'child')

    def __repr__(self):
        return "<Parent(parent_id='%s')>" % self.parent_id
