#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/')
#  move raynor into ceph_storage
shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj? ')
# Rename the current kerrigan file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

