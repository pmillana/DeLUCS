"""
This script builds a viral dataset in pickle
format from a folder with FASTA files. The
desired label of the file must be in the file ID
after the accession number separated by a dot.

:param dataset: Name of the Dataset.
:param data_path: Path of the folder with the sequences.
:returns: None

:Example: python build_dp.py --dataset='Influenza' --data_path = '../data/Influenza'
"""

import os
from Bio import SeqIO
import pickle
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', action='store', type=str, default='None')
    parser.add_argument('--data_path', action='store', type=str, default='None')
    args = parser.parse_args()

    dataset = args.dataset
    seq_dir = args.data_path
    data = []

    for filename in os.listdir(seq_dir):
        label = filename.split('.')[0]
        filename = os.path.join(seq_dir, filename)
        print(filename)

        # Read FASTA file.
        files = SeqIO.parse(filename, "fasta")

        for file in files:

            label = file.id.split('.')[1]
            accession_number = file.id.split('.')[0]

            # Get Sequence
            seq = str(file.seq)
            seq = seq.replace('-', '').upper()

            data.append((label, seq, accession_number))

    pathTrain = os.path.join(seq_dir, 'train.p')
    pickle.dump(data, open(pathTrain, "wb"))


if __name__ == '__main__':
    main()
