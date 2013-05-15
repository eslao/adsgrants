import re

test_list = open('doe_grant_numbers.txt', 'r')
test_sublist = [line for line in test_list]
test_sublist2 = [i.replace('\n', '') for i in test_sublist]

remove_prefix1 = re.compile(r'DE-FG02-')
remove_prefix2 = re.compile(r'DE-')


new_sublist1 = [remove_prefix1.sub("", item) for item in test_sublist2]
new_sublist2 = [remove_prefix2.sub("", item) for item in new_sublist1]


print new_sublist2

f = open('doe_grant_numbers_unprefixed', 'w')

f.write(new_sublist2)
