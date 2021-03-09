from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
# connecting flask to the SQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


# Models that we need
class Product(db.Model):
    """
    Primary use for this class is to act as a data model for the data pulled off from the rabbitMQ
    """
    id: int = db.Column(db.Integer,
                        primary_key=True,
                        # We do not create the product here , it's created in the admin app
                        # this app would pull values from the rabbitMQ and use them
                        # same id from Admin app
                        autoincrement=False)
    title: str = db.Column(db.String(200))
    image: str = db.Column(db.String(200))


class ProductUser(db.Model):
    id: int = db.Column(db.Integer,
                        primary_key=True)
    user_id: int = db.Column(db.Integer)
    product_id: int = db.Column(db.Integer)
    # Make sure product id and user id is unique and not repeated at all
    UniqueConstraint('user_id',
                     'product_id',
                     name='user_product_unique')


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0')
