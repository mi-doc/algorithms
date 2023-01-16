#!/bin/bash

# read -p "Enter your name: " name
# if [[ $name = $USER ]]
# then
#     echo 'YES'
# else 
#     echo 'NO'
# fi

if ! grep rama -q requirements.txt
then
    echo 'No text'
else 
    grep '^ZSH' text.txt
    var1=$(grep -n ZSH_THEME ~/.zshrc | grep -v '#' | awk -F : '{printf $1}')
    echo $var1
fi