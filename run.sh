#!/bin/bash
docker run --rm -v $PWD/images:/images  -v $PWD/icons:/icons leffen/vueicongen:0.3  -i $1 -o $2