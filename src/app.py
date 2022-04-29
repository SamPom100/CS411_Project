# importing modules
import flask
from flask import Flask, Response, request, render_template, redirect, url_for, jsonify
import requests
from flaskext.mysql import MySQL
import flask_login
from api_keys_public import google_maps_key, weather_key
import os


mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'super secret string'  # Change this!

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Salo5561!'
app.config['MYSQL_DATABASE_DB'] = 'travel_planner'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#begin code used for login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


conn = mysql.connect()
cursor = conn.cursor()
cursor.execute("SELECT email FROM users")
users = cursor.fetchall()

def getUserList():
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM users")
    return cursor.fetchall()

class User(flask_login.UserMixin):
	pass

@login_manager.user_loader
def user_loader(email):
	users = getUserList()
	if not(email) or email not in str(users):
		return
	user = User()
	user.id = email
	return user

@login_manager.request_loader
def request_loader(request):
	users = getUserList()
	email = request.form.get('email')
	if not(email) or email not in str(users):
		return
	user = User()
	user.id = email
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT password FROM users WHERE email = '{0}'".format(email))
	data = cursor.fetchall()
	pwd = str(data[0][0] )
	user.is_authenticated = request.form['password'] == pwd
	return user

#LOGIN WITHOUT GOOGLE AOTH
@app.route('/register', methods=['GET', 'POST'])
def login():
	if flask.request.method == 'GET':
		return render_template('register.html')
	
	email = flask.request.form['email']
	cursor = conn.cursor()
	#check if email is registered
	if cursor.execute("SELECT password FROM users WHERE email = '{0}'".format(email)):
		data = cursor.fetchall()
		pwd = str(data[0][0] )
		if flask.request.form['password'] == pwd:
			user = User()
			user.id = email
			flask_login.login_user(user) #okay login in user
			return flask.redirect(flask.url_for('protected')) #protected is a function defined in this file

	#information did not match
	return render_template('register.html')

@app.route('/logout')
def logout():
	flask_login.logout_user()
	return render_template('home.html')

@login_manager.unauthorized_handler
def unauthorized_handler():
	return render_template('unauth.html')

#User registration
@app.route("/register", methods=['GET'])
def register():
	return render_template('register.html', supress='True')

@app.route("/register", methods=['POST'])
def register_user():
	try:
		email=request.form.get('email')
		password=request.form.get('password')
		first_name=request.form.get('first_name')
		last_name=request.form.get('last_name')

	except:
		return flask.redirect(flask.url_for('register'))
	cursor = conn.cursor()
	test =  isEmailUnique(email)
	if test:
		print(cursor.execute("INSERT INTO Users (email, password, first_name, last_name) VALUES ('{0}', '{1}', '{2}', '{3}')".format(email, password, first_name, last_name)))
		conn.commit()
		user = User()
		user.id = email
		flask_login.login_user(user)
		return render_template('profile.html', name=first_name)
	else:
		return flask.redirect(flask.url_for('register'))


def getUserIdFromEmail(email):
	cursor = conn.cursor()
	cursor.execute("SELECT user_id FROM users WHERE email = '{0}'".format(email))
	return cursor.fetchone()[0]

def isEmailUnique(email):
	cursor = conn.cursor()
	if cursor.execute("SELECT email  FROM users WHERE email = '{0}'".format(email)):
		return False
	else:
		return True

@app.route("/profile")
@flask_login.login_required
def protected():
	return render_template('profile.html', name=flask_login.current_user.id)

# This method executes before any API request
@app.before_request
def before_request():
    print('before API request')

#Google Maps Search API
@app.route("/search", methods=['GET'])
def search():
	return render_template('search.html', supress='True')

@app.route('/search', methods = ['POST']) 
def CityPlans():
        #get city name from html form
        city = request.form.get('city')
        
        api_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='

        # Your API key
        api_key = google_maps_key

        # updating the URL
        url = api_url + ("fun things to do in "+ city) + "&key=" + api_key 

        # Sending HTTP request
        response = requests.get(url)

    # checking the status code of the request
        if response.status_code == 200:
                
        # retrieving data in the json format
            data = response.json()

        # take the main dict block
            main = data["main"]

            city = data["name"]

            address = main["formatted_address"]

            rating = main["rating"]  

            category = main["types"] 
           
            return render_template('destination.html', city = city, address = address, rating = rating, category = category)
        else:

        # showing the error message
            
            return render_template('search.html')

# Weather API
@app.route("/weather", methods=['GET'])
def weather():
	return render_template('weather.html', supress='True')

@app.route('/weather', methods = ['POST']) 
def getWeather():
    if request.method == 'POST':
        #get city name from html form
        city = request.form.get('city')
        
        api_url = 'https://api.openweathermap.org/data/2.5/weather?q='

        # Your API key
        api_key = weather_key

        # updating the URL
        url = api_url + city + "&appid=" + api_key 

        # Sending HTTP request
        response = requests.get(url)

    # checking the status code of the request
        if response.status_code == 200:
                
        # retrieving data in the json format
            data = response.json()

        # take the main dict block
            main = data["main"]
            
        # getting city
            city = data["name"]
            
        # getting temperature
            temperature = main["temp"]
            
        # getting feel like
            feels_like = main["feels_like"]  
           
            return render_template('weather_ret.html', city = city, temperature = temperature, feels_like = feels_like)
        else:

        # showing the error message
            
            return render_template('weather.html')




# Friends Search
@app.route("/friends", methods=['GET'])
def friends():
	return render_template('friends.html', supress='True')

#http://127.0.0.1:5000/ the default return value
@app.route("/")
def hello_world():
  return render_template('home.html')

# run the flask app from Python file running
if __name__ == "__main__":
    app.run(port=5000, debug=True)