from typing import List

from event_calendar.event_calendar import Month, Label


class CalendarMonth:
    def __init__(self, month: Month, label_config: List[Label], prev_url: str, next_url: str):
        self.month = month
        self.label_config = label_config
        self.prev_url = prev_url
        self.next_url = next_url
