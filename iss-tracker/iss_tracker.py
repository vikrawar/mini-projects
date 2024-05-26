import requests
import smtplib
import time
from datetime import datetime
import ephem

def get_iss_location():
    """
    Fetches the current latitude and longitude of the ISS.

    Returns:
        tuple: A tuple containing the latitude and longitude of the ISS.
    """
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    return float(data['iss_position']['latitude']), float(data['iss_position']['longitude'])

def is_night(lat, long):
    """
    Determines if it's nighttime at the specified location.

    Args:
        lat (float): Latitude of the location.
        long (float): Longitude of the location.

    Returns:
        bool: True if it is nighttime, False otherwise.
    """
    observer = ephem.Observer()
    observer.lat = str(lat)
    observer.lon = str(long)
    observer.date = datetime.utcnow()
    sun = ephem.Sun()
    sun.compute(observer)
    return sun.alt < 0

def send_email(sender_email, sender_password, receiver_email):
    """
    Sends an email notification indicating that the ISS is overhead.

    Args:
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        receiver_email (str): The receiver's email address.
    """
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg='Subject:ISS visible\n\nThe ISS is above you! Look up!'
        )

def track_iss(lat=123, long=123, sender_email="test@gmail.com", sender_password="xyz", receiver_email="abc@pace.edu"):
    """
    Tracks the ISS and sends an email notification when the ISS is overhead at night.

    Args:
        lat (float): Latitude of the location. Defaults to 123.
        long (float): Longitude of the location. Defaults to 123.
        sender_email (str): The sender's email address. Defaults to "test@gmail.com".
        sender_password (str): The sender's email password. Defaults to "xyz".
        receiver_email (str): The receiver's email address. Defaults to "abc@pace.edu".
    """
    while True:
        # Check if it's night time
        if is_night(lat, long):
            # Get the current ISS location
            iss_lat, iss_long = get_iss_location()

            # Check if the ISS is within a 5-degree range of the specified location
            if (lat - 5 < iss_lat < lat + 5) and (long - 5 < iss_long < long + 5):
                # Send email notification
                send_email(sender_email, sender_password, receiver_email)
                # Sleep for 10 hours after sending the notification
                time.sleep(60 * 60 * 10)

        # Wait for 1 minute before checking again
        time.sleep(60)

def main():
    """
    Interface for user to input parameters and start tracking the ISS.
    """
    # Get user input for parameters
    lat = input("Enter latitude (default is 123): ") or 123
    long = input("Enter longitude (default is 123): ") or 123
    sender_email = input("Enter sender email (default is test@gmail.com): ") or "test@gmail.com"
    sender_password = input("Enter sender email password (default is xyz): ") or "xyz"
    receiver_email = input("Enter receiver email (default is abc@pace.edu): ") or "abc@pace.edu"

    # Convert latitude and longitude to float
    lat = float(lat)
    long = float(long)

    # Start tracking the ISS
    track_iss(lat, long, sender_email, sender_password, receiver_email)

# Call the main function
if __name__ == "__main__":
    main()
