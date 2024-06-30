from flask import Flask, request
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_DB_URL"))
db = client.flask_database
flights = db.flights
hotels = db.hotels

@app.route("/flight", methods=["POST"])
def post_flight():
    if request.method == 'POST':
        data = request.get_json()
        flight = data.get('flight', '')
        # Example: Saving to MongoDB
        flights.insert_one({'flight': flight})
        return f"Flight '{flight}' added to database"

@app.route("/hotel", methods=["POST"])
def post_hotel():
    if request.method == 'POST':
        data = request.get_json()
        hotel = data.get('hotel', '')
        # Example: Saving to MongoDB
        hotels.insert_one({'hotel': hotel})
        return f"Hotel '{hotel}' added to database"

if __name__ == "__main__":
    app.run(debug=True)