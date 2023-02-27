--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Alugueis; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Alugueis" (
    "ID" integer NOT NULL,
    "ID_Clientes" integer NOT NULL,
    "ID_Livros" integer NOT NULL,
    "Data_Aluguel" character(15) NOT NULL
);


ALTER TABLE public."Alugueis" OWNER TO postgres;

--
-- Name: Alugueis_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Alugueis" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Alugueis_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Clientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Clientes" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "CPF" character(11) NOT NULL,
    "Telefone" character(11) NOT NULL,
    "E-mail" character varying(255)
);


ALTER TABLE public."Clientes" OWNER TO postgres;

--
-- Name: Clientes_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Clientes" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Clientes_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Livros; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Livros" (
    "ID" integer NOT NULL,
    "NomeLivro" character varying(255),
    "Idioma" character varying(255) NOT NULL,
    "NumeroPaginas" integer DEFAULT 0
);


ALTER TABLE public."Livros" OWNER TO postgres;

--
-- Name: Livros_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Livros_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Livros_ID_seq" OWNER TO postgres;

--
-- Name: Livros_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Livros_ID_seq" OWNED BY public."Livros"."ID";


--
-- Name: Livros ID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Livros" ALTER COLUMN "ID" SET DEFAULT nextval('public."Livros_ID_seq"'::regclass);


--
-- Data for Name: Alugueis; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Alugueis" ("ID", "ID_Clientes", "ID_Livros", "Data_Aluguel") FROM stdin;
1	4	11	21/02/2030     
\.


--
-- Data for Name: Clientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Clientes" ("ID", "Nome", "CPF", "Telefone", "E-mail") FROM stdin;
1	Fco Deyvison Viana Rodrigues	06967798383	85985696765	deyvisonviana9@gmail.com
3	Daphne Regina da Silva Torrelio	09839388304	85999327897	daphnetorrelio365@gmail.com
4	Tarik	12345678910	12345678910	@gmail.com
\.


--
-- Data for Name: Livros; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Livros" ("ID", "NomeLivro", "Idioma", "NumeroPaginas") FROM stdin;
11	As aventuras bizarras de João Joestrela	Português (BR)	125
10	Joana e a lâmpada LED	Espanhol(MEXICANO)	255
12	Coraline e o mundo secreto	Inglês(usa)	200
\.


--
-- Name: Alugueis_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Alugueis_ID_seq"', 1, true);


--
-- Name: Clientes_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Clientes_ID_seq"', 4, true);


--
-- Name: Livros_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Livros_ID_seq"', 12, true);


--
-- Name: Alugueis Alugueis_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Alugueis"
    ADD CONSTRAINT "Alugueis_pkey" PRIMARY KEY ("ID");


--
-- Name: Clientes Clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Clientes"
    ADD CONSTRAINT "Clientes_pkey" PRIMARY KEY ("ID");


--
-- Name: Livros Livros_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Livros"
    ADD CONSTRAINT "Livros_pkey" PRIMARY KEY ("ID");


--
-- Name: Alugueis fk_clientes; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Alugueis"
    ADD CONSTRAINT fk_clientes FOREIGN KEY ("ID_Clientes") REFERENCES public."Clientes"("ID") ON DELETE CASCADE;


--
-- Name: Alugueis fk_livros; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Alugueis"
    ADD CONSTRAINT fk_livros FOREIGN KEY ("ID_Livros") REFERENCES public."Livros"("ID") ON DELETE SET NULL;


--
-- PostgreSQL database dump complete
--

