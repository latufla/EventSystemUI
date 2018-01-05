from datetime import datetime, timedelta

from jinja2 import Environment, PackageLoader, select_autoescape

from view.data.player import Player
from view.loc import Loc
from view.view.profile import View

from view.data.event import Event as EventData
from view.data.event_result import EventResult
from view.enum.event_label import EventLabels

now = datetime.utcnow()

events = [
    EventData(0, "Game 1: Starters", datetime(2018, 1, 6), EventLabels.GAME, "http://google.com"),
    EventData(1, "Lesson 2: Red card", now + timedelta(days=2), EventLabels.LESSON, "http://ya.com"),
    EventData(3, "Tournament: Starters", now + timedelta(days=7, hours=4), EventLabels.TOURNAMENT, "http://vk.com")
]

events_history = list(
    map(lambda e: EventResult(e, 1, 1000, True), events)
)

player = Player(1, "Red Fox", "", "https://pbs.twimg.com/profile_images/606791373593837568/eL5DHK0L.png")
player.points = 1000
view = View(player, [])

env = Environment(
    loader=PackageLoader('PyTest', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('testbed/try_profile.html')
html = template.render(view=view, loc=Loc())

with open("test_bed.html", "w") as file:
    file.write(html)
