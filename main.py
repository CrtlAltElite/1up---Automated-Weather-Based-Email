import csv
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from dotenv import load_dotenv

# Loading environment variables from a .env file
load_dotenv()
OPEN_WEATHER_KEY = os.environ.get("OPEN_WEATHER_KEY")  # API key for OpenWeatherMap
SENDGRID_KEY = os.environ.get("SENDGRID_KEY")  # API key for SendGrid

# Function to read CSV data
def read_csv(file_path):
    # Open the CSV file for reading
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Read the file as a dictionary
        return [row for row in reader]  # Return a list of dictionaries, each representing a row

# Function to check if it's raining in a city
def is_raining(city, country_code):
    # Construct the URL for the API request
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={OPEN_WEATHER_KEY}"
    response = requests.get(url)  # Make the API request
    data = response.json()  # Parse the response as JSON
    # Return True if any weather condition is in the range of rain codes (500-531)
    return any(weather['id'] for weather in data['weather'] if 200 <= weather['id'] <= 622)

# Function to send email using SendGrid
def send_email(receiver_email, subject, body):
    # Prepare the email message
    message = Mail(
        from_email='studentsuccess@codingtemple.com',
        to_emails=receiver_email,
        subject=subject,
        plain_text_content=body)

    try:
        sg = SendGridAPIClient(SENDGRID_KEY)  # Initialize SendGrid client with the API key
        response = sg.send(message)  # Send the email
        # Print the response status
        print(f"Email sent to {receiver_email}: Status Code {response.status_code}")
    except Exception as e:
        # Print any errors during the email sending process
        print(f"Error sending email to {receiver_email}: {e}")

# Main function to process CSV data, check weather and send emails
def main(csv_file):
    clients = read_csv(csv_file)  # Read clients from the CSV file
    for client in clients:
        # Check if it is raining in the client's city
        if is_raining(client['city'], client['country_code']):
            # Prepare the email content
            subject = "Special Promotion on Windshield Wipers!"
            body = "It's raining in your city! Grab your discounted windshield wipers now."
            # Send the email
            send_email(client['email'], subject, body)

# Standard Python boilerplate to execute the main function
if __name__ == "__main__":
    main('clients.csv')  # Call the main function with the CSV file name
