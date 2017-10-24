# helloCelery

## 安装依赖

```
pip install -r requirements.txt
```

安装erLang、RabbitMQ。

## 测试celery、rabbitmq以及task是否正确运行

安装完rabbitmq之后，应该会自动运行。现在在终端A可以打开worker来执行任务了：

```
celery -A tasks worker --loglevel=info
```

然后在python命令行里面执行：

```
>>> from tasks import add
>>> add.delay(3,4)
<AsyncResult: 2bccb202-87fa-4a09-82d8-c473e31a5868>
```

此时在终端A中就可以看到任务执行的结果了：

```
[2017-10-24 10:40:51,675: INFO/MainProcess] Received task: tasks.add[2bccb202-87fa-4a09-82d8-c473e31a5868]  
[2017-10-24 10:40:51,678: INFO/ForkPoolWorker-3] Task tasks.add[2bccb202-87fa-4a09-82d8-c473e31a5868] succeeded in 0.00029417199994s: 7
```