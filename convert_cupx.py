import csv
import os
import re
import shutil
import sys
from pathlib import Path

import binwalk

# Copied and adapted from https://github.com/lordfolken/xcsoar-cupx-converter. Many thank @lordfolken

DATA_ROOT = 'data/'


def cpux2xcsoar(cupx_file):
    # generate temporary directory
    temp_dir = Path(__file__).resolve().parent / 'temp'
    os.makedirs(temp_dir, exist_ok=True)

    # copy cupx file into temporary directory
    cupx_file_name = os.path.basename(cupx_file)
    cupx_file_path = os.path.join(temp_dir, cupx_file_name)
    shutil.copy(DATA_ROOT + cupx_file_name, cupx_file_path)
    cupx_file_extracted_path = '{}/_{}.extracted'.format(temp_dir.name, cupx_file_name)

    # binwalk cupx_file and extract all files
    binwalk.scan(cupx_file_path, quiet=True, signature=True, extract=True)

    # look for points.cup file without case sensitivity
    cup_file = None
    for filename in os.listdir(cupx_file_extracted_path):
        if re.search(r'points.cup', filename, re.IGNORECASE):
            cup_file = filename
            break

    # Takes a POINTS.CUP file in cupx format and converts it to a waypoints_details file.
    input_file = open('{}/{}'.format(cupx_file_extracted_path, cup_file), 'r')

    # convert to unix line format
    input_file_content = input_file.read().replace('\r\n', '\n').replace('\r', '\n')

    # create output directory
    os.makedirs('output', exist_ok=True)

    CUP_FILENAME = 'output/{}.cup'.format(cupx_file_name)
    with open(CUP_FILENAME, 'w') as cup_unix_file:
        cup_unix_file.write(input_file_content)

    # create output sub directories
    for subdir in ['pics', 'docs']:
        os.makedirs('output/{}'.format(subdir), exist_ok=True)

    # Create a corresponding waypoints_details file
    with open(CUP_FILENAME, 'r') as csv_in_file:
        csv_reader = csv.reader(csv_in_file)
        with open(csv_in_file.name.replace('.cupx.cup', '.wp_details.txt'), 'w') as output_file:
            for row in csv_reader:
                # skip the cup header: "name,code,country,lat,lon,elev,style,rwdir,rwlen,rwwidth,freq,desc,userdata,pics"
                if csv_reader.line_num == 1:
                    try:
                        pics_idx = row.index('pics')
                        code_idx = row.index('code')
                    except:
                        pics_idx = None
                    continue
                # bullet proofing: if the field "pics" does not exist skip the row
                if pics_idx is not None:
                    output_file.write('[{}]\n'.format(row[code_idx]))
                    for item in row[pics_idx].split(';'):
                        for dir_ext in [['Pics', '.jpg'], ['Docs', '.pdf']]:
                            if item.endswith(dir_ext[1]):
                                shutil.copy('{}/{}/{}'.format(cupx_file_extracted_path, dir_ext[0], item),
                                            'output/{}/'.format(dir_ext[0].lower()))
                                output_file.write('image={}/{}\n'.format(dir_ext[0], item))

    # delete temporary directory
    shutil.rmtree(temp_dir)


if __name__ == '__main__':
    cpux2xcsoar(sys.argv[1]) if len(sys.argv > 0) else print('no cupx-file specified')
