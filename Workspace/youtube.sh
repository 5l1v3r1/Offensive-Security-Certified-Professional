#!/bin/bash


URL=""

echo "il faut mettre une URL"

read URL

youtube-dl -x "$URL"