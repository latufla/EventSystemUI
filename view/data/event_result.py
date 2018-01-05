from view.data.event import Event


class EventResult:
    def __init__(self, event: Event, place: int, reward: int, rewarded: bool):
        self.event = event
        self.place = place
        self.reward = reward
        self.rewarded = rewarded
