# Examples for broken "Rename Symbol"

This file contains two examples of broken "Rename Symbol" functionality in our codebases.
It can either be reproduced with VSHaxe extension / Rename Symbol, or by using:

```shell
# ./byte_offset.py src/LocalVar.hx TESTRENAME
221

# node rename.js -s src -l src/LocalVar.hx@221 -n FOOBAR
# node rename_nothrow.js -s src -l src/LocalVar.hx@221 -n FOOBAR
```
* rename.js -> build directly from [haxe-rename](https://github.com/HaxeCheckstyle/haxe-rename)
* rename_nothrow.js -> same, but all `throw` statements replaced with `trace`
* byte_offset.py -> Quickly get the byte offset of a string in a file.

Usage: `python byte_offset.py <file_path> <name>`