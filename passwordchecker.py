import requests
import hashlib
import sys

# give it a hash function of the password
# request data and give us a response
def request_api_data(query_char): 
    # request something as if we are in a browser and we get a data back

    # password API url
    # API url that we're going to use
    # requests 400 usually means that a request is not good
    # The API uses 'hashing' or running it through a hashing algorithm to generate a key
    # Send SHA1 hash keys to the API
    # This pwn API has all the password that has been leaked hashed in SHA1
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    # API uses a technique called k anonymity
    # k anonymity allows somebody to recevie an information about us yet not know who we are
    # We only give the first 5 characters of the hashed key and the API looks for
    # The first 5 characters of all SHA1 to see if it has been leaked
    
    res = requests.get(url) # get a response from API by requesting it
    # Check for API error 
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_pass_leaks_count(hashes, hash_to_check):
    # reads the requested informations from the API
    # gives all the hashes that match the beginning of the 5 character hash password
    # we have to use .splitlines method on the stirng that 
    # returns a list of the lines in the stirng and breaks the line boundaries
    # instead of splitting each individual element, we split individual hash and count
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        # check if the hash function requested form the API is equal to the 
        # tail hashed password in SHA1 that we never sent to anybody on our own machine
        if h == hash_to_check:
            return count # return how many times this password has been leaked
    
    return 0 # if not, then 0 leak

# check pwnapi
def pwned_api_check(password):
    # Check password if it exist in API response from the request_api_data()
    # utf-8 is just a format, so like b in front, need utf-8 for hashing
    # gives a sha1 hash object
    # hexdigest helps us convert the hash object to hexadecimal string
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # hash password into sha1
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_pass_leaks_count(response, tail)

# going to recevie the arguemnt we going to input in our command line
def main(args):
    for password in args:
        count = pwned_api_check(password)

        # if there were matches or counts
        if count:
            print(f"{password} was found {count} times... you should probably change your password!")

        # if there were no matches
        else:
            print(f"{password} was NOT found. Carry on!")

    return 'done!'

# only run this file if it's the main file being run
# and not if it's being imported
# Run the whole file and exit out. At the end of it all, return what the main function returns
# so 'done!'
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))