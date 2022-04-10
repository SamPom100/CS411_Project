# importing modules
from flask import Flask,render_template, request, Response, jsonify
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

#http://127.0.0.1:5000/ the default return value
@app.route("/")
def hello_world():
  return render_template('search.html')

# This method executes before any API request
@app.before_request
def before_request():
    print('before API request')

@app.route('/search', methods = ['POST']) 
def getCity():
    if request.method == 'POST':
        #get city name from html form
        city = request.form.get('city')
        
        api_url = 'https://api.openweathermap.org/data/2.5/weather?q='

        # Your API key
        api_key = "9581e38eae9390c82ece6c4d09f43b8f"

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

            response_body = {
            "City": city,
            "Temparature": temperature,
            "Feels Like": feels_like
            }
           
            return response_body
        else:

        # showing the error message
            response_body = {
            'HTTP error'
            }
            return response_body
        

# run the flask app from Python file running
if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.debug = True
    app.run()
