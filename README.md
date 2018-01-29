# explore-sqlalchemy
simple app to explore sqlalchemy


### notes
- `relationship.backref` creates bidirectional relationship implicitly
- `relationship.back_populates` a one-way backref, when used on both tables will
   work the same as backref which will give us a bidirectional relationship.
   It can be a more explicit way of creating a `relationship.backref.
- `many-to-many` via `association object` requires that child objects are associated with an association instance before being appended to the parent;

  ```
    # select parent
    p = session.query(Parent).get(1)

    # create child record via association table.
    a = ParentChild(extra_data="some data")
    a.child = Child()

    # append child to parent table
    # then commit.
    p.children.append(a)
    session.commit()
  ```

- in `many-to-many` via `assiciation object` access from parent to child goes through the association object

  ```
    # select parent
    p = session.query(Parent).get(1)

    # access child via association object.
    a.children # [<ParentChild(parent_id='1', child_id=1)>]
    a.children[0].child # <Child(child_id='1')>

    # the same with child object
    c = session.query(Parent).get(1)
    c.parents # [<ParentChild(parent_id='1', child_id=1)>]
    c.parents[0].child # [<ParentChild(parent_id='1', child_id=1)>]
  ```
