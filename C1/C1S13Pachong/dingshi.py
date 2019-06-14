from datetime import datetime
from threading import Timer
# 打印时间函数
def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t = Timer(inc, printTime, (inc,))
    t.start()
# 5s
printTime(5)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# APSchedular 定时任务框架 BlockingScheduler 和 BackgroundScheduler
# APScheduler 四个组件分别为：
# 触发器(trigger)： date, interval, cron(特定周期性)
# 业存储(job store)：APScheduler 默认使用 MemoryJobStore，可以修改使用 DB 存储方案
# 执行器(executor)：在作业中提交制定的可调用对象到一个线程或者进城池来进行。
#                  当作业完成时，执行器将会通知调度器。
#                  ProcessPoolExecutor    ThreadPoolExecutor*
# 调度器(scheduler)。
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=6, minute=30)
scheduler.start()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from datetime import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler
 
def tick():
    print('Tick! The time is: %s' % datetime.now())
 
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    # 间隔3秒钟执行一次
    scheduler.add_job(tick, 'interval', seconds=3)
    # 这里的调度任务是独立的一个线程
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # 其他任务是独立的线程执行
        while True:
            time.sleep(2)
            print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print('Exit The Job!')
