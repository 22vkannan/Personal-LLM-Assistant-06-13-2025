from icalendar import Calendar
import os

def ingest_calendar(file_path):
    with open(file_path, 'rb') as f:
        cal = Calendar.from_ical(f.read())
        for component in cal.walk():
            if component.name == "VEVENT":
                store_memory(component.get("summary"))
