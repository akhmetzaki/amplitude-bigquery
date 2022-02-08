from amplitudebq import main
from datetime import datetime, timedelta
import zipfile
START_DATE = '20211031'
END_DATE = (datetime.utcnow().date() - timedelta(days=1)).strftime('%Y%m%d')


def historic_parse():
    # global END_DATE, START_DATE
    end_date = END_DATE
    while end_date != START_DATE:
        try:
            main(end_date)
        except zipfile.BadZipfile as e:
            print('empty zipfile', end_date)
        end_date = (datetime.strptime(end_date, '%Y%m%d') - timedelta(days=1)).strftime('%Y%m%d')


if __name__ == '__main__':
    historic_parse()
