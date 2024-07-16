# Hyperion Project

## Overview
Hyperion is a Django-based web application that includes a polls app and user authentication. It provides functionality for users to register, log in, vote in polls, and view poll results.

## Features
- User registration and authentication
- Poll creation and voting
- View poll results
- Admin interface for managing polls and users

## Setup and Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Virtualenv (recommended)

### Installation Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/hyperion.git
    cd hyperion
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser for accessing the admin interface:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    - Open a web browser and go to `http://127.0.0.1:8000/`
    - Admin interface: `http://127.0.0.1:8000/admin/`

## Usage

### Polls
- Navigate to the polls section to view available polls.
- Vote on a poll by selecting an option and submitting your vote.
- View poll results after voting.

### User Authentication
- Register a new user account.
- Log in with your credentials.
- Log out from the application.

## Project Structure
