def get_today_events_message(event):
    return f"""
    🎯 **Event Today**: {event.get('eventName')}

    🗓️ Date: {event['eventDate']}
    📍 Location: {event['eventVenue']}, {event.get('location', 'Unknown')}
    🔗 Link: {event.get('eventLink', 'N/A')}

    📝 Description:  
    {event.get('eventDescription', 'No description provided.')}

    ⏰ Don't miss it!
    """


def get_notify_in7days_message(event):
    return f"""
    ⏳ **Upcoming Event in 7 Days**: {event['eventName']}

    🗓️ Date: {event['eventDate']}
    📍 Location: {event['eventVenue']}, {event.get('location', 'Unknown')}
    🔗 Link: {event.get('eventLink', 'N/A')}

    📝 Description:  
    {event.get('eventDescription', 'No description provided.')}

    🔔 Plan ahead!
    """


def get_notify_new_events_message(event):
    return f"""
    🆕 **New Event Added**: {event['eventName']}

    🗓️ Date: {event['eventDate']}
    📍 Location: {event['eventVenue']}, {event.get('location', 'Unknown')}
    🔗 Link: {event.get('eventLink', 'N/A')}

    📝 Description:  
    {event.get('eventDescription', 'No description provided.')}

    🚀 Just listed. Spread the word!
    """
