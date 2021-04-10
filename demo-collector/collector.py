from flask import Flask
from flask import request, render_template
from kafka import KafkaProducer

import json

producer = KafkaProducer(value_serializer=lambda v:json.dumps(v).encode('utf-8'),bootstrap_servers='localhost:9092')
DEMO_TOPIC = 'demo-topic'

#create topic command
#bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic demo-topic

#consume command
#bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic demo-topic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/demo', methods=['POST'])
def collect_events():
    request_data = json.loads(request.data) #request.get_json()
    print ("input: ", str(request_data))
    print ("")

    ret = {}
    """
        {
        "data": {
            "content_ids": ["tmanh17", "manhdt"], 
            "content_name": "CompleteRegistration",
            "content_category": "Conversion"
        },
        "timestamp": 1573724975688,
        "status": "Ok",
        "name": "ViewContent",
        "session_id": "1dpkl2skp:4nqm04f7t"
        }
    """
    ret['data_content_ids'] = request_data['data']['content_ids']
    ret['data_content_name'] = request_data['data']['content_name']
    ret['data_content_category'] = request_data['data']['content_category']

    ret['timestamp'] = request_data['timestamp']
    ret['status'] = request_data['status']
    ret['name'] = request_data['name']
    ret['session_id'] = request_data['session_id']

    print ("output: ", str(ret))
    producer.send(DEMO_TOPIC, str(ret))
    producer.flush()

    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)