# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# This was my start at an attempt to scrape data from every individual nsf grant page.

# <codecell>

from urllib2 import *

# <codecell>

award=1538

# <codecell>

type(award)

# <codecell>

award_str = str(award).zfill(7)

# <codecell>

award_str

# <codecell>

url = 'http://www.nsf.gov/awardsearch/showAward?AWD_ID=' + award_key

# <codecell>

award_str

# <codecell>

url

# <codecell>

type(awards)

# <codecell>

range(10)

# <codecell>

awards = range(10)

# <codecell>

awards

# <codecell>

awards = [str(a).zfill(7) for a in range(10)]

# <codecell>

awards

# <codecell>

urls = [('http://www.nsf.gov/awardsearch/showAward?AWD_ID=' + a) for a in awards]

# <codecell>

urls

# <codecell>

urls[1]

# <codecell>

record = urlopen(urls[5]).read()

# <codecell>

record[:5]

# <codecell>

record[-9999:]

# <codecell>


