#!/usr/bin/env python
import pika

creds =pika.credentials.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='queue',
                                                               credentials=creds,
                                                               port=5672
                                                               ))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()