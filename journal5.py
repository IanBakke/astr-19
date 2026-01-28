import numpy as np 
from tabulate import tabulate

x = np.linspace(0.0, 2*np.pi, 10000)
sin_x = np.sin(x)

table_data = [(a,b) for a, b in zip(x, sin_x)]

table_headers = ["x", "sin(x)"]
python_table = tabulate(table_data, tablefmt="grid", headers=table_headers, floatfmt=".3f")


def main():
	print(python_table)

if __name__=='__main__':
	main()