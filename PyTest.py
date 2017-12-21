from datetime import datetime, timedelta

from event_calendar.view import View
from event_calendar.event_calendar import Labels, Month, Day, Event, PassCard, EventStates

now = datetime.utcnow()

month = Month(now.date())

pass_card = PassCard(now.date(), 31, 8)
month.apply_pass_card(pass_card)

event0 = Event("Lesson 1: Greeting", datetime(2017, 12, 6), Labels.LESSON, "http://google.com")
event0.description_short = "I`ll teach u how to say hello"
event0.state = EventStates.FINISHED
month.add_event(event0)
pass_card.events_visited.append(event0)

event = Event("Lesson 2: Red card", now + timedelta(days=2), Labels.LESSON, "http://ya.com")
event.description_short = "Being a good red citizen"
month.add_event(event)

event21 = Event("Lesson 3: Black card", now + timedelta(days=7), Labels.LESSON, "http://ok.ru")
event21.priority = 2
event21.description_short = "Being a good black citizen"
month.add_event(event21)

event2 = Event("Tournament: novice", now + timedelta(days=7, hours=4), Labels.TOURNAMENT, "http://vk.com")
event2.priority = 1
event2.description_short = "First year novices are welcome"
month.add_event(event2)

view = View(month, pass_card, Labels.ALL, "http://google.com", "http://ya.com")

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('PyTest', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('example.html')
html = template.render(view=view)

with open("PyTest.html", "w") as file:
    file.write(html)
