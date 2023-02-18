import sys

if len(sys.argv) == 3:
	text = sys.argv[1]
	times = int(sys.argv[2])

	for i in range(times):
		print(text)