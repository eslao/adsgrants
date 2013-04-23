import requests

r = requests.get('http://adslabs.org/adsabs/api/search/?q=DE-FG02-05CH11275&fl=bibcode&dev_key=8IIQgx5DrWZBwr2o')

#print r.json()

json_output = str(r.json())
# this converts it from a requests response object to a string, which allows it to be written to the file

newfile = open("request_output.txt","a")
newfile.write(json_output)
newfile.close()