#!/usr/bin/env python
import sys, os
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['errorbar.capsize'] = 6
matplotlib.rcParams['axes.grid'] = True
matplotlib.rcParams['font.size'] = 18
matplotlib.rcParams['figure.figsize'] = (9.75, 5.85) #(10, 6)
matplotlib.rcParams['savefig.dpi'] = 600


def main(inFile,outFile):
    if not os.path.isfile(inFile):
        raise ValueError('File {:} does not exist'.format(str(inFile)))

    #if output exists mv to .bak
    if os.path.isfile(outFile):
        print('ATTENTION: {:} exists, moving to *.bak'.format(outFile))
        os.rename(outFile, outFile+'.bak')

    x, y = np.loadtxt(inFile, skiprows=4, usecols=(0,2), unpack=True)
    plt.xlabel("Pore Diameter [Å]")
    plt.ylabel("Pore-Size Distribution")
    plt.xlim([min(x),max(x)])
    plt.plot(x,y)
    plt.tight_layout()
    plt.savefig(outFile)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Plot RASPA Pore-Size Distribution')
    parser.add_argument('input', type=str, help='RASPA PSD Output File')
    parser.add_argument('output', type=str, help='Filename for the PNG Output')
    args = parser.parse_args()
    main(args.input,args.output)
