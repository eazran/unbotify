
#!/usr/bin/env python

import random
from pprint import pprint

def main():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(numbers)
    pprint(numbers)    

if __name__ == '__main__':
    main()