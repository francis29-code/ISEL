CREATE TABLE UserClient(
	tipo varchar(10) not null,
	nome varchar(160) not null,
	username varchar(20) not null,
	password varchar(10) not null,
	email varchar(160) not null,
	valido boolean not null,
	Fotografia  varchar(160) not null,
	CONSTRAINT pk_username primary key(username)	
);
CREATE TABLE Ficheiro(
	nome varchar(160) not null,
	id int not null,
	username varchar(20) not null,
	mime varchar(15) not null,
	tipo varchar(15) not null,
	conteudo varchar(160) not null,
	conteudo_thumbs varchar(160) not null,
	constraint fk_user foreign key(username) references userclient(username),
	CONSTRAINT pk_nome primary key(nome)
);