# python 3.13.2

import sys
import string
import random
import re



def getCLIArgumentValue(key):
    return args[args.index(f"-{key}") + 1]

def getRandomPositionValue(iterable):
    i = random.randint(0, (len(iterable) - 1))
    return iterable[i]



args = sys.argv
# CLI arguments :
#   -len [number] = length of the id
#   -mode [type] = type of included symbols
#   -info = print info about this program
#   -help / -elp = print this message

# The value of -mode [type] argument must be combination of flags as listed here
# below. If omitted, takes default ('lLd').
#   'l' = lower case letters
#   'L' = upper case letters
#   'd' = digits
#   'h' = hexidigits
#   'o' = octdigits
# for example :
#   flag 'lLh' will generate an id with both case letters and hexidigits.

if (not (len(args) - 1)):
    args_len = input("Length of id : ") or "0"
    args_mode = input("Mode type : ") or "lLd"

    args.extend([
        '-len', args_len,
        '-mode', args_mode,
    ])


# -info
if (args.count("-info")):
    print("""
# Build on python 3.13.2
    """)
    sys.exit()

# -help
if (args.count("-help") or args.count("-elp")):
    print("""
# CLI arguments :
#   -len [number] = length of the id
#   -mode [type] = type of included symbols
#   -info = print info about this program
#   -help / -elp = print this message

# The value of -mode [type] argument must be combination of flags as listed here
# below. If omitted, takes default ('lLd').
#   'l' = lower case letters
#   'L' = upper case letters
#   'd' = digits
#   'h' = hexidigits
#   'o' = octdigits
# for example :
#   flag 'lLh' will generate an id with both case letters and hexidigits.
    """)
    sys.exit()
    

# length
try:
    id_length = int( getCLIArgumentValue('len') )
except:
    print(f"'{ getCLIArgumentValue('len') }' is not a number.")
    sys.exit()

# mode
s = ""

if (re.search(r'l', getCLIArgumentValue('mode'))):
    s = "".join([s, string.ascii_lowercase])
if (re.search(r'L', getCLIArgumentValue('mode'))):
    s = "".join([s, string.ascii_uppercase])
if (re.search(r'd', getCLIArgumentValue('mode'))):
    s = "".join([s, string.digits])
if (re.search(r'h', getCLIArgumentValue('mode'))):
    s = "".join([s, string.hexdigits])
if (re.search(r'o', getCLIArgumentValue('mode'))):
    s = "".join([s, string.octdigits])

if (not len(s)):
    print(f"Mode '{ getCLIArgumentValue('mode') }' is not defined.")
    sys.exit()


a = ""

for n in range(id_length):
    a += getRandomPositionValue(s)
    
print(a)
