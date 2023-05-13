/*

    TABLE CREATION

*/

--Table to store calendar
DROP TABLE IF EXISTS calendar;
CREATE TABLE calendar (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    --link TEXT // Will use id instead
);

--Table to store event (messages posted by users)
DROP TABLE IF EXISTS event;
CREATE TABLE event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_date DATETIME, --Format ('YYYY-MM-DD hh:mm:ss')
    txt_content TEXT,
    id_cal INTEGER REFERENCES calendar (id));

--Creation of dummy content

--Calendar
INSERT INTO calendar VALUES (1);
INSERT INTO calendar VALUES (2);

--Messages
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2022-10-10 11:24:55', 'Premier message', 1);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2022-10-10 15:54:06', 'Maths en L697', 1);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2022-10-11 14:31:44', 'Histoire géo en L265', 1);

--Messages second calendrier

INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-10-09 11:24:55', 'Premier message', 2);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-10-10 15:54:06', 'Maths en L697', 2);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-10-11 08:11:25', 'Histoire géo en L265', 2);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-10-11 14:31:44', 'Histoire géo en L265', 2);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-10-12 19:00:52', 'Pour demain il faut faire ça', 2);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-10-13 09:26:18', 'Y a steak frites à la cantine', 2);


/*



--Table pour stocker le calendrier
DROP TABLE IF EXISTS calendar;
CREATE TABLE calendar (
id INTEGER PRIMARY KEY AUTOINCREMENT
);

--Table pour stocker les événements (messages postés par les utilisateurs)
DROP TABLE IF EXISTS event;
CREATE TABLE event (
id INTEGER PRIMARY KEY AUTOINCREMENT,
event_date DATETIME,
txt_content TEXT,
id_cal INTEGER REFERENCES calendar (id),
hash TEXT
);

--Création de contenu fictif
--Calendrier
INSERT INTO calendar VALUES (1);
INSERT INTO calendar VALUES (2);

--Messages
INSERT INTO event (event_date, txt_content, id_cal, hash) VALUES ('2022-10-10 11:24:55', 'Premier message', 1, SHA1(CAST(id_cal AS TEXT)));
INSERT INTO event (event_date, txt_content, id_cal, hash) VALUES ('2022-10-10 15:54:06', 'Maths en L697', 1, SHA1(CAST(id_cal AS TEXT)));
INSERT INTO event (event_date, txt_content, id_cal, hash) VALUES ('2022-10-11 14:31:44', 'Histoire géo en L265', 1, SHA1(CAST(id_cal AS TEXT)));

--Messages deuxième calendrier
INSERT INTO event (event_date, txt_content, id_cal, hash) VALUES ('2023-10-09 11:24:55', 'Premier message', 2, SHA1(CAST(id_cal AS TEXT)));
INSERT INTO event (event_date, txt_content, id_cal, hash) VALUES ('2023-10-10 15:54:06', 'Maths en L697', 2, SHA1(CAST(id_cal AS TEXT)));
INSERT INTO event (event_date, txt_content, id_cal, hash) VALUES ('2023-10-11 08:11:25', 'Histoire géo en L265', 2, SHA1(CAST(id_cal AS TEXT)));
INSERT INTO event (event_date, txt_content, id_cal, hash) VALUES ('2023-10-11 14:31:44', 'Histoire géo en L265', 2, SHA1(CAST(id_cal AS TEXT)));
INSERT INTO event (event_date, txt_content, id_cal, hash) VALUES ('2023-10-12 19:00:52', 'Pour demain il faut faire ça', 2, SHA1(CAST(id_cal AS TEXT)));
INSERT INTO event (event_date, txt_content, id_cal, hash) VALUES ('2023-10-13 09:26:18', 'Y a steak frites à la cantine', 2, SHA1(CAST(id_cal AS TEXT)));


*/
