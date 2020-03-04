#!/bin/bash
while [ -n "$1" ]
do
case "$1" in
-d) param="$2"
echo "Found the -d option, with parameter value $param"
shift ;;
--) shift
break ;;
*) echo "$1 is not an option";;
esac
shift
done

touch $param
