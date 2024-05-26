# ISS Tracker

This project tracks the International Space Station (ISS) and sends an email notification when the ISS is overhead at night.

## Features
- Fetches the current location of the ISS
- Checks if it's nighttime at a given location
- Sends an email notification when the ISS is overhead at night

## Installation
To run this project, you'll need to install the required dependencies. You can do this using the following command:

`pip install -r requirements.txt`


## Usage
1. Clone the repository.
2. Run the notebook and provide the requested input when prompted:
   - Latitude
   - Longitude
   - Sender email
   - Sender email password
   - Receiver email

## Dependencies
- requests
- smtplib
- datetime
- ephem
