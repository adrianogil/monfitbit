# Define FITBIT_SLEEP_DATA
# Define FITBIT_SCRIPTS_SRC

function awake-time()
{
    p2 $FITBIT_SCRIPTS_SRC/get_awake_time.py 
}