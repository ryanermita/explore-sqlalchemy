from db import Base
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship


class Child(Base):
    __tablename__ = 'child_table'
    child_id = Column(Integer, primary_key=True)
    parents = relationship("ParentChild", back_populates="child")

    def __repr__(self):
        return "<Child(child_id='%s')>" % self.child_id
