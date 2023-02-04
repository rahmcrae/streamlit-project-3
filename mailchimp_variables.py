import os

api_key = os.getenv('MAILCHIMP_API_KEY')
audience_id = os.getenv('MAILCHIMP_AUDIENCE_ID')
url = f"https://us13.api.mailchimp.com/3.0/lists/{audience_id}/members"