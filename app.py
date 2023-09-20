from flask import Flask, jsonify
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


if __name__ == '__main__':
    app.run()
