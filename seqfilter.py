#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""usage: blobtools seqfilter       -i FASTA -l LIST [-o PREFIX] [-v]
                                    [-h|--help]

    Options:
        -h --help                   show this

        -i, --infile <FASTA>        FASTA file of sequences (Headers are split at whitespaces)
        -l, --list <LIST>           TXT file containing headers of sequences to keep
        -o, --out <PREFIX>          Output prefix
        -v, --invert                Invert filtering (Sequences w/ headers NOT in list)
"""

from __future__ import division
from docopt import docopt
import lib.BtCore as bt
import lib.BtLog as BtLog
import lib.BtIO as BtIO
import lib.BtPlot as BtPlot
from os.path import dirname, isfile, basename, splitext


if __name__ == '__main__':
    main_dir = dirname(__file__)
    #print data_dir
    args = docopt(__doc__)
    fasta_f = args['--infile']
    list_f = args['--list']
    invert = args['--invert']
    out_prefix = args['--outprefix']

    # Was output prefix supplied?
    if out_prefix:
        out_f = "%s.fna" % (out_prefix)
    else:
        out_f = "%s.filtered.fna" % (splitext(fasta_f)[0])
    # Check input files
    if not isfile(fasta_f):
        BtLog.error('0', fasta_f)
    if not isfile(list_f):
        BtLog.error('0', list_f)

    items = BtIO.parseSet(list_f)
    output = []
    for header, sequence in BtIO.readFasta(fasta_f):
        if header in items:
            if not (invert):
                output.append(">%s\n%s" % (header, sequence))
        else:
            if (invert):
                output.append(">%s\n%s" % (header, sequence))
    with open(out_f, "w") as fh:
        fh.write("".join(output))


