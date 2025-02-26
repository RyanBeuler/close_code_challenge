from hashlib import blake2b
import requests
import json

# URL for the POST request
url = 'https://api.close.com/buildwithus/'

# Headers for the POST request
headers = {'Content-Type': 'application/json'}

# JSON returned by GET request to https://api.close.com/buildwithus/ using Postman
json_data = {"traits": ["Craftsman", "Pragmatic", "Curious", "Methodical", "Driven", "Collaborator"], "key": "Close-848a36d6", "meta": {"description": "Enclosed are some traits that [Joe](https://www.linkedin.com/in/jkemp101/) believes great engineers exhibit. Using the included UTF-8 `key`, construct a JSON array using the lowercase hex digest of the blake2b hash for each trait (digest size=64). POST this bare array back to this endpoint. Example array: [\"1f9ec19c7...57fd27e5\", \"79c72b47088...bf13026c\", ...] If the hashes are correct you will get a Verification ID you should include in your application. 400 responses indicate a problem with the hashes in your array. Note, the key rotates each day around midnight EST."}}

# Retreive the JSON data traits
traits = json_data['traits']

# Retreive the JSON data key and convert into bytes
key = json_data['key'].encode('utf-8')

# Empty list to store the hash values
hashes = []

# Iterate through the traits and hash each trait
for trait in traits:
    # Create a Blake2b hash object
    hasher = blake2b(key=key, digest_size=64)
    # Update the hash object with the trait
    hasher.update(trait.encode('utf-8'))
    # Retrieve the hex digest of the hash and append to the list
    hashes.append(hasher.hexdigest())

# Convert the list of hash values to a JSON array
json_array = json.dumps(hashes)

# Make a POST request to the URL with the JSON array
response = requests.post(url, headers=headers, data=json_array)

# Print the response status code
print("Status Code: ", response.status_code)

# Print the response content
print("Response: ", response.content)