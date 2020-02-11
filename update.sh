#!/bin/sh

URL='https://plex.tv/downloads/latest/5?channel=16&build=linux-x86_64&distro=debian' 
FURL=`curl -sIkL "$URL" | grep 'Location' | cut -d ' ' -f 2 | tr -d '\r\n'`
FNAME=`echo "$FURL" | rev | cut -d / -f 1 | rev`

echo $FURL
echo $FNAME

wget -O "$FNAME" "$FURL"
dpkg -i "$FNAME"
