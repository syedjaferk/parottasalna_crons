import argparse
import requests
from tech_event_notifier import get_events

from pydantic import BaseModel
from typing import List


class Message(BaseModel):
    question: str
    options: List[str]
    correct_option_id: int
    explanation: str
    chat_id: str
    type: str
    is_anonymous: bool


parser = argparse.ArgumentParser(description="Quiz")

parser.add_argument('--telegram_url', type=str, help='Telegram Bot Url With Token', required=True)
parser.add_argument('--chat_id', type=str, help='Chat ID', required=True)
parser.add_argument('--message_thread_id', type=int, help="Message Thread ID", required=True)

args = parser.parse_args()

today, in7week, new = get_events()


def get_today_events_message(event):
    today_message = f"""
    🎯 **Event Today**: {event.get('eventName')}

    🗓️ Date: {event['eventDate']}
    📍 Location: {event['eventVenue']}, {event.get('location', 'Unknown')}
    🔗 Link: {event.get('eventLink', 'N/A')}

    📝 Description:  
    {event.get('eventDescription', 'No description provided.')}

    ⏰ Don't miss it!
    """
    return today_message


def get_notify_in7days_message(event):
    in7week_message =  f"""
    ⏳ **Upcoming Event in 7 Days**: {event['eventName']}

    🗓️ Date: {event['eventDate']}
    📍 Location: {event['eventVenue']}, {event.get('location', 'Unknown')}
    🔗 Link: {event.get('eventLink', 'N/A')}

    📝 Description:  
    {event.get('eventDescription', 'No description provided.')}

    🔔 Plan ahead!
    """
    return in7week_message


def get_notify_new_events_message(event):
    new_message = f"""
    🆕 **New Event Added**: {event['eventName']}

    🗓️ Date: {event['eventDate']}
    📍 Location: {event['eventVenue']}, {event.get('location', 'Unknown')}
    🔗 Link: {event.get('eventLink', 'N/A')}

    📝 Description:  
    {event.get('eventDescription', 'No description provided.')}

    🚀 Just listed. Spread the word!
    """
    return new_message


class Sender:
    def __init__(self, message: Message, telegram_bot_url):
        self.message = message
        self._telegram_bot_url = telegram_bot_url

    def send_message(self):
        res = requests.post(self._telegram_bot_url, json=self.message)
        return res

    def run(self):
        return self.send_message()


for event in today:
    message = get_today_events_message(event)
    print(message)
    message_val = {
        "chat_id": args.chat_id,
        "text": message,
        "parse_mode": "Markdown",
        "message_thread_id": args.message_thread_id
    }
    send = Sender(message=message_val, telegram_bot_url=args.telegram_url)
    print(send.run())


for event in in7week:
    message = get_notify_in7days_message(event)
    message_val = {
        "chat_id": args.chat_id,
        "text": message,
        "parse_mode": "Markdown",
        "message_thread_id": args.message_thread_id
    }
    send = Sender(message=message_val, telegram_bot_url=args.telegram_url)
    print(send.run())



for event in new:
    message = get_notify_new_events_message(event)
    message_val = {
        "chat_id": args.chat_id,
        "text": message,
        "parse_mode": "Markdown",
        "message_thread_id": args.message_thread_id
    }
    send = Sender(message=message_val, telegram_bot_url=args.telegram_url)
    print(send.run())
