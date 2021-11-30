#!/usr/bin/env python3

# Script to install fedora domain
#
# Copyright (C) 2021 Andrew Cagney
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.  See <https://www.gnu.org/licenses/gpl2.txt>.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

# Possibly useful reference:
# http://meta.libera.cc/2020/12/quick-netbsd-serial-console-install-on.html

import sys
import os

#argv[0]
domain = sys.argv[1]
gateway = sys.argv[2]
pooldir = sys.argv[3]
sourcedir = sys.argv[4]
testingdir = sys.argv[5]
command = sys.argv[6:]

print("domain", domain)
print("gateway", gateway)
print("pooldir", pooldir)
print("sourcedir", sourcedir)
print("testingdir", testingdir)
print("command", command)

# expects ARG0
os.execvp(command[0], command)