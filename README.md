# Reviews API

A simple API that allows users to post and retrieve reviews.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:renatosouza/reviewsAPI.git
$ cd reviewsAPI
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
Using the local host (`http://127.0.0.1:8000/`) you can access the API. The endpoints and the overall usage are available in the [API Documentation](https://documenter.getpostman.com/view/9384142/SW7c2n16).

## Load example data

To test the application, some initial data is provided. Load it:
```sh
(env)$ python manage.py loaddata users.json
(env)$ python manage.py loaddata reviews.json
```

That loads 3 common users and 1 admin user into the database, with the following credentials:
```sh
username: renato
password: password

username: felipe
password: password

username: valeska
password: password

username: admin
password: superpassword
```

Beyond that, it also loads 9 reviews (3 from each user) into the database.

## Tests

To run the tests:
```sh
(env)$ python manage.py test reviews/tests/
```