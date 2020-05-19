import json
import datetime
def sendJson(socket,data):

    json_data = json.dumps(data).encode()
    socket.send(json_data)



def convertDateJson(o):

    if isinstance(o, datetime.datetime):

        return o.__str__()



def recvJson(socket):

    recv_data = socket.recv(1024)

    return json.loads(recv_data, encoding="utf-8")

def sendTicketsToJson(data):

    return json.dumps({'Filtred tickets':[ticket.ticketToJson() for ticket in data]},indent=4)

def dumpTicket(ticket):

    return json.dumps(ticket , indent= 4)


