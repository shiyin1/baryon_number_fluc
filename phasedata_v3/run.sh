#!/bin/bash
for a in {1..31} 
do
b=$((900+(a - 1)*10))
cp -r final mub$b/
cd mub$b/final
rm *.o
rm exe
make
./exe
cd ../..
done