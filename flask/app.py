from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import werkzeug.security as security
from flask_cors import CORS
from config import key
import requests
import datetime
import json
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d7954752636cf8e90f3202e1b25682e'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(75))
    email = db.Column(db.String(75))
    password = db.Column(db.String(75))

    assets = db.relationship("Asset", backref="user", lazy=True)


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    content = db.Column(db.Text())


class Forex(db.Model):
    __tablename__ = "forex"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    content = db.Column(db.Text())


class Crypto(db.Model):
    __tablename__ = "crypto"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    content = db.Column(db.Text())


class Coin(db.Model):
    __tablename__ = "coins"
    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.String(20))
    name = db.Column(db.String(20))
    symbol = db.Column(db.String(20))


class Favourite(db.Model):
    __tablename__ = "favourites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    asset = db.Column(db.String(40))
    asset_id = db.Column(db.String(10))
    asset_category = db.Column(db.String(40))


class Asset(db.Model):
    __tablename__ = "assets"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    asset = db.Column(db.String(40))
    asset_id = db.Column(db.String(10))
    asset_category = db.Column(db.String(40))
    amount = db.Column(db.Float())
    units = db.Column(db.Float())


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class ForexSchema(ma.SQLAlchemyAutoSchema):
    class Mete:
        model = Forex


class CryptoSchema(ma.SQLAlchemyAutoSchema):
    class Mete:
        model = Crypto


class CoinSchema(ma.SQLAlchemyAutoSchema):
    class Mete:
        model = Coin


class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Mete:
        model = Article


user_schema = UserSchema()
users_schema = UserSchema(many=True)

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


@app.route('/', methods=['GET'])
def getUsers():
    users = User.query.all()
    return jsonify({"users": users_schema.dump(users)})


@app.route('/', methods=['GET'])
def getUser():
    user = User.query.order_by(User.id.desc()).limit(1)
    return jsonify({"user": user_schema.dump(user)})


@app.route("/add-user", methods=['POST'])
def addUser():
    data = request.get_json()
    user = User(
        email=data["email"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        password=security.generate_password_hash((data["password"]))
    )
    db.session.add(user)
    db.session.commit()

    users = User.query.all()

    return jsonify({"users": users_schema.dump(users)})


@app.route("/delete-user/<id>", methods=['Delete'])
def deleteUser(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    users = User.query.all()

    return jsonify({"users": users_schema.dump(users)})


@app.route("/fetch-articles", methods=['GET'])
def fetchArticles():
    response = requests.get(
        f"https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key{key}")
    data = response.json()

    article = Article(content=json.dumps(data['Data']))
    db.session.add(article)
    db.session.commit()

    return data['Data']


@app.route("/fetch-crypto", methods=['GET'])
def fetchCrypto():
    response = requests.get(
        f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false")
    data = response.json()

    crypto = Crypto(content=json.dumps(data))
    db.session.add(crypto)
    db.session.commit()

    return data


@app.route("/fetch-forex", methods=["GET"])
@app.route("/fetch-forex/<currency>", methods=["GET"])
def fetchForex(currency='USD'):
    response = requests.get(
        f'https://api.exchangerate.host/latest?base={currency}')
    data = response.json()
    currencies = []
    with open("./forex.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] in data['rates'] and type(data['rates'][row[3]]) is not dict:
                currencies.append({
                    "rate": data['rates'][row[3]],
                    "currency": row[2],
                    "currency_code": row[3],
                    "country": row[0],
                    "country_code": row[1],
                })

    return jsonify({"forex": currencies})


@app.route("/get-crypto", methods=["GET"])
def getCrypto():
    crypto = Crypto.query.order_by(Crypto.id.desc()).limit(1)
    return jsonify({"crypto": json.loads(crypto[0].content)})


@app.route("/update-coins", methods=['GET'])
def updateCoins():
    response = requests.get(
        f"https://api.coingecko.com/api/v3/coins/list")
    data = response.json()

    for item in data:
        coin = Coin(name=item['name'], coin_id=item['id'],
                    symbol=item['symbol'])
        db.session.add(coin)

    db.session.commit()

    return data


@app.route("/get-articles", methods=['GET'])
def getAlticles():
    article = Article.query.order_by(Article.id.desc()).limit(1)

    return {"articles": json.loads(article[0].content)}


if __name__ == '__main__':
    app.run(debug=True)
