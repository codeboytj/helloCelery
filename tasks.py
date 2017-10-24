# coding=utf-8
from celery import Celery

# Celery 的第一个参数是当前模块的名称，这个参数是必须的，这样的话名称可以自动生成。
# 第二个参数是中间人关键字参数，指定你所使用的消息中间人的 URL，此处使用了 RabbitMQ，也是默认的选项。
# 例如，对于 RabbitMQ 你可以写 amqp://localhost ，而对于 Redis 你可以写 redis://localhost .
app = Celery('tasks', broker='amqp://guest@localhost//')

# 定义了一个单一任务，称为 add ，返回两个数字的和。
@app.task
def add(x, y):
    return x + y