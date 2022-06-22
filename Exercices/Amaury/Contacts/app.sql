-- Database: app

-- DROP DATABASE IF EXISTS app;

CREATE DATABASE app
    WITH
    OWNER = "user"
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Table: public.contacts

-- DROP TABLE IF EXISTS public.contacts;

CREATE TABLE IF NOT EXISTS public.contacts
(
    id integer NOT NULL DEFAULT nextval('contacts_id_seq'::regclass),
    firstname character varying(30) COLLATE pg_catalog."default",
    lastname character varying(30) COLLATE pg_catalog."default",
    email character varying(45) COLLATE pg_catalog."default",
    password character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT contacts_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.contacts
    OWNER to "user";