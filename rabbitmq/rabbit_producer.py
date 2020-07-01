# -*- coding: UTF-8 -*-
import math
import json
import copy
import collections
import os
import cv2
import time
import traceback
import pika

def producer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare('hello')
    count = 0
    while count < 100:
        count += 1
        print('produce a message')
        channel.basic_publish(exchange='', routing_key='hello', body='hello world!')
        time.sleep(2)
    connection.close()

if __name__ == "__main__":
    producer()