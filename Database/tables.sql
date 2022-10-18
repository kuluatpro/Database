create table if not exists users (
user_id varchar(10) not null,
rights varchar(100) not null,
primary key (user_id)
);

create table if not exists task (
task_id varchar(10) not null,
pver_name varchar(50) not null,
oem varchar(10) not null,
primary key (task_id)
);

create table if not exists warnings (
defect_id int primary key auto_increment,
code_line varchar(100) not null,
line_in_source int not null,
function_name varchar(100) not null,
warning_prio varchar(10) not null,
user_id varchar(10) not null,
task_id varchar(10) not null,
foreign key (user_id) references users (user_id),
foreign key (task_id) references task (task_id)
);




-- alter table warnings add assessor varchar(10);

