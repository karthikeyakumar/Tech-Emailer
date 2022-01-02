import time
from apscheduler.schedulers.blocking import BlockingScheduler
from run import sendMail

sched = BlockingScheduler()


# @sched.scheduled_job("interval", minutes=1)
# def timed_job():
#     print("This job is run every one minute.")
#     sendMail()


@sched.scheduled_job("cron", day_of_week="mon-fri", hour=8)
def scheduled_job():
    print("This job is run every weekday at 8 AM.")
    sendMail()


sched.start()
