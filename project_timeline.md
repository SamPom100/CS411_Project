# Project Timeline

## Meetings

### when2meet 📅
* We first created a [when2meet](when2meet.com) to establish a weekly meeting schedule; however, we ended up meeting whenever possible and sometimes in smaller groups in case other group members could not attend

### Lab Section 👨‍🔬
* In our lab section (A5), our whole group met weekly to provide project updates, suggestions, and collaborative bug fixing.

### WhatsApp 📞
* To allow for external communication, we created a WhatsApp group chat to ask questions, deliver updates, and post updates to allow for a more-inclusive and open collaborative environment

## **Assignment 1**

We proposed the following ideas:

1. MBTA schedules and determining the quickest route to class
2. Potential NFT project
3. Law Firm project
4. Potential bio-related project
5. Food recommendations
6. Trip recommendation/planner

And narrowed it down in [`Assignments/Assignment1.md`](https://github.com/SamPom100/CS411_Project/blob/main/Assignments/Assignment1.md)

## **Assignment 2**

We wrote our user stories in [`Assignments/Assignment2.md`](https://github.com/SamPom100/CS411_Project/blob/main/Assignments/Assignment2.md)

## **Assignment 3**

To start the project, we proposed the architecture located in [`Assignments/Assignment3.md`](https://github.com/SamPom100/CS411_Project/blob/main/Assignments/Assignment3.md)

## Project Changes
### *New Project Deliverables*

* Having over-estimated the time provided, we narrowed our deliverables by only doing the following:
    1. Using a Weather API to get the desired city's weather
    2. Using google maps API to load fun things to do and hotels given the provided location
    3. Have a google log-in
    4. Have a normal, flask-integrated log-in system

### *Original Project Deliverables*
* Inititally we planned on delivering the following items along with our current application:
    1. The ability to save travel information to your profile 
    2. The ability to add friends and collaborate on planning trips together
    3. Syncing travel plans to google calendar 

### *Back-end implementation*

* We began to implement the back-end using Flask; however, we’ve decided to not proceed with Django with a vote.

### *Front-end implementation*

* Rather than the proposed React.js implementation, we pursued HTML/CSS, being more convenient and comfortable to use for our team.

### *Collecting API Payload*
* We collected API payload by obtaining the appropriate `.json` files, no direct use of xml due to all collected payloads being in `.json`.

### *Database*
* Instead of MongoDB, we used MySQL and SQL Workbench to run and allow for communication between the backend and the database query.

### *APIs used*
In our project, we used the following APIs: 
* Openweathermap to collect city temperature 
* Google maps to get weather, things to do, and hotels.

### *Protection*
* We have our API keys saved locally and not published on git.
* For google log-in, we implemented a login-requirement feature to ensure the user cannot simply manipulate the login URL to obtain desired personal data.


## *In-depth framework-use analysis*
*Languages used: **Python 3** | **HTML** | **CSS*** 
* HTML/CSS - We created various CSS templates to add some pizazz on our front-end UI design, and used HTML to create a menu, buttons, and our webpage to allow for easy conversation between the client and the web application. Moreover, the HTML buttons connect the front-end and back-end.

* Flask - this software is responsible for our back-end completely, using it to fetch payloads, call APIs, and manage our database. For example, we used flask to call weather and hotel information apis.
* SQL - We made an SQL table to manage users, friends, desired destinations, and vacation plans. We also planned working with adding friends and setting vacation plans before realizing our project scope was too large given our timeframe.



