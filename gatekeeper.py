from flask import Flask, jsonify, request
from kafka import KafkaProducer
import json

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:9092'],
    value_serializer=lambda m: json.dumps(m).encode('utf-8'))

def process_data(data):
    producer.send('activities',data)

@app.route("/activities", methods=["POST"])
def read_item():
    input_data = request.json
    for activity in input_data['activities']:
        if activity['operation'] not in ['insert', 'delete']:
            error_msg = 'activity operation not allowed'
            return jsonify(
                message=error_msg,
                category="error",
                status=404
            )
        process_data(activity)
        return jsonify(message="success")

if __name__ == "__main__":
    app.run(debug=True)