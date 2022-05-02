# importing modules
from flask import *
from api_keys_public import *
import flask, requests, flask_login, webbrowser, url_for
from flaskext.mysql import MySQL

from methods import call_weather_api

mysql = MySQL()
app = Flask(__name__)
app.secret_key = flask_app_secret

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = my_sql_database_key
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

#LOGIN WITH GOOGLE AUTH

client_id_google = google_id

from google_auth_oauthlib.flow import Flow
import pathlib
import os
import pip._vendor.cachecontrol as cachecontrol
import google
import google.oauth2.id_token as id_token

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

client_secret_file = os.path.join(pathlib.Path(__file__).parent, "client_secret_google.json")

flow = Flow.from_client_secrets_file(
	client_secrets_file = client_secret_file, 
	scopes = ["https://www.googleapis.com/auth/userinfo.profile","https://www.googleapis.com/auth/userinfo.email", "openid"],
	redirect_uri = "127.0.0.1:5000/callback"
)

def require_login(function):
	def wrapper(*args, **kwargs):
		if "google_id" not in session:
			return abort(401) # Login is needed
		else:
			return function()
		return wrapper()


@app.route('/google_login')
def google_login():
	auth_url, state = flow.authorization_url()
	session["state"] = state
	return redirect(auth_url)

@app.route('/callback')
def callback():
	flow.fetch_token(authorization_response=request.url)
	if not session[state] == request.args["state"]:
		abort(500)
	
	creds = flow.credentials
	request_sess = request.session()
	cached_sess = cachecontrol.CacheControl(request_sess)
	token_req = google.auth.transport.requests.Request(session=cached_sess)

	id_data = id_token.verify_oauth2_token(
		id_token = creds._id_token,
		request = token_req,
		audience = client_id_google
	)

	session["google_id"] = id_data.get("sub")
	session["name"] = id_data.get("name")
	return redirect("/protected_area")


@app.route('/google_logout')
def google_logout():
	session.clear()
	return redirect("/")

@app.route('/google_login')
def index():
	session["google_id"] = "Test"
	return flask.redirect("/protected_area")

@require_login
@app.route('/protected_area')
def protected_area():
	return "<h1> Hi </h1>"



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
        response = call_weather_api(request.form.get('city'))
    # checking the status code of the request
        if response.status_code == 200:
            return render_template('weather_ret.html', city = request.form.get('city'), temperature = response.json()['main']['temp'], feels_like = response.json()['main']['feels_like'])
        else:
        # showing the error message
            return render_template('weather.html') + "<h3 style = \"color: #ff0000\">An error occured loading up the city provided</h3>\""




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
	webbrowser.open_new('http://127.0.0.1:5000/')
	app.run(port=5000, debug=True)
