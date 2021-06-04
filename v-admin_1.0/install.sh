#!/bin/bash
cd /home
rm v-admin.py

cd /bin
rm v-admin

cd
wget -O /home/v-admin.py https://raw.githubusercontent.com/Thomode/v-admin/main/v-admin_1.0/v-admin.py
wget -O /bin/v-admin https://raw.githubusercontent.com/Thomode/v-admin/main/v-admin_1.0/v-admin; chmod +x /bin/v-admin

rm install.sh