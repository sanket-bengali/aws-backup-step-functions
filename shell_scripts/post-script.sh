#!/bin/bash
echo "post-script start..." > post-script-log
sudo service apache2 start
sudo service apache2 status
echo "post-script complete..." >> post-script-log
