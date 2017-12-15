from calendar import Calendar, TextCalendar
from datetime import datetime, date, timedelta
from enum import Enum

from event_calendar.event_calendar import Labels, Month, Day, Event, PassCard

now = datetime.utcnow()

month = Month(now.date())

pass_card = PassCard(now.date(), 31)
month.apply_pass_card(pass_card)

event0 = Event("Event0", datetime(2017, 12, 6))
month.add_event(event0)

event = Event("Event1 mother of dragons", now + timedelta(days=2))
month.add_event(event)

event2 = Event("Event2 mother of dragons", now + timedelta(days=7), Labels.TOURNAMENT)
month.add_event(event2)

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('PyTest', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('calendar.html')
html = template.render(month=month, labels=Labels.ALL)

with open("PyTest.html", "w") as file:
    file.write(html)
