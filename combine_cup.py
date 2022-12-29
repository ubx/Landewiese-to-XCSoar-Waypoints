import csv
import glob
import sys

import pandas as pd

# credited:
# https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python/12280052
# https://github.com/ekapope/Combine-CSV-files-in-the-folder/blob/master/Combine_CSVs.py


OUTPUT_ROOT = 'output/'


def combine(out_fb):
    all_filenames = [i for i in glob.glob('*.{}'.format('cupx.cup'), root_dir=OUTPUT_ROOT)]
    print('Compined source files:')
    print(all_filenames)

    # combine all files in the list
    combined_csv = pd.concat([pd.read_csv(OUTPUT_ROOT + f) for f in all_filenames])
    combined_csv.sort_values(by='name')
    # export to csv
    print('Combined file:')
    print(out_fb)
    combined_csv.to_csv(OUTPUT_ROOT + out_fb, index=False, encoding='utf-8-sig', quoting=csv.QUOTE_MINIMAL)


if __name__ == '__main__':
    combine(sys.argv[1] if len(sys.argv) > 1 else combine('combined_cup.cup'))
