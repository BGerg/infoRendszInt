from random import randint
from time import sleep

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


class Color:
    RED = "RED"
    BLUE = "BLUE"
    GREEN = "GREEN"


color_repo = {
    1: Color.RED,
    2: Color.GREEN,
    3: Color.BLUE
}


for i in range(20):
    color = color_repo[randint(1, 3)]
    channel.basic_publish(exchange='', routing_key='/queue/colorQueue', body=color)
    print(f" [x] Sent '{color}'")
    sleep(0.1)

connection.close()

