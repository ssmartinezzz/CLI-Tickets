import datetime


def formatDate(date):
    if (date == ""):
        pass
    else:
        return datetime.datetime.strptime(date, "%d/%m/%Y")




