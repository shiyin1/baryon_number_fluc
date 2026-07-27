#!/bin/bash
for a in {1..33} 
do
b=$(((a - 1)*5+800))
cp -r final mub$b/
cd mub$b/final
rm *.o
rm exe
make
./exe
cd ../..
done