CREATE TABLE todo
(
    id    serial primary key,
    name        VARCHAR(40) not null,
    description        varchar(255)
);

insert into todo (name,description) values ('Pigeons','Fill room with pigeons');
insert into todo (name,description) values ('Cat','Throw cat into room with pigeons');
insert into todo (name,description) values ('Profit','!!!');

alter table todo owner to docker;