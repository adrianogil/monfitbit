import os
import csv

import datetime

sleep_data_csv_file = os.environ['FITBIT_SLEEP_DATA']

last_sleep_awake_time=None

with open(sleep_data_csv_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sleep_end_time = row['End Time']
        sleep_end_time = datetime.datetime.strptime(sleep_end_time, "%Y-%m-%d %I:%M%p")
        # print(sleep_end_time)

        if last_sleep_awake_time is not None:
            if sleep_end_time > last_sleep_awake_time:
                last_sleep_awake_time = sleep_end_time
        else:
            last_sleep_awake_time = sleep_end_time

diff_time = datetime.datetime.now() - last_sleep_awake_time

hours = diff_time.seconds / (60*60)
minutes = diff_time.seconds / 60 - hours * 60
seconds = diff_time.seconds - (60*60) * hours - minutes * 60

print('Time awake %d hours, %d minutes and %d seconds' % (hours, minutes, seconds) )