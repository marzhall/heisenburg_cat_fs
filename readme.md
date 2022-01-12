# RANDOMFS - a webdav virtual filesytem demonatration

Random FS serves a webdav server that hosts a single
file, `random.txt`, which - when opened - returns
a file with a random number between 0 and 10.

The site is hosted at localhost:8086, and can be
mounted as a filesystem on windows and linux. The
filesystem then looks like:

```
/
.----random.txt
```

and `cat`ing random.txt will give you a random number.

## Why

Used as a demo to explore davfs on windows and linux
as a virtual fileystem alternative to 9p et al.