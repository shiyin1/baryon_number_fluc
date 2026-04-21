#!/bin/bash
for a in {1..18} 
do
b=$((875+(a - 1)*5))
cp -r final mub$b/
cd mub$b/final
rm *.o
rm exe
make
./exe
cd ../..
done