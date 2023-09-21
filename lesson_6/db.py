import databases
import sqlalchemy

from settings import settings

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('first_name', sqlalchemy.String(32)),
    sqlalchemy.Column('last_name', sqlalchemy.String(32)),
    sqlalchemy.Column('email', sqlalchemy.String(128)),
    sqlalchemy.Column('password', sqlalchemy.String(128)),
)

products = sqlalchemy.Table(
    'products',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(40)),
    sqlalchemy.Column('description', sqlalchemy.String(400)),
    sqlalchemy.Column('price', sqlalchemy.Integer),
    sqlalchemy.Column('is_stock', sqlalchemy.Boolean),
)

orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('product_id', sqlalchemy.ForeignKey('products.id')),
    sqlalchemy.Column('date', sqlalchemy.DateTime),
    sqlalchemy.Column('status', sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

metadata.create_all(engine)
