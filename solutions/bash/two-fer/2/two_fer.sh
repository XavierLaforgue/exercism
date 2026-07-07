#!/usr/bin/env bash

main () {
# if [ "$1" = "" ] 
if [ -z "$1" ] # test for empty string
then
	echo "One for you, one for me."
else # test for not empty string: else if [ -n "$1" ]
	echo "One for $1, one for me."
fi
}

# call main with all of the positional arguments
main "$@"
