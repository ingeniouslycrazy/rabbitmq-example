#!/usr/bin/env python
import pika, sys, os # pyright: ignore[reportMissingModuleSource]

def main():
    creds =pika.credentials.PlainCredentials('user', 'password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='queue',
                                                                   credentials=creds,
                                                                   port=5672
                                                                   ))
    channel = connection.channel()
    
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

