import os
from pymongo import MongoClient
from rich import print
from dotenv import load_dotenv
load_dotenv()

URI = os.getenv('ATLAS_MONGODB_URI')
assert URI is not None, 'ATLAS_MONGODB_URI is not set'

client = MongoClient(URI)
db = client.busseforce
coll = db.unified_tasks

def get_last_task():
    return coll.find_one(sort=[('_id', -1)])

if __name__ == '__main__':    
    task = get_last_task()

    print(task)