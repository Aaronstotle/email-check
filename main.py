import requests
import pandas as pd
import datetime
import os


''' This program imports a list of emails from a txt file and checks their reputation using the emailrep.io API, it outputs a timestamped CSV file. 

Set the API key needed from email rep: 

export API_KEY='Your API Key here'


Sample JSON response below

{'email': '00finess00@example.com', 'reputation': 'none', 'suspicious': True, 'references': 0, 'details': {'blacklisted': False, 'malicious_activity': False, 'malicious_activity_recent': False, 'credentials_leaked': False, 'credentials_leaked_recent': False, 'data_breach': False, 'first_seen': 'never', 'last_seen': 'never', 'domain_exists': True, 'domain_reputation': 'n/a', 'new_domain': False, 'days_since_domain_creation': 9777, 'suspicious_tld': False, 'spam': False, 'free_provider': True, 'disposable': False, 'deliverable': False, 'accept_all': False, 'valid_mx': True, 'primary_mx': '', 'spoofable': True, 'spf_strict': True, 'dmarc_enforced': False, 'profiles': []}},


Production improvents: use env variable for API key, add functions so it looks cleaner

'''
#Open txt file

e = open('emails.txt', "r")

#Set API Key 

key = os.environ['API_KEY']

url = ('https://emailrep.io/')
headers = {
    "Key": "" + key,
    "Accept": "application/json",
    "User-Agent": "email-checker"
}

# Create new list to store response
scanResults = []

#Send API request for each line in email.txt
for line in e:
    c = requests.get(url + line, headers=headers)
    scanResults.append((c.json()))

#Loop through results and create a list of dicts

report = []
counter = 0
for x in scanResults:
    email = scanResults[counter]['email']
    rep = scanResults[counter]['reputation']
    spam = scanResults[counter]['details']['spam']
    mal = scanResults[counter]['details']['malicious_activity']
    #Map required list values to dictionary to generate csv
    ds = {
        'Email': email,
        "Reputation": rep,
        "Spam": spam,
        "Malicious Activity": mal,
        'Date checked': datetime.datetime.now()
    }
    report.append(ds)
    counter += 1

#Save results to CSV file

df = pd.DataFrame(report)

date = datetime.datetime.now().strftime("%Y%m%d_%H_%M")

df.to_csv('email_report_' + date + '.csv', date_format='%Y%m%d_%H_%M')
