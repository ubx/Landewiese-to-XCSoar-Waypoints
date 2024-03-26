import glob
import os
import sys
import zipfile

import combine_cup as comb
import convert_cupx as cnv

DATA_DIR = 'data'
OUTPUT_DIR = 'output'


def unzip():
    all_filenames = [i for i in glob.glob('*.zip', root_dir=os.path.join(DATA_DIR, ''))]
    print('Input zip file(s):\n', all_filenames)
    for fn in all_filenames:
        with zipfile.ZipFile(os.path.join(DATA_DIR, fn), 'r') as zip_ref:
            zip_ref.extractall(os.path.join(DATA_DIR, ''))


def convert():
    all_filenames = [i for i in glob.glob('*.cupx', root_dir=os.path.join(DATA_DIR, ''))]
    print('Input cpux file(s):\n', all_filenames)
    for fn in all_filenames:
        cnv.cpux2xcsoar(os.path.join(DATA_DIR, fn))


def concat_wp_details(file_name):
    all_filenames = [i for i in glob.glob('*.txt', root_dir=os.path.join(OUTPUT_DIR, ''))]
    print('Input txt file(s):\n', all_filenames)
    with open(os.path.join(OUTPUT_DIR, file_name), 'w') as outfile:
        for filename in all_filenames:
            with open(os.path.join(OUTPUT_DIR, filename)) as infile:
                contents = infile.read()
                outfile.write(contents)


if __name__ == '__main__':
    unzip()
    convert()
    name = sys.argv[1] if len(sys.argv) > 1 else 'landewiesen'
    comb.combine('{}.cup'.format(name))
    concat_wp_details('{}_details.txt'.format(name))
    print('Waypoint details file: {}_details.txt\n'.format(name))

