#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import telebot
import paho.mqtt.client as mqtt

if "TELEINTERCOM_TOKEN" in os.environ:
    if len(os.environ['TELEINTERCOM_TOKEN']) == 45:
        TELEINTERCOM_TOKEN = os.environ['TELEINTERCOM_TOKEN']
else:
    print ('Telegram API Token is not set')
    raise AssertionError("Please configure API_TOKEN as environment variables")

if "MQTT_IP" in os.environ:
    MQTT_IP = os.environ['TELEIMQTT_IPNTERCOM_TOKEN']
else:
    print ('MQTT_IP is not set')
    raise AssertionError("Please configure MQTT_IP as environment variables")

SBSCR_TOPIC = 'open'
PORT = 1883

bot = telebot.TeleBot(TELEINTERCOM_TOKEN)
client = mqtt.Client()
client.connect(MQTT_IP, PORT, 60)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['open'])
def send_open(message):
    bot.send_message(message.chat.id, 'Please wait for 4 seconds')
    client.publish('open', '1')
    print(message.chat.id)


bot.polling()