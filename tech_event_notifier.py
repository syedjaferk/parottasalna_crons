import requests
import json
from datetime import datetime, timedelta
import os

EVENTS_URL = "https://raw.githubusercontent.com/FOSSUChennai/tamilnadu.tech/refs/heads/main/src/data/events.json"
LOCAL_EVENTS_FILE = "events_yesterday.json"


def fetch_events():
    response = requests.get(EVENTS_URL)
    response.raise_for_status()
    return response.json()


def load_previous_events():
    if not os.path.exists(LOCAL_EVENTS_FILE):
        return []
    with open(LOCAL_EVENTS_FILE, "r") as file:
        return json.load(file)


def save_current_events(events):
    with open(LOCAL_EVENTS_FILE, "w") as file:
        json.dump(events, file, indent=2)


def notify(message, event):
    print(f"[{message}] {event['eventName']} on {event['eventDate']} at {event.get('location', 'Unknown')}")
    print(f"Link: {event['eventLink']}")
    print(f"Venue : {event['eventVenue']}")


def get_events():
    today = datetime.now().date()
    next_week = today + timedelta(days=7)

    todays_events = []
    upcoming_events_in_7_days = []
    new_events = []

    events = fetch_events()
    previous_events = load_previous_events()
    previous_ids = {e.get('id') or f"{e['eventName']}_{e['eventDate']}" for e in previous_events}

    for event in events:

        event_date = datetime.strptime(event['eventDate'], "%Y-%m-%d").date()
        event_id = event.get('id') or f"{event['eventName']}_{event['eventDate']}"

        if event_date == today:
            todays_events.append(event)
        elif event_date == next_week:
            upcoming_events_in_7_days.append(event)
        elif event_id not in previous_ids:
            new_events.append(event)

    save_current_events(events)

    return todays_events, upcoming_events_in_7_days, new_events
