# CSRF Attack Demonstration with Flask

This project demonstrates a **Cross-Site Request Forgery (CSRF)** attack using a Flask web application. The goal is to illustrate how CSRF works and how attackers can exploit vulnerabilities to perform unauthorized actions on behalf of authenticated users.

---

project/
├── app.py               # Main Flask application
├── Dockerfile           # Dockerfile for containerization
├── templates/
│   ├── login.html       # Login page
│   ├── signup.html      # Signup page
│   ├── dashboard.html   # Dashboard after login
│   └── csrf_attack.html # Page simulating the CSRF attack
├── static/
│   ├── styles.css       # Custom styles for the app
│   └── diable.png       # Logo for the app
└── requirements.txt     # Python dependencies

--- 

## Features

- **User Authentication**: Sign up and log in with session handling.
- **Simulated CSRF Attack**: Demonstrates password change exploitation via a hidden form.
- **Email Notification**: Sends an email to notify users about suspicious activity.
- **Themed UI**: A "Diable" theme with custom styling for added engagement.

---

## Prerequisites

1. **Python**: Install Python 3.12 or higher.
2. **Docker**: Ensure Docker is installed on your system.
3. **Email Server**: Use a Gmail account for sending emails.

---


## Installation

### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

## Build and Run the Docker Container
```bash
docker build -t csrf_attack_demo .
docker run -p 5005:5005 csrf_attack_demo
```

## Usage

### 1. Access the Application

Open your browser and navigate to:
```bash
http://localhost:5005

```

### 2. Create an Account
 - Click on the "Sign Up" link.
 - Fill in your details and submit.

### 3. Log In
 - Use your email and password to log in.
 - Upon login, you will be redirected to the dashboard, and an email will be sent to your address.

### 4. Simulate the CSRF Attack
 - Open your email and click on the link included in the message:
 - The link directs you to a page containing a hidden form that automatically submits a password change request without user interaction. Upon visiting the link, the password of the logged-in user will be changed to newpassword123

### 5. Observe the Result
 - Check the Flask console logs to see the CSRF activity and password change.
 - Try logging in again with the new password (newpassword123) to verify the attack's success.