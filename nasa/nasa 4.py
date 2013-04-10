# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import csv
import requests
import json
from pprint import pprint
import time
requests.__version__

# <codecell>

prefix = 'http://labs.adsabs.harvard.edu/adsabs/api/search/?q='
suffix1 = '&fl=bibcode&dev_key='
suffix2 = '&hl=full&hl=abstract&rows=5&dev_key='
apikey = '8IIQgx5DrWZBwr2o'

# <codecell>

with open('/Users/christine/adsgrants/nasa/NASA_grants_test.csv', 'rU') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    f2 = open('/Users/christine/adsgrants/nasa/NASA_grants_output.csv', 'wb')
    grantswriter = csv.writer(f2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        grant = row[1]
        result = requests.get(prefix + grant + suffix1 + apikey).json()
        if str(result).find("bibcode") == -1:
            biblist = "no hits"
        else:
            bibcodes = result['results']['docs']
            biblist = [item['bibcode'] for item in bibcodes]
        row.append(biblist)
        grantswriter.writerow(row)
        print row
        time.sleep(1)

