import time
import random
from celery import Celery

app=Celery('tasks')
@app.task
def cal_decombobulator_xy():
    time.sleep(random.randint(0,5))
    print("task done!")

@app.task
def kill_joel():
    request.get("http://http://10.0.10.221:8000/")
