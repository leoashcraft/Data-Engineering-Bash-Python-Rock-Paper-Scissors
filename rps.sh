#!/bin/bash

read -p "Are you ready to play Rock Paper Scissors!? (yes/no) " yn

case $yn in 
	yes ) echo Launching Python script...;;
	no ) echo Ending bash...;
		exit;;
	* ) echo Please enter yes or no;
		exit 1;;
esac

python3 ./rock-paper-scissors.py