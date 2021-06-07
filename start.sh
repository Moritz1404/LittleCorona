#!/bin/bash
echo "Little Corona"

var=`termgraph --version`
var_new=${var% *}

if [[ "$var_new" != "termgraph" ]]
then
    echo "Installing packages"
    pip3 install termgraph
fi

if [[ "$1" = "d" ]]
then
    python3 main.py d
elif [[ "$1" = "n" ]]
then
    python3 main.py n
elif [[ "$1" = "h" ]]
then
    python3 main.py h
elif [[ "$1" = "a" ]]
then
    python3 main.py a
else
    python3 main.py
fi

echo "Aachen"
echo "7 Day Incidence"
termgraph values.dat --custom-tick "🦠" --width 20
