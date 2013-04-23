import requests

prefix = "http://adslabs.org/adsabs/api/search/"
apikey = "8IIQgx5DrWZBwr2o"

def searchads(grantno):
	url = prefix+"?q="+grantno+"&fl=bibcode&dev_key="+apikey
	result = requests.get(url)
	json_output = result.json()
	return json_output

grantno = "DE-FG02-05CH11275"
myresult = searchads(grantno)

#print myresult

result_string = str(myresult)

newfile = open("request_output2.txt","a")
newfile.write(result_string)
newfile.close()

#print r.json()

#json_output = str(r.json())
# this converts it from a requests response object to a string, which allows it to be written to the file