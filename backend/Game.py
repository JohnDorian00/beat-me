import word_model
import pprint

rooms = {}


class Room:
    # The init method or constructor
    def __init__(self, creator):
        # Instance Variable
        self.players = {}
        self.id = str(len(rooms))
        self.word = "день"
        self.words = word_model.get_words_list(self.word, 15)

        self.add_player(creator)

        rooms[self.id] = self

    def add_player(self, player):
        self.players[player["sid"]] = {"name": player["name"], "color": "blue"}

    def remove_player(self, player):
        self.players.pop(player["id"])

    def get_players(self):
        return self.players

    def check_word(self, word):
        if word == self.word:
            return 1
        elif word in self.words:
            return self.words.index(word) + 2
        else:
            return None

    def close_room(self):
        rooms.pop(self.id)

    def get_id(self):
        return self.id


def create_room(player):
    room = Room(player)
    print_rooms()
    return room


def join_room(room_code, player):
    room = rooms.get(room_code)
    if room is not None:
        room.add_player(player)
        return room
    return None


def leave_room(room_code, player):
    rooms.get(room_code).remove_player(player)
    return


def send_word(sid, word):
    # print('Word from player "{}" is "{}"'.format(sid, word))
    player_info = get_player_info(sid)
    room_id = player_info["room_id"]
    if room_id is not None:
        word_level = rooms.get(room_id).check_word(word)
        if word_level is not None:
            return {"room_id": room_id, "word_level": word_level, "color": player_info["player"]["color"]}
    return None


def get_player_info(sid):
    for room in rooms:
        players = rooms.get(room).get_players()
        if sid in players:
            return {"room_id": rooms.get(room).get_id(), "player": players[sid]}
    return None


def print_rooms():
    print("Rooms--------------------")
    for room in rooms:
        print("  Room id: {}\n  Players: {}\n  Words: {}\n  -----------------------".format(rooms.get(room).id, rooms.get(room).players, rooms.get(room).words))