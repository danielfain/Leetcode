def mario(height):
	for i in range(1, height + 1):
		print(" " * (height - i) + "#" * i + " " + "#" * i + " " * (height - i))





height = 10
print(mario(height))