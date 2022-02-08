from amplitudebq import main
from datetime import datetime, timedelta
import zipfile
START_DATE = datetime.strptime('20211031', '%Y%m%d')
END_DATE = (datetime.utcnow().date() - timedelta(days=1)).strftime('%Y%m%d')


def historic_parse():
    # global END_DATE, START_DATE
    end_date = END_DATE
    while end_date != START_DATE:
        try:
            main(end_date.strftime('%Y%m%d'))
        except zipfile.BadZipfile as e:
            print('empty zipfile', end_date.strftime('%Y%m%d'))
        end_date = end_date - timedelta(days=1)


if __name__ == '__main__':
    historic_parse()
