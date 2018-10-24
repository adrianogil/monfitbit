import os
import csv

import datetime

sleep_data_csv_file = os.environ['FITBIT_SLEEP_DATA']

last_week_sleep = []

with open(sleep_data_csv_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sleep_start_time = row['Start Time']
        sleep_start_time = datetime.datetime.strptime(sleep_start_time, "%Y-%m-%d %I:%M%p")
        # print(sleep_end_time)

        diff_time = datetime.datetime.now() - sleep_start_time

        if diff_time.days < 7:
            last_week_sleep.append(int(row['Minutes Asleep']))

print('Sleep in last week:')

mean_minutes_time = 0.0
total_registers = 0

for d in last_week_sleep:
    hours = d / 60
    minutes = d - hours * 60

    mean_minutes_time = mean_minutes_time + d
    total_registers = total_registers + 1

    print('- %d hours, %d minutes' % (hours, minutes) )


mean_minutes_time = mean_minutes_time * 1.0 / total_registers

hours = int(mean_minutes_time / 60)
minutes = mean_minutes_time - hours * 60
print('Mean sleep time: %d hours, %d minutes' % (hours, minutes) )