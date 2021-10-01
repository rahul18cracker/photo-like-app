# This module will act as a consumer for the RabbitMQ, it will create and push messages on the message bus
import pika

params = pika.URLParameters('amqps://zsndkndb:qtENlLY3K4LLXJGMJ41hNpHzvmBiBPRB@gull.rmq.cloudamqp.com/zsndkndb')

# connect to rabbit MQ service
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch,
             method,
             properties,
             body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin',
                      on_message_callback=callback)
print("Started consuming")

channel.start_consuming()

channel.close()
