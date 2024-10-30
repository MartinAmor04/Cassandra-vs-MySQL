CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH REPLICATION = {
    'class': 'SimpleStrategy',
    'replication_factor': 1
};

USE my_keyspace;

CREATE TABLE IF NOT EXISTS sample_data (
    id int PRIMARY KEY,
    name text,
    value int
);
