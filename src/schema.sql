CREATE DATABASE IF NOT EXISTS travel_planner;
USE travel_planner;

CREATE TABLE users (
    user_id int4 AUTO_INCREMENT,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    first_name	varchar(255) NOT NULL,
    last_name	varchar(255) NOT NULL,
    dob	date NOT NULL,
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

CREATE TABLE locations
(
	city_id int4 AUTO_INCREMENT,
	city varchar(255),
    PRIMARY KEY (city_id)
);

CREATE TABLE activity
(
	act_id int4 AUTO_INCREMENT,
	activity varchar(255),
    PRIMARY KEY (act_id)
);

CREATE TABLE plan
(
	plan_id int4 AUTO_INCREMENT,
	user_id int4,
    city_id int4,
    act_id int4,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (city_id) REFERENCES locations(city_id),
    FOREIGN KEY (act_id) REFERENCES activity(act_id),
    PRIMARY KEY (plan_id)
);

CREATE TABLE plan_with
(
	plan_id int4,
    user_id int4,
    friend_id int4,
    FOREIGN KEY (plan_id) REFERENCES plan(plan_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (friend_id) REFERENCES users(user_id),
	PRIMARY KEY (plan_id, user_id, friend_id)

);

