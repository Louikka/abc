generate_random_id.py
---

### CLI arguments (optional) and commands :
- `-len [number]` - length of the id (default `8`)
- `-mode [type]` - type of included symbols (default `lLd`)
- `-info` - print info about this program
- `-help` or `-elp` - print this message

The value of `-mode [type]` argument must be combination of the flags =><br />
&emsp;`l` for lower case letters,<br />
&emsp;`L` for upper case letters,<br />
&emsp;`d` for digits,<br />
&emsp;`h` for hexidigits,<br />
&emsp;`o` for octdigits.

> For example, flag `lLh` will generate an id with both case letters and hexidigits.

Also, the value of `-mode [type]` argument can be `custom=[symbols]`, i.e. user-defined combination of symbols.