from db import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class ParentChild(Base):
    __tablename__ = 'parent_child_table'
    extra_data = Column(String(50))
    parent_id = Column(Integer, ForeignKey('parent_table.parent_id'), primary_key=True)
    child_id = Column(Integer, ForeignKey('child_table.child_id'), primary_key=True)

    # relationships
    child = relationship("Child", back_populates="parents")
    parent = relationship("Parent", back_populates="children")

    def __repr__(self):
        return "<ParentChild(parent_id='%s', child_id=%s)>" % (self.parent_id,
                                                               self.child_id)
