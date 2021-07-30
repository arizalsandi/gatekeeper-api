# Gatekeepr API : Payload Datastream Processing

Case : Create some Gatekeeper API to validate and processing incoming JSON message which come from our Backend team

## Gatekeeper APi Flow

![gatekeeper-api-flow](https://user-images.githubusercontent.com/84316622/127626592-efa39c30-cf4a-4f4b-a528-fa0f7081ca7f.jpg)

From this flow, the payload from API request will pass the Flask as Gatekeeper.

If the payload is valid, it will send into Kafka. 

Kafka will deliver the message as Topic to consumer

Consumer will consume message from kafka, and then the event will store to Postgresql

## Prerequisite
1. Python 3.6 or above
2. Flask
3. Kafka
4. Postgresql

## Setup
You need to start the Kafka environment such as Zookeeper service and Kafka service

Use this to enable Zookeeper Service :
```$ bin/zookeeper-server-start.sh config/zookeeper.properties```

And use this to enable Kafka service :
```$ bin/kafka-server-start.sh config/server.properties```

For reference, please use this official site to additional information :
[Apache Kafka Quickstart](https://kafka.apache.org/quickstart)








