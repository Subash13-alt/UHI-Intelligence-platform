from apscheduler.schedulers.background import BackgroundScheduler
from app.services.data_update import update_all_data

scheduler = BackgroundScheduler()
scheduler.add_job(update_all_data, 'interval', hours=24)
scheduler.start()
