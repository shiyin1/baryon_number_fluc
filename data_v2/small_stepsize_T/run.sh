#!/bin/bash
for a in {1..161} 
do
b=$((800+(a - 1)*1))
cp -r final mub$b/
cd mub$b/final
rm *.o
rm exe
make
./exe
cd ../..
done