# YouTube_spam_remover

This is a Python project that allows you to extract the comments from a YouTube video, remove spam comments, and save the clean comments in a CSV file.

Getting Started
Prerequisites
To use this project, you need to have the following software installed:

Python 3.x
The Google API Client Library for Python (google-api-python-client)
The BeautifulSoup4 library (bs4)
Installing
To install the required Python libraries, run:

Copy code
pip install google-api-python-client bs4
Configuration
Before using the project, you need to obtain a YouTube API key from Google. Follow these steps:

Go to the Google Developers Console
Create a new project (or select an existing one)
Enable the YouTube Data API v3 for the project
Create a new API key
You also need to have a Google OAuth 2.0 client secret file, which you can obtain by following the Google OAuth2 Python Quickstart.

Usage
To use the project, run the extractor.py file with the following command:

Copy code
python extractor.py
The program will prompt you to enter the following information:

The YouTube video URL (without the time stamp and featured)
The maximum number of comments to extract (up to 1000)
Whether to save the API key for future use
The path to the Google OAuth 2.0 client secret file
Once you enter this information, the program will extract the comments from the video, remove spam comments, and save the clean comments in a CSV file.
