class Loc:
    def __call__(self, loc_key: str):
        return self.all[loc_key]["en"]

    JANUARY = "january"
    FEBRUARY = "february"
    MARCH = "march"
    APRIL = "april"
    MAY = "may"
    JUNE = "june"
    JULY = "july"
    AUGUST = "august"
    SEPTEMBER = "september"
    OCTOBER = "october"
    NOVEMBER = "november"
    DECEMBER = "december"
    MONTHS = [JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER]

    PASS_CARD_CALENDAR_LABEL = "pass_card_calendar_label"
    LESSON_CALENDAR_LABEL = "lesson_calendar_label"
    TOURNAMENT_LABEL = "tournament_calendar_label"

    CALENDAR_CONTENT_MENU_TAB = "calendar_content_menu_tab"
    EVENT_LIST_CONTENT_MENU_TAB = "event_list_content_menu_tab"
    PASS_CARD_CONTENT_MENU_TAB = "pass_card_content_menu_tab"

    NOT_READY_EVENT_STATE = "not_ready_event_state"
    STARTED_EVENT_STATE = "started_event_state"
    FINISHED_EVENT_STATE = "finished_event_state"
    REWARDED_EVENT_STATE = "rewarded_event_state"

    def __init__(self):
        self.all = {
            self.JANUARY: {
                "en": "January",
            },
            self.FEBRUARY: {
                "en": "February",
            },
            self.MARCH: {
                "en": "March",
            },
            self.APRIL: {
                "en": "April",
            },
            self.MAY: {
                "en": "May",
            },
            self.JUNE: {
                "en": "June",
            },
            self.JULY: {
                "en": "July",
            },
            self.AUGUST: {
                "en": "August",
            },
            self.SEPTEMBER: {
                "en": "September",
            },
            self.OCTOBER: {
                "en": "October",
            },
            self.NOVEMBER: {
                "en": "November",
            },
            self.DECEMBER: {
                "en": "December",
            },

            self.CALENDAR_CONTENT_MENU_TAB: {
                "en": "Calendar",
            },
            self.EVENT_LIST_CONTENT_MENU_TAB: {
                "en": "Events",
            },
            self.PASS_CARD_CONTENT_MENU_TAB: {
                "en": "Pass card",
            },

            self.PASS_CARD_CALENDAR_LABEL: {
                "en": "Calendar",
            },
            self.LESSON_CALENDAR_LABEL: {
                "en": "Lesson",
            },
            self.TOURNAMENT_LABEL: {
                "en": "Tournament",
            },

            self.NOT_READY_EVENT_STATE: {
                "en": "Not ready",
            },
            self.STARTED_EVENT_STATE: {
                "en": "Started",
            },
            self.FINISHED_EVENT_STATE: {
                "en": "Finished",
            },
            self.REWARDED_EVENT_STATE: {
                "en": "Rewarded",
            }
        }
