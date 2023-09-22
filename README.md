# Todo Flask API
## Objective 1 (day1) :

``` - GET /: Retrieve a message that will return object ```

``` - GET /users: Retrieve all of the users ```

- You can always use any Postam/Fiddler/HTTP library to test the API if you prefer that.



<hr>

# Creating the API
- Create a directory ``` todo ```
- Run ``` cd todo/ ```
- Inside the todo, run ``` pipenv shell ``` to create your own environment and enter into it.
- Install dependencies. We need just two: Flask and Flask-SQLAlchemy(for database mapper). Run the below commands

```
~/ pipenv install flask

```

```
~/ pipenv install flask-sqlalchemy

```

# Creating the first route ``` '/' ```
- create a file called app.py and add the following

        from flask import Flask, jsonify
        from flask_sqlalchemy import SQLAlchemy

        app = Flask(__name__)

        @app.route('/)
        def home():
            return {
                'message': 'Welcome to building API'
            }, 200

        if__name__ = '__main__':
            app.run()



- On terminal run server with ``` flask run ``` and send your request to the link generated.
- When we sent a request to the endpoint / via postman or browser, you'll see response of object 
```
{
    'message': 'Welcome to building API'
}
```
which means everything is working fine

<hr>

## Its time to build our user model
- but the complete app will have user and to-do models.
- These two models will have a one-to-many relationship — i.e., one user can have many to-dos, and one to-do needs to have a user
- Check App.py for complete codes, 
 We connected db(sqlite) and SQLALchemy wrapper

## Testing user model in flask shell
- Open a Flask shell ,use,(``` flask shell ```), and let’s test our models.
```
>>> from app import User, db
>>> db.create_all()
>>> instance_user = User(
    name='George',
    email='gokumu@67.com'
)
>>> User.query.all()

```

- After running db.create_all(), these models have been created, and we can query them.
- The db.Model object exposes our models to a query method that we use to query them.

## Inserting some rows into db

```
>>> db.session.add(instance_user)
>>> db.session.commit()

```

- The function db.session.add adds a variable to the database temporarily. The second function, db.session.commit, saves it permanently. Other functions include db.session.add_all, which takes an array of objects to be added to the database, and db.session.delete, which deletes an object

- Test your users endpoint now, and good you'll have the ``` /users ``` endpoint returning a list of users in json format


## Objective 2,  Day 2:

``` - POST /add-user:  Creating new users```

``` - PUT /update-user/id: updating users details```

``` - GET /users/id: Get single user```

``` - DELETE /delete-user/id: Delete an existing user ```

### Posting new user route and method
<hr>
<h3>Method 1</h3>
        
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

<p>In the above method we have a decorator for defining the route, and a method create user</p>

- In the method ``` create-user() ```, we have
    
        user = request.get_json()
    - this line gets the users details that are being added from the front-end and storing it in user object. But the details here must be in json object format.

    - It then assigns the details when creating a new instance of user in this line,

            new_user = User(
                    name = user['name'],
                    email = user['email']
                )
    - Then we add the user to db and save it using the following line:

            db.session.add(new_user)
            db.session.commit()
    - Finally we return a serialized user object that was added, with the help of ```jsonify``` from flask.

<hr>

<h3>Method 2</h2>

    @app.route('/add-user', methods=["POST"])
    def create_user():
        new_user = User(
            name = request.form.get("name"),
            email = request.form.get("email")
        )

        db.session.add(new_user)
        db.session.commit()

        resp = {
            "message": "user created succesfully",
            "user": {
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email
            }
        }

        return make_response(
            jsonify(resp), 201
        )

 - In the above method we use the form method from flask requests, ``` request.form.get('something from the client form') ```
 - This grabs the details from client form and assigns them to the instance varibales.
     
        new_user = User(
                name = request.form.get("name"),
                email = request.form.get("email")
            )
    - NOTE: In this method we get the data from the form itself, the type of data to use from the client client should be of form-data type.


<hr>

<h3>Updating User and Deleting user</h3>

- To update/delete user we must target the unique user we want to update/delete.
- then we must query the user from the db, by filtering using by the target id,

        user_from_db = User.query.filter_by(id=id).first_or_404()

- for delete

        user_to_delete = User.query.filter_by(id=id).first()

And wahala, you can test your endpoints via postman or fiddler.

Thanks, 😊😊😊😊

Created with ❤️ for ❤️


    
