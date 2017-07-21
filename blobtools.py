#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage: blobtools <command> [<args>...] [--help] [--version]

commands:

    create        create a BlobDB
    view          generate tabular view/CONCOCT/COV files from BlobDB
    plot          generate a BlobPlot from a BlobDB
    covplot       generate a CovPlot from a BlobDB and a COV file

    map2cov       generate a COV file from BAM file
    seqfilter     subset sequences in FASTA file based sequence IDs in list
    taxify        generate a BlobTools compatible HITS file
    bamfilter     subset paired-end reads in a BAM file

    -h, --help      show this
    -v, --version   show version number

See 'blobtools <command> --help' for more information on a specific command.

examples:

    # Create a BlobDB
    ./blobtools create -i test.fna -b test.bam -t test.blast.out -o test

    # Generate a tabular view
    ./blobtools view -i test.blobDB.json

    # Generate a blobplot
    ./blobtools blobplot -i test.blobDB.json

"""

from __future__ import division
import sys
from subprocess import call
from os.path import join, dirname
try:
    from docopt import docopt
except ImportError:
    sys.exit("[ERROR]\t: The module docopt is not installed. \n \tPlease run : pip install docopt")


__version__ = "blobtools v1.0"
MAINDIR = join(dirname(__file__), '')
DATADIR = join(MAINDIR, 'data/')
LIBDIR = join(MAINDIR, 'lib/')

if __name__ == '__main__':
    args = docopt(__doc__,
                  version=__version__,
                  options_first=True)

    argv = [args['<command>']] + args['<args>']
    if args['<command>'] == 'create':
        exit(call(['python', LIBDIR + 'create.py'] + argv))
    elif args['<command>'] == 'view':
        exit(call(['python', LIBDIR + 'view.py'] + argv))
    elif args['<command>'] == 'blobplot' or args['<command>'] == 'plot':
        argv[0] = "blobplot"
        exit(call(['python', LIBDIR + 'blobplot.py'] + argv))
    elif args['<command>'] == 'map2cov':
        exit(call(['python', LIBDIR + 'map2cov.py'] + argv))
    elif args['<command>'] == 'covplot' or args['<command>'] == 'comparecov':
        argv[0] = "covplot"
        exit(call(['python', LIBDIR + 'covplot.py'] + argv))
    elif args['<command>'] == 'seqfilter':
        exit(call(['python', LIBDIR + 'seqfilter.py'] + argv))
    elif args['<command>'] == 'taxify':
        exit(call(['python', LIBDIR + 'taxify.py'] + argv))
    elif args['<command>'] == 'bamfilter':
        exit(call(['python', LIBDIR + 'bamfilter.py'] + argv))
    else:
        exit(call(['./blobtools', '--help']))

