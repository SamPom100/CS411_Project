CREATE DATABASE IF NOT EXISTS travel_planner;
USE travel_planner;

CREATE TABLE users (
    user_id int4 AUTO_INCREMENT,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    first_name	varchar(255) NOT NULL,
    last_name	varchar(255) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE friends
(
	user_id int4,
	friend_id int4,
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (friend_id) REFERENCES users(user_id),
	PRIMARY KEY (user_id, friend_id)
);

CREATE TABLE destination
(
	city varchar(255),
    PRIMARY KEY (city)
);

CREATE TABLE activity
(
	act_id int4 AUTO_INCREMENT,
	act varchar(255),
    city varchar(255),
    FOREIGN KEY (city) REFERENCES destination(city),
    PRIMARY KEY (act_id)
);

CREATE TABLE vacation_plan
(
	plan_id int4 AUTO_INCREMENT,
    city varchar(255),
	user_id int4,
    act_id int4,
    date_created date,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (city) REFERENCES destination(city),
    FOREIGN KEY (act_id) REFERENCES activity(act_id),
    PRIMARY KEY (plan_id)
);

CREATE TABLE plan_with
(
	plan_id int4,
    user_id int4,
    friend_id int4,
    FOREIGN KEY (plan_id) REFERENCES vacation_plan(plan_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (friend_id) REFERENCES users(user_id),
	PRIMARY KEY (plan_id, user_id, friend_id)

);

CREATE TABLE liked_act
(
    act_id int4,
    user_id int4,
    plan_id int4,
    FOREIGN KEY (act_id) REFERENCES activity(act_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (plan_id) REFERENCES vacation_plan(plan_id),
    PRIMARY KEY (act_id, user_id)
);


INSERT INTO users (email, password, first_name, last_name) VALUES ('s@bu.edu', '123456', 'Sharon', 'Mizrahi');
