#!/bin/bash

rm /home/v-admin.py
rm /bin/v-admin
wget -O /home/v-admin.py https://raw.githubusercontent.com/Thomode/v-admin/main/v-admin_1.0/v-admin.py
wget -O /bin/v-admin https://raw.githubusercontent.com/Thomode/v-admin/main/v-admin_1.0/v-admin; chmod +x /bin/v-admin

rm install.sh