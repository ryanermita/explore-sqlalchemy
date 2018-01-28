from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import os

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'explore_sqlalchemy.db'), echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Parent(Base):
    __tablename__ = 'parent_table'
    parent_id = Column(Integer, primary_key=True)
    children = relationship("Child", secondary="parent_child_table",
                            back_populates="parents")

    def __repr__(self):
        return "<Parent(parent_id='%s')>" % self.parent_id


class Child(Base):
    __tablename__ = 'child_table'
    child_id = Column(Integer, primary_key=True)
    parents = relationship("Parent", secondary="parent_child_table",
                           back_populates="children")

    def __repr__(self):
        return "<Child(child_id='%s')>" % self.child_id


class ParentChild(Base):
    __tablename__ = 'parent_child_table'
    parent_child_id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent_table.parent_id'), nullable=False)
    child_id = Column(Integer, ForeignKey('child_table.child_id'), nullable=False)

    def __repr__(self):
        return "<ParentChild(parent_id='%s', child_id=%s)>" % (self.parent_id,
                                                               self.child_id)


def recreate_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
