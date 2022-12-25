from flask import Flask, json
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit, join_room, leave_room

import pprint
import word_model

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# enable CORS
CORS(app)

# rest
@app.route("/get_list")
def get_list():
    words = word_model.get_words_list("собака", 15)

    response = app.response_class(
        response=json.dumps(words),
        status=200,
        mimetype='application/json'
    )
    return response


# WebSocket
socketio = SocketIO(app, cors_allowed_origins='*')


@socketio.on('connect')
def connect(data, methods=['GET']):
    print('Client connect')
    send("Client connect!", broadcast=True)


@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')
    send("Client disconnected!", broadcast=True)




@socketio.on('join')
def on_join(data):
    username = data['username']
    print(username + ' has entered the room.')
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    print(username + ' has left the room.')
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)



@socketio.on('my_event')
def my_event(data, methods=['GET']):
    send("pong")


socketio.run(app, host='192.168.1.11', port=5000, debug=True)
