#!/usr/bin/env python

"""
make.py

A drop-in or mostly drop-in replacement for GNU make.
"""

import os
from optparse import OptionParser
from pymake.data import Makefile
from pymake.parser import parsestream, parsecommandlineargs

op = OptionParser()
op.add_option('-f', '--file', '--makefile',
              action='append',
              dest='makefiles',
              default=[])

options, arguments = op.parse_args()

m = Makefile()
targets = parsecommandlineargs(m, arguments)

if len(options.makefiles) == 0:
    if os.path.exists('Makefile'):
        options.makefiles.append('Makefile')
    else:
        raise Error("No makefile found")

for f in options.makefiles:
    parsestream(open(f), f, m)
