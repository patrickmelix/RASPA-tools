#!/usr/bin/env python
from ase import io, Atoms, Atom
import os

def main(inFile,outFile):
    if not os.path.isfile(inFile):
        raise ValueError('File {:} does not exist'.format(str(inFile)))

    #if output exists mv to .bak
    if os.path.isfile(outFile):
        print('ATTENTION: {:} exists, moving to *.bak'.format(outFile))
        os.rename(outFile, outFile+'.bak')

    atoms = []
    with open(inFile,'r') as f:
        for line in f.readlines():
            if 'MODEL' in line:
                atoms.append(Atoms())
            elif 'CRYST1' in line:
                atoms[-1].set_cell(line.split()[1:])
            elif 'ENDMDL' in line:
                continue
            else:
                line = line.split()
                atoms[-1].append(Atom(line[2], line[4:7]))


    io.write(atoms, outFile, format='xyz')


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Convert RASPA PDB to extXYZ')
    parser.add_argument('input', type=str, help='RASPA PDB File')
    parser.add_argument('output', type=str, help='Filename for the XYZ Output')
    args = parser.parse_args()
    main(args.input,args.output)
