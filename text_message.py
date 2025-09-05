from twilio.rest import Client
import os
from twilio.rest.api.v2010.account.message import MessageInstance
from dotenv import load_dotenv
load_dotenv()
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client('ACcee4cac3f033053cc958f7974eabd9f3', '089bc7f3032ef90e5d6f834f85ba464b')


def send_message(body) -> MessageInstance:
    """
    Uses twilio API to send message.
    :param body: Text that is being sent to client.
    :return: Message to send.
    """
    message = client.messages.create(
        from_='+447488895681',
        to='+447533487088',
        body=body
    )

    return message
