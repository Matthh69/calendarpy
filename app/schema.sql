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

/*
    DEMO QUERIES

    4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a
*/

--Calendar
INSERT INTO calendar VALUES (4);

/*
    HASH : 4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce
    LINK : http://127.0.0.1:5000/calendar/2023-06-28/4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce
*/


--Messages

/*
    WEEK 0
*/

--Monday 19
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-19 08:24:55', 'Bonjour, vous en êtes où du front ?', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2021-06-19 10:20:00', 'On a bientôt terminé, il nous manques qq images', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-19 12:54:55', 'Super, penser a commit sur GIT', 4);

--Tuesday 20
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-20 08:24:55', 'On a eu un soucis pour commit sur git !', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-20 10:20:00', 'Qu''est ce qu''il s''est passé ?', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-20 12:54:55', 'Un soucis avec le merge', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-20 12:57:55', 'Ok on verra ça demain', 4);

--Wednesday 21
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-21 08:24:55', 'Hello on se voit en L325 après le cours de C#', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-21 10:20:00', 'Oui pas de soucis à tt de suite', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-21 12:54:55', 'Je vais chercher un sandwich j''arrive !', 4);

--Thursday 22
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-22 08:24:55', 'J''ai eu un soucis avec le project en C# quelqu''un peut il m''aider', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-22 10:20:00', 'Oui je suis en L238 si tu a besoins', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-22 12:54:55', 'Ah ok je suis a Berthet encore !', 4);

--Friday 23
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-23 08:24:55', 'Bonjour on a cours aujourd''hui ?', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-23 10:20:00', 'Non mais on doit se voir à 10h pour finaliser le projet MESI', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-23 12:54:55', 'Ah oui c''est vrai ! En quelle salle ?', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-23 13:01:35', 'En L324', 4);

/*
    WEEK 1
*/

--Monday 26
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-26 08:24:55', 'Aujourd''hui nous avons rdv à 13h en salle L324 pour travail le rapport du projet MESI', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-26 10:20:00', 'N''oubliez pas vos ordinateur', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-26 12:54:55', 'Juste pour vous dire que je serai en retard de 10 minutes environ', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-26 13:01:35', 'Nous avons changer de salle nous sommes en L432', 4);

--Tuesday 27
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-27 09:12:30', 'Bonjour, aujourd''hui nous allons travailler sur la présentation et le powerpoint tjrs à 13h en L490', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-27 10:16:30', 'Oui d''accord il faut penser a mettre en partage le pptx', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-27 18:49:30', 'J''ai eu un soucis de PC quelqu''un peut il m''envoyer le pptx ?', 4);

--Wednesday 28
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-28 09:12:30', 'L321 pour ajourd''hui tjrs à 13h', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-28 10:16:30', 'Non ajourd''hui on va manger Italien à 13h, il y a les Rotolos', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-28 18:49:30', 'Ah ouais c''est vrai reservez moi un plats S.V.P', 4);

--Thursday 29
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-29 09:12:30', 'Aujourd''hui notre passage en soutenance pour MESI', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-29 10:16:30', 'Dernière ligne droite réviser bien vos passages', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-29 18:49:30', 'Good luck les amis', 4);

--Friday 30
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-30 09:12:30', 'Merci à tous pour votre implication dans le projet on a vraimment assurer sur la présentation', 4);
INSERT INTO event (event_date, txt_content, id_cal) VALUES ('2023-06-30 10:16:30', 'Oui bravo à tous et merci encore', 4);