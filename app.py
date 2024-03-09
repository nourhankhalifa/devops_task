from flask import Flask, request, render_template
from pymongo import MongoClient
from datetime import datetime
import os
app = Flask(__name__)

mongo_uri = os.environ.get('MONGO_URI')
# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client['users']  # Use 'users' database

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        timestamp = datetime.now()
        # Inserting data into MongoDB
        db.users.insert_one({'name': name, 'timestamp': timestamp})
        return 'Name "{}" added to the database with timestamp: {}'.format(name, timestamp)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=5000, debug=True))

