from typing import List

from event_calendar.event_calendar import Month, Label, PassCard


class Tabs:
    CALENDAR = "calendar_tab"
    EVENT_LIST = "event_list_tab"
    PASS_CARD = "pass_card_tab"


class View:
    def __init__(self, month: Month, pass_card: PassCard, label_config: List[Label], prev_url: str, next_url: str):
        self.month = month
        self.pass_card = pass_card

        self.label_config = label_config

        self.prev_url = prev_url
        self.next_url = next_url

        self.active_tab = Tabs.CALENDAR
        self.min_width = 700
        self.max_width = 1000
