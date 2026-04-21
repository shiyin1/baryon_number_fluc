#!/bin/bash
for a in {1..19} 
do
b=$((870+(a - 1)*5))
cp -r final mub$b/
cd mub$b/final
rm *.o
rm exe
make
./exe
cd ../..
done