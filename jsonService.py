import json
import models
def sendJson(socket,data):

    json_data = json.dumps(data).encode()
    socket.send(json_data)

"""
    json_data = json.JSONEncoder().encode(data)

    socket.send(json_data)

"""
def recvJson(socket):

    recv_data = socket.recv(1024)

    return json.loads(recv_data, encoding="utf-8")

def sendTicketToJson(data):

    return json.dumps(dict (r) for r in data.ticketToJson())



