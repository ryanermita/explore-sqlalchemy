from db import Base
from sqlalchemy import Column, Integer
from sqlalchemy.ext.associationproxy import association_proxy


class Child(Base):
    __tablename__ = 'child_table'
    child_id = Column(Integer, primary_key=True)
    parents = association_proxy('child_parents', 'parent')

    def __repr__(self):
        return "<Child(child_id='%s')>" % self.child_id
