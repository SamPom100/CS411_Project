# CS411 Lab Team Assignment 2

## Requirements

- 5 user stories
- Descriptions of what each user story covers
- "Happy path" and "exceptions"

- Information about how the user will interact with the application

- Due March 27th



## What is a User Story

- Description with prompts if needed of a set of interactions with the app from a user or subsystem's perspective

- Perspective of the end user

- Informal, general explanation of a software feature

- Further converted into use cases, then formalized requirements



## User Stories for Trip Planner App

### User Story 1
“As a user, I want to look up a place and see what to do there”
- User opens our web-app 
- User inputs the place they want to go 
- Web app recommends checks backend server to see if that place has been searched before 

If NOT, then it checks 

- Weather API for weather
- Yahoo for top things to do in the area
- Other APIs
- Inputs API data into backend server
- Gets data from backend server

If YES then

- Gets data from backend server
Displays results to user




### User Story 2
“As a user, I want to link any travel plans to my calendar”
- User opens our web-app
- User login into their profile
- User inputs locations they want to go
- Web app recommends 10 things to do in the location:

If the user is interested
- Find available dates
- Send booking email to user
- ADD event to user’s preferred calendar (google calendar)
Else:
- Show more options




