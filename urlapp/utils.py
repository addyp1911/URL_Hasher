
import re
import datetime

def url_validator(value):
    """A custom method to validate any website url """

    regex = re.compile(
            r'^https?://|www\.|https?://www\.|http?://www\.' # http://www. or https:// or www.
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|' #domain...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if value and not regex.match(value):
        raise AssertionError("The website url is invalid")
    return value


def get_date_range():
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    return yesterday, today
