from view.data.icon import Icon
from view.loc import Loc


class EventLabel:
    def __init__(self, loc_key: str, color: str = None, icon: Icon = None):
        self.loc_key = loc_key
        self.color = color

        self.icon = icon


class EventLabels:
    PASS_CARD = EventLabel(Loc.PASS_CARD_CALENDAR_LABEL, "#ADD8E6")
    LESSON = EventLabel(Loc.LESSON_CALENDAR_LABEL, "darkcyan", Icon("big book icon", "white"))
    TOURNAMENT = EventLabel(Loc.TOURNAMENT_LABEL, "darkorange", Icon("big trophy icon", "white"))

    ALL = [PASS_CARD, LESSON, TOURNAMENT]