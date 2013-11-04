# sublime-multi-number-input

sublime-multi-number-input is plugin for sublime text.
This plugin provides a feature to input incremental/decremental numbers for multi cursor.

# How to use

## Installation

To install manually in a shell/Terminal (on OS X, Linux or Cygwin), via git:

    cd ~/"/Sublime Text 3/Data/Packages/User/" # location on Windows; will be different on Linux & MacOS
    git clone https://github.com/aurosB/sublime-multi-number-input.git

or, if you don't have git installed:

    cd ~/"/Sublime Text 3/Data/Packages/User/"
    rm -rf airosB-sublime-multi-number-input*  # remove any old versions
    curl -L https://github.com/airosB/sublime-multi-number-input/tarball/master | tar xf -

The plugin should be picked up automatically. If not, restart Sublime Text 3.

## Usage
    Set keymap on your setting.
      { "keys": ["super+ctrl+1"], "command": "multi_number_input"}

    Input initial number on input field and press Enter. Empty input will be taken as "1".
    You can use whitespaces for separate args: ''Initial Digits Step''

    ex) 2 5 3 -> 00002, 00005, 00008, 00011,...
    ex) 0  -3 -> 0, -3, -6, -9, ...


## Contributing to rack-override-user-agent

* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet.
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it.
* Fork the project.
* Start a feature/bugfix branch.
* Commit and push until you are happy with your contribution.
* Make sure to add tests for it. This is important so I don't break it in a future version unintentionally.
* Please try not to mess with the Rakefile, version, or history. If you want to have your own version, or is otherwise necessary, that is fine, but please isolate to its own commit so I can cherry-pick around it.

## Copyright

Copyright (c) 2013 ryooo321. See LICENSE.txt for further details.
