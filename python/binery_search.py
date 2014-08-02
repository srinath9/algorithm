def search(s,t):
	low =0
	high = len(s)-1
	mid = (low+ high)/2

	while low<=high:
		if s[low] > t:
			return 0
		elif t ==s[mid] :
			return True
		elif t<s[mid]:
			high = mid-1
			mid = (high+low)/2
			print mid
		else :
			low = mid+1
			mid = (low+high)/2

	return False

s = range(1,100) + range(1000,9999)

print search(s,7658)