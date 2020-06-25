import json
import datetime
"""
This file has methods that convert to JSON or from JSON the values that are passed in them.
    See documentation of json module.
"""
def send_json(data):

    return json.dumps(data)

def convert_date(o):
    """
    This function converts an instance of datetime.datetime to an string object that can now be inserted into a JSON.
    @param o: value of a datetime.datetime
    @return: it returns the datetime value in a string format.
    """
    if isinstance(o, datetime.datetime):

        return o.__str__()

def recv_json(recv_data):

    return json.loads(recv_data)

def sendTicketsToJson(data):

    return json.dumps({ticket.ticketToJson() for ticket in data},indent=4)

def dumpTicket(ticket):

    return json.dumps(ticket , indent= 4)


