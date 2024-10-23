from flask import Flask, jsonify
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

def get_salesforce_token():
    url = 'https://login.salesforce.com/services/oauth2/token?='
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'CookieConsentPolicy=0%3A0; LSKey-c%24CookieConsentPolicy=0%3A0; BrowserId=HE9WVTSuEe-5J_s02izSmA'
    }
    data = {
        'grant_type': 'password',
        'client_id': os.getenv('SALESFORCE_CLIENT_ID'),
        'client_secret': os.getenv('SALESFORCE_CLIENT_SECRET'),
        'username': os.getenv('SALESFORCE_USERNAME'),
        'password': os.getenv('SALESFORCE_PASSWORD')
    }
    
    response = requests.post(url, headers=headers, data=data)
    return response.json()

# set up root route
@app.route("/")
def salesforce_token():
    token_response = get_salesforce_token()
    return jsonify(token_response)

# Get the PORT from environment
port = os.getenv('PORT', '8080')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
