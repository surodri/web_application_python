#! /bin/bash -e

./bootstrap.sh
source audit_trail_env/bin/activate

nosetests /audit_trail_system/test/units --with-xunit

python setup.py bdist.egg
