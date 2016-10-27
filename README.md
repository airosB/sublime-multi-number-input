# sublime-multi-number-input

sublime-multi-number-input is package for sublime text.
This can input incremental/decremental numbers on multi-cursors.

## Screenshots

set multi-cursors:

![before](https://raw.githubusercontent.com/airosB/sublime-multi-number-input/images/sample1.png)

apply Multi Number Input:

![done1](https://raw.githubusercontent.com/airosB/sublime-multi-number-input/images/sample2.png)

apply with options:

![done2](https://raw.githubusercontent.com/airosB/sublime-multi-number-input/images/sample3.png)

# How to use

## Installation

Use Package Control. Package name is "Multi Number Input".

Or you can install this manually.


## Usage
Set keymap on your setting.
  { "keys": ["super+ctrl+1"], "command": "multi_number_input"}

+ An input field will apper.
+ Set initial number on the field and press enter.
+ Empty input means "1".
+ Option usege: [initial number] [digits] [step]

ex) 2 5 3 -> 00002, 00005, 00008, 00011,...
ex) 0  -3 -> 0, -3, -6, -9, ...


## Copyright

Copyright (c) 2013 ryooo321 and 2013-2016 airosB.
