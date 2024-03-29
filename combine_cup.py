import csv
import glob
import sys
import os
import pandas as pd

# credited:
# https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python/12280052
# https://github.com/ekapope/Combine-CSV-files-in-the-folder/blob/master/Combine_CSVs.py


OUTPUT_DIR = 'output'


def combine(out_fb):
    all_filenames = [i for i in glob.glob('*.cupx.cup', root_dir=os.path.join(OUTPUT_DIR, ""))]
    print('Combined source files:\n', all_filenames)

    # combine all files in the list
    combined_csv = pd.concat([pd.read_csv(os.path.join(OUTPUT_DIR, f), on_bad_lines='skip') for f in all_filenames])
    combined_csv.sort_values(by='name')
    # export to csv
    print('Combined file:\n', out_fb)
    combined_csv.to_csv(os.path.join(OUTPUT_DIR, out_fb), index=False, encoding='utf-8-sig', quoting=csv.QUOTE_MINIMAL)


if __name__ == '__main__':
    combine(sys.argv[1] if len(sys.argv) > 1 else combine('combined_cup.cup'))
