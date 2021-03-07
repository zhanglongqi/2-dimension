def main(l1: int, l2: int, input: str, output: str, debug: bool):
	coord = [
	    'x1\tx2\n',
	]

	with open(input, 'r') as f:
		f.readline()  # skip head line
		for l in f.readlines():
			l = l.strip()
			index = int(l)
			x1 = index % l1
			x2 = int(index / l1)
			if debug: print(f'{x1}\t{x2}\t{index}')

			coord.append(f'{x1}\t{x2}\n')
	with open(output, 'w') as f:
		f.writelines(coord)


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
