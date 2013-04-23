import requests

test_list = open('doe_grant_numbers_subset2.txt', 'r')
test_sublist = [line for line in test_list]
test_sublist2 = [i.replace('\n', '') for i in test_sublist]
# reads the contents of doe_grant_numbers_subset2.txt into a list, removes line breaks

prefix = "http://adslabs.org/adsabs/api/search/"
apikey = "8IIQgx5DrWZBwr2o"
# just sets the variables for the first part of the search string and the API key

def searchads(grantno):
	url = prefix+"?q="+grantno+"&fl=bibcode&dev_key="+apikey
	result = requests.get(url)
	json_output = result.json()
	return json_output
	# the function to actually search ADS for set grant numbers
	# currently set to return just the bibcode
	# this returns json data at present, but we're not doing anything with it here

for item in test_sublist2:
	grantno =  "%s" % item
	myresult = searchads(grantno)
	result_string = str(myresult)
	newfile = open("request_output3.txt","a")
	newfile.write(result_string)
	newfile.close()
	# this is a loop to supply the function searchads(grantno) using as the arguments the grant numbers in the list created above
	# currently, it writes the results as a string to a text file