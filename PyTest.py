# from datetime import datetime, timedelta
#
# from event_calendar.loc import Loc
# from event_calendar.view import View, Tabs
# from event_calendar.event_calendar import Labels, Month, Day, Event, PassCard, EventStates, Player
#
# import event.event
# import event.view
#
# import event_edit.view
#
# from jinja2 import Environment, PackageLoader, select_autoescape
#
#
# def try_event_edit(now):
#     e = Event("Lesson 2: Red card", now + timedelta(days=2), Labels.LESSON, "http://ya.com")
#     e.description_short = "Being a good red citizen"
#
#     view = event_edit.view.View(e, "")
#
#     env = Environment(
#         loader=PackageLoader('PyTest', 'templates'),
#         autoescape=select_autoescape(['html', 'xml'])
#     )
#
#     template = env.get_template('example.html')
#     html = template.render(view=view, loc=Loc())
#
#     with open("PyTest.html", "w") as file:
#         file.write(html)
#
#
# def try_event(now):
#     e = event.event.Event(1, "Lesson 1: Greeting", datetime(2017, 12, 6), Labels.LESSON, "http://google.com")
#     e.description = "<p>Jack Dempsey duckbilled barracudina Razorback sucker longfin escolar; mahseer midshipman warbonnet bramble shark. Blackchin bigeye squaretail eeltail catfish rough scad! Stonecat Cornish Spaktailed Bream hillstream loach longnose lancetfish eel lyretail eel saury: salmon shark Hammerjaw loach minnow, walking catfish.</p>" \
#                     "<p>Jack yellowfin cutthroat trout clingfish arrowtooth eel yellowtail horse mackerel redmouth whalefish tubeblenny herring tripletail, Owens pupfish summer flounder. Horsefish beachsalmon smalltooth sawfish mud cat catfish tadpole fish.</p>" \
#                     "<p>Slickhead stoneroller minnow sailfish yellowtail horse mackerel Long-finned sand diver cod, dojo loach sand knifefish lamprey yellowfin croaker labyrinth fish spiny dogfish kappy ground shark. Delta smelt ide noodlefish eel hammerhead shark cookie-cutter shark clown loach sixgill shark bluefish sea chub powen Modoc sucker.</p>" \
#                     "<p>Southern flounder kelp perch armored searobin yellow-and-black triplefin fangtooth South American Lungfish. Southern Dolly Varden zebra shark smelt-whiting bamboo shark clownfish atka mackerel, shrimpfish. Platy airbreathing catfish Cornish Spaktailed Bream lampfish lagena. Orangespine unicorn fish ribbon sawtail fish, squeaker Blind shark upside-down catfish darter flagfin, blue catfish. Zebra tilapia ilisha stonefish popeye catafula treefish Redhorse sucker. Alooh vendace pomfret ghoul scup kuhli loach ghost carp muskellunge luderick Mexican golden trout orangespine unicorn fish dory, bluntnose minnow orbicular velvetfish, leaffish.</p>" \
#                     "<p>Nurseryfish zebra trout Alaska blackfish dace squaretail blue eye. Butterflyfish barb; icefish, dorado bandfish snubnose parasitic eel Black mackerel river loach.</p>"
#     e.state = EventStates.STARTED
#     e.participant_list.append(event.event.Player(1, "Alex", ""))
#     e.participant_list.append(event.event.Player(2, "La", ""))
#     e.participant_list.append(event.event.Player(3, "Uri", ""))
#     e.participant_list.append(event.event.Player(4, "William", ""))
#
#     e.wait_list.append(event.event.Player(5, "Ann", ""))
#     e.wait_list.append(event.event.Player(6, "Dick", ""))
#     e.wait_list.append(event.event.Player(7, "Jimmy", ""))
#
#     view = event.view.View(e, True, "", "")
#
#     env = Environment(
#         loader=PackageLoader('PyTest', 'templates'),
#         autoescape=select_autoescape(['html', 'xml'])
#     )
#
#     template = env.get_template('example.html')
#     html = template.render(view=view, loc=Loc())
#
#     with open("PyTest.html", "w") as file:
#         file.write(html)
#
#
# def try_event_calendar(now):
#     month = Month(now.date())
#
#     pass_card = PassCard(now.date(), 31, 8)
#     month.apply_pass_card(pass_card)
#
#     event0 = Event("Lesson 1: Greeting", datetime(2017, 12, 6), Labels.LESSON, "http://google.com")
#     event0.description_short = "I`ll teach u how to say hello"
#     event0.state = EventStates.FINISHED
#     month.add_event(event0)
#     pass_card.events_visited.append(event0)
#
#     event = Event("Lesson 2: Red card", now + timedelta(days=2), Labels.LESSON, "http://ya.com")
#     event.description_short = "Being a good red citizen"
#     month.add_event(event)
#
#     event21 = Event("Lesson 3: Black card", now + timedelta(days=7), Labels.LESSON, "http://ok.ru")
#     event21.priority = 2
#     event21.description_short = "Being a good black citizen"
#     month.add_event(event21)
#
#     event2 = Event("Tournament: novice", now + timedelta(days=7, hours=4), Labels.TOURNAMENT, "http://vk.com")
#     event2.priority = 1
#     event2.description_short = "First year novices are welcome"
#     month.add_event(event2)
#
#     view = View(month, pass_card, Labels.ALL, "http://google.com", "http://ya.com")
#     view.active_tab = Tabs.PASS_CARD
#
#     env = Environment(
#         loader=PackageLoader('PyTest', 'templates'),
#         autoescape=select_autoescape(['html', 'xml'])
#     )
#
#     template = env.get_template('example.html')
#     html = template.render(view=view, loc=Loc())
#
#     with open("PyTest.html", "w") as file:
#         file.write(html)
#
#
# now = datetime.utcnow()
# # try_event(now)
# # try_event_calendar(now)
# try_event_edit(now)
