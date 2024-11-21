# LinkedIn Job Automation

This project automates the process of applying to jobs on LinkedIn using user data stored in MongoDB and the LinkedIn API. The program retrieves user information, such as resumes and job preferences, and applies to jobs listed on LinkedIn on their behalf.

## Features

- **MongoDB Integration**: Fetches user information from a MongoDB database.
- **LinkedIn API Integration**: Utilizes LinkedIn’s OAuth 2.0 authorization and the Jobs API to apply for jobs on LinkedIn.
- **Job Application Automation**: Automatically applies for jobs based on user preferences stored in MongoDB.
- **Error Handling**: Handles errors for MongoDB access and API responses, ensuring smooth operation.

## Requirements

- Python 3.x
- `requests` library
- `pymongo` library
- MongoDB server running locally (or configure it to use a remote database)
- LinkedIn API credentials (Client ID, Client Secret, Redirect URI, Authorization Code)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/linkedIn-job-automation.git



Ensure MongoDB is running on your local machine or configure the connection string in the code if using a remote MongoDB instance.

Set up your LinkedIn API credentials:

Create an application on the LinkedIn Developer Portal: https://www.linkedin.com/developers/
Obtain your CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, and AUTHORIZATION_CODE.
Replace the placeholders in the code with your LinkedIn credentials.



Setup MongoDB Database:
Your MongoDB should have a database named jobAutomationDB and a collection users. Each document in the users collection should have the following fields:

name: The user's name
jobs: A list of job IDs to apply for
resume: A URL or file path to the user's resume
coverLetter: A personalized cover letter (optional)


Error Handling
If the access token cannot be obtained, the process halts with an error message.
Errors encountered while fetching user data from MongoDB or applying to jobs are printed to the console.
