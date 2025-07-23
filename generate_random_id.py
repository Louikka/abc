# python 3.13.2

import sys
import string
import random
import re



def getCLIArgumentValue(key):
    i = sys.argv.index(key)

    if ((i + 1) >= len(sys.argv)):
        return None
    else:
        return sys.argv[i + 1]

def getRandomCharInString(s):
    i = random.randint(0, (len(s) - 1))
    return s[i]



args = sys.argv
defLen = "8"
defMode = "lLd"

if not (len(args) - 1):
    args_len = input("Length of id : ") or defLen
    args_mode = input("Mode type : ") or defMode

    args.extend([
        '-len', args_len,
        '-mode', args_mode,
    ])

if not args.count('-len'):
    args.extend([ '-len', defLen ])
if not args.count('-mode'):
    args.extend([ '-mode', defMode ])


# -info
if args.count('-info'):
    print("""
# Build on python 3.13.2

# Also, fun fact : when generating 8-symbols id using only lowercase letters
# the probability of getting two exactly identical id's is ~4.79e-12 (or
# approx. 0.0000000005%).
    """)
    sys.exit()

# -help
if (args.count('-help') or args.count('-elp')):
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
    id_length = int( getCLIArgumentValue('-len') )
except Exception as err:
    print( str(err) )
    sys.exit()

# mode
s = ""
argValue = getCLIArgumentValue('-mode')

if re.search(r'l', argValue):
    s = "".join([s, string.ascii_lowercase])
if re.search(r'L', argValue):
    s = "".join([s, string.ascii_uppercase])
if re.search(r'd', argValue):
    s = "".join([s, string.digits])
if re.search(r'h', argValue):
    s = "".join([s, string.hexdigits])
if re.search(r'o', argValue):
    s = "".join([s, string.octdigits])

if not len(s):
    print(f"Mode '{ argValue }' is not defined.")
    sys.exit()


a = ""

for n in range(id_length):
    a += getRandomCharInString(s)

print(a)
