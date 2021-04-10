CREATE EXTERNAL TABLE kafka_table
(`timestamp` timestamp , `page` string, `newPage` boolean,
added int, deleted bigint, delta double)
STORED BY 'org.apache.hadoop.hive.kafka.KafkaStorageHandler'
TBLPROPERTIES
("kafka.topic" = "hive-external-table",
"kafka.bootstrap.servers"="localhost:9092");

bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic hive-external-table
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic manhdt < "{1, "page", 1, 1, 1, 1.1}"
bin/kafka-console-consumer.sh --bootstrap-server localhost:909 --topic hive-external-table

{1, "page", 1, 1, 1, 1.1}