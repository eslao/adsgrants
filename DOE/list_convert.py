import urllib

doesublist = open('doe_grant_numbers_subset.txt', 'r')
my_sublist = [line for line in doesublist]

#print my_sublist
# just for debugging

my_sublist2 = [i.replace('\n', '') for i in my_sublist]

#print my_sublist2
# just for debugging

for item in my_sublist2:
	output =  "%s" % item
	print "http://adslabs.org/adsabs/api/search/?q=\"" + str(output) + "\"&dev_key=8IIQgx5DrWZBwr2o"