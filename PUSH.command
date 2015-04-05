#!/bin/bash

# To use this script just open up the terminal and go to wherever this file
# is located (the root directory by default) with CD. Then type ./PUSH.command
# and it will commit all your changes to the GitHub repository at:
# https://github.com/liam4/evolution-script-docs/tree/master

git add *
git commit -m 'Automatic commit by PUSH.command'
git push git@github.com:liam4/evolution-script-docs.git master
git push git@github.com:liam4/evolution-script-docs.git gh-pages