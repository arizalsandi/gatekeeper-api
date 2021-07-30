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

Run `gatekeeper.py` to enable gatekeeper API and run `kafka_consumer.py` to start consume Topic from API

After Gatekeeper and Kafka Consumer started, go to Insomnia and use this link (http://127.0.0.1:5000/activities) and post the Payload like bellow here to create the Event

```
{
    "activities": [
        {
            "operation": "insert",
            "table": "table100",
            "column":[
                {
                "name":"col101",
                "type":"INTEGER",
                "value":101
                },
						{
                "name":"col102",
                "type":"INTEGER",
                "value":102
                },
						{
                "name":"col103",
                "type":"INTEGER",
                "value":103
              }
				]
		}
 ]
}
```



If the payload valid, it will return Json notification like this :

![Screenshot from 2021-07-30 16-04-44](https://user-images.githubusercontent.com/84316622/127629658-33ab3e71-8d8f-40a4-b77f-11d3c45516f6.png)

For invalid case, im still only add for Invalid Operation and for the other case will be improving later.


