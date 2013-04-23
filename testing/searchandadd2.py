import requests

test_list = open('doe_grant_numbers_subset2.txt', 'r')
test_sublist = [line for line in test_list]
test_sublist2 = [i.replace('\n', '') for i in test_sublist]


for item in test_sublist2:
	output =  "%s" % item
		
	print "http://adslabs.org/adsabs/api/search/?q=\"" + str(output) + "\"&fl=bibcode&dev_key=8IIQgx5DrWZBwr2o"
	
	