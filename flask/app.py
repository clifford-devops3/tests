from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d7954752636cf8e90f3202e1b25682e'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)



class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    age = db.Column(db.Integer)


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)


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


if __name__ == '__main__':
    app.run(debug=True)
