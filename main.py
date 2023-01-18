import ctypes
import os
from config import Config
import time
from apscheduler.schedulers.background import BlockingScheduler
def check(hours):
    print("hmm")
    lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
    if hour>=hours:
        sched.pause()
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Your screen time exceeded 2 hours, its time to shutdown the system.\nIf the system is not turned off in 10 minutes, system is auto-shutting down.', 'TimeUp', 0)
        time.sleep(600)
        os.system('shutdown -s')
        # sched.pause()

sched = BlockingScheduler(timezone="Asia/Kolkata")
sched.add_job(check,trigger='interval',args=[Config.hours,],seconds=1)
sched.start()
