BEGIN TRANSACTION;
DROP TABLE IF EXISTS "FABRICANTES";
CREATE TABLE "FABRICANTES" (
	"ID_FABR"	INTEGER NOT NULL,
	"NOMEFABR"	TEXT NOT NULL,
	PRIMARY KEY("ID_FABR")
);
DROP TABLE IF EXISTS "ENTRADAS";
CREATE TABLE "ENTRADAS" (
	"IN_DATA"	TEXT NOT NULL,
	"IN_QUANT"	REAL NOT NULL,
	"IN_IDPROD"	INTEGER NOT NULL,
	FOREIGN KEY("IN_IDPROD") REFERENCES "ESTOQUE"("ID_PROD")
	PRIMARY KEY("IN_IDPROD")
);
DROP TABLE IF EXISTS "COMPRAS";
CREATE TABLE "COMPRAS" (
	"PC_IDPROD"	INTEGER NOT NULL,
	"PC_LIM_MIN"	REAL,
	FOREIGN KEY("PC_IDPROD") REFERENCES "ESTOQUE"("ID_PROD"),
	PRIMARY KEY("PC_IDPROD")
);
DROP TABLE IF EXISTS "ESTOQUE";
CREATE TABLE "ESTOQUE" (
	"ID_PROD"	INTEGER NOT NULL,
	"COD_INT"	TEXT,
	"COD_FABR"	TEXT NOT NULL,
	"PRODUTO"	TEXT NOT NULL,
	"ID_FABR"	INTEGER NOT NULL,
	"SALDO"		REAL NOT NULL,
	FOREIGN KEY("ID_FABR") REFERENCES "FABRICANTES"("ID_FABR"),
	PRIMARY KEY("ID_PROD")
);
DROP TABLE IF EXISTS "SAIDAS";
CREATE TABLE "SAIDAS" (
	"OUT_DATA"	TEXT NOT NULL,
	"OUT_QUANT"	REAL NOT NULL,
	"OUT_IDPROD"	INTEGER NOT NULL,
	"OUT_DESTINO"	TEXT NOT NULL,
	FOREIGN KEY("OUT_IDPROD") REFERENCES "ESTOQUE"("ID_PROD"),
	PRIMARY KEY ("OUT_IDPROD")
);
INSERT INTO "FABRICANTES" ("ID_FABR","NOMEFABR") VALUES 
 (1,'AllPrint'),
 (2,'Balluff'),
 (3,'Banner'),
 (4,'Beta'),
 (5,'Bonfiglioli'),
 (6,'Conexel'),
 (7,'Contrinex'),
 (8,'Hohner'),
 (9,'Igus'),
 (10,'Keyence'),
 (11,'Metaltex'),
 (12,'Moeller'),
 (13,'Phoenix'),
 (14,'Pial'),
 (15,'ProAuto'),
 (16,'Schmersall'),
 (17,'Schneider'),
 (18,'SEW'),
 (19,'Siemens'),
 (20,'Steck'),
 (21,'Ventisilva'),
 (22,'Weg'),
 (23,'Andra'),
 (24,'OCTO');
 INSERT INTO "ENTRADAS" ("IN_DATA","IN_QUANT","IN_IDPROD") VALUES
 ("10/10/2023",15.0,15),
 ("15/05/2021",25.0,5),
 ("21/12/2019",5.0,11),
 ("13/07/2020",20.0,20);
INSERT INTO "ESTOQUE" ("ID_PROD","COD_INT","COD_FABR","PRODUTO","ID_FABR","SALDO") VALUES 
 (1,'10570','8WH2000-0AH01','Borne de Passagem Az 6,0',19,0.0),
 (2,'10571','8WH2000-0AJ01','Borne de Passagem Az 10,0',19,0.0),
 (3,'10572','8WH2000-0AK01','Borne de Passagem Az 16,0',19,0.0),
 (4,'10573','8WH1000-0AN01','Borne de Passagem Az 50,0',19,0.0),
 (5,'10575','8WH2000-0AF00','Borne de Passagem Cz 2,5',19,0.0),
 (6,'10586','8WH2000-0AG00','Borne de Passagem Cz 4,0',19,0.0),
 (7,'10590','8WH2000-0AH00','Borne de Passagem Cz 6,0',19,0.0),
 (8,'10591','8WH2000-0AJ00','Borne de Passagem Cz 10,0',19,0.0),
 (9,'10592','8WH2000-0AK00','Borne de Passagem Cz 16,0',19,0.0),
 (10,'10593','8WH1000-0AN00','Borne de Passagem Cz 50,0',19,0.0),
 (11,'10594','8WH2000-0CF07','Borne de Passagem PE 2,5',19,0.0),
 (12,'10598','8WH2000-0CG07','Borne de Passagem PE 4,0',19,0.0),
 (13,'10599','8WH2000-0CH07','Borne de Passagem PE 6,0',19,0.0),
 (14,'10600','8WH2000-0CJ07','Borne de Passagem PE 10,0',19,0.0),
 (15,'10601','8WH2000-0CK07','Borne de Passagem PE 16,0',19,0.0),
 (16,'10602','8WH2020-0AF00','Borne de Passagem Duplo Cz 2,5',19,0.0),
 (17,'10603','8WH2040-4LF00','Borne de Passagem Triplo Cz 2,5',19,0.0),
 (18,'10604','8WH2000-1GG08','Borne Fusível 4,0 x 6,3A máx.',19,0.0),
 (19,'10605','ASK1','Borne Fusível 4,0 x 6,3A Conexel',19,0.0),
 (20,'10606','3NW7 013','Base p/ Fusível 10 x 38 - 32A',19,0.0),
 (21,'4020','3NW6 003-1','Fusível 10 x 38 - 10A',19,0.0),
 (22,'10607','8WH9000-1GA00','Tampa Final 2,5',19,0.0),
 (23,'10608','8WH9000-1VA00','Tampa Final Duplo 2,5',19,0.0),
 (24,'10609','8WH9000-1GE00','Tampa Final Triplo 2,5',19,0.0),
 (25,'10610','8WH9003-1GA00','Tampa Final 4,0',19,0.0),
 (26,'10611','8WH9004-1GA00','Tampa Final 6,0',19,0.0),
 (27,'10612','8WH9005-1GA00','Tampa Final 10,0',19,0.0),
 (28,'10613','8WH9006-1GA00','Tampa Final 16,0',19,0.0),
 (29,'10614','8WH9020-6BC10','Ponte 2,5 — 2Pos',19,0.0),
 (30,'10615','8WH9020-6BF10','Ponte 2,5 — 5Pos',19,0.0),
 (31,'10616','8WH9020-6BL10','Ponte 2,5 — 10Pos',19,0.0),
 (32,'10617','8WH9070-0AA00','Placa Separação 1,5/4,0',19,0.0),
 (33,'10618','8WH9070-0BA00','Placa Separação Duplo 2,5',19,0.0),
 (34,'10619','8WH9150-0CA00','Poste Final',19,0.0),
 (35,'10620','8WA1 808','Poste Final',19,0.0),
 (36,'10621','TSTW C016400.000','Suporte p/ Trilho 45º',6,0.0),
 (37,'10629','WQG1-P07B/AD10.0 (5.192)','Terminação Reta PG7',15,0.0),
 (38,'10630','WQG1-P09B/AD13.0 (6.680)','Terminação  Reta PG9',15,0.0),
 (39,'10631','WQG1-P11B/AD15.8 (7.494)','Terminação  Reta PG11',15,0.0),
 (40,'10632','WQG1-P13B/AD18.5 (6.223)','Terminação  Reta PG13.5',15,0.0),
 (41,'10633','WQG1-P16B/AD21.2 (10.337)','Terminação  Reta PG16',15,0.0),
 (42,'10634','WQG1-P21B/AD28.5 (5.448)','Terminação  Reta PG21',15,0.0),
 (43,'10635','WQW1-P13 B/AD18.5 (6.229)','Terminação  Curva PG13.5',15,0.0),
 (44,'10636','GMK-P07B (5.200)','Contra-Porca PG7',15,0.0),
 (45,'10637','GMK-P09B (6.204)','Contra-Porca PG9',15,0.0),
 (46,'10638','GMK-P11B (5.208)','Contra-Porca PG11',15,0.0),
 (47,'10639','GMK-P13B (5.210)','Contra-Porca PG13',15,0.0),
 (48,'10640','GMK-P16B (5.447)','Contra-Porca PG16',15,0.0),
 (49,'10641','GMK-P21B (5.209)','Contra-Porca PG21',15,0.0),
 (50,'10642','GMK-P21DG (5.202)','Contra-Porca PG21 Cinza',15,0.0),
 (51,'10643','PCB-ECO PG11 PT (16.076)','Contra-Porca PG11',15,0.0),
 (52,'10645','WQSG-AD10.0B  (11.245)','Suporte Fechado AD10.0',15,0.0),
 (53,'10646','WQSG-AD13.0B  (5.250)','Suporte Fechado AD13.0',15,0.0),
 (54,'10655','WQSG-AD18.5B  (6.236)','Suporte Fechado AD18.0',15,0.0),
 (55,'10656','WQSG-AD21.2B  (6.237)','Suporte Fechado AD21.0',15,0.0),
 (56,'10657','WQSG-AD28.5B  (6.687)','Suporte Fechado AD28.5',15,0.0),
 (57,'10658','SKM-AD15.8/M4 (13.215)','Abraçadeira Aço AD-15.8',15,0.0),
 (58,'10659','SKM-AD21.2/M4 (10.504)','Abraçadeira Aço AD-21.2',15,0.0),
 (59,'10660','SKM-AD28.5/M4 (13.217)','Abraçadeira Aço AD-28.5',15,0.0),
 (60,'10661','PCB-PG9N CZE (1.560)','Prensa-Cabos  PG9',15,0.0),
 (61,'10662','PCB-PG11 PT (459)','Prensa-Cabos  PG11',15,0.0),
 (62,'10663','PCB-PG13.5 PT (461)','Prensa-Cabos  PG13.5',15,0.0),
 (63,'10664','PCB-PG16  PT (463)','Prensa-Cabos  PG16',15,0.0),
 (64,'10665','PCB-PG21 PT (465)','Prensa-Cabos  PG21',15,0.0),
 (65,'10666','PG9 CZ','Prensa-Cabos  Cinza PG9',15,0.0),
 (66,'10667','PG11 CZ','Prensa-Cabos  Cinza PG11',15,0.0),
 (67,'10668','PG13.5 CZ','Prensa-Cabos  Cinza PG13.5',15,0.0),
 (68,'10679','PG16 CZ','Prensa-Cabos  Cinza PG16',15,0.0),
 (69,'10680','PG21 CZ','Prensa-Cabos  Cinza PG21',15,0.0),
 (70,'10681','PCB-ECO M16 x 1,5 CZ (16.091)','Prensa-Cabos  Plástico M16',15,0.0),
 (71,'10682','PCB-ECO M20 x 1,5 CZ (16.093)','Prensa-Cabos  Plástico M20',15,0.0),
 (72,'10683','PCB-ECO M25 x 1,5 CZ (16.095)','Prensa-Cabos  Plástico M25',15,0.0),
 (73,'10684','PCB-ECO M32 x 1,5 CZ (16.097)','Prensa-Cabos  Plástico M32',15,0.0),
 (74,'10685','PCM-M16  x 1,5 (2.670)','Prensa-Cabos  Metálico M16',15,0.0),
 (75,'9846','PCM-M20  x 1,5 (2671)','Prensa-Cabos  Metálico M20',15,0.0),
 (76,'9847','PCM-M25 x 1,5 (11.921)','Prensa-Cabos  Metálico M25',15,0.0),
 (77,'9883','PCM-M32  x 1,5 (2.672)','Prensa-Cabos  Metálico M32',15,0.0),
 (78,'10686','WQE-AD18.5G  (11.456)','Terminal Cone Cinza AD18',15,0.0),
 (79,'10687','TE-250 10A (6.176)','Tomada p/ Trilho 250V x 10A',15,0.0),
 (80,'10689','DG238-10.0-03P-19-01AH (6.381)','Emenda p/ Fios 3 vias 0,75/2,5',15,0.0),
 (81,'6943','XCSPA791','Fim-de Curso de Segurança',17,0.0),
 (82,'6944','XCSZ14','Atuador',17,0.0),
 (83,'7313','XCSZ12','Atuador',17,0.0),
 (84,'6810','QS18VP6LPQ8','Sensor Reflexivo Polarizado  Banner',3,0.0),
 (85,'817','QS18VP6LVQ8','Sensor Difuso Banner',3,0.0),
 (86,'10691','BOS18M-PA-1PD-E5-C-S4','Sensor Difuso Balluff',2,0.0),
 (87,'911','XS212BLPAM 12','Sensor Indutivo Schneider',17,0.0),
 (88,'924','DW-AS-623-M8-001','Sensor Indutivo Contrinex',7,0.0),
 (89,'10705','BKT67M-001-U-S92','Sensor de Contraste Balluff',2,0.0),
 (90,'6554','LR-W500C','Sensor de Contraste Keyence',10,0.0),
 (91,'10707','FS-N11CP','Sensor de Fibra Otica Keyence',10,0.0),
 (92,'10708','FU-77TZ','Sensor de Fibra Õtica Keyence',10,0.0),
 (93,'10710','PS350','Sensor Ultrassonico  AllPrint',1,0.0),
 (94,'10712','PFD-1M-R','Sensor Difuso Metaltex',11,0.0),
 (95,'6206','WWAKC4K','Conector M12 90º Banner',3,0.0),
 (96,'909','XZCC12FCM40B','Conector  M12 90º Schneider',17,0.0),
 (97,'9162','XUZB11','Fita Reflexiva Schneider (metro)',17,0.0),
 (98,'910','XUZC50','Espelho Reflexivo 50 x 50 Schneider',17,0.0),
 (99,'2084','TH10R0180','Encoder Taco Gerador Hohner',8,0.0),
 (100,'10716','CON_M8_3P','Conector M8 3Pinos Cabo 10m',13,0.0),
 (101,'10718','COM_M8_4P','Conector M8 4Pinos Cabo 2m',13,0.0),
 (102,'10719','3RA1911-1AA00','Bloco de Ligação RV/RT',19,0.0),
 (103,'10720','3RA1921-1DA00','Bloco de Ligação RV/RT',19,0.0),
 (104,'10734','3RH1911-1FA22','Contato Auxiliar Superior 2NA/2NF',19,0.0),
 (105,'10735','3RH1911-1FA31','Contato Auxiliar Superior 3NA/1NF',19,0.0),
 (106,'10736','3RQ3118-1AB00','Relé de Interface 1NAF',19,0.0),
 (107,'10739','3RQ3901-0A','Pente de Conexão 2 Pólos',19,0.0),
 (108,'10740','3RQ3901-0B','Pente de Conexão 4 Pólos',19,0.0),
 (109,'10741','3RQ3901-0C','Pente de Conexão 8 Pólos',19,0.0),
 (110,'10742','3RQ3901-0D','Pente de Conexão 16 Pólos',19,0.0),
 (111,'10743','3RT1015-1BB41','Contator a Potência 3KW/7A',19,0.0),
 (112,'10744','3RT1016-1BB41','Contatora Potência 4KW/9A',19,0.0),
 (113,'10746','3RT1916-1BB00','Supressor Varistor 24V',19,0.0),
 (114,'10747','3RT1916-1CB00','Supressor RC 24V',19,0.0),
 (115,'10748','3RT2916-1CB00','Supressor RC 24V',19,0.0),
 (116,'10749','3RV1011-1AA10','Disjuntor-motor 1,1/1,6 A',19,0.0),
 (117,'10750','3RV1901-1B','Contato Auxiliar Lateral 2NA',19,0.0),
 (118,'10751','3RV1915-2AB','Ponte Trifásica 2 Posições',19,0.0),
 (119,'10752','3RV2031-4EA10','Disjuntor-motor 22/32A',19,0.0),
 (120,'10753','3RV2901-1A','Contato Auxiliar Lateral 1NA/1NF',19,0.0),
 (121,'10754','3SB6031-2AA40-0YA0','Seletora 2Pos. c/Ret. Sinal. Verde',19,0.0),
 (122,'10755','3SB6130-0AB20-1CA0','Botão Impulso Vermelho 1NF',19,0.0),
 (123,'10756','3SB6130-0AB30-1BA0','Botão Impulso Amarelo 1NA',19,0.0),
 (124,'10757','3SB6130-1HB20-1CA0','Botão Cogumelo Emergência 1NF',19,0.0),
 (125,'10758','3SB6130-2AM10-1NA0','Seletora 3Pos. s/Ret. 2NA',19,0.0),
 (126,'10759','3SB6133-0DB60-1BA0','Botão Impulso Branco Sinal. 24V',19,0.0),
 (127,'10760','3SB6213-6AA20-1AA0','Sinaleiro LED Vermelho 24V',19,0.0),
 (128,'10761','3SB6213-6AA40-1AA0','Sinaleiro LED Verde 24V',19,0.0),
 (129,'10762','3SB6400-1AA10-1BA0','Elemento de Contato 1NA',19,0.0),
 (130,'10763','3SB6400-1AA10-1CA0','Elemento de Contato 1NF',19,0.0),
 (131,'10764','3SB6403-1BA40-1AA0','Sinaleiro LED Verde 24V',19,0.0),
 (132,'10765','3SB6811-0AA10-0BA0','Caixa vazia 1 Furo',19,0.0),
 (133,'10766','3SB6813-0AA10-0BA0','Caixa vazia 3 Furos',19,0.0),
 (134,'10767','3SB6814-0AA10-0BA0','Caixa vazia 4 Furos',19,0.0),
 (135,'10768','3SB6815-0AA10-0BA0','Caixa vazia 5 Furos',19,0.0),
 (136,'10769','3SE5232-0HR01','Fim de Curso Haste Flexível',19,0.0),
 (137,'10770','5SM1346-0MB','Interruptor  DR 63A x 30mA',19,0.0),
 (138,'10771','8WA1 204','Borne Parafuso 16mm²',19,0.0),
 (139,'10772','8WD4308-0EE','Tubo Metálico - 150 mm',19,0.0),
 (140,'10773','LZS:RT4D4L24','Relé de Interface 2NAF - 24Vcc',19,0.0),
 (141,'10774','16905','Interruptor DR 125A x 30mA',17,0.0),
 (142,'10775','BMH1901P31A2A','Servomotor Lexium 30Nm - 5,2KW - 23A',17,0.0),
 (143,'1871','CA2KN40M7','Contatora Auxiliar 220Vca 4NA',17,0.0),
 (144,'10776','DF101','Porta Fusível 10 x 38',17,0.0),
 (145,'5085','EZ9F33210','Disjuntor 2 pólos C10 A',17,0.0),
 (146,'9609','EZEFASB2','Separador de Fases p/ EZC 250',17,0.0),
 (147,'9611','EZESPDR3P','Distanciador  de Fases p/ EZC250',17,0.0),
 (148,'10783','GV1G10','Capa Proteção Trifásica',17,0.0),
 (149,'1858','GV2AF01','Bloco de Licação GV2/K',17,0.0),
 (150,'5325','GV2G254','Ponte Trifásica 2 Posições',17,0.0),
 (151,'10784','GV2G454','Ponte Trifásica 4 Posições',17,0.0),
 (152,'1866','GV2ME07','Disjuntor-motor 1,6/2,5A',17,0.0),
 (153,'1857','GVAN11','Contato Auxiliar Lateral 1NA/1NF',17,0.0),
 (154,'9608','GVAN20','Contato Auxiliar Lateral 2NA',17,0.0),
 (155,'9631','HMISST','IHM Magelis STU Módulo Traseiro',17,0.0),
 (156,'9630','HMIS85','IHM Magelis STU Painel 5,7"',17,0.0),
 (157,'1859','LA4KE1B','Supressor Varistor 24V',17,0.0),
 (158,'10785','LADN01','Contato Auxiliar Superior 1NF',17,0.0),
 (159,'10786','LADN11','Contato Auxiliar Superior 1NA/1NF',17,0.0),
 (160,'10813','LXM32AD72N4','Servodrive Lexium LXM 32A',17,0.0),
 (161,'10815','RSB2A080BDS','Relé Interface 24V 2NAF',17,0.0),
 (162,'4030','RSL1PVBU','Relé Interface 24V 1NAF',17,0.0),
 (163,'4032','RZM031BN','Diodo + LED Verde 24V',17,0.0),
 (164,'10830','VW3M5103R100','Cabo de Potência 10m',17,0.0),
 (165,'10831','VW3M8102R100','Cabo Encoder 10m',17,0.0),
 (166,'5315','XA2EVB5LC','Sinaleiro LED LR 24V',17,0.0),
 (167,'10816','XAL-D03','Caixa vazia 3 Furos',17,0.0),
 (168,'10817','XAL-D04','Caixa vazia 4 Furos',17,0.0),
 (169,'1883','XB5AA21','Botão Impulso PR 1NA',17,0.0),
 (170,'904','XB5AA41','Botão Impulso VM 1NA',17,0.0),
 (171,'1881','XB5AA51','Botão Impulso AM 1NA',17,0.0),
 (172,'1880','XB5AA61','Botão Impulso AZ 1NA',17,0.0),
 (173,'5318','XB5AD21','Seletora 2Pos. c/Ret. Pr 1NA',17,0.0),
 (174,'9607','XB5AD25','Seletora 2Pos. c/Ret. Pr 1NA/1NF',17,0.0),
 (175,'10832','XB5AD41','Seletora 2Pos. s/Ret. PR 1NA',17,0.0),
 (176,'4037','XB5AK123B5','Seletora 2Pos. c/Ret. Sinal. Vd 2NA',17,0.0),
 (177,'6486','XB5AS8444','Botão Cogumelo Emergência 2NF',17,0.0),
 (178,'10818','ZB5SZ3','Tampão cego 22mm',17,0.0),
 (179,'5319','ZBE-101','Elemento de Contato 1NA',17,0.0),
 (180,'9613','ZBE-102','Elemento de Contato 1NF',17,0.0),
 (181,'10833','ZBV-B1','Sinaleiro LED BR 24V',17,0.0),
 (182,'10834','ZBV-B5','Sinaleiro LED LR 24V',17,0.0),
 (183,'9614','ZBY9420','Etiqueta Circular "Emergência"',17,0.0),
 (184,'10835','BN 63B 4','Motor Trifásico 0,18/0,21KW - 1,2/0,69A',5,0.0),
 (185,'10836','FB18.37.xx','Esteira Porta-cabos 18x37x65',9,0.0),
 (186,'10837','OH-306','Resistor de Frenagem SEW 0,6KW/100Ω',18,0.0),
 (187,'10838','E14CD','Microventilador Axial 14cm',21,0.0),
 (188,'10850','LC2-50','Célula de Carga 50Kgf',1,0.0),
 (189,'10851','620-DC-TE','Relé Programável Easy Moeller',12,0.0),
 (190,'10852','BMV5.0','Módulo de Controle de Freio SEW',18,0.0),
 (191,'10853','DBG11B-11','Console Inversores SEW',18,0.0),
 (192,'10854','9874585','Conector CONIN 12Pin. Fêmea',18,0.0),
 (193,'9975','RJ45','Conector RJ45 Plástico',4,0.0),
 (194,'7435','ZAF-236-11ZP','Fim de Curso Haste Flexível Schmersal',16,0.0),
 (195,'821','PB 675060','Tomada 2P+T 10A',14,0.0),
 (196,'10885','B58N2048S6AWES','Encoder Increm. 2048 ppr CONIN M23',18,0.0),
 (197,'10857','ACLOP','Acoplamento  Plástico 23 x 6 mm',8,0.0),
 (198,'10858','ACLOM','Acoplamento  Metálico 36 x 10 mm',8,0.0),
 (199,'10859','MDX61B0040-5A3-4-0T/DER11B','Servo-Drive MDX61 B+ 4KW',18,0.0),
 (200,'10860','MDX61B0022-5A3-4-0T/DEH11B','Servo-Drive MDX61 B+ 2,2KW',18,0.0),
 (201,'10861','DER11B','Módulo de Encoder/Resolver',18,0.0),
 (202,'6552','DB15M','Conector DB15 Macho',4,0.0),
 (203,'7429','DB9M','Conector DB9 Macho',4,0.0),
 (204,'6551','DB15F','Conector DB15 Fêmea',4,0.0),
 (205,'9307','DB9F','Conector DB9 Fêmea',4,0.0),
 (206,'9306','DB15P','Capa DB15 Plástica',4,0.0),
 (207,'9301','DB9P','Capa DB9 Plástica',4,0.0),
 (208,'6817','CUC-DST-GZNI-A/DSSC15','Capa DB15 Metálica',13,0.0),
 (209,'9361','CUC-DST-GZNI-A/DSSC9','Capa DB9 Metálica',13,0.0),
 (210,'10862','DB15CM2','Capa DB15 Metálica 2ª Linha',24,0.0),
 (211,'10863','DB9CM2','Capa DB9 Metálica 2ª Linha',24,0.0),
 (212,'10905','N4006','Tomada Blindada 16A - 3P+T - 380/440V',20,0.0),
 (213,'10906','3NW6 001-1','Fusível 10 x 38 - 6A',19,0.0),
 (214,'10907','3NW6 004-1','Fusível 10 x 38 - 4A',19,0.0),
 (215,'10908','RJ45 Blindado','Conector RJ45 Blindado',4,0.0),
 (216,'10909','3RV2011-1AA10','Disjuntor-motor 1,1/1,6A',19,0.0),
 (217,'10910','3RV2011-1CA10','Disjuntor-motor 1,8/2,5A',19,0.0),
 (218,NULL,'3RV2011-1BA10','Disjuntor-motor 1,4/2,0A',19,0.0),
 (219,NULL,'3RV2011-1FA10','Disjuntor-motor 3,5/5,0A',19,0.0),
 (220,NULL,'3RV1915-2CB','Ponte Trifásica 4 Posições',19,0.0),
 (221,NULL,'3RV2021-4BA10','Disjuntor-motor 13/20A',19,0.0),
 (222,NULL,'5SY4216-8','Disjuntor 2 pólos D16 A',19,0.0),
 (223,NULL,'5SL1332-7MB','Disjuntor 3 pólos C32 A',19,0.0),
 (224,NULL,'5TW3032-1','Seccionadora Tripolar 32A',19,0.0),
 (225,NULL,'3RH2911-1AA01','Contato Auxiliar Frontal 1NF',19,0.0),
 (226,NULL,'3RU2116-1JC0','Relé Térmico 7/10A',19,0.0),
 (227,NULL,'3RU2916-3AA01','Suporte Relé 3RU Parafusos',19,0.0),
 (228,NULL,'3RU2916-3AC01','Suporte Relé 3RU Mola',19,0.0),
 (229,NULL,'LZS:RT4D4T30','Relé de Interface 2NAF - 230Vac',19,0.0);
COMMIT;
