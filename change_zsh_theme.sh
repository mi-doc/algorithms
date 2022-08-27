#!/bin/bash

read -p "Enter zsh theme: " theme

grep '^ZSH_THEME=' ~/.zshrc
sed -i "s/^\(ZSH_THEME=\"\).*/\1$theme\"/" ~/.zshrc
grep '^ZSH_THEME=' ~/.zshrc

zsh
source ~/.zshrc