# Logistic Regression Integration with Java Web Application

This project integrates a **Logistic Regression model** with a **Java web application**. It demonstrates the usage of **JDBC** for database connectivity, **DAO** pattern for interacting with the database, and a **web interface** for managing user data and interacting with machine learning models.

## Features

- **Database Connectivity**: Uses JDBC to connect to a MySQL database.
- **User Management**: Allows users to register and manage their profiles.
- **Machine Learning Integration**: The logistic regression model is used for predictions, and it's integrated into the web application.
- **Web Interface**: Built with **HTML**, **CSS**, and **Bootstrap** for a responsive user interface.
- **Model Integration**: Seamlessly integrates the logistic regression model into the Java backend to process user inputs and provide predictions.

## Project Structure

- **`src/main/java/com/example/`**: Contains all Java source code.
    - **`model`**: Defines the user and machine learning model classes.
    - **`dao`**: Contains Data Access Object classes for interacting with the database.
    - **`util`**: Contains utility classes like `DBConnection` for database connections.
    - **`web`**: Contains servlets and web-related components.
- **`src/main/webapp/`**: Contains web resources (HTML, CSS, JS).
    - **`WEB-INF`**: Contains configuration files and JSP pages.

## Requirements

- **JDK 17** (or a preferred version).
- **MySQL** Database.
- **Maven** for dependency management.

## Setup

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/logistic-regression-integration.git
