from event.event import Event


class View:
    def __init__(self, event: Event, action_url: str):
        self.event = event

        self.action_url = action_url

        self.min_width = 400
        self.max_width = 1200
