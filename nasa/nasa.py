# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import csv
import requests
import json
import time
import codecs
requests.__version__

# <codecell>

prefix1 = 'http://labs.adsabs.harvard.edu/adsabs/api/search/?q='
prefix2 = 'http://labs.adsabs.harvard.edu/adsabs/api/record/'
suffix1 = '&fl=bibcode,property&rows=200&dev_key='
suffix2 = '&hl=full&hl=abstract&rows=200&dev_key='
apikey = ''
#columns = ['PR Number', 'Grant Number', 'Pgrp / Center', 'Proposal Title', 'PI Name', 'Technical Officer', 'Institution', 'Award Date', 'Performance Start Date', 'Performance End Date', 'Status', 'Congressional Directed Item', 'ADS status', 'Bibcode', 'Title', 'Author', 'Author affiliation', 'Keyword', 'Identifier', 'Citation count', 'Publication', 'Volume', 'Issue', 'Page', 'Abstract']

# <codecell>

def getadslist (adsfield, csvfield):
    if str(hit).find("'" + adsfield + "':") == -1:
        newrow.append('no ' + csvfield + ' data')
    else:
        newrow.append('; '.join(hit[adsfield]))

# <codecell>

def getadsstr (adsfield, csvfield):
    if str(hit).find("'" + adsfield + "':") == -1:
        newrow.append('no ' + csvfield + ' data')
    else:
        newrow.append(hit[adsfield])

# <codecell>

def getadsdict (adsfield, csvfield):
    if str(hit).find("'" + adsfield + "':") == -1:
        newrow.append('no ' + csvfield + ' data')
    else:
        newrow.append(str(hit[adsfield]))

# <codecell>

def getadsint (adsfield, csvfield):
    if str(hit).find("'" + adsfield + "':") == -1:
        newrow.append('no ' + csvfield + ' data')
    else:
        newrow.append(str(hit[adsfield]))

# <codecell>

#with open('/Users/christine/adsgrants/nasa/NASA_Awards.csv', 'rU') as f:
#with codecs.open('/Users/christine/adsgrants/nasa/NASA_Awards_1018379.csv', mode='rU', encoding='ascii', errors='ignore') as f:
with codecs.open('/Users/christine/adsgrants/nasa/NASA_Awards.csv', mode='rU', encoding='ascii', errors='ignore') as f:
#with codecs.open('/Users/christine/adsgrants/nasa/NASA_Awards-2007-2012_all-fields_test.csv', mode='rU', encoding='ascii', errors='ignore') as f:
#with open('/Users/christine/adsgrants/nasa/NASA_grants_test.csv', 'rU') as f:
#with open('/Users/christine/adsgrants/nasa/NASA_grants_2006-2012.csv', 'rU') as f:
#with open('/Users/christine/adsgrants/nasa/NASA_grants_2006-2012_NNX13AB84G.csv', 'rU') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    #f2 = open('/Users/christine/adsgrants/nasa/NASA_grants_output_highlights_NNX13AB84G.csv', 'wb')
    #f2 = open('/Users/christine/adsgrants/nasa/NASA_grants_output_highlights.csv', 'wb')
    #f2 = open('/Users/christine/adsgrants/nasa/NASA_grants_output_test.csv', 'wb')
    #f2 = open('/Users/christine/adsgrants/nasa/NASA_grants_output_single_query_test.csv', 'wb')
    f2 = open('/Users/christine/adsgrants/nasa/NASA_grants_output_single_query.csv', 'wb')
    grantswriter = csv.writer(f2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #grantswriter.writerow(columns)
    for row in reader:
        grant = row[18]
        print grant
        #grantpi = ' '.join(row[4].split()[1:])
        result = requests.get(prefix1 + grant + suffix2 + apikey).json()
        time.sleep(1)
        if str(result).find("'bibcode':") == -1:
            newrow = list(row)
            #print newrow
            newrow.append('grant not found in ADS')
            newrow.append(prefix1 + grant + suffix2 + apikey)
            #print newrow
            #print '========='
            grantswriter.writerow(newrow)
        else:
            result_data = [hit for hit in result['results']['docs']]
            #print result_data
            #'; '.join(item['keyword']),
            #result_lists = [item in result['results']['docs']]
            #[[item['bibcode'], item['title'], '; '.join(item['pub']), '; '.join(item['property']), '; '.join(item['author']), '; '.join(item['aff']),  '; '.join(item['keyword']),  '; '.join(item['highlights']),] for item in result['results']['docs']]
            #result_lists = [[item['bibcode'] for item in result_data], ['; '.join(item['property']).encode('ascii', 'xmlcharrefreplace') for item in result_data]]
            #print result_lists
            #properties = [item['property'] for item in result_data]
            #print properties
            #newrow.extend(biblist)
            #print newrow
            for hit in result_data:
                newrow = list(row)
                newrow.append(prefix1 + grant + suffix2 + apikey)
                hitdata = ['grant found in ADS', hit['bibcode']]
                newrow.extend(hitdata)
                getadsstr('title', 'title')
                getadslist('author', 'author') 
                getadslist('aff', 'author affiliation')
                getadslist ('keyword', 'keyword')
                getadslist ('identifier', 'identifier')
                getadsint('citation_count', 'citation count')
                getadsstr('pub', 'publication')
                getadsstr('volume', 'volume')
                getadsstr('issue', 'issue')
                getadslist('page', 'page') 
                getadsstr('abstract', 'abstract')
                getadsdict('highlights', 'highlights')
                asciinewrow = [item.encode('ascii', 'xmlcharrefreplace') for item in newrow]
                #print newrow
                #print asciinewrow
                grantswriter.writerow(asciinewrow)
            #print '========='

# <codecell>


