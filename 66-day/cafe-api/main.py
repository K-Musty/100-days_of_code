import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_cafe():
    with app.app_context():
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        random_cafe = random.choice(cafes)
        return jsonify(cafe={"can_take_calls":random_cafe.can_take_calls,
                   "coffee_price":random_cafe.coffee_price,
                   "has_sockets":random_cafe.has_sockets,
                   "has_toilet":random_cafe.has_toilet,
                   "has_wifi":random_cafe.has_wifi,
                   "id":random_cafe.id,
                   "img_url":random_cafe.img_url,
                   "location":random_cafe.location,
                   "map_url":random_cafe.map_url,
                   "name":random_cafe.name,
                   "seats":random_cafe.seats})

@app.route("/all")
def all_cafe():
    cafes = db.session.query(Cafe).all()
    # or return
    # cafes = []
    # for cafe in cafes:
    #     cafes.append(cafe.to_dict())
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route("/search")
def search_cafe():
    location_query = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=location_query).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = bool(request.form.get("has_toilet")),
        has_wifi = bool(request.form.get("has_wifi")),
        has_sockets = bool(request.form.get("has_sockets")),
        can_take_calls = bool(request.form.get("can_take_calls")),
        coffee_price = request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_cafe_price(cafe_id):
   new_price = request.args.get("new_price")
   cafe = db.session.query(Cafe).get(cafe_id)
   if cafe:
       cafe.coffee_price = new_price
       db.session.commit()
       return jsonify(response={"success": "Successfully Updated price."}), 200
   else:
       return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database."}), 404

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    cafe = db.session.query(Cafe).get(cafe_id)
    if not cafe:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


    if api_key == "TopSecretAPIKey":
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted cafe from database."}), 200
    elif api_key != "TopSecretAPIKey":
        return jsonify(error="That's not allowed, Make sure you have the correct api_key."), 403

if __name__ == '__main__':
    app.run(debug=True)
