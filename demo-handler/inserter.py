from kafka import KafkaConsumer

DEMO_TOPIC = 'demo-topic'

consumer = KafkaConsumer(DEMO_TOPIC)
for message in consumer:
    print (message)