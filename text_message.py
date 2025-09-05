from twilio.rest import Client
import os
from twilio.rest.api.v2010.account.message import MessageInstance
from dotenv import load_dotenv
load_dotenv()
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
from_number = os.environ.get('FROM')
to_number = os.environ.get('TO')
client = Client(account_sid, auth_token)


def send_message(body) -> MessageInstance:
    """
    Uses twilio API to send message.
    :param body: Text that is being sent to client.
    :return: Message to send.
    """
    message = client.messages.create(
        from_=from_number,
        to=to_number,
        body=body
    )

    return message
