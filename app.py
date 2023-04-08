# server side using Flask
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# to keep confidential data in secret
import os
from dotenv import load_dotenv
load_dotenv()

GCP_PROJECT_ID = os.getenv('MONGO_DB_STORAGE')

# connect to MongoDB database
from pymongo import MongoClient
client = MongoClient('mongodb+srv://siwon:rlaznf11@cluster0.icysouv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsiwon


# main page
@app.route('/')
def home():
    return render_template('index.html')