from django.contrib.auth.models import User
from adventure.models import Player, Room
import random


Room.objects.all().delete()

# r_outside = Room(title="Outside Cave Entrance",
#                description="North of you, the cave mount beckons")

# r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
# passages run north and east.""")

# r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""")

# r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
# to north. The smell of gold permeates the air.""")

# r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""")

# r_outside.save()
# r_foyer.save()
# r_overlook.save()
# r_narrow.save()
# r_treasure.save()

room_name_list = ["Cavern", "Passage", "Atrium", "Forest", "Mountainside", "Mudpit", "Hilltop", "Underwater Cave", "Riverside", "Village", "Shrine", "Hedge Maze", "Dungeon", "Cellar", "Crypt", "Graveyard", "Battlefield", "Library", "Lagoon", "Waterfall", "Cliffside", "Mansion", "Garden", "Church", "Trading Post", "Ale House", "Abandoned Campground", "Jail"]

arr = [
  [None, None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None, None]
]

available_coordinates = {}

for x in range(0, 10):
  for y in range(0, 10):
    available_coordinates[str(x) + str(y)] = 1


# Initialize a starting room with a couple neighbors to reduce chance of isolation
start_room = Room(x_coordinate=5,y_coordinate=5, title="Clearing")
arr[5][5] = start_room
start_room.save()
del available_coordinates['55']
another_room = Room(x_coordinate=5, y_coordinate=4, title=random.choice(room_name_list))
arr[5][4] = another_room
another_room.save()
del available_coordinates['54']
another_room = Room(x_coordinate=5, y_coordinate=6, title=random.choice(room_name_list))
arr[5][6] = another_room
another_room.save()
del available_coordinates['56']

for i in range(0, 73):
  random_coordinate = random.choice(list(available_coordinates))
  x_coord = int(random_coordinate[0])
  y_coord = int(random_coordinate[1])
  another_room = Room(x_coordinate=x_coord, y_coordinate=y_coord, title=random.choice(room_name_list))
  arr[x_coord][y_coord] = another_room
  another_room.save()
  del available_coordinates[random_coordinate]


for i in range(0,10):
  for j in range(0,10):
    if arr[i][j] is None:
      pass #It's not a room, don't do anything
    else:
      if i < 9:
        if arr[i + 1][j] is not None: #There's a room to the south
          if random.random() < 0.80: # Remove this if statement to guarantee paths, increase number to make paths more likely
            arr[i][j].connectRooms(arr[i + 1][j], "s")
            arr[i + 1][j].connectRooms(arr[i][j], "n")
          #Make the connection both directions to avoid 1-way paths
      if j < 9:
        if arr[i][j + 1] is not None: #There's a room to the east
          if random.random() < 0.80: # Remove this if statement to guarantee paths, increase number to make paths more likely
            arr[i][j].connectRooms(arr[i][j + 1], "e")
            arr[i][j + 1].connectRooms(arr[i][j], "w")

# a_room_0 = Room(title="Clearing", description="You find yourself in a clearing. You have no idea how you got here.")
# a_room_0.save()

# a_room_1 = Room(title="Cavern", description="You enter a dark passageway. It's hard to tell where you're going.")
# a_room_1.save()

# a_room_2 = Room(title="Kitchen", description="You're in a kitchen. That doesn't seem right, but it smells like cupcakes, so that's nice.")
# a_room_2.save()

# a_room_3 = Room(title="Forest", description="You enter a dark forest with heavy ground cover. Be careful not to trip.")
# a_room_3.save()

# a_room_4 = Room(title="Cliff Edge", description="There's a pretty steep cliff here. You can't make it down safely")
# a_room_4.save()

# a_room_5 = Room(title="Abandoned Village", description="Makeshift shelters litter the area, but there are no signs of any residents.")
# a_room_5.save()

# a_room_6 = Room(title="Shrine", description="A towering statue of a six-eyed fox occupies a pedestal covered with mysterious carvings. You dare not get too close")
# a_room_6.save()

# a_room_7 = Room(title="Hilltop", description="You work your way to the top of a hill. You can barely see over the surrounding trees. It looks like the forest stretches for miles in every direction")
# a_room_7.save()

# a_room_8 = Room(title="Hedge Maze Entrance", description="As the mist shrowd lifts, you find yourself at the entrance of an onimous hedge maze. You can make out a light on a hill in the distance. It is your only path forward")
# a_room_8.save()

# a_room_9 = Room(title="Hedge Serenety pool", description="You come across a tranquil pond.  A brief respite from the tumultuous maze. Puzzled, you sit and gaze into the water. You notice an arrow pointing north fashioned from pebbles.")
# a_room_9.save()

# a_room_10 = Room(title="Hedge Chess Board", description="You step on to an enormous marble chess board.  Nature has consumed what was once an ostentation display of wealth. The pieces are life sized! You notice the queen piece has her are extended pointing. She has been turned to the _____ . On her back there is an inscriptinon, As the sun goes west you must go south. Remember this or perish as you move forth.")
# a_room_10.save()

# a_room_11 = Room(title="Hedge Ancient Oak", description="You are excited to arrive a a clearing with one solitary decrepit Oak tree. A raven has roosted in its barren branches. You scale the tree and examine the nest.  You find a tattered scroll reading: You have traveled far and wide, your final test is just inside. The sun rises in the  ____ and then goes _____ . Follow these directions to pass your test. Proceed _____ to continue.")
# a_room_11.save()

# a_room_12 = Room(title="Hedge Darkness Trial", description="Everything goes dark. You have arrived at the final test of your bravery. One wrong move will send you back to the beginning. Remember the words of the raven")
# a_room_12.save()

# a_room_13 = Room(title="Hedge Portal", description=" If room description is Hedge Portal it Sends user back to HedgeMaze Entrance")
# a_room_13.save()

# a_room_14 = Room(title="Hedge Test 1 Passed:Rose garden", description=" You have chosen wisely. Remember the words of the ravenscroll")
# a_room_14.save()

# a_room_15 = Room(title="Hedge Gauntlet Passed!:Bird sanctuary", description="A cacophony of ravens! You have escaped the maze. Proceed to  fufill your destiny!")
# a_room_15.save()



#attach wrong turns that link to hedge entrance

# After creating a room, plug it into the room matrix below wherever you want. Feel free to add extra rows/columns as needed
# A room with 'None' on all four sides will be inaccessible

# Link rooms together
# r_outside.connectRooms(r_foyer, "n")
# r_foyer.connectRooms(r_outside, "s")

# r_foyer.connectRooms(r_overlook, "n")
# r_overlook.connectRooms(r_foyer, "s")

# r_foyer.connectRooms(r_narrow, "e")
# r_narrow.connectRooms(r_foyer, "w")

# r_narrow.connectRooms(r_treasure, "n")
# r_treasure.connectRooms(r_narrow, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=arr[5][5].id
  p.save()

