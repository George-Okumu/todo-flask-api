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


