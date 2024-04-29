
# Flask Calendar Web App

A dynamic calendar web application designed to make scheduling and socializing seamless and fun. Built using Python, Flask, and FullCalendar.js, this application allows users to easily manage their schedules and plan activities with friends.

## Features

- **User Authentication**: Secure login and sign-up functionalities to manage personal accounts.
- **Interactive Calendar**: Users can add and view events directly on a responsive calendar interface.
- **Mobile Compatibility**: Responsive design ensures functionality across different devices.
- **Random Event Picker**: Suggests random activities to make deciding on hangouts fun and effortless.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python 3.6 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installing

Clone the repository to your local machine:

git clone [https://github.com/yourusername/flask-calendar-app.git](https://github.com/nmsu-cs/project-rise.git)
cd project-rise


Install the required packages:

pip install flask Flask-SQLAlchemy flask-login

### Setting Up the Database // ### Running the Application

Initialize the database with the following commands:

Simply run main.py -- which will start the local server, and initialize the database.

Navigate to `http://localhost:5000` in your web browser to view the app.

## Project Structure

Flask Web App/
│
├── instance/
│   └── database.db
├── website
│   ├── static
│   │   └── node_modules
│   │       └── @fullcalendar
│   │           ├── core
│   │           ├── daygrid
│   │           ├── interaction
│   │           └── timegrid
│   ├── templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── sign_up.html
│   │   ├── poll.html
│   │   ├── create_poll.html
│   │   ├── view_polls.html
│   │   └── random_event.html
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   └── views.py
├── main.py
├── package.json
└── package-lock.json

## Contributing

We welcome contributions from everyone. If you would like to contribute, please fork the repository and submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## References

- Built the front end and back end with the help of @Tech With Tim's youtube channel
          - USED VIDEO: https://www.youtube.com/watch?v=dam0GPOAvVI&start=429
- Help with fullCalendar.js framework implementation with @Error Solution's youtube
          - USED VIDEO: https://youtu.be/fcLrjVKkrc8?si=bYcxsvy9GgezOD4D
  
