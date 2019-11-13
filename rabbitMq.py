import pika


# https://www.cnblogs.com/pangguoping/p/5720134.html

def producer6():
    # 生产者
    credentials = pika.PlainCredentials(username='rabbitmq_ztk', password='rabbitmq_ztk')
    # 链接rabbit服务器（localhost是本机，如果是其他服务器请修改为ip地址）
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.100.21', 5672, credentials=credentials))
    # 创建频道
    channel = connection.channel()
    # 声明消息队列，消息将在这个队列中进行传递。如果将消息发送到不存在的队列，rabbitmq将会自动清除这些消息。如果队列不存在，则创建
    channel.queue_declare(queue='live.course.end.notice', durable=True)
    # exchange -- 它使我们能够确切地指定消息应该到live.course.end.notice哪个队列去。
    # 向队列插入数值 routing_key是队列名 body是要插入的内容


    channel.basic_publish(exchange='',
                          routing_key='live.course.end.notice',
                          body=b'helloworld')
    print("开始队列")
    # 缓冲区已经flush而且消息已经确认发送到了RabbitMQ中，关闭链接
    connection.close()

producer6()
