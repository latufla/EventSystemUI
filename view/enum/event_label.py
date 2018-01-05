from view.data.icon import Icon
from view.loc import Loc


class EventLabel:
    def __init__(self, type_name: str, loc_key: str, color: str = None, icon: Icon = None):
        self.type_name = type_name

        self.loc_key = loc_key
        self.color = color

        self.icon = icon


class EventLabels:
    PASS_CARD = EventLabel("PassCard", Loc.PASS_CARD_CALENDAR_LABEL, "#ADD8E6")
    LESSON = EventLabel("Lesson", Loc.LESSON_CALENDAR_LABEL, "darkcyan", Icon("big book icon", "white"))
    TOURNAMENT = EventLabel("Tournament", Loc.TOURNAMENT_LABEL, "darkorange", Icon("big trophy icon", "white"))
    GAME = EventLabel("Game", Loc.GAME_LABEL, "darkorange", Icon("big game icon", "white"))

    EVENT_TYPES = [LESSON, TOURNAMENT, GAME]
    ALL = [PASS_CARD, LESSON, TOURNAMENT, GAME]