# python 3.13.2

import sys
import string
import random



def getCLIArgumentValue(key):
    i = sys.argv.index(key)

    if ((i + 1) >= len(sys.argv)):
        return None
    else:
        return sys.argv[i + 1]

def getRandomCharInString(s):
    i = random.randint(0, (len(s) - 1))
    return s[i]

def containsOneOfSubstrings(s, subs):
    for substring in subs:
        if substring in s:
            return True
    return False



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
Build on python 3.13.2

Also, fun fact : when generating 8-symbols id using only lowercase letters the
probability of getting two exactly identical id's is ~4.79e-12 (or approx.
0.0000000005%).
    """)
    sys.exit()

# -help
if (args.count('-help') or args.count('-elp')):
    print("""
CLI options :
     -len [number]  Length of the id
     -mode [type]   Type of included symbols
     -info          Prints info about this program
     -help, -elp    Prints this message


The value of -mode [type] argument must be combination of flags as listed here
below. If omitted, takes default ('lLd').
    'l' = lower case letters
    'L' = upper case letters
    'd' = digits
    'h' = hexidigits
    'o' = octdigits

For example, flag 'lLh' will generate an id with both case letters and
hexidigits.

Or, value of -mode [type] argument can be 'custom=[symbols]', i.e. user-defined
combination of symbols.
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

if argValue[0:7] == 'custom=':
    s = argValue[7:]
elif containsOneOfSubstrings(argValue, string.punctuation):
    print(f"Mode '{ argValue }' is not defined.")
    sys.exit()
else:
    if 'l' in argValue:
        s = "".join([s, string.ascii_lowercase])
    if 'L' in argValue:
        s = "".join([s, string.ascii_uppercase])
    if 'd' in argValue:
        s = "".join([s, string.digits])
    if 'h' in argValue:
        s = "".join([s, string.hexdigits])
    if 'o' in argValue:
        s = "".join([s, string.octdigits])

if not len(s):
    print(f"Mode '{ argValue }' is not defined.")
    sys.exit()


a = ""

for n in range(id_length):
    a += getRandomCharInString(s)

print(a)
