import os 
os.system('cls')

arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def jump_search(arr, x):

	n = len(arr)

	step = int(n ** 0.5)

	# Mencari block yang berisi elemen x (input)
	start = 0

	
	try:
		while arr[min(step, n) - 1] < x:

			
			start = step
			step += int(n ** 0.5)
			
			if start >= n:
				return -1
	except TypeError:
		pass
	

	# Melakukan linear search di block tersebut
	try:
		while arr[start] < x:
			start += 1

			if start == n:
				return -1
	except TypeError:
		if isinstance(arr[start], list):
			
			for j in range(len(arr[start])):
				if arr[start][j] == x:
					
					return start, j 

	# Cek apakah elemen yang dicari adalah elemen yang sesuai 
	if arr[start] == x:
		return start

	return -1

x = 'Wibi'
print(arr)
result = jump_search(arr, x)

if result == -1:
	print(f"Elemen {x} tidak ditemukan")
elif isinstance(result, tuple):
    print(f'{x} found at index {result[0]} columns {result[1]}')
else:
	print(f"{x} berada di array index ke - {result}")


