generate_random_id.py
---

### CLI arguments (optional) and commands :
- `-len [number]` - length of the id
- `-mode [type]` - type of included symbols
- `-info` - print info about this program
- `-help` or `-elp` - print this message

The value of `-mode [type]` argument must be combination of the flags =>  
&nbsp;&nbsp;`l` for lower case letters,   
&nbsp;&nbsp;`L` for upper case letters,  
&nbsp;&nbsp;`d` for digits,  
&nbsp;&nbsp;`h` for hexidigits,  
&nbsp;&nbsp;`o` for octdigits.  
If omitted, takes default (`lLd`).

> For example, flag `lLh` will generate an id with both case letters and hexidigits.
