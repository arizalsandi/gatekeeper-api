from kafka import KafkaConsumer
import psycopg2
import json
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')

consumer = KafkaConsumer (
    'activities',
    bootstrap_servers=['127.0.0.1:9092'],
    auto_offset_reset='earliest',
    group_id='activities',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

#Connect to Database
conn = psycopg2.connect('host=127.0.0.1 port=5432 dbname=blankspace user=blankspace password=blankspace')
conn.autocommit=True
cur = conn.cursor()

def create_table(message):
    column = ""
    for col in message['column']:
        column += f'{col["name"]} {col["type"]},'
    
    query_table = f'CREATE TABLE {message["table"]} ({column[:-1]} )'

    cur.execute(query_table)
    logging.warning('TABLE CREATED')
    insert_table(message)


def alter_table(message):
    logging.warning('ALTER TABLE')

def insert_table(message):
    col_name = ""
    col_val= ""
    for col in message["column"]:
        col_name += f'{col["name"]},'
        col_val += f'\'{col["value"]}\','
    
    insert_query = f" INSERT INTO {message['table']} ({col_name[:-1]}) VALUES ({col_val[:-1]})"

    cur.execute(insert_query)
    logging.warning('INSERT SUCCESS')

def delete_value(message):
    where_str=""
    for col in message["column"]:
        where_str += f' AND {col["name"]} - \'{col["value"]}\''
    delete_query = f'DELETE FROM {msg["table"]} where 1=1 {where_str}'
    cur.execute(delete_query)
    logging.warning('DELETE SUCCESS')
    
for message in consumer:
    #SELECT 1 FROM information_schema.tables
    cur.execute("select * from information_schema.tables where table_name=%s", (message.value["table"],))

    if message.value["operation"] == 'insert':
        if bool(cur.rowcount):
            insert_table(message.value)
        else:
            create_table(message.value)
    elif message.value["operation"] == 'delete':
        if bool(cur.rowcount):
            delete_value(message.value)

conn.commit()
conn.close()
