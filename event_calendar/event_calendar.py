from datetime import datetime, date, timedelta
from calendar import Calendar
from enum import Enum


class MonthL11nKeys:
    JANUARY = "January",
    FEBRUARY = "February",
    MARCH = "March",
    APRIL = "April",
    MAY = "May",
    JUNE = "June",
    JULY = "July",
    AUGUST = "August",
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"

    ALL = [JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER]


class Label:
    def __init__(self, type_name: str, color: str, icon: str):
        self.type_name = type_name
        self.color = color
        self.icon = icon


class Labels:
    PASS_CARD = Label("pass_card", "#ADD8E6", "")
    EVENT = Label("event", "#ADFF2F", "")
    TOURNAMENT = Label("tournament", "#FFD700", "")

    ALL = [PASS_CARD, EVENT, TOURNAMENT]


class PassCard:
    """
    Pass card for variable amount of days
    """

    def __init__(self, start_date: date, days: int):
        self.start_date = start_date
        self.expire_date = self.start_date + timedelta(days=days)

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

    def __init__(self, name: str, start_datetime: datetime, label: Label = Labels.EVENT):
        self.name = name
        self.start_datetime = start_datetime

        self.short_name = self.name[0:6] + " ..."

        self.label = label

    def __repr__(self):
        return "{name: " + str(self.name) + "}"


class Month:
    """
    Single month of Days. Use it instead of whole year
    """

    def __init__(self, now: date):
        self.id = now.month
        self.name = MonthL11nKeys.ALL[self.id - 1]

        self.year = now.year

        c = Calendar()
        self.days = list(
            map(lambda d: Day(d), c.itermonthdates(now.year, now.month))
        )

        self.today = next(d for d in self.days if d.date == now)

    def add_event(self, event: Event):
        event_start_date = event.start_datetime.date()
        event_day = next(d for d in self.days if d.date == event_start_date)
        event_day.event = event
        event_day.label = event.label

    def apply_pass_card(self, pass_card: PassCard):
        for d in self.days:
            if d.date in pass_card.days:
                d.label = Labels.PASS_CARD


class Day:
    """
    Day with possible event
    """

    def __init__(self, date: date, event: Event = None):
        self.date = date
        self.event = event

        self.label = None

    def __repr__(self):
        return "{date: " + str(self.date) + ", event: " + str(self.event) + "}"
