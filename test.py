dictionary = {1:[5,7], 5:[6,3], 6:[], 3:[2], 2:[], 7:[], 8:[]}
a = [1,2,3,8,5,6,7]
arr = []


def rec(cur, value, arr):
	arr.append({cur:[]})
	for i in value:
		rec(i, dictionary[i], arr[-1].get(arr[-1].keys()[-1]))

roots = []
for id in a:
	flg = True
	for item,value in dictionary.iteritems():
		if id in value:
			flg = False
			break
	if flg:
		roots.append(id)

for root in roots:
	rec(root, dictionary[root], arr)
print 'from our hierarchy format to frontend plugin format'
print arr
#####################################

new_dict = {}

def map_to_dict(cur, new_dict):
	for k,v in cur.iteritems():
		new_dict[k] = []
		for child in v:
			new_dict[k].extend(child)
			map_to_dict(child, new_dict)

for di in arr:
	map_to_dict(di, new_dict)


print 'from frontend plugin format to our hierarchy format'
print new_dict

[	{1: [
			{5: [
					{6: []}, 
					{3: [
							{2: []}
						]
					}
				]
			}, 
			{7: []}
		]
	}
]