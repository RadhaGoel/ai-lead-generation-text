from apscheduler.schedulers.blocking import BlockingScheduler
from main import main

scheduler = BlockingScheduler()

# run the agent every 6 hours
scheduler.add_job(main, "interval", hours=6)

print("Scheduler started. Agent will run every 6 hours.")

scheduler.start()