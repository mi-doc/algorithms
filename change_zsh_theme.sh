#!/bin/bash

read -p "Enter zsh theme: " theme

echo $theme
sed -i "s/^\(ZSH_THEME=\"\).*/\1"$theme"\"/" text.txt
