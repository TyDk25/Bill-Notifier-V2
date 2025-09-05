from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timedelta
from text_message import send_message

uri = "mongodb+srv://tyronecoding25_db_user:WI93k9SqvWfTPdqM@billsnotifier.yc64vuj.mongodb.net/?retryWrites=true&w=majority&appName=BillsNotifier"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
in_advance = (datetime.today() + timedelta(days=4)).day
# Send a ping to confirm a successful connection
try:
    db = client["MyBillsDatabase"]
    collection = db["BillsData"]
except Exception as e:
    print(e) 

def get_bills():
    
    bills_due = collection.find({"Bill_Date": in_advance})

    if bills_due:
        bill_message = [
            f"{bill['Bill_Name']}, Amount: £{bill['Bill_Amount']}" for bill in bills_due
     ]
        message = f'Bills Due Tomorrow:\n' + "\n".join(bill_message)
        send_message(message)
    
    else:
        message = 'No bills due tomorrow.'

        return message


get_bills()