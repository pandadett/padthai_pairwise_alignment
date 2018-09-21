#!/usr/bin/env python
# vim: fdm=indent
'''
author:     Nuttada Panpradist and Fabio Zanini
date:       09/20/18
content:    Padthai_align_sequences
'''
# Modules
import os
import subprocess as sp


# Script
if __name__ == '__main__':

    alignment = align_pairwise("AAACCC","AC")
    assert alignment == ("AAACCC", "--AC--")
