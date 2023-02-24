def minimum(arr):
	aux = arr[0]
	for i in arr:
		if(aux > i):
			aux = i
	return aux
