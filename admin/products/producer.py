# This module will act as a producer for the RabbitMQ, it will create and push messages on the message bus
import pika

params = pika.URLParameters('amqps://zsndkndb:qtENlLY3K4LLXJGMJ41hNpHzvmBiBPRB@gull.rmq.cloudamqp.com/zsndkndb')

# connect to rabbit MQ service
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish():
    channel.basic_publish(exchange='',
                          routing_key='admin',
                          body='hello')
