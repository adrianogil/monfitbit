# Define FITBIT_SLEEP_DATA
# Define FITBIT_SCRIPTS_SRC

function fitbit-awake-time()
{
    p2 $FITBIT_SCRIPTS_SRC/get_awake_time.py 
}

function fitbit-sleep-last-week()
{
    p2 $FITBIT_SCRIPTS_SRC/last_week_sleep.py
}