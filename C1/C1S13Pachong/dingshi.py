from datetime import datetime
from threading import Timer
# 打印时间函数
def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t = Timer(inc, printTime, (inc,))
    t.start()
# 5s
printTime(5)


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
