import requests
import time
from datetime import datetime
import psutils
import argparse

try:
    parser = argparse.ArgumentParser(description='Crash Inspector Tool')
    parser.add_argument("token", type=str, help="Token assigned by Telegram when creating your Bot")
    parser.add_argument("user_id", type=str, help="User ID on Telegram")
    parser.add_argument("process_name", type=str, help="Name of the process to monitor")
    parser.add_argument("interval", type=int, help="Time interval in seconds to check the process")
    args = parser.parse_args()

except Exception as e:
    print(f"Error: {type(e)}")

while True:
    found = False
    for proc in psutils.process_iter():
        if (args.process.name() == args.process_name):
            print(args.process_name + " is running" + str(datetime.now()))
            found = True

        if (found == False):
            message = f"Process {args.process_name} is not running at {datetime.now()}"
            print(message)
            url = f"https://api.telegram.org/bot{args.token}/sendMessage?chat_id={args.user_id}&text={message}"
            requests.get(url).json
            quit()

    time.sleep(args.interval * 60)