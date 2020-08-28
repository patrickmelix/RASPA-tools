#!/bin/bash
set -e
for f in "$@"
do
   echo "$f"
   sed -n -e '/Number of molecules:/,/Average Widom/ p' "$f" | sed -e '$d'
done

exit 0
