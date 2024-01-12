#!/bin/bash

read -p "Commit message: " Commit

git add .
git commit -m "${Commit}"
git push
