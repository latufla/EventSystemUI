import datetime

import event_calendar
from event_calendar.event_calendar import Label, Labels


class Event(event_calendar.event_calendar.Event):
    def __init__(self, id: int, title: str, start_datetime: datetime, label: Label = Labels.LESSON, url=""):
        super(Event, self).__init__(title, start_datetime, label, url)

        self.id = id


class Player(event_calendar.event_calendar.Player):
    def __init__(self, id: int, name: str, url: str):
        super(Player, self).__init__(name, url)

        self.id = id
