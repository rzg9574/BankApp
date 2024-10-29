from pymongo import MongoClient
import os
import sys

def init():
    dbLogin = os.environ.get('dbLogin', None)
    if dbLogin:
        client = MongoClient(dbLogin)
        db = client["Banking"]
        print("DataBase Initalized", file=sys.stderr)

        return db 