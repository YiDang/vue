from datetime import datetime

def isDateFuture(date1):
    date_format = '%m/%d/%Y'
    date_formalized = datetime.strptime(date1, date_format)
    delta = (datetime.today() - date_formalized).days
    return delta > 0
