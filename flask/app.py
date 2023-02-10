from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import key
import requests
import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d7954752636cf8e90f3202e1b25682e'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Person(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    age = db.Column(db.Integer)


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    content = db.Column(db.Text())


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person


class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Mete:
        model = Article


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


@app.route('/', methods=['GET'])
def getData():
    people = Person.query.all()
    return jsonify({"people": people_schema.dump(people)})


@app.route("/add-person", methods=['POST'])
def addPerson():
    data = request.get_json()
    person = Person(name=data['name'], age=data["age"])
    db.session.add(person)
    db.session.commit()

    people = Person.query.all()

    return jsonify({"people": people_schema.dump(people)})


@app.route("/delete-person/<id>", methods=['Delete'])
def deletePerson(id):
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()

    people = Person.query.all()

    return jsonify({"people": people_schema.dump(people)})


@app.route("/fetch-articles", methods=['GET'])
def fetchArticles():
    response = requests.get(
        f"https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key{key}")
    data = response.json()

    article = Article(content=json.dumps(data['Data']))
    db.session.add(article)
    db.session.commit()

    return data['Data']


@app.route("/get-articles", methods=['GET'])
def getAlticles():
    article = Article.query.order_by(Article.id.desc()).limit(1).all()

    return jsonify({"articles":json.loads(article[0].content)})


if __name__ == '__main__':
    app.run(debug=True)
