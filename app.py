from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# build a todo api that will enable you to get the list of users and their todos lists
# user - create a user - class user

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initianlizing the db
db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(15), nullable=False)
    email=db.Column(db.String(32), nullable=False, unique=True)



@app.route('/')
def home():
    return {
        'message': 'Welcome to our API'
    }, 200


@app.route('/users')
def users():
    users_ar = []
    for user in User.query.all():
        user_object = {
            'id': user.id,
            'name':user.name,
            'email':user.email
        }

        users_ar.append(user_object)

    return jsonify(users_ar)
    # return jsonify([
    #    {
    #        'name':user.name,
    #        'email':user.email
    #    }
    #    for user in User.query.all()
    # ])

@app.route('/add-user', methods=["POST"])
def create_user():
    user = request.get_json()

    new_user = User(
        name = user['name'],
        email = user['email']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }), 201


@app.route('/update-user/<int:id>', methods=["PUT"])
def update_user(id):
    new_user_details = request.get_json()
    user_from_db = User.query.filter_by(id=id).first_or_404()

    user_from_db.name = new_user_details['name']
    user_from_db.email = new_user_details['email']

    db.session.commit()

    return jsonify({
        "id": user_from_db.id,
        "name": user_from_db.name,
        "email": user_from_db.email
    }), 200


@app.route('/delete-user/<int:id>', methods=["DELETE"])
def delete_user(id):
    user_to_delete = User.query.filter_by(id=id).first()
    

    # return jsonify({"message": "user deleted successfully"}), 200

    if(user_to_delete):
        db.session.delete(user_to_delete)
        db.session.commit()
        return jsonify({"message": "user deleted successfully"}), 200
    else:
        return make_response(
            jsonify({
                "error": "user not found"
            }), 404
        )
    

    
    

# @app.route('/add-user', methods=["POST"])
# def create_user():
#     new_user = User(
#         name = request.form.get("name"),
#         email = request.form.get("email")
#     )

#     db.session.add(new_user)
#     db.session.commit()

#     resp = {
#         "message": "user created succesfully",
#         "user": {
#         'id': new_user.id,
#         'name': new_user.name,
#         'email': new_user.email
#         }
#     }

#     return make_response(
#         jsonify(resp), 201
#     )


if __name__ == '__main__':
    app.run()
