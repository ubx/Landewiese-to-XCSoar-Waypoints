import glob
import os
import sys
import zipfile

import combine_cup as comb
import convert_cupx as cnv

DATA = 'data'
OUTPUT = 'output'


def unzip():
    all_filenames = [i for i in glob.glob('*.{}'.format('zip'), root_dir=os.path.join(DATA, ''))]
    print('Input zip file(s):')
    print(all_filenames)
    for fn in all_filenames:
        with zipfile.ZipFile(os.path.join(DATA, fn), 'r') as zip_ref:
            zip_ref.extractall(os.path.join(DATA, ''))


def convert():
    all_filenames = [i for i in glob.glob('*.{}'.format('cupx'), root_dir=os.path.join(DATA, ''))]
    print('Input cpux file(s):')
    print(all_filenames)
    for fn in all_filenames:
        cnv.cpux2xcsoar(os.path.join(DATA, fn))


def concat_wp_details(file_name):
    all_filenames = [i for i in glob.glob('*.{}'.format('txt'), root_dir=os.path.join(OUTPUT, ''))]
    print('Input txt file(s):')
    print(all_filenames)
    with open(os.path.join(OUTPUT, file_name), 'w') as outfile:
        for filename in all_filenames:
            with open(os.path.join(OUTPUT, filename)) as infile:
                contents = infile.read()
                outfile.write(contents)


if __name__ == '__main__':
    unzip()
    convert()
    name = sys.argv[1] if len(sys.argv) > 1 else 'landewisen'
    comb.combine('{}.cup'.format(name))
    concat_wp_details('{}_detatils.txt'.format(name))
