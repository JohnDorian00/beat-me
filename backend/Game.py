import word_model
import random
import pprint

rooms = {}


class Room:
    # The init method or constructor
    def __init__(self, creator):
        # Instance Variable
        # Start values
        self.players = {}
        self.id = str(len(rooms))
        self.colors = {"#FF0000": False, "#FFE800": False, "#11FF00": False, "#00FFF7": False, "#000DFF": False, "#C800FF": False}

        # Restart values
        self.word = "день"
        self.words = word_model.get_words_list(self.word, 15)
        self.words.insert(0, self.word)
        self.answeredWords = []
        self.winner = None

        # Start init
        self.add_player(creator)
        rooms[self.id] = self

    def add_player(self, player):
        self.players[player["sid"]] = {"name": player["name"], "color": self.get_random_color()}

    def remove_player(self, player):
        self.players.pop(player["id"])

    def get_players(self):
        return self.players

    def get_player(self, sid):
        player = self.players.get(sid)
        player["sid"] = sid
        return player

    def get_winner(self):
        return self.winner

    def get_words(self):
        return self.answeredWords

    def get_random_color(self):
        color = random.choice(list(self.colors.keys()))
        if self.colors[color] is True:
            self.get_random_color()
        else:
            self.colors[color] = True
            return color

    def check_word(self, word, sid):
        player = self.get_player(sid)
        if word in self.words and sid is not None and player is not None:
            self.answeredWords.append({"word": word, "lvl": self.words.index(word) + 1, "sid": player["sid"], "color": player["color"]})
            if word == self.word:
                self.winner = {"sid": player["sid"], "color": player["color"], "name": player["name"]}
                return True
            else:
                return False
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


def join_room(room_id, player):
    room = rooms.get(room_id)
    if room is not None:
        room.add_player(player)
        return room
    return None


def leave_room(room_code, player):
    rooms.get(room_code).remove_player(player)
    return


def get_winner(room_id):
    room = rooms.get(room_id)
    if room is not None:
        return room.get_winner()


def send_word(sid, word):
    # print('Word from player "{}" is "{}"'.format(sid, word))
    player_info = get_player_info(sid)
    room_id = player_info["room_id"]
    if room_id is not None:
        room = rooms.get(room_id)
        result = room.check_word(word, sid)
        if result is not None:
            return {"room_id": room_id, "isFin": room.get_winner()}
    return None


def get_player_info(sid):
    for room in rooms:
        players = rooms.get(room).get_players()
        if sid in players:
            return {"room_id": rooms.get(room).get_id(), "player": players[sid]}
    return None


def get_players(room_id):
    room = rooms.get(room_id)
    if room is not None:
        return room.get_players()
    return None


def get_words(room_id):
    room = rooms.get(room_id)
    if room is not None:
        return room.get_words()
    return None


def print_rooms():
    print("Rooms--------------------")
    for room in rooms:
        print("  Room id: {}\n  Players: {}\n  Words: {}\n  -----------------------".format(rooms.get(room).id, rooms.get(room).players, rooms.get(room).words))