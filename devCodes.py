import os
from datetime import datetime

def DevCode1():
    print("DEVCODE1 is running!")

def Time():
    now = datetime.now()
    print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")