import datetime
import messages


def formatDate(date):
    if (date == ""):
        pass
    else:
        return datetime.datetime.strptime(date, "%d/%m/%Y")



def idValidator(id):
    try:
        int(id)
        return True
    except ValueError:
        return False

def checkStatus(status):
    if ((status == "pending") |(status == "in process") |(status == "solved")):

        pass

    else:

        print(messages.ERR_MSG_STATUS)




