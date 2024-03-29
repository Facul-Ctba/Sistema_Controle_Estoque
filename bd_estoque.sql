BEGIN TRANSACTION;
DROP TABLE IF EXISTS "SAIDAS";
CREATE TABLE "SAIDAS" (
	"OUT_PROD_ID"	INTEGER NOT NULL,
	"OUT_DATA"	TEXT NOT NULL,
	"OUT_QUANT"	REAL NOT NULL,
	"OUT_DESTINO"	TEXT NOT NULL,
	PRIMARY KEY("OUT_PROD_ID")
);
DROP TABLE IF EXISTS "PONTO_COMPRA";
CREATE TABLE "PONTO_COMPRA" (
	"PC_PROD_ID"	INTEGER NOT NULL,
	"PC_QUANT"	REAL,
	PRIMARY KEY("PC_PROD_ID")
);
DROP TABLE IF EXISTS "FORNECEDORES";
CREATE TABLE "FORNECEDORES" (
	"FORN_ID"	INTEGER,
	"FORN_NOME"	TEXT
);
DROP TABLE IF EXISTS "PRODUTOS";
CREATE TABLE "PRODUTOS" (
	"PROD_ID"	INTEGER,
	"COD_INT"	TEXT,
	"COD_FORN"	TEXT,
	"PRODUTO"	TEXT NOT NULL,
	"FORN_NOME"	TEXT,
	"SALDO"	REAL NOT NULL
);
DROP TABLE IF EXISTS "ENTRADAS";
CREATE TABLE "ENTRADAS" (
	"IN_DATA"	TEXT NOT NULL,
	"IN_QUANT"	REAL NOT NULL,
	"IN_CODINT"	TEXT,
	"IN_CODFORN"	TEXT,
	"IN_PRODUTO"	TEXT NOT NULL
);
INSERT INTO "FORNECEDORES" ("FORN_ID","FORN_NOME") VALUES (1,'AllPrint'),
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
 (23,'Andra');
INSERT INTO "PRODUTOS" ("PROD_ID","COD_INT","COD_FORN","PRODUTO","FORN_NOME","SALDO") VALUES (1,'10570','8WH2000-0AH01','Borne de Passagem Az 6,0','Siemens',0.0),
 (2,'10572','8WH2000-0AK01','Borne de Passagem Az 16,0','Siemens',0.0),
 (3,'10573','8WH1000-0AN01','Borne de Passagem Az 50,0','Siemens',0.0),
 (4,'10575','8WH2000-0AF00','Borne de Passagem Cz 2,5','Siemens',0.0),
 (5,'10586','8WH2000-0AG00','Borne de Passagem Cz 4,0','Siemens',0.0),
 (6,'10590','8WH2000-0AH00','Borne de Passagem Cz 6,0','Siemens',0.0),
 (7,'10591','8WH2000-0AJ00','Borne de Passagem Cz 10,0','Siemens',0.0),
 (8,'10592','8WH2000-0AK00','Borne de Passagem Cz 16,0','Siemens',0.0),
 (9,'10593','8WH1000-0AN00','Borne de Passagem Cz 50,0','Siemens',0.0),
 (10,'10594','8WH2000-0CF07','Borne de Passagem PE 2,5','Siemens',0.0),
 (11,'10598','8WH2000-0CG07','Borne de Passagem PE 4,0','Siemens',0.0),
 (12,'10599','8WH2000-0CH07','Borne de Passagem PE 6,0','Siemens',0.0),
 (13,'10600','8WH2000-0CJ07','Borne de Passagem PE 10,0','Siemens',0.0),
 (14,'10601','8WH2000-0CK07','Borne de Passagem PE 16,0','Siemens',0.0),
 (15,'10602','8WH2020-0AF00','Borne de Passagem Duplo Cz 2,5','Siemens',0.0),
 (16,'10603','8WH2040-4LF00','Borne de Passagem Triplo Cz 2,5','Siemens',0.0),
 (17,'10604','8WH2000-1GG08','Borne Fusível 4,0 x 6,3A máx.','Siemens',0.0),
 (18,'10605','ASK1','Borne Fusível 4,0 x 6,3A Conexel','Siemens',0.0),
 (19,'10606','3NW7 013','Base p/ Fusível 10 x 38 - 32A','Siemens',0.0),
 (20,'4020','3NW6 003-1','Fusível 10 x 38 - 10A','Siemens',0.0),
 (21,'10607','8WH9000-1GA00','Tampa Final 2,5','Siemens',0.0),
 (22,'10608','8WH9000-1VA00','Tampa Final Duplo 2,5','Siemens',0.0),
 (23,'10609','8WH9000-1GE00','Tampa Final Triplo 2,5','Siemens',0.0),
 (24,'10610','8WH9003-1GA00','Tampa Final 4,0','Siemens',0.0),
 (25,'10611','8WH9004-1GA00','Tampa Final 6,0','Siemens',0.0),
 (26,'10612','8WH9005-1GA00','Tampa Final 10,0','Siemens',0.0),
 (27,'10613','8WH9006-1GA00','Tampa Final 16,0','Siemens',0.0),
 (28,'10614','8WH9020-6BC10','Ponte 2,5 — 2Pos','Siemens',0.0),
 (29,'10615','8WH9020-6BF10','Ponte 2,5 — 5Pos','Siemens',0.0),
 (30,'10616','8WH9020-6BL10','Ponte 2,5 — 10Pos','Siemens',0.0),
 (31,'10617','8WH9070-0AA00','Placa Separação 1,5/4,0','Siemens',0.0),
 (32,'10618','8WH9070-0BA00','Placa Separação Duplo 2,5','Siemens',0.0),
 (33,'10619','8WH9150-0CA00','Poste Final','Siemens',0.0),
 (34,'10620','8WA1 808','Poste Final','Siemens',0.0),
 (35,'10621','TSTW C016400.000','Suporte p/ Trilho 45º','Conexel',0.0),
 (36,'10629','WQG1-P07B/AD10.0 (5.192)','Terminação Reta PG7','ProAuto',0.0),
 (37,'10630','WQG1-P09B/AD13.0 (6.680)','Terminação  Reta PG9','ProAuto',0.0),
 (38,'10631','WQG1-P11B/AD15.8 (7.494)','Terminação  Reta PG11','ProAuto',0.0),
 (39,'10632','WQG1-P13B/AD18.5 (6.223)','Terminação  Reta PG13.5','ProAuto',0.0),
 (40,'10633','WQG1-P16B/AD21.2 (10.337)','Terminação  Reta PG16','ProAuto',0.0),
 (41,'10634','WQG1-P21B/AD28.5 (5.448)','Terminação  Reta PG21','ProAuto',0.0),
 (42,'10635','WQW1-P13 B/AD18.5 (6.229)','Terminação  Curva PG13.5','ProAuto',0.0),
 (43,'10636','GMK-P07B (5.200)','Contra-Porca PG7','ProAuto',0.0),
 (44,'10637','GMK-P09B (6.204)','Contra-Porca PG9','ProAuto',0.0),
 (45,'10638','GMK-P11B (5.208)','Contra-Porca PG11','ProAuto',0.0),
 (46,'10639','GMK-P13B (5.210)','Contra-Porca PG13','ProAuto',0.0),
 (47,'10640','GMK-P16B (5.447)','Contra-Porca PG16','ProAuto',0.0),
 (48,'10641','GMK-P21B (5.209)','Contra-Porca PG21','ProAuto',0.0),
 (49,'10642','GMK-P21DG (5.202)','Contra-Porca PG21 Cinza','ProAuto',0.0),
 (50,'10643','PCB-ECO PG11 PT (16.076)','Contra-Porca PG11','ProAuto',0.0),
 (51,'10645','WQSG-AD10.0B  (11.245)','Suporte Fechado AD10.0','ProAuto',0.0),
 (52,'10646','WQSG-AD13.0B  (5.250)','Suporte Fechado AD13.0','ProAuto',0.0),
 (53,'10655','WQSG-AD18.5B  (6.236)','Suporte Fechado AD18.0','ProAuto',0.0),
 (54,'10656','WQSG-AD21.2B  (6.237)','Suporte Fechado AD21.0','ProAuto',0.0),
 (55,'10657','WQSG-AD28.5B  (6.687)','Suporte Fechado AD28.5','ProAuto',0.0),
 (56,'10658','SKM-AD15.8/M4 (13.215)','Abraçadeira Aço AD-15.8','ProAuto',0.0),
 (57,'10659','SKM-AD21.2/M4 (10.504)','Abraçadeira Aço AD-21.2','ProAuto',0.0),
 (58,'10660','SKM-AD28.5/M4 (13.217)','Abraçadeira Aço AD-28.5','ProAuto',0.0),
 (59,'10661','PCB-PG9N CZE (1.560)','Prensa-Cabos  PG9','ProAuto',0.0),
 (60,'10662','PCB-PG11 PT (459)','Prensa-Cabos  PG11','ProAuto',0.0),
 (61,'10663','PCB-PG13.5 PT (461)','Prensa-Cabos  PG13.5','ProAuto',0.0),
 (62,'10664','PCB-PG16  PT (463)','Prensa-Cabos  PG16','ProAuto',0.0),
 (63,'10665','PCB-PG21 PT (465)','Prensa-Cabos  PG21','ProAuto',0.0),
 (64,'10666','PG9 CZ','Prensa-Cabos  Cinza PG9','ProAuto',0.0),
 (65,'10667','PG11 CZ','Prensa-Cabos  Cinza PG11','ProAuto',0.0),
 (66,'10668','PG13.5 CZ','Prensa-Cabos  Cinza PG13.5','ProAuto',0.0),
 (67,'10679','PG16 CZ','Prensa-Cabos  Cinza PG16','ProAuto',0.0),
 (68,'10680','PG21 CZ','Prensa-Cabos  Cinza PG21','ProAuto',0.0),
 (69,'10681','PCB-ECO M16 x 1,5 CZ (16.091)','Prensa-Cabos  Plástico M16','ProAuto',0.0),
 (70,'10682','PCB-ECO M20 x 1,5 CZ (16.093)','Prensa-Cabos  Plástico M20','ProAuto',0.0),
 (71,'10683','PCB-ECO M25 x 1,5 CZ (16.095)','Prensa-Cabos  Plástico M25','ProAuto',0.0),
 (72,'10684','PCB-ECO M32 x 1,5 CZ (16.097)','Prensa-Cabos  Plástico M32','ProAuto',0.0),
 (73,'10685','PCM-M16  x 1,5 (2.670)','Prensa-Cabos  Metálico M16','ProAuto',0.0),
 (74,'9846','PCM-M20  x 1,5 (2671)','Prensa-Cabos  Metálico M20','ProAuto',0.0),
 (75,'9847','PCM-M25 x 1,5 (11.921)','Prensa-Cabos  Metálico M25','ProAuto',0.0),
 (76,'9883','PCM-M32  x 1,5 (2.672)','Prensa-Cabos  Metálico M32','ProAuto',0.0),
 (77,'10686','WQE-AD18.5G  (11.456)','Terminal Cone Cinza AD18','ProAuto',0.0),
 (78,'10687','TE-250 10A (6.176)','Tomada p/ Trilho 250V x 10A','ProAuto',0.0),
 (79,'10689','DG238-10.0-03P-19-01AH (6.381)','Emenda p/ Fios 3 vias 0,75/2,5','ProAuto',0.0),
 (80,'6943','XCSPA791','Fim-de Curso de Segurança','Schneider',0.0),
 (81,'6944','XCSZ14','Atuador','Schneider',0.0),
 (82,'7313','XCSZ12','Atuador','Schneider',0.0),
 (83,'6810','QS18VP6LPQ8','Sensor Reflexivo Polarizado  Banner','Banner',0.0),
 (84,'817','QS18VP6LVQ8','Sensor Difuso Banner','Banner',0.0),
 (85,'10691','BOS18M-PA-1PD-E5-C-S4','Sensor Difuso Balluff','Balluff',0.0),
 (86,'911','XS212BLPAM 12','Sensor Indutivo Schneider','Schneider',0.0),
 (87,'924','DW-AS-623-M8-001','Sensor Indutivo Contrinex','Contrinex',0.0),
 (88,'10705','BKT67M-001-U-S92','Sensor de Contraste Balluff','Balluff',0.0),
 (89,'6554','LR-W500C','Sensor de Contraste Keyence','Keyence',0.0),
 (90,'10707','FS-N11CP','Sensor de Fibra Otica Keyence','Keyence',0.0),
 (91,'10708','FU-77TZ','Sensor de Fibra Õtica Keyence','Keyence',0.0),
 (92,'10710','PS350','Sensor Ultrassonico  AllPrint','AllPrint',0.0),
 (93,'10712','PFD-1M-R','Sensor Difuso Metaltex','Metaltex',0.0),
 (94,'6206','WWAKC4K','Conector M12 90º Banner','Banner',0.0),
 (95,'909','XZCC12FCM40B','Conector  M12 90º Schneider','Schneider',0.0),
 (96,'9162','XUZB11','Fita Reflexiva Schneider (metro)','Schneider',0.0),
 (97,'910','XUZC50','Espelho Reflexivo 50 x 50 Schneider','Schneider',0.0),
 (98,'2084','TH10R0180','Encoder Taco Gerador Hohner','Hohner',0.0),
 (99,'10716','','Conector M8 3Pinos Cabo 10m','Phoenix',0.0),
 (100,'10718','','Conector M8 4Pinos Cabo 2m','Phoenix',0.0),
 (101,'10719','3RA1911-1AA00','Bloco de Ligação RV/RT','Siemens',0.0),
 (102,'10720','3RA1921-1DA00','Bloco de Ligação RV/RT','Siemens',0.0),
 (103,'10734','3RH1911-1FA22','Contato Auxiliar Superior 2NA/2NF','Siemens',0.0),
 (104,'10735','3RH1911-1FA31','Contato Auxiliar Superior 3NA/1NF','Siemens',0.0),
 (105,'10736','3RQ3118-1AB00','Relé de Interface 1NAF','Siemens',0.0),
 (106,'10739','3RQ3901-0A','Pente de Conexão 2 Pólos','Siemens',0.0),
 (107,'10740','3RQ3901-0B','Pente de Conexão 4 Pólos','Siemens',0.0),
 (108,'10741','3RQ3901-0C','Pente de Conexão 8 Pólos','Siemens',0.0),
 (109,'10742','3RQ3901-0D','Pente de Conexão 16 Pólos','Siemens',0.0),
 (110,'10743','3RT1015-1BB41','Contator a Potência 3KW/7A','Siemens',0.0),
 (111,'10744','3RT1016-1BB41','Contatora Potência 4KW/9A','Siemens',0.0),
 (112,'10746','3RT1916-1BB00','Supressor Varistor 24V','Siemens',0.0),
 (113,'10747','3RT1916-1CB00','Supressor RC 24V','Siemens',0.0),
 (114,'10748','3RT2916-1CB00','Supressor RC 24V','Siemens',0.0),
 (115,'10749','3RV1011-1AA10','Disjuntor-motor 1,1/1,6 A','Siemens',0.0),
 (116,'10750','3RV1901-1B','Contato Auxiliar Lateral 2NA','Siemens',0.0),
 (117,'10751','3RV1915-2AB','Ponte Trifásica 2 Posições','Siemens',0.0),
 (118,'10752','3RV2031-4EA10','Disjuntor-motor 22/32A','Siemens',0.0),
 (119,'10753','3RV2901-1A','Contato Auxiliar Lateral 1NA/1NF','Siemens',0.0),
 (120,'10754','3SB6031-2AA40-0YA0','Seletora 2Pos. c/Ret. Sinal. Verde','Siemens',0.0),
 (121,'10755','3SB6130-0AB20-1CA0','Botão Impulso Vermelho 1NF','Siemens',0.0),
 (122,'10756','3SB6130-0AB30-1BA0','Botão Impulso Amarelo 1NA','Siemens',0.0),
 (123,'10757','3SB6130-1HB20-1CA0','Botão Cogumelo Emergência 1NF','Siemens',0.0),
 (124,'10758','3SB6130-2AM10-1NA0','Seletora 3Pos. s/Ret. 2NA','Siemens',0.0),
 (125,'10759','3SB6133-0DB60-1BA0','Botão Impulso Branco Sinal. 24V','Siemens',0.0),
 (126,'10760','3SB6213-6AA20-1AA0','Sinaleiro LED Vermelho 24V','Siemens',0.0),
 (127,'10761','3SB6213-6AA40-1AA0','Sinaleiro LED Verde 24V','Siemens',0.0),
 (128,'10762','3SB6400-1AA10-1BA0','Elemento de Contato 1NA','Siemens',0.0),
 (129,'10763','3SB6400-1AA10-1CA0','Elemento de Contato 1NF','Siemens',0.0),
 (130,'10764','3SB6403-1BA40-1AA0','Sinaleiro LED Verde 24V','Siemens',0.0),
 (131,'10765','3SB6811-0AA10-0BA0','Caixa vazia 1 Furo','Siemens',0.0),
 (132,'10766','3SB6813-0AA10-0BA0','Caixa vazia 3 Furos','Siemens',0.0),
 (133,'10767','3SB6814-0AA10-0BA0','Caixa vazia 4 Furos','Siemens',0.0),
 (134,'10768','3SB6815-0AA10-0BA0','Caixa vazia 5 Furos','Siemens',0.0),
 (135,'10769','3SE5232-0HR01','Fim de Curso Haste Flexível','Siemens',0.0),
 (136,'10770','5SM1346-0MB','Interruptor  DR 63A x 30mA','Siemens',0.0),
 (137,'10771','8WA1 204','Borne Parafuso 16mm²','Siemens',0.0),
 (138,'10772','8WD4308-0EE','Tubo Metálico - 150 mm','Siemens',0.0),
 (139,'10773','LZS:RT4D4L24','Relé de Interface 2NAF - 24Vcc','Siemens',0.0),
 (140,'10774','16905','Interruptor DR 125A x 30mA','Schneider',0.0),
 (141,'10775','BMH1901P31A2A','Servomotor Lexium 30Nm - 5,2KW - 23A','Schneider',0.0),
 (142,'1871','CA2KN40M7','Contatora Auxiliar 220Vca 4NA','Schneider',0.0),
 (143,'10776','DF101','Porta Fusível 10 x 38','Schneider',0.0),
 (144,'5085','EZ9F33210','Disjuntor 2 pólos C10 A','Schneider',0.0),
 (145,'9609','EZEFASB2','Separador de Fases p/ EZC 250','Schneider',0.0),
 (146,'9611','EZESPDR3P','Distanciador  de Fases p/ EZC250','Schneider',0.0),
 (147,'10783','GV1G10','Capa Proteção Trifásica','Schneider',0.0),
 (148,'1858','GV2AF01','Bloco de Licação GV2/K','Schneider',0.0),
 (149,'5325','GV2G254','Ponte Trifásica 2 Posições','Schneider',0.0),
 (150,'10784','GV2G454','Ponte Trifásica 4 Posições','Schneider',0.0),
 (151,'1866','GV2ME07','Disjuntor-motor 1,6/2,5A','Schneider',0.0),
 (152,'1857','GVAN11','Contato Auxiliar Lateral 1NA/1NF','Schneider',0.0),
 (153,'9608','GVAN20','Contato Auxiliar Lateral 2NA','Schneider',0.0),
 (154,'9631','HMISST','IHM Magelis STU Módulo Traseiro','Schneider',0.0),
 (155,'9630','HMIS85','IHM Magelis STU Painel 5,7"','Schneider',0.0),
 (156,'1859','LA4KE1B','Supressor Varistor 24V','Schneider',0.0),
 (157,'10785','LADN01','Contato Auxiliar Superior 1NF','Schneider',0.0),
 (158,'10786','LADN11','Contato Auxiliar Superior 1NA/1NF','Schneider',0.0),
 (159,'10813','LXM32AD72N4','Servodrive Lexium LXM 32A','Schneider',0.0),
 (160,'10815','RSB2A080BDS','Relé Interface 24V 2NAF','Schneider',0.0),
 (161,'4030','RSL1PVBU','Relé Interface 24V 1NAF','Schneider',0.0),
 (162,'4032','RZM031BN','Diodo + LED Verde 24V','Schneider',0.0),
 (163,'10830','VW3M5103R100','Cabo de Potência 10m','Schneider',0.0),
 (164,'10831','VW3M8102R100','Cabo Encoder 10m','Schneider',0.0),
 (165,'5315','XA2EVB5LC','Sinaleiro LED LR 24V','Schneider',0.0),
 (166,'10816','XAL-D03','Caixa vazia 3 Furos','Schneider',0.0),
 (167,'10817','XAL-D04','Caixa vazia 4 Furos','Schneider',0.0),
 (168,'1883','XB5AA21','Botão Impulso PR 1NA','Schneider',0.0),
 (169,'904','XB5AA41','Botão Impulso VM 1NA','Schneider',0.0),
 (170,'1881','XB5AA51','Botão Impulso AM 1NA','Schneider',0.0),
 (171,'1880','XB5AA61','Botão Impulso AZ 1NA','Schneider',0.0),
 (172,'5318','XB5AD21','Seletora 2Pos. c/Ret. Pr 1NA','Schneider',0.0),
 (173,'9607','XB5AD25','Seletora 2Pos. c/Ret. Pr 1NA/1NF','Schneider',0.0),
 (174,'10832','XB5AD41','Seletora 2Pos. s/Ret. PR 1NA','Schneider',0.0),
 (175,'4037','XB5AK123B5','Seletora 2Pos. c/Ret. Sinal. Vd 2NA','Schneider',0.0),
 (176,'6486','XB5AS8444','Botão Cogumelo Emergência 2NF','Schneider',0.0),
 (177,'10818','ZB5SZ3','Tampão cego 22mm','Schneider',0.0),
 (178,'5319','ZBE-101','Elemento de Contato 1NA','Schneider',0.0),
 (179,'9613','ZBE-102','Elemento de Contato 1NF','Schneider',0.0),
 (180,'10833','ZBV-B1','Sinaleiro LED BR 24V','Schneider',0.0),
 (181,'10834','ZBV-B5','Sinaleiro LED LR 24V','Schneider',0.0),
 (182,'9614','ZBY9420','Etiqueta Circular "Emergência"','Schneider',0.0),
 (183,'10835','BN 63B 4','Motor Trifásico 0,18/0,21KW - 1,2/0,69A','Bonfiglioli',0.0),
 (184,'10836','FB18.37.xx','Esteira Porta-cabos 18x37x65','Igus',0.0),
 (185,'10837','OH-306','Resistor de Frenagem SEW 0,6KW/100Ω','SEW',0.0),
 (186,'10838','E14CD','Microventilador Axial 14cm','Ventisilva',0.0),
 (187,'10850','LC2-50','Célula de Carga 50Kgf','AllPrint',0.0),
 (188,'10851','620-DC-TE','Relé Programável Easy Moeller','Moeller',0.0),
 (189,'10852','BMV5.0','Módulo de Controle de Freio SEW','SEW',0.0),
 (190,'10853','DBG11B-11','Console Inversores SEW','SEW',0.0),
 (191,'10854','9874585','Conector CONIN 12Pin. Fêmea','SEW',0.0),
 (192,'9975','RJ45','Conector RJ45 Plástico','Beta',0.0),
 (193,'7435','ZAF-236-11ZP','Fim de Curso Haste Flexível Schmersal','Schmersall',0.0),
 (194,'821','PB 675060','Tomada 2P+T 10A','Pial - Andra',0.0),
 (195,'10885','B58N2048S6AWES','Encoder Increm. 2048 ppr CONIN M23','SEW',0.0),
 (196,'10857','','Acoplamento  Plástico 23 x 6 mm','',0.0),
 (197,'10858','','Acoplamento  Metálico 36 x 10 mm','Hohner',0.0),
 (198,'10859','MDX61B0040-5A3-4-0T/DER11B','Servo-Drive MDX61 B+ 4KW','SEW',0.0),
 (199,'10860','MDX61B0022-5A3-4-0T/DEH11B','Servo-Drive MDX61 B+ 2,2KW','SEW',0.0),
 (200,'10861','DER11B','Módulo de Encoder/Resolver','SEW',0.0),
 (201,'6552','','Conector DB15 Macho','Beta',0.0),
 (202,'7429','','Conector DB9 Macho','Beta',0.0),
 (203,'6551','','Conector DB15 Fêmea','Beta',0.0),
 (204,'9307','','Conector DB9 Fêmea','Beta',0.0),
 (205,'9306','','Capa DB15 Plástica','Beta',0.0),
 (206,'9301','','Capa DB9 Plástica','Beta',0.0),
 (207,'6817','CUC-DST-GZNI-A/DSSC15','Capa DB15 Metálica','Phoenix',0.0),
 (208,'9361','CUC-DST-GZNI-A/DSSC9','Capa DB9 Metálica','Phoenix',0.0),
 (209,'10862','','Capa DB15 Metálica 2ª Linha','',0.0),
 (210,'10863','','Capa DB9 Metálica 2ª Linha','',0.0),
 (211,'10905','N4006','Tomada Blindada 16A - 3P+T - 380/440V','Steck',0.0),
 (212,'10906','3NW6 001-1','Fusível 10 x 38 - 6A','Siemens',0.0),
 (213,'10907','3NW6 004-1','Fusível 10 x 38 - 4A','Siemens',0.0),
 (214,'10908','RJ45 Blindado','Conector RJ45 Blindado','Beta',0.0),
 (215,'10909','3RV2011-1AA10','Disjuntor-motor 1,1/1,6A','Siemens',0.0),
 (216,'10910','3RV2011-1CA10','Disjuntor-motor 1,8/2,5A','Siemens',0.0),
 (217,'','3RV2011-1FA10','Disjuntor-motor 3,5/5,0A','Siemens',0.0),
 (218,'','3RV1915-2CB','Ponte Trifásica 4 Posições','Siemens',0.0),
 (219,'','3RV2021-4BA10','Disjuntor-motor 13/20A','Siemens',0.0),
 (220,'','5SY4216-8','Disjuntor 2 pólos D16 A','Siemens',0.0),
 (221,'','5SL1332-7MB','Disjuntor 3 pólos C32 A','Siemens',0.0),
 (222,'','5TW3032-1','Seccionadora Tripolar 32A','Siemens',0.0),
 (223,'','3RH2911-1AA01','Contato Auxiliar Frontal 1NF','Siemens',0.0),
 (224,'','3RU2116-1JC0','Relé Térmico 7/10A','Siemens',0.0),
 (225,'','3RU2916-3AA01','Suporte Relé 3RU Parafusos','Siemens',0.0),
 (226,'','3RU2916-3AC01','Suporte Relé 3RU Mola','Siemens',0.0),
 (227,'','LZS:RT4D4T30','Relé de Interface 2NAF - 230Vac','Siemens',0.0),
 (228,'98765','1234','Produto Novo ABC','SEW',0.0);
COMMIT;
