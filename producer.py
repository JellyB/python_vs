import json
import random
import pika

print('pika version: %s' % pika.__version__)

credentials = pika.PlainCredentials(username='rabbitmq_ztk', password='rabbitmq_ztk')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.100.21', 5672, credentials=credentials))
main_channel = connection.channel()
main_channel.queue_declare(queue='live.course.end.notice', durable=True)
# main_channel.exchange_declare(exchange='', exchange_type='direct')
# main_channel.exchange_declare(exchange='', exchange_type='direct')

users = ['0287341823', '123412341234', '1234123414', '123412341234', '132412341234']


def get_user():
    return random.choice(users)


_COUNT_ = 10

for i in range(0, _COUNT_):
    user_id = get_user()
    msg = {
        'classId': '99072',
        'syllabusId': '81324123',
        'userId': user_id,
        'courseWareId': '2341234'
    }
    main_channel.basic_publish(
        exchange='',
        routing_key='live.course.end.notice',
        body=json.dumps(msg),
        properties=pika.BasicProperties(content_type='text/plain'))
    print('send ticker %s' % user_id)

connection.close()