rooms = {}

class Room:
    # The init method or constructor
    def __init__(self, id, creator):
        # Instance Variable
        self.players = {}
        self.add_player(creator)
        self.id = len(rooms)

    def add_player(self, player):
        self.players[len(self.players)] = player

    def remove_player(self, player):
        self.players.pop(player["id"])

    def closeRoom(self):
        rooms.pop(self.id)


def create_room(player):
    room_code = len(rooms)
    rooms[room_code] = Room(room_code, player)
    return room_code


def join_room(room_code, player):
    rooms.get(room_code).add_player(player)


def leave_room(room_code, player):
    rooms.get(room_code).remove_player(player)


def get_rooms():
    for room in rooms:
        print(rooms.get(room).id, rooms.get(room).players)