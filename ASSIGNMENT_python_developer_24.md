# Python assignment

## What to build

For this assignment, you will build a backend web service that enables users to publish posts and subscribe to other users posts. Pretend like Company devs should be able to integrate with your backend web service and run it inside our infrastructure. 

## What do you need

To complete this assignment you will require the following:

* Python >= 3.8
* any Python web framework e.g. Flask, Bottle, CherryPy, Tornado, Django, FastAPI (it's recommended to pick the one you feel most comfortable with)
* any data store for storing the data models and user data e.g. PostgreSQL, MariaDB, MongoDB, Cassandra, CouchDB, Riak, Redis, Memcached (it's recommended to pick the one you feel most comfortable with)
* private GitHub or Bitbucket account and public git repository where you will upload the code
* use RESTful or GraphQL or gRPC (the choice is yours) to implement the APIs

## Functional requirements

### User registration

* User is able to register by selecting a username and password
* User may not register if the username is already taken
* User may not register if the password is not strong enough (define some rules e.g. minimum 10 characters, a mix of letters, numbers and special characters)
* After registration is complete, user should receive an authorization token to use

### User login

* User can't log in if the username and password are not correct
* After the login is complete, the user should receive an authorization token to use

### User posts

* User can publish a post at any time, post must have a title (e.g. up to 100 characters long) and post text can be only up to 1000 characters long
* User can search his/her posts by the title name via a simple substring match (e.g. searching "sport" should return any post titles such as "The best sporting events in town", "Scream SPORT if you like it", "Sport in everyday life")
* User can search his/her posts by date published via start date and end date filters (e.g. return all posts between 10/07/2022 and 21/07/2022 where both start date and end date are inclusive), only date is taken into account (not the time of the posting)
* If the user didn't provide a start date, it implies all the posts from the beginning of time until the end date (included)
* If the user didn't provide an end date, it implies all the posts from the start date (included) until now
* As a result of searching user posts, user should receive a list of tuples: post published date, post title, post text

### User profile

* User can add short biography (text up to 200 characters) for his/her profile
* User can view how many subscribers he/she currently has
* User can view how many subscriptions he/she currently has
* User can view how many posts he/she currently has

### Managing user subscriptions

* User can view all the other usernames available, view their profile short biography, how many subscribers they currently have and how many posts they currently have
* User can subscribe to any other user simply by adding their username to the list of subscriptions
* User can't subscribe to a username that doesn't exist
* User can remove a subscription at any time
* User can have up to 100 subscriptions, no more than that

### Filtering user subscriptions

* User can also search through his/her subscriptions by using any of the following filters: list of usernames, simple substring match for the post title, simple substring match for the post text
* List of usernames should have a limit (e.g. up to 10 usernames) and should contain usernames that exist
* As a result of the filtering, user should receive a list of tuples: username, post published date, post title, post text

## Non-functional requirements

### Backend service

* Access to user profile, user posts and subscriptions should be protected via an authorization token
* Response time should be limited to 2 seconds for every non-search request
* Response time should be limited to 30 seconds for every search request
* In case of an error, the response should provide some kind of feedback about the error (e.g. 404 Bad Request with response body "Username does not exist")
* Should be able to sustain up to 100 daily active users
* Should be able to sustain up to 10 parallel active users
* Add a sufficient amount of documentation in the code according to what you feel necessary in case anyone else would take over this project from you in the future

### Data store

* All the user data should be persisted on local storage, which means when the backend service is restarted (e.g. after a crash) no user data is lost
* Access to the data store from the backend service should be as secure as possible
* All created data structures should be optimized to maximize the speed of required queries (triggered by the backend service)
* Should be able to sustain up to 1000 unique user profiles
* Should be able to sustain up to 100 parallel connections

## Local development environment

Make sure to prepare some kind of development environment that works best for you. The only requirement is that the environment should be reproducible on another host so that your code can be run and tested by Company devs.

Recommended way would be to use Docker e.g. using docker-compose you can create an environment to bundle your Python backend service with a data store such as MongoDB or PostgreSQL.

Or, more simply, just pull the Docker image for the data store you want to use (e.g. https://hub.docker.com/_/mongo) and connect to it via your Python backend service running in the Python virtual environment (e.g. https://github.com/ruanbekker/mongodb-with-python-tutorial).

If you're not familiar with Docker at all, that's okay, just use any approach you're familiar with and make sure to give instructions so we can set it up on our side.

## The output of an assignment

When you finish with the assignment, please prepare the following:

* Code and other resoures uploaded on your private GitHub or Bitbucket account
* Share the link to your public git repository (from GitHub or Bitbucket) where you uploaded everything so the Company dev team can check it out
* `README.md` file with instructions on how to build, configure and run your code (the service and the data store)
* `DOCS.md` file (or multiple files) where you documented all of your APIs so the Company dev team can see how to integrate
* `TESTING.md` file (or multiple files) where you documented how you tested the APIs with some examples (e.g. using `curl`, Postman, Swagger, Python or shell script or any other testing approach)

## Final note

Intellectual property of this code is only yours, feel free to leave it on your GitHub or Bitbucket account as open source if you like and use it as a showcase for future purposes. Company will not request the removal of the code once the assignment is complete and verified.

If you have any additional questions or require assistance, please don't hesitate to contact us via e-mail: [iva@company.xyz](iva@company.xyz)
