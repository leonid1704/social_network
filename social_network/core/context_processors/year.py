import datetime


def year(request):
    """add year"""
    return {
        'year': datetime.datetime.now().year
    }
