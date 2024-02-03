import databases
import sqlalchemy

DATABASE_URL = "sqlite:///lastdatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
task_db = sqlalchemy.Table("tasks",
                           metadata,
                           sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                           sqlalchemy.Column("title", sqlalchemy.String),
                           sqlalchemy.Column("description", sqlalchemy.String),
                           sqlalchemy.Column("done", sqlalchemy.Boolean))

items_db = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Float)
)

users_db = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String),
    sqlalchemy.Column("lastname", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("password", sqlalchemy.String)
)

orders_db = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("item_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("items.id")),
    sqlalchemy.Column("date", sqlalchemy.Date),
    sqlalchemy.Column("done", sqlalchemy.Boolean)
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)