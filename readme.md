# Automated Weather-Based Email Workshop

## Overview
This workshop covers the development of a Python application that reads client data from a CSV file, checks the current weather for each client's city using an API, and sends out promotional emails based on the weather condition (rain). 

## Objectives
- Understand how to read data from CSV files in Python.
- Learn how to make API requests to gather weather data.
- Automate sending emails based on data-driven conditions.

## Key Python Packages

### `csv`
- **Purpose**: To read from and write to CSV files in Python.
- **Usage in Project**: We use `csv.DictReader` to read client data from a CSV file and process it as a list of dictionaries.

### `requests`
- **Purpose**: To send HTTP requests in Python, essential for API interactions.
- **Usage in Project**: Used to make GET requests to the OpenWeatherMap API to fetch current weather data for each client's city.

### `sendgrid`
- **Purpose**: SendGrid's Python library, used for sending emails through the SendGrid platform.
- **Usage in Project**: Utilized to programmatically send emails to clients. This includes composing the email and handling the sending process.

### `os`
- **Purpose**: Provides a way of using operating system dependent functionality like reading or writing to the environment variables.
- **Usage in Project**: Used to access API keys stored in environment variables for security purposes.

### `dotenv`
- **Purpose**: To load environment variables from a `.env` file into the script, which is crucial for not hardcoding sensitive data like API keys.
- **Usage in Project**: Implemented at the start of the script to load the OpenWeatherMap and SendGrid API keys.

## Workshop Flow

1. **Introduction to the Project**: Understanding the goal and the steps involved.
2. **Setting Up the Environment**: Installing necessary packages and setting up API keys.
3. **Reading and Understanding CSV Data**: Using the `csv` package to read client data.
4. **API Interaction for Weather Data**: Making GET requests to OpenWeatherMap API using the `requests` package.
5. **Automating Email Dispatch**: Composing and sending emails through SendGrid using the `sendgrid` package.
6. **Bringing It All Together**: Writing the main script to automate the entire process.
7. **Testing and Troubleshooting**: Running the script and analyzing the results.

## Additional Resources
- Python Documentation: https://www.python.org/doc/
- CSV File Handling in Python: https://docs.python.org/3/library/csv.html
- Requests: HTTP for Humans: https://requests.readthedocs.io/en/master/
- SendGrid Python API Library: https://github.com/sendgrid/sendgrid-python
- Dotenv: https://pypi.org/project/python-dotenv/

## Conclusion
This workshop provides a hands-on experience in automating a practical task using Python. It combines data handling, API interaction, and email automation, offering a glimpse into the power of Python for real-world applications.
