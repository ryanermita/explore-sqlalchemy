from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'explore_sqlalchemy.db'), echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

from models.parent_model import Parent
from models.child_model import Child
from models.parent_child_model import ParentChild


def recreate_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def test_create():
    p = Parent()
    session.add(p)
    session.commit()

    # select parent
    p = session.query(Parent).get(1)

    # create child record via association table.
    c = Child()

    # append child to parent table
    # then commit.
    p.children.append(c)
    session.commit()
