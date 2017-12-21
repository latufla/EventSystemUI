from datetime import datetime, date, timedelta
from calendar import Calendar

from event_calendar.loc import Loc


def trim_microseconds(t):
    return t - timedelta(microseconds=t.microsecond)


class Icon:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color


class Label:
    def __init__(self, loc_key: str, color: str = None, icon: Icon = None):
        self.loc_key = loc_key
        self.color = color

        self.icon = icon


class Labels:
    PASS_CARD = Label(Loc.PASS_CARD_CALENDAR_LABEL, "#ADD8E6")
    LESSON = Label(Loc.LESSON_CALENDAR_LABEL, "darkcyan", Icon("big book icon", "white"))
    TOURNAMENT = Label(Loc.TOURNAMENT_LABEL, "darkorange", Icon("big trophy icon", "white"))

    ALL = [PASS_CARD, LESSON, TOURNAMENT]


class EventState:
    def __init__(self, loc_key: str, color: str = None):
        self.loc_key = loc_key
        self.color = color


class EventStates:
    NOT_READY = EventState(Loc.NOT_READY_EVENT_STATE, "grey")
    STARTED = EventState(Loc.STARTED_EVENT_STATE, "green")
    FINISHED = EventState(Loc.FINISHED_EVENT_STATE, "orange")
    REWARDED = EventState(Loc.REWARDED_EVENT_STATE, "red")


class PassCard:
    """
    Pass card for variable amount of days
    """

    def __init__(self, start_date: date, days: int, max_events_visited: int):
        self.start_date = start_date
        self.expire_date = self.start_date + timedelta(days=days)

        self.events_visited = []
        self.max_events_visited = max_events_visited

        c = Calendar()

        start_month = list(c.itermonthdates(self.start_date.year, self.start_date.month))
        self._start_month_days = list(filter(lambda d: d >= self.start_date, start_month))

        expire_month = c.itermonthdates(self.expire_date.year, self.expire_date.month)
        self._expire_month_days = list(filter(lambda d: d <= self.expire_date, expire_month))

        self._days = self._start_month_days + self._expire_month_days

    def __repr__(self):
        return "{start_date: " + str(self.start_date) + ", expire_date: " + str(self.expire_date) + "}"

    @property
    def start_month_days(self):
        return self._start_month_days

    @property
    def expire_month_days(self):
        return self._expire_month_days

    @property
    def days(self):
        return self._days


class Event:
    """
    Special event, displaying on calendar
    """

    def __init__(self, title: str, start_datetime: datetime, label: Label = Labels.LESSON, url=""):
        self.title = title
        self.start_datetime = start_datetime

        self.label = label
        self.url = url

        self.description_short = ""

        self.participant_list = []
        self.max_participants = 10

        self.wait_list = []

        self.state = EventStates.NOT_READY

        self.priority = 0

    def __repr__(self):
        return "{name: " + str(self.title) + "}"

    @property
    def start_date(self):
        return self.start_datetime.date()

    @property
    def start_time(self):
        return trim_microseconds(self.start_datetime).time()

    @property
    def short_name(self):
        return self.title[0:6] + " ..."


class Month:
    """
    Single month of Days. Use it instead of whole year
    """

    def __init__(self, now: date):
        self.id = now.month
        self.loc_key = Loc.MONTHS[self.id - 1]

        self.year = now.year

        c = Calendar()
        self.days = list(
            map(lambda d: Day(d), c.itermonthdates(now.year, now.month))
        )

        self.today = next(d for d in self.days if d.date == now)

        self.events = []

    def add_event(self, event: Event):
        event_start_date = event.start_datetime.date()
        event_day = next(d for d in self.days if d.date == event_start_date)
        event_day.events.append(event)

        self.events.append(event)

    def apply_pass_card(self, pass_card: PassCard):
        for d in self.days:
            if d.date in pass_card.days:
                d.label = Labels.PASS_CARD


class Day:
    """
    Day with possible event
    """

    def __init__(self, date: date):
        self.date = date
        self.events = []

        self.label = None

    def __repr__(self):
        return "{date: " + str(self.date) + ", event: " + str(self.events) + "}"

    def get_color(self):
        if len(self.events) > 0:
            events_by_priority = sorted(self.events, key=lambda e: e.priority)
            return events_by_priority[0].label.color

        if self.label:
            return self.label.color

        return None

    def get_event_icons(self):
        return list(map(lambda e: e.label.icon, self.events))
