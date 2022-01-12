# RandomFS - a webdav virtual filesytem demo

RandomFS serves a webdav server that hosts a single
file, `random.txt`, which - when opened - contains
a random number between 0 and 10. The number changes
each time you open it.

The site is hosted at localhost:8086, and can be
mounted as a filesystem on windows and linux. When
mounted, the filesystem looks like:

```
/
.----random.txt
```

and `cat`ing random.txt will give you a random number.

## To run

`python webdav_random_fs.py`

## Why

Used as a demo to explore davfs on windows and linux
as a virtual fileystem alternative to 9p et al.
