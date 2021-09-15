import requests
from bs4 import BeautifulSoup # creates a BeautifulSoup object that allows us to parse through html
import pprint # prints pretty strings

# requests the url/website Do a get request to grab that url
res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')


# tells BeautifulSoup parses to parse the html so converting from string to object
# creates a soup object and makes it into a readable html
# I can grab the <body> element from the html by doing soup.body
soup = BeautifulSoup(res.text, 'html.parser') 
soup2 = BeautifulSoup(res2.text, 'html.parser') # make a second soup object with different link
links = soup.select('.storylink') # grab all the links
links2 = soup2.select('.storylink') # second page link 
subtext = soup.select('.subtext') # grab all the elements with the score class
subtext2 = soup2.select('.subtext') # grab second page subtext 

# group the two links and subtext together
mega_links = links + links2
mega_subtext = subtext + subtext2

# sort stories by the amonut of votes
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True) # sort by votes in reverse

# function hacker news that receive links and votes
def create_custom_hm(links, subtext):
    hn = []
    # enumerate through all the links passed in so we can filter the desired ones
    # and so we can save it into hn from the list 
    for idx, item in enumerate(links):
        # get the title from all the links
        title = item.getText() # get the text inside of the tag so the titles in the link
        # the default will be None if the link does not work 
        href = item.get('href', None) # grab the href attribute from each of the links
        vote = subtext[idx].select('.score') # select the class with scores under subtext class
        if len(vote): # if it's not 0, then do the following
            # gets the vote from all the subtext of arrays so the first array [0]
            points = int(vote[0].getText().replace(' points', '')) # return only the casted point
            if points > 99:
                hn.append({'title': title, 'href': href, 'votes': points})
                # append a dictionary when you need to append more than one variable
                # append a dictionary of title and href property into the hn list
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hm(mega_links, mega_subtext))
