import re

test_list = open('doe_grant_numbers.txt', 'r')
test_sublist = [line for line in test_list]
test_sublist2 = [i.replace('\n', '') for i in test_sublist]

remove_prefix1 = re.compile(r'DE-FG02-')
remove_prefix2 = re.compile(r'DE-FC02-')
remove_prefix3 = re.compile(r'DE-AI02-')
remove_prefix4 = re.compile(r'DE-AI01-')
remove_prefix5 = re.compile(r'DE-')

new_sublist1 = [remove_prefix1.sub("", item) for item in test_sublist2]
new_sublist2 = [remove_prefix2.sub("", item) for item in new_sublist1]
new_sublist3 = [remove_prefix3.sub("", item) for item in new_sublist2]
new_sublist4 = [remove_prefix4.sub("", item) for item in new_sublist3]
new_sublist5 = [remove_prefix5.sub("", item) for item in new_sublist4]

print new_sublist5

f = open('doe_grant_nos_unprefixed', 'w')

for item in new_sublist5:
	f.write(item)
	f.write('\n')