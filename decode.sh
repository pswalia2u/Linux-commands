#!/bin/bash
state=$(<base64.txt)
for i in {1..13}; do
   state=$(<<<"$state" base64 --decode)
done
echo "$state"