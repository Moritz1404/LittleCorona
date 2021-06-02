#!/bin/bash
echo "Little Corona"

if [[ "$1" = "d" ]]
then
    python3 main.py d
elif [[ "$1" = "n" ]]
then
    python3 main.py n
elif [[ "$1" = "h" ]]
then
    python3 main.py h
else
    python3 main.py
fi