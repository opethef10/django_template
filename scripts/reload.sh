#! /usr/bin/env bash
touch /var/www/__PROJECT___pythonanywhere_com_wsgi.py
for i in {1..3}; do
  echo -n "."
  sleep 1
done
echo "Server is reloaded"
