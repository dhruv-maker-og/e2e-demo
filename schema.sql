DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id    INTEGER PRIMARY KEY,
    name  TEXT NOT NULL,
    email TEXT NOT NULL
);

INSERT INTO users (name, email) VALUES
    ('Ada Lovelace',  'ada@example.com'),
    ('Alan Turing',   'alan@example.com'),
    ('Grace Hopper',  'grace@example.com');
