#!/bin/sh

for instancia in InstanciasSAT/*
do
    instancianombre=$(echo $instancia | sed 's/InstanciasSAT//g')
    python Reductor/main.py $instancia $1 > X-SAT/$instancianombre
done

