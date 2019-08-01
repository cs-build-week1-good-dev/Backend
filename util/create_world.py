from django.contrib.auth.models import User
from adventure.models import Player, Room
import random


Room.objects.all().delete()



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
  #Swapping x and y because array syntax is opposite of graph syntax
  another_room = Room(x_coordinate=y_coord, y_coordinate=x_coord, title=random.choice(room_name_list))
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
      #uncomment this else statement to make rooms wrap from bottom to top
      # else: 
      #   if arr[0][j] is not None:
      #     if random.random() < 0.80: # Remove this if statement to guarantee paths, increase number to make paths more likely
      #       arr[i][j].connectRooms(arr[0][j], "s")
      #       arr[0][j].connectRooms(arr[i][j], "n")
      if j < 9:
        if arr[i][j + 1] is not None: #There's a room to the east
          if random.random() < 0.80: # Remove this if statement to guarantee paths, increase number to make paths more likely
            arr[i][j].connectRooms(arr[i][j + 1], "e")
            arr[i][j + 1].connectRooms(arr[i][j], "w")
      #uncomment this else statement to make rooms wrap from back to other side
      # else:
      #   if arr[i][0] is not None:
      #     if random.random() < 0.80: # Remove this if statement to guarantee paths, increase number to make paths more likely
      #       arr[i][j].connectRooms(arr[i][0], "e")
      #       arr[i][0].connectRooms(arr[i][j], "w")
          



players=Player.objects.all()
for p in players:
  p.currentRoom=arr[5][5].id
  p.save()

