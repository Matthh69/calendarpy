/*

    TABLE CREATION

*/

--Table to store calendar
CREATE TABLE calendar (
    id INTEGER PRIMARY KEY,
    --link TEXT // Will use id instead
);

--Table to store event (messages posted by users)
CREATE TABLE event (
    id INTEGER PRIMARY KEY,
    event_date DATETIME, --Format ('YYYY-MM-DD hh:mm:ss')
    txt_content TEXT,
    id_cal INTEGER REFERENCES calendar (id));

--Creation of dummy content

--Calendar
INSERT INTO calendar VALUES (1);
INSERT INTO calendar VALUES (2);

--Messages
INSERT INTO event VALUES (1, '2022-10-10 11:24:55', 'Premier message', 1);
INSERT INTO event VALUES (2, '2022-10-10 15:54:06', 'Maths en L697', 1);
INSERT INTO event VALUES (3, '2022-10-14 08:11:25', 'Histoire géo en L265', 1);


INSERT INTO event VALUES (1, '2023-10-10 11:24:55', 'Premier message', 2);
INSERT INTO event VALUES (2, '2023-10-10 15:54:06', 'Maths en L697', 2);
INSERT INTO event VALUES (3, '2023-10-14 08:11:25', 'Histoire géo en L265', 2);