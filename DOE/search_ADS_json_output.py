import requests
import json
from pprint import pprint
import time

test_list = open('doe_grant_numbers.txt', 'r')
test_sublist = [line for line in test_list]
test_sublist2 = [i.replace('\n', '') for i in test_sublist]
# reads the contents of doe_grant_numbers_subset2.txt into a list, removes line breaks

prefix = "http://adslabs.org/adsabs/api/search/"
apikey = "8IIQgx5DrWZBwr2o"
# just sets the variables for the first part of the search string and the API key

def searchads(grantno):
	url = prefix+"?q="+grantno+"&fl=bibcode,title,author,pub,keyword,aff,property&rows=200&dev_key="+apikey
	result = requests.get(url)
	json_output = result.json()
	return json_output
	# the function to actually search ADS for set grant numbers
	# currently set to return just the bibcode
	# returning the json output here is necessary to get the correct result from searchTheList(test_sublist2)
	# check out requests param method for constructing url string

def searchTheList(test_sublist2):
	for item in test_sublist2:
		grantno =  "%s" % item
		myresult = searchads(grantno)	
		with open('doe_output.json', 'a') as outfile:
  			json.dump(myresult, outfile)
  			time.sleep(1)

  		pprint(myresult)
  		# outputs the results attractively onscreen, if that's what you're into

searchTheList(test_sublist2)

# I thought that this might  be overcoded, as we seemed to be processing the json data twice, but if I remove any lines, it breaks
# I should really clean up the variable names here. Kinda ugly.