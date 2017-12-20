from event_calendar.event_calendar import Month, Labels


class CalendarMonth:
    def __init__(self, month: Month, label_config: Labels, prev_url: str, next_url: str):
        self.month = month
        self.label_config = label_config
        self.prev_url = prev_url
        self.next_url = next_url
