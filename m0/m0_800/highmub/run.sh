#!/bin/bash
for a in {1..25} 
do
b=$(((a - 1)*10+960))
cp -r final mub$b/
cd mub$b/final
rm *.o
rm exe
make
./exe
cd ../..
done