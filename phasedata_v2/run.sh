#!/bin/bash
for a in {1..89} 
do
b=$(((a - 1)*10))
cd mub$b/final
rm *.o
rm exe
make
./exe
cd ../..
done