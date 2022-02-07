import pandas as pd
import json


def parse_json():
    with open('bigquery-schema-events.json', 'r') as f:
        events_df = pd.DataFrame(json.loads(f.read()))

    with open('bigquery-schema-events-properties.json') as f:
        prop_df = pd.DataFrame(json.loads(f.read()))

    events_df.to_csv('events.csv')
    prop_df.to_csv('props.csv')


if __name__ == '__main__':
    parse_json()