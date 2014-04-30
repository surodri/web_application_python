#! /bin/bash

rm -rf audit_trail_env
virtualenv audit_trail_env
source audit_trail_env/bin/activate || exit 1

pip install -r requirements.txt

