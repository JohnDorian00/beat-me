import pprint

from flask import Flask, json, request
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit, join_room, leave_room

import git

import Game

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# enable CORS
CORS(app)


# rest
@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('https://github.com/JohnDorian00/beat-me/tree/main/backend')
        origin = repo.remotes.origin

        origin.pull()

        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


    # WebSocket
socketio = SocketIO(app, cors_allowed_origins='*', logger=True, engineio_logger=True)


@socketio.on('connect')
def connect():
    print('Client connected sid = ', request.sid)
    send("Client connected! sid = " + request.sid)


@socketio.on('disconnect')
def disconnect():
    print('Client disconnected, sid = ', request.sid)
    # send("Client disconnected!", broadcast=True)


@socketio.on('creating_room')
def creating_room(user):
    user = {'sid': request.sid, 'name': user["name"]}
    room = Game.create_room(user)
    room_id = room.get_id()
    msg = "User {} joined room with id: {}".format(user, room_id)
    join_room(room_id)
    print(msg)
    send(msg, to=room_id)
    socketio.emit('join_response', room_id, to=request.sid)
    send_players(room_id)


@socketio.on('joining_room')
def joining_room(room_id, user):
    user = {'sid': request.sid, 'name': user["name"]}
    room = Game.join_room(room_id, user)
    if room is None:
        return
    msg = "User {} joined room with id: {}".format(user, room_id)
    join_room(room_id)
    print(msg)
    send(msg, to=room_id)
    socketio.emit('join_response', room_id, to=request.sid)
    send_players(room_id)


@socketio.on('word2back')
def word2back(word):
    result = Game.send_word(request.sid, word)
    if result is not None:
        send_words(result["room_id"])
        if result["isFin"] is not None:
            socketio.emit('fin', result["isFin"], to=result["room_id"])


def send_words(room_id):
    socketio.emit('send_words', Game.get_words(room_id), to=room_id)


def send_players(room_id):
    socketio.emit('send_players', Game.get_players(room_id), to=room_id)


def update_all(room_id):
    pass

@socketio.on('message')
def handle_message(data):
    print('received message: ', data)

# socketio.run(app, host='192.168.1.11', port=5000, debug=True)
