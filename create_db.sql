DROP DATABASE IF EXISTS bulk_insert_experiment;

DROP ROLE IF EXISTS bulk_insert_experiment;

CREATE DATABASE bulk_insert_experiment;

CREATE USER bulk_insert_experiment WITH PASSWORD 'bulk_insert_experiment';

GRANT ALL PRIVILEGES ON DATABASE bulk_insert_experiment TO bulk_insert_experiment;
