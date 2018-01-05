from view.data.event import Event


class View:
    def __init__(self, event: Event, save_url: str):
        self.event = event

        self.save_url = save_url

        self.min_width = 400
        self.max_width = 1200
