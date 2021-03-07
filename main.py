def main(l1: int, l2: int, input: str, output: str, debug: bool):
	index = [
	    'index\n',
	]

	with open(input, 'r') as f:
		f.readline()  # skip head line
		for l in f.readlines():
			l = l.strip()
			x1, x2 = l.split('\t')
			i = l1 * int(x2) + int(x1)
			if debug: print(f'{x1}\t{x2}\t{i}')

			index.append(f'{i}\n')
	with open(output, 'w') as f:
		f.writelines(index)


if __name__ == '__main__':

	import argparse

	parser = argparse.ArgumentParser(description='right sum operation')

	parser.add_argument('--l1', type=int, required=True)
	parser.add_argument('--l2', type=int, required=True)
	parser.add_argument('--input', type=str, required=True)
	parser.add_argument('--output', type=str, required=True)

	parser.add_argument('-D', '--debug', action='store_true', help='show more debug info')

	args = parser.parse_args()
	main(args.l1, args.l2, args.input, args.output, args.debug)
