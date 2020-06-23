import json
import datetime
def sendJson(data):

    return json.dumps(data)

def convertDateJson(o):

    if isinstance(o, datetime.datetime):

        return o.__str__()

def recvJson(recv_data):

    return json.loads(recv_data)

def sendTicketsToJson(data):

    return json.dumps({ticket.ticketToJson() for ticket in data},indent=4)

def dumpTicket(ticket):

    return json.dumps(ticket , indent= 4)


