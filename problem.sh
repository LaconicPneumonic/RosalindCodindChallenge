#!/usr/bin/env bash

BASEDIR=$(dirname "$0")/$1

mkdir $BASEDIR/
touch $BASEDIR/$1.py
code $BASEDIR/$1.py
cd $BASEDIR/