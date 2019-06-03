#!/bin/bash
echo "pre-script start..." > pre-script-log
sudo service apache2 stop
echo "pre-script complete..." >> pre-script-log
