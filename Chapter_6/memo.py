# memo.py

import sys

option = sys.argv[1]

if optin == '-a':
    memo = sysargv[2]
    f = open('memo.txt.', 'a')
    f.write(memo)
    f.write('\n')
    f.close()

if option == '-v':
    f = open('memo.txt)
    memo = f.read()
    f.close()
    print(memo)
