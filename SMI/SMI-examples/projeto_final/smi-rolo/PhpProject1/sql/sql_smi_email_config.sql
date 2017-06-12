CREATE TABLE email(
	dominio varchar(20) not null,
	smtp_server varchar(30) not null,
	port int not null,
	UseSsl boolean not null,
	CONSTRAINT pk_dominio1 primary key(dominio)
);
 

insert into email(dominio,smtp_server,port,UseSsl) values("sapo","smtp.sapo.pt",587,0);
insert into email(dominio,smtp_server,port,UseSsl) values("hotmail","smtp.live.com",25,0);
insert into email(dominio,smtp_server,port,UseSsl) values("gmail","smtp.gmail.com",465,1);
insert into email(dominio,smtp_server,port,UseSsl) values("ipl","smtp.net.ipl.pt",587,0);
insert into email(dominio,smtp_server,port,UseSsl) values("isel","pod51014.outlook.com",587,0);
