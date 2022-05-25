# email-check
This is Python script that uses the emailrep.io API to check a list of emails found in a given txt file.

Emailrep.io sends a json response

Sample response

```
{'email': '00finess00@example.com', 'reputation': 'none', 'suspicious': True, 'references': 0, 'details': {'blacklisted': False, 'malicious_activity': False, 'malicious_activity_recent': False, 'credentials_leaked': False, 'credentials_leaked_recent': False, 'data_breach': False, 'first_seen': 'never', 'last_seen': 'never', 'domain_exists': True, 'domain_reputation': 'n/a', 'new_domain': False, 'days_since_domain_creation': 9777, 'suspicious_tld': False, 'spam': False, 'free_provider': True, 'disposable': False, 'deliverable': False, 'accept_all': False, 'valid_mx': True, 'primary_mx': '', 'spoofable': True, 'spf_strict': True, 'dmarc_enforced': False, 'profiles': []}},

```

The program currently reads from the email, reputation, malicious_activity, and spam fields. Note those last two fields are nested within the 'details' dict. 


# Setup

This program requires the pandas and requests python libraries, they can be installed via pip. 

```
pip install pandas requests

```


# Things to Note

This script is intended to run on a Linux machine as you can see in the file path located on the last lines.


# Usage 

python3 main.py





