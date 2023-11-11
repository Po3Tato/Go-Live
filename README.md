# Go-Live

## Overview
Go-Live is a Python application designed to streamline the process of starting live streams, particularly it was written to automate Livestreaming at my Church. It automates the opening and arrangement of necessary software such as OBS Studio and Zoom, allowing for a quick startup with no human intervention.

## Features
- Automatic launch of OBS Studio in the correct working directory.
- Auto-joining of specified Zoom meetings with meeting ID and password.
- Auto-resizing and positioning of application windows for Zoom and OBS.
- Customizable through environment variables for different meeting IDs and passwords.

## Prerequisites
Before using Go-Live, make sure the following software is installed:
- [OBS Studio](https://obsproject.com/)
- [Zoom Client](https://zoom.us/download)

## Setup
1. Clone the repository or download the source code.
2. Install the required dependencies by running `pip install -r requirements.txt` (make sure you have Python installed).
3. Update the `.env` file with your Zoom meeting ID and password.

## Configuration
To configure Go-Live for your environment, follow these steps:
1. Open the `.env` file in a text editor.
2. Set the `ZOOM_MEETING_ID` and `ZOOM_MEETING_PASSWORD` variables with your meeting details.

## Usage

To start the live stream setup, run the script with:

`python go_live.py`

Make sure to set Zoom to automatically join audio by following these steps:

    Open your Zoom client and sign in to your account.
    Click on your profile picture or the gear icon to go to "Settings."
    Navigate to the "Audio" tab.
    Check the option "Automatically join audio by computer when joining a meeting."

Customization

You can customize the window positions and sizes by editing the resize_app function calls in the main function with your desired coordinates and dimensions.
Contributions

Contributions to Go-Live are welcome. Feel free to fork the repository, make changes, and submit a pull request.