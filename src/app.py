# importing modules
from flask import Flask, jsonify, request, Response
import webbrowser, requests
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Salo5561!'
app.config['MYSQL_DATABASE_DB'] = 'travel_planner'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#begin code used for location
conn = mysql.connect()
cursor = conn.cursor()
cursor.execute("SELECT city FROM locations WHERE city_id = 2")
city = cursor.fetchall()
print(city)

#http://127.0.0.1:5000/ the default return value
@app.route("/")
def hello_world():
  return "This is the home page."

# This method executes before any API request
@app.before_request
def before_request():
    print('before API request')

# http://127.0.0.1:5000/weather, returns from the "database"
@app.route('/weather', methods=['GET', 'POST'])
def get_weather():
        # API base URL
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q='

        # City Name
    cursor = conn.cursor()
    cursor.execute("SELECT city FROM locations WHERE city = 'boston'")
    city = 'boston'

        # Your API key
    api_key = "9581e38eae9390c82ece6c4d09f43b8f"

        # updating the URL
    url = api_url + city + "&appid=" + api_key

        # Sending HTTP request
    response = requests.get(url)

    if request.method == 'POST':
        
        # checking the status code of the request
        if response.status_code == 200:
                
            # retrieving data in the json format
            data = response.json()

            # take the main dict block
            main = data['main']
            
            # getting city
            city = main['name']
            
            # getting temperature
            temperature = main['temp']
            
            # getting feel like
            feels_like = main['feels_like']  
           
            return "City: " + city + "Temperature: " + temperature + "Feels like: " + feels_like

        else:

            # showing the error message
            return 'HTTP error'

    return requests.get(url).json()
        

# run the flask app from Python file running
if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.debug = True
    app.run(port=5000)
    
