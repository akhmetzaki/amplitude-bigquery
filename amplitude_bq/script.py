from .amplitudebq import main
from datetime import datetime, timedelta

START_DATE = datetime.strptime('20211020', '%Y%m%d')
END_DATE = (datetime.utcnow().date() - timedelta(days=1)).strftime('%Y%m%d')


def historic_parse():
    global START_DATE
    start_date = START_DATE
    while start_date != END_DATE:
        main(start_date.strftime('%Y%m%d'))
        start_date = start_date + timedelta(days=1)


if __name__ == '__main__':
    historic_parse()
