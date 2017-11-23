def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break

	return result


def mergesort(a):
	if len(a) < 2:
		return a

	middle = len(a) // 2
	left = mergesort(a[:middle])
	right = mergesort(a[middle:])

	return merge(left, right)

# Driver code to test above
arr = [12, 6, 11, 5, 13, 7]
print ("Given array is")
print(arr)
 
arr = mergesort(arr)
print ("\nSorted array is")
print (arr)