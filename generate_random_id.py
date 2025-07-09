##
# Build on Python 3.13.2
##

import sys
import string
import random


def getCLIArgumentValue(key):
    return args[args.index(f"-{key}") + 1]

def getRandomPositionValue(iterable):
    i = random.randint(0, (len(iterable) - 1))
    return iterable[i]



args = sys.argv
# cli arguments :
#   -len [number] = length of the id
#   -mode [type] = type of included symbols (see below)
#   -help / -elp = print this comment

# possible values of -mode [type] argument :
#     'abc' = only letters (both cases)
#     'abc123' = letters and digits
#     'abc123+' = letters, digits and '_' symbol
# if omitted, takes default ('abc')

if (not (len(args) - 1)):
    args_len = input("Length of id : ") or "0"
    args_mode = input("Mode type : ") or "abc"

    args.extend([
        '-len', args_len,
        '-mode', args_mode,
    ])


if (args.count("-help") or args.count("-elp")):
    print("""
# cli arguments :
#   -len [number] = length of the id
#   -mode [type] = type of included symbols (see below)
#   -help / -elp = print this comment

# possible values of -mode [type] argument :
#     'abc' = only letters (both cases)
#     'abc123' = letters and digits
#     'abc123+' = letters, digits and '_' symbol
# if omitted, takes default ('abc')
    """)
    sys.exit()
    

try:
    l = int( getCLIArgumentValue('len') )
except:
    print(f"'{getCLIArgumentValue('len')}' is not a number.")
    sys.exit()

match (getCLIArgumentValue('mode')):
    case 'abc':
        s = string.ascii_letters
    case 'abc123':
        s = "".join([string.ascii_letters, string.digits])
    case 'abc123+':
        s = "".join([string.ascii_letters, string.digits, '_'])
    case _:
        print(f"Mode '{getCLIArgumentValue('mode')}' is not defined.")
        sys.exit()

a = ""

for n in range(l):
    a += getRandomPositionValue(s)
    
print(a)
