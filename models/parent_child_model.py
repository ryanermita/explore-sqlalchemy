from db import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, backref


class ParentChild(Base):
    __tablename__ = 'parent_child_table'
    extra_data = Column(String(50))
    parent_id = Column(Integer, ForeignKey('parent_table.parent_id'), primary_key=True)
    child_id = Column(Integer, ForeignKey('child_table.child_id'), primary_key=True)

    # relationships
    parent = relationship("Parent",
                          backref=backref("parent_children",
                                          cascade="all, delete-orphan")
                          )
    child = relationship("Child", backref="child_parents")

    def __init__(self, child=None, parent=None):
        self.parent = parent
        self.child = child

    def __repr__(self):
        return "<ParentChild(parent_id='%s', child_id=%s)>" % (self.parent_id,
                                                               self.child_id)
