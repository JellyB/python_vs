import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.100.21'))
channel = connection.channel()


channel.queue_declare(queue='live.course.end.notice')

channel.basic_publish(exchange='', routing_key='',body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()