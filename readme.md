# HeisencatFS - a webdav virtual filesytem demo

HeisencatFS serves a webdav server that hosts a single
file, `the_cat_box.txt`, which - when opened - randomly
tell you either "the cat is alive" or "the cat is dead."
The state of the cat changes each time you open it.

The site is hosted at localhost:8086, and can be
mounted as a filesystem on windows and linux. When
mounted, the filesystem looks like:

```
/
.----the_cat_box.txt
```

and `cat`ing the_cat_box.txt will give you a state.

## To run

`python heisencatFS.py`

## Why

Used as a demo to explore davfs on windows and linux
as a virtual fileystem alternative to 9p et al.
