
def binary_sum(s,start,stop):
	if start >= stop:
		return 0
	elif start == stop-1:
		return s[start]
	else :
		mid = (start + stop)/2


		return binary_sum(s,mid,stop)+ binary_sum(s,start,mid)


s = range(1,100)
result = binary_sum(s,0,len(s))
print result