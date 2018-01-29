from db import Base
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship


class Parent(Base):
    __tablename__ = 'parent_table'
    parent_id = Column(Integer, primary_key=True)
    children = relationship("ParentChild", back_populates="parent")

    def __repr__(self):
        return "<Parent(parent_id='%s')>" % self.parent_id
