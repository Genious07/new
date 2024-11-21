import requests
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["jobAutomationDB"]
users_collection = db["users"]

# Replace with your own LinkedIn API credentials
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'YOUR_REDIRECT_URI'
AUTHORIZATION_CODE = 'YOUR_AUTHORIZATION_CODE'

# Step 1: Get access token
def get_access_token():
    auth_url = 'https://www.linkedin.com/oauth/v2/accessToken'
    data = {
        'grant_type': 'authorization_code',
        'code': AUTHORIZATION_CODE,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    
    response = requests.post(auth_url, data=data)
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        return access_token
    else:
        print("Error obtaining access token:", response.json())
        return None

# Fetch user data from MongoDB
def get_users():
    try:
        return list(users_collection.find({}))
    except Exception as e:
        print(f"Error fetching users from DB: {e}")
        return []

# Apply jobs on LinkedIn using API
def apply_jobs_on_linkedin(user_data, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # Apply for each job in the user's job list
    for job_id in user_data['jobs']:
        url = f'https://api.linkedin.com/v2/jobs/{job_id}/apply'
        payload = {
            "resume": user_data['resume'],  # Ensure you have a resume URL or file
            "coverLetter": "Your personalized cover letter"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 201:
            print(f"Successfully applied to job {job_id}")
        else:
            print(f"Failed to apply to job {job_id}: {response.json()}")

# Main execution
def main():
    users = get_users()
    access_token = get_access_token()
    
    if access_token:
        for user in users:
            print(f"Processing user: {user['name']} - Applying to jobs...")
            apply_jobs_on_linkedin(user, access_token)
    else:
        print("Error: Could not retrieve access token.")

if __name__ == "__main__":
    main()
