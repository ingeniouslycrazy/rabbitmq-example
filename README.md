# RabbitMQ-Example

## About 
This project contains a Python app to
- send messages to a RabbitMQ queue
- receive messages from a RabbitMQ queue
as well as an example dev environment.

You will need Docker or Podman to run this example

## Setup

You can start with pulling the 2 base images, a RabbitMQ image to run a dev server for local testing and a Python image to run the project source code.

```
docker pull python:3.14.2-slim-trixie
docker pull rabbitmq:4.2.3 
```

Next lets build custom images using the base images. For RabbitMQ we will enable the admin UI, for Python we will install the dependency `pika`, which lets us make connections to a RabbitMQ server. You can build both with:

```
docker compose build
```

## Usage (local dev env)

Before sending or receiving messages, we need a RabbitMQ server to respond to those requests. We can start a local server with:

```
docker compose up -d
```

This will start a RabbitMQ server with hostname "queue" and exposed ports 15672, 15692, and 5672. Those ports are 15672 for a UI, 15692 for a Prometheus Exporter API, and 5672 for connecting to the RabbitMQ server.

Next we will start the consumer, which will run until stopped by the user and wait for incoming messages. We do so with:

```
docker compose run --rm cli python consumer.py
```

Last but not least we need to send messages. In order to do that we need a second terminal, becaue the first one is used by the consumer. Open a second terminal and start the producer with:

```
docker compose run --rm cli python producer.py
```

The producer will send a "Hello World" to RabbitMQ and the consumer will receive this message. You can test this by checking the first terminal with the consumer after sending one or many messages.