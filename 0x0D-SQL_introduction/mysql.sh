#!/bin/bash

if [ $# -eq 2 ]
then 
	cat "$1" | sudo mysql "$2"
else
	cat "$1" | sudo mysql
fi