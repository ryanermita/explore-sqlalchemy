# explore-sqlalchemy
simple app to explore sqlalchemy


### notes
- `relationship.backref` creates bidirectional relationship implicitly
- `relationship.back_populates` a one-way backref, when used on both tables will
   work the same as backref which will give us a bidirectional relationship.
   It can be a more explicit way of creating a `relationship.backref.
