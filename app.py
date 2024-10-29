from pymongo import MongoClient
import os
import sys
from flask import Flask, request, jsonify
from plaid import Client

class Manager:

    def __init__(self, db=None):
        self.db = db
        app = Flask(__name__)

        client = Client(
            client_id=os.getenv("PLAID_CLIENT_ID"),
            secret=os.getenv("PLAID_SECRET"),
            environment=os.getenv("PLAID_ENV")
        )
        

    @app.route('/create_link_token', methods=['POST'])
    def create_link_token(self):
        response = self.client.LinkToken.create({
            'user': {'client_user_id': 'unique_user_id'},
            'client_name': 'Your App Name',
            'products': ['auth', 'transactions'],  # Specify needed products
            'country_codes': ['US'],
            'language': 'en',
        })
        return jsonify({'link_token': response['link_token']})
    
    @app.route('/get_access_token', methods=['POST'])
    def get_access_token():
        public_token = request.json.get('public_token')
        exchange_response = client.Item.public_token.exchange(public_token)
        access_token = exchange_response['access_token']
        # Store access_token securely for future use
        return jsonify({'access_token': access_token})
    
    
    @app.route('/transactions', methods=['GET'])
    def get_transactions():
        access_token = 'your_stored_access_token'  # Replace with stored access token
        response = client.Transactions.get(access_token, start_date='2023-01-01', end_date='2023-01-31')
        return jsonify(response['transactions'])
            
        
    