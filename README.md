# Secure CRUD API using Flask, PostgreSQL & Docker

Project Overview

This project is a secure, containerized CRUD (Create, Read, Update, Delete) API built using Flask and PostgreSQL. The application is fully dockerized using Docker and Docker Compose, with Nginx as a reverse proxy and Gunicorn as the production server.

The project demonstrates backend development, database integration, containerization, and DevOps best practices.


#  Tech Stack

- Python 3.11
- Flask
- SQLAlchemy
- PostgreSQL 15
- Gunicorn
- Nginx
- Docker
- Docker Compose


# Architecture

Client → Nginx → Gunicorn → Flask App → PostgreSQL

- Nginx handles incoming HTTP requests
- Gunicorn runs the Flask app
- PostgreSQL stores task data
- Docker Compose manages multi-container setup

# How To Run The Project

## Clone the repository

```bash
git clone https://github.com/soumyashree2311/secure-crud.git
cd secure-crud
