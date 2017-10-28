from sys import argv as sys_argv

if __name__ == "__main__":
	with open('sample.txt', 'w+') as t:
		for s in sys_argv[1:]:
			t.write(s)