# NOTA
[![CC BY 4.0][cc-by-shield]][cc-by]

NOTA: Simple List Sharing API

Welcome to NOTA, a simple list sharing API built with Python and Django Rest Framework.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [API Documentation](#api-documentation)
- [Installation](#installation)
- [Endpoints](#endpoints)

## Introduction
NOTA is a user-friendly application designed to facilitate list sharing among users. With features like user registration, login/logout functionalities, and the ability to create, edit, delete, and share lists, NOTA provides a seamless experience for managing and sharing your lists with others.

## Features
1. User Authentication: Utilizes JWT token-based authentication for secure user registration, login, and logout.
2. User Management: Allows users to create, edit, and delete their lists.
3. List Sharing: Enables users to share their lists with other users.
4. Swagger Integration: Integrated Swagger for easy access to API documentation.

## API Documentation
Explore the endpoints and functionalities of NOTA through its API documentation provided via Swagger.

## Installation
Follow these steps to set up NOTA on your local machine:

1. Create Virtual Environment: Set up a virtual environment using the following command:
```
python -m venv venv
```
2. Activate Virtual Environment: Activate the virtual environment:
```
source venv/bin/activate
```
3. Install Required Packages: Install the necessary packages using pip:
```
pip install -r requirements.txt
```
4. Run Server: Start the server to run NOTA:
```
python manage.py runserver
```

## Endpoints
Explore the various endpoints implemented in NOTA:

### Core Functionality
- Generate Token: Generate access and refresh tokens for authentication.
- Register User: Register a new user.
- Login User: Log in a user.
- Change Password: Change the user's password.
- Update User Profile: Update the user's profile.
- Logout User: Log out the user.
- Logout User from All Devices: Log out the user from all devices.
- Delete User: Delete the user account.

### App Features
- Create User List Labels: Create labels for user lists.
- Create User List: Create a new user list.
- Update User List: Update an existing user list.
- Share User List: Share a user list with other users.
- Delete User List: Delete a user list.

## License


Nota © 2024 by Gowtham Hanumanthu is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg