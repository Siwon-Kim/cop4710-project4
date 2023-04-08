# server side using Flask
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# to keep confidential data in secret
import os
from dotenv import load_dotenv
load_dotenv()
MONGO_DB_STORAGE = os.getenv('MONGO_DB_STORAGE')

# connect to MongoDB database
from pymongo import MongoClient
client = MongoClient(MONGO_DB_STORAGE)
db = client.dbProject4


# connect to FE: main client page
@app.route('/')
def home():
    return render_template('client.html')