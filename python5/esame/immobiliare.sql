--1. Tabella filiali

CREATE TABLE filiali (
    partita_iva VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(100),
    indirizzo_sede VARCHAR(255),
    civico VARCHAR(10),
    telefono VARCHAR(20)
);

--2. Tabella case_in_vendita
CREATE TABLE case_in_vendita (
    catastale VARCHAR(20) PRIMARY KEY,
    indirizzo VARCHAR(255),
    numero_civico VARCHAR(10),
    piano VARCHAR(50),
    metri INTEGER,
    vani INTEGER,
    prezzo NUMERIC(15, 2),
    stato VARCHAR(10) CHECK (stato IN ('LIBERO', 'OCCUPATO')),
    filiale_proponente VARCHAR(50),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);

--3. Tabella case_in_affitto

CREATE TABLE case_in_affitto (
    catastale VARCHAR(20) PRIMARY KEY,
    indirizzo VARCHAR(255),
    civico VARCHAR(10),
    tipo_affitto VARCHAR(10) CHECK (tipo_affitto IN ('PARZIALE', 'TOTALE')),
    bagno_personale BOOLEAN,
    prezzo_mensile NUMERIC(15, 2),
    filiale_proponente VARCHAR(50),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);

--4. Tabella vendite_casa

CREATE TABLE vendite_casa (
    catastale VARCHAR(20),
    data_vendita DATE,
    filiale_proponente VARCHAR(50),
    filiale_venditrice VARCHAR(50),
    prezzo_vendita NUMERIC(15, 2),
    PRIMARY KEY (catastale, data_vendita),
    FOREIGN KEY (catastale) REFERENCES case_in_vendita(catastale),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva)
);

--5. Tabella affitti_casa

CREATE TABLE affitti_casa (
    catastale VARCHAR(20),
    data_affitto DATE,
    filiale_proponente VARCHAR(50),
    filiale_venditrice VARCHAR(50),
    prezzo_affitto NUMERIC(15, 2),
    durata_contratto INTERVAL,
    PRIMARY KEY (catastale, data_affitto),
    FOREIGN KEY (catastale) REFERENCES case_in_affitto(catastale),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva)
);


/*Passaggi per creare le tabelle su pgAdmin:

    Apri pgAdmin e connettiti al tuo database PostgreSQL.
    Nella Tree View di pgAdmin, seleziona il database in cui desideri creare le tabelle.
    Clicca con il tasto destro su Query Tool (Strumento di query) sotto la sezione "Schemi" del database.
    Copia e incolla il codice SQL per ciascuna tabella nell'editor delle query.
    Premi F5 o clicca su Execute per eseguire le query e creare le tabelle nel database.

Spiegazioni aggiuntive:

    Tipo NUMERIC(15, 2): viene usato per rappresentare valori numerici con due decimali (utile per i prezzi).
    Tipo VARCHAR: è usato per rappresentare stringhe di testo. La lunghezza massima (come VARCHAR(255)) può essere modificata in base alle tue necessità.
    Tipo BOOLEAN: rappresenta valori TRUE o FALSE, ad esempio per il campo bagno_personale.
    Tipo INTERVAL: viene usato per rappresentare una durata di tempo, come la durata di un contratto di affitto.
*/

--1. Inserimento Dati per la Tabella filiali
INSERT INTO filiali (partita_iva, nome, indirizzo_sede, civico, telefono)
VALUES
('IT12345678901', 'Filiale Roma', 'Via Roma', '10', '0612345678'),
('IT98765432100', 'Filiale Milano', 'Corso Italia', '25', '0223456789'),
('IT11223344556', 'Filiale Napoli', 'Piazza del Plebiscito', '5', '0812345678');

--2. Inserimento Dati per la Tabella case_in_vendita
INSERT INTO case_in_vendita (catastale, indirizzo, numero_civico, piano, metri, vani, prezzo, stato, filiale_proponente)
VALUES
('C12345', 'Via Roma', '10', '1°', 100, 4, 250000.00, 'LIBERO', 'IT12345678901'),
('C67890', 'Corso Italia', '25', '2°', 80, 3, 180000.00, 'OCCUPATO', 'IT98765432100'),
('C11223', 'Piazza del Plebiscito', '5', '3°', 120, 5, 350000.00, 'LIBERO', 'IT11223344556');

--3. Inserimento Dati per la Tabella case_in_affitto
INSERT INTO case_in_affitto (catastale, indirizzo, civico, tipo_affitto, bagno_personale, prezzo_mensile, filiale_proponente)
VALUES
('C12345', 'Via Roma', '10', 'TOTALE', true, 1000.00, 'IT12345678901'),
('C67890', 'Corso Italia', '25', 'PARZIALE', false, 700.00, 'IT98765432100'),
('C11223', 'Piazza del Plebiscito', '5', 'TOTALE', true, 1500.00, 'IT11223344556');

--4. Inserimento Dati per la Tabella vendite_casa
INSERT INTO vendite_casa (catastale, data_vendita, filiale_proponente, filiale_venditrice, prezzo_vendita)
VALUES
('C12345', '2025-01-15', 'IT12345678901', 'IT98765432100', 240000.00),
('C67890', '2025-02-20', 'IT98765432100', 'IT11223344556', 175000.00),
('C11223', '2025-03-10', 'IT11223344556', 'IT12345678901', 340000.00);

--5. Inserimento Dati per la Tabella affitti_casa
INSERT INTO affitti_casa (catastale, data_affitto, filiale_proponente, filiale_venditrice, prezzo_affitto, durata_contratto)
VALUES
('C12345', '2025-01-01', 'IT12345678901', 'IT98765432100', 1000.00, '1 year'),
('C67890', '2025-02-01', 'IT98765432100', 'IT11223344556', 700.00, '6 months'),
('C11223', '2025-03-01', 'IT11223344556', 'IT12345678901', 1500.00, '2 years');

/*
Sommario dei Dati Inseriti:

    Filiali: 3 filiali con i rispettivi dettagli.
    Case in Vendita: 3 case con dettagli relativi a indirizzo, metri, stato, prezzo e filiale proponente.
    Case in Affitto: 3 case in affitto con tipo di affitto, bagno personale, prezzo mensile e filiale proponente.
    Vendite Casa: 3 vendite, con data, prezzo e le filiali coinvolte.
    Affitti Casa: 3 affitti, con data, prezzo, durata del contratto e le filiali coinvolte.
*/


--UTENTI

CREATE TABLE utenti (
    utente VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255),
    privilegi CHAR(1) CHECK (privileggi IN ('w', 'r')),
    note VARCHAR(255),
    registrazione BOOLEAN
);


--INSERIMENTO

INSERT INTO utenti (utente, password, privilegi, note, registrazione)
VALUES
('admincomune@comune.zagarolo.it', 'root01', 'w', 'IT12345678901', False),
('mariorossi@comune.zagarolo.it', 'mario01', 'r', 'non registrato', False),
('gianni@comune.zagarolo.it', 'gianni123', 'r', 'non registrato', False),
('f', 'fF12345#', 'w', 'IT98765432100', False),
('a', 'a', 'w', 'IT11223344556', True),
('b', 'b', 'r', 'non registrato', True);

