from flask import Flask, jsonify, request
import webbrowser, requests
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


app = Flask(__name__)

# simple "database"
incomes = [
  { 'description': 'Chicago', 'weather': 50 }
]

#http://127.0.0.1:5000/ the default return value
@app.route("/")
def hello_world():
  return "This is the home page."

# This method executes before any API request
@app.before_request
def before_request():
    print('before API request')

# http://127.0.0.1:5000/weather, returns from the "database"
@app.route('/weather')
def get_weather():
  return jsonify(incomes)

# add to the database
# curl -X POST -H "Content-Type: application/json" -d '{
#   "description": "Boston",
#   "amount": 35.0
# }' http://localhost:5000/weather
# @app.route('/weather', methods=['POST'])
def add_weather():
  incomes.append(request.get_json())
  return '', 204

# get weather data from OpenWeather
@app.route('/getWeather')
def call_weather():
  api_url = 'https://api.openweathermap.org/data/2.5/weather?q=BOSTON&APPID=9581e38eae9390c82ece6c4d09f43b8f&units=imperial'
  return requests.get(api_url).json()


# run the flask app from Python file running
if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(port=5000)

