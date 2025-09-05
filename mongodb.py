import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timedelta
from text_message import send_message
from dotenv import load_dotenv
load_dotenv()

mongo_uri = os.environ.get('URI')
client = MongoClient(mongo_uri, server_api=ServerApi('1'))
in_advance = (datetime.today() + timedelta(days=1)).day

try:
    db = client["MyBillsDatabase"]
    collection = db["BillsData"]
except Exception as e:
    print(e) 

def get_bills() -> str:
    
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


if __name__ == "__main__":
    get_bills()