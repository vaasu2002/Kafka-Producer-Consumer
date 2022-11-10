import argparse

from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from src.entity.generic import Generic
from src.kafka_config import sasl_conf
from src.database.mongodb import MongodbOperation




def consumer_using_sample_file(topic,file_path):
    schema_str = Generic.get_schema_to_produce_consume_data(file_path=file_path)
    json_deserializer = JSONDeserializer(schema_str,
                                         from_dict=Generic.dict_to_object)

    consumer_conf = sasl_conf() # Kafka cluster configuration
    consumer_conf.update({ # we need to specify the group id so kafka know from where it has to start reading data
        'group.id': 'group2', # group id
        'auto.offset.reset': "earliest"}) # row number

    consumer = Consumer(consumer_conf) # Created consumer
    consumer.subscribe([topic])

    mongodb = MongodbOperation()
    records = [] # list to store records (batch insertion)
    x = 0 # tracker
    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            record: Generic = json_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE)) # we will be reading one record at a time as object


            if record is not None:
                records.append(record.to_dict())
                if x % 5000 == 0: # once there will be 5000 records we will inside record into mongodb(batch insertion)
                    mongodb.insert_many(collection_name="kafka-sensor-topic", records=records)
                    records = [] # again record list empty
            x = x + 1 # tracker append
        except KeyboardInterrupt:
            break

    consumer.close()
