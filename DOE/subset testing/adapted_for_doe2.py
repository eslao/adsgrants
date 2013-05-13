# Adapted from Christine Eslao's script
# by Brendan Short
# to handle DOE data

import csv
import requests
import json
from pprint import pprint
import time
requests.__version__



prefix1 = 'http://labs.adsabs.harvard.edu/adsabs/api/search/?q='
prefix2 = 'http://labs.adsabs.harvard.edu/adsabs/api/record/'
suffix1 = '&fl=bibcode&dev_key='
suffix2 = '&hl=full&hl=abstract&rows=5&dev_key='
suffix3 = '?fl=author,pub,aff,property,keyword,title&rows=200&dev_key='
apikey = '8IIQgx5DrWZBwr2o'


#with open('/Users/christine/adsgrants/nasa/NASA_grants_test.csv', 'rU') as f:
with open('DOE_results_subset.csv', 'rU') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    f2 = open('DOE_test_output.csv', 'wb')
    grantswriter = csv.writer(f2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        grant = row[3]
        grantpi = ' '.join(row[4].split()[1:])
        result = requests.get(prefix1 + grant + suffix1 + apikey).json()
        if str(result).find("'bibcode':") == -1:
            biblist = "no hits"
        else:
            bibcodes = result['results']['docs']
            biblist = [item['bibcode'] for item in bibcodes]
            for bib in biblist:
                biburl = prefix2 + bib + suffix3 + apikey
                bibresult = requests.get(biburl).json()
                newrow = list(row)
                newrow.append(bib)
                newrow.append(biburl)
                newrow.append(bibresult['title'].encode('ascii', 'xmlcharrefreplace'))
                #newrow.append(bibresult['pub'].encode('ascii', 'xmlcharrefreplace'))
                if str(bibresult).find("'pub':") == -1:
                    newrow.append('unknown')
                else:
                    newrow.append(bibresult['pub'].encode('ascii', 'xmlcharrefreplace'))
                bibauthors = '; '.join(bibresult['author']).encode('ascii', 'xmlcharrefreplace')
                newrow.append(bibauthors)
                if str(bibauthors.lower()).find(grantpi.lower()) == -1:
                    bibpi = 'PI not found'
                else:
                    bibpi = 'PI in authors'
                newrow.append(bibpi)
                bibproperty = '; '.join(bibresult['property'])
                newrow.append(bibproperty.encode('ascii', 'xmlcharrefreplace'))
                if str(bibresult).find("'keyword':") == -1:
                    bibkw = 'no keywords'
                else:
                    bibkw = '; '.join(bibresult['keyword'])
                newrow.append(bibkw)
                print newrow
                grantswriter.writerow(newrow)
                time.sleep(1)

