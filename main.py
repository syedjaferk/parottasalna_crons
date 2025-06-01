import argparse
from notifier.messaging import get_today_events_message, get_notify_in7days_message, get_notify_new_events_message
from notifier.sender import Sender
from tech_event_notifier import get_events

parser = argparse.ArgumentParser(description="Tech Event Notifier")
parser.add_argument('--telegram_url', type=str, required=True)
parser.add_argument('--chat_id', type=str, required=True)
parser.add_argument('--message_thread_id', type=int, required=True)
args = parser.parse_args()

today, in7week, new = get_events()


def notify_events(events, formatter):
    for event in events:
        message_text = formatter(event)
        print(message_text)  # Logging
        message_data = {
            "chat_id": args.chat_id,
            "text": message_text,
            "parse_mode": "Markdown",
            "message_thread_id": args.message_thread_id
        }
        sender = Sender(message=message_data, telegram_bot_url=args.telegram_url)
        print(sender.run())

# Notify categories
notify_events(today, get_today_events_message)
notify_events(in7week, get_notify_in7days_message)
notify_events(new, get_notify_new_events_message)
