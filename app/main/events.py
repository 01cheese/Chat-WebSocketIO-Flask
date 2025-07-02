from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit('status', {
        'msg': f"{session.get('name')} has entered the room.",
    }, to=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    name = session.get('name')
    msg_content = message.get('msg', '').strip()

    if not msg_content:
        return
    emit('message', {
        'msg': f"{name}: {msg_content}"
    }, to=room)



@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status', {
        'msg': f"{session.get('name')} has left the room.",
    }, to=room)

