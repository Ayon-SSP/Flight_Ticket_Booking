# Flight Ticket Booking [`📺 Video Link`](https://youtu.be/BVY7doCcjkA)

Create a web application for flight ticket booking. Use any tech stack for the backend and db. A basic UI made outta HTML and CSS is expected. Submissions with a  plain console based CRUD app won't be entertained.

# Flight Booking & Management System ✈️

## Overview
This project is a Flight Booking & Management System developed using Django as the backend framework. It provides a user-friendly interface for users to search, book flights, and manage their bookings. The system also includes admin functionality to add and remove flights. The application features token-based authentication for secure user access.

## Features
- User Authentication: Token-based authentication system to ensure secure user access.
- Flight Search: Users can search for available flights based on date and time.
- Flight Booking: Users can book flights based on seat availability (default seat count is 60).
- Booking Management: Users can view and manage their flight bookings.
- Admin Privileges: Admins have the ability to add and remove flights through the Django admin panel.

## Tech Stack
- Backend: Django, PostgreSQL, SQLAlchemy (preprocessing)
- Frontend: Django Template Language (Jinja), Bootstrap (frontend integration)

## Installation
1. Clone the repository:


# 🎯 Block Model

    Take Home Intervies Round 2 Ayon-ssp c-> DevRev

                                                                     User
                                                                       |
                                                                       ↓
                                                               +-------------------------------------------------------------------------+
                                                               |        Django Default Auth_system and access control                    | (Using Tokens)
                                                               |    User(SignUp, Login, Logout) Admin[Login, create suing django-admin]  |
                                                               +-------------------------------------------------------------------------+
                                                                       ↑        |              |
                                                                       |        |              |  [Admin]           (verify tokens and redirect to the user type)
                                                                [User] |        |              |
                                                                       |        |              |
                                                                       |        ↓              ↓
                   +---------------------------------------------------------------+         +---------------------------------------------------------------+
                   |            Data Storage and Manipulation [SQL (psql)]         |         |            Data Storage and Manipulation [SQL (psql)]         |
                   +---------------------------------------------------------------+         +---------------------------------------------------------------+
                   |    ● Searching for flights based on date and time             |         |    ●  Add Flights                                             |
                   |    ● Booking tickets on a flight based on availability        |         |    ●  Remove flights                                          |
                   |        (assuming the default seat count is 60)                |         |    ●  View all the booking based on flight number             |
                   |    ● My Booking -> to list out all the bookings made by       |         |        and time                                               |
                   |             that user                                         |         +---------------------------------------------------------------+
                   +---------------------------------------------------------------+                            |
                                     ↑                             |   <--(psycopg2)                            |   <--(psycopg2)
                                     |                             |                                            |
                                     |                             |                                            |
                                     |                             ↓                                            |
                                                                                                     +--------------------------+
        [Preprocessing]---(SQLAlchemy ORM)--->[PostgreSQL Database]----------------------------------|     Admin accessible     |
                                                                                                     +--------------------------+



```css
-> Frontend Django Template language(jinja) Html + JS + Bootstrap
                        if time can shift to react JS

-> Backend Django Auth System
       - User(SignUp, Login, Logout)
       - Admin[Login, create suing django-admin]
       - Access control *
       - Using Tokens

-> Backend server takes care of
       - Searching for flights based on date and time
       - Booking tickets on a flight based on availability
           (assuming the default seat count is 60)
       - My Booking -> to list out all the bookings made by
                that user
       - Add Flights
       - Remove flights
       - View all the booking based on flight number
                     and time

-> DataBase (PostgreSQL)
       - PostgreSQL[sql commands]
       - DB schema
       - Access control *
       - Primary key & Foreign key
       - Used ORM (Object-Relational Mapping)


```
