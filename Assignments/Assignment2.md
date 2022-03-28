# CS411 Lab Team Assignment 2

https://docs.google.com/document/d/1bCQtv3H0S7zDGbpG-YgipvVEgwPDY7vqLpmsI-Vufls/edit

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



# User Stories for Trip Planner App

## User Story 1
“As a user, I want to be able to select and find my desired trip location on the application”

### Happy Path:
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
- Displays results to user

### Unhappy Path:
User opens our web-app.
User inputs where they want to go.
Our web-app doesn’t recognize the place, and can’t display any information to them about the weather.

This feature is important because users would like to know the weather and stuff to do in the area they’re headed to before going, to see if they’ll have a nice trip or not.


&nbsp;
&nbsp;
&nbsp;


## User Story 2: 
“As a user, I want to link any travel plans to my calendar”

### Happy Path: 
Ideally the user can link the app to their google calendar and once they choose an activity they like, they can schedule it and add it to their calendar. 

### Exceptions: 
Users cannot find the location they want to visit on the web app therefore they cannot schedule activities to add to their calendar. 
There are only a couple of activities available but the user does not like any of the possible options. 

### Description of feature:
The feature is important because it lets the user see their vacation plans without having to log into the app. The user can just check their calendar for events. 

Actions user will perform:
User opens our web-app
User login into their profile
User inputs locations they want to go
Web app recommends 10 things to do in the location:
If the user is interested
Find available dates
Send booking email to user
ADD event to user’s preferred calendar (google calendar)
Else:
Show more options

&nbsp;
&nbsp;
&nbsp;

## User Story 3: 
“As a user I want to be able to add people to my travel plans“

### Happy Path:
The user will open our web app and login into their profile. They will find their existing booking in their profile and they will have the option to add people to their current plans. They can then add the emails fo the people they to share their plans with. If the person who receives the invite wants to accept it, they can accept the invitation and will be directed to the web application and can then view the travel plans. If the person does not want to accept the invitation they can just decline the invitation and they will not be able to view travel plans. 

### Exceptions:
Issues that can arise with this is that the user could input the incorrect email and the travel plans could not be sent to the correct person. Also depending on the types of packages selected the user may encounter a limit on the number of people they are allowed to share their travel details with. 

### Description of Feature:
This feature is important because it will enable the user to share their plans with their friends and we can have people creating group trips together on the website to making travel planning much easier for people. This is a benefit to people that frequently travel in groups as to not have any gaps in communication with each other. 

&nbsp;
&nbsp;
&nbsp;

## User Story 4:
As a user, I would like to be able to select my favorite options from the proposed list of trip ideas, created from the user’s interests input into the application. 

### Happy Path: 
User opens our web application
User logins into their profile
User begins to create a plan for their desired location
A list of options is created based off the user’s selected interests
A save option is created to save it onto your user account

### Unhappy Path:
A user cannot choose a list of proposed options and are given only one based on their interests. However, the user is not completely content with the proposed plan and wished, for example, another ski resort option was provided.

### Feature significance:
Having an array of proposed trip plans to select from would allow the user to be more content with their travel plan (created from the application). While the user can select their interests when generating a list of travel plans, that does not mean they’ll necessarily be satisfied with all the places provided. For instance, they would prefer to go to another ski resort because their child wants to go really badly, and that could’ve been in the list of proposed travel plans.

&nbsp;
&nbsp;
&nbsp;

## User Story 5: Unhappy Ones
“As a user, I won’t be able to make reservations through one site”
User opens our web-app
User logs into their profile
User enters their desired location
User enters where they want to live and what they want to do
User get different URL for reservation
User needs to click the URL and jump to different websites in order to make reservations.
“As a user, I won’t be able to compare the price if I’m the member of one hotel and not the other”
User opens our web-app
User logs into their profile
User enters their desired location
User enters where they want to live and what they want to do
User gets the price for all the flights, hotels and activities without knowing if they are the member or not.
“As a user, I won’t be able to change the reservation automatically, if there is a lower price pops up”
User opens our web-app
User logs into their profile
User enters their desired location
User enters where they want to live and what they want to do
User make the reservation through the external URL
Our site cannot monitor the reservation, so if there is a better price pop up, the reservation cannot be changed automatically.

&nbsp;
&nbsp;
&nbsp;

## User Story 6:
“As a user, I want to be able to filter my search better to select the correct desired destination”

### Happy path:
  - User opens our web-app
  - User logs into their profile
  - User enters their desired location
  - If the name of the location entered has multiple destinations:
  - More context for the location (the state and country) is shown

### Unhappy path: 
  - User opens our web-app
  - User logs into their profile
  - User enters their desired location
  - The web-app does not show enough context making the user select the incorrect destination

### Feature significance: This feature would enable users to enter and select the correct desired locations. For example, if the user's desired location is Miami in Florida, but the the web-app selects another city with the same name like Miami in Ohio, it would be incorrect and thus, having this feature would eliminate any such issues.
