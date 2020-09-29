# combine_sheets
A script to combine multiple excel files with one worksheet per file into a single
excel file with multiple worksheets.

usage: combine_sheets [-h] [-i INPUT_PATH] [-o OUTPUT_FILE] [-g] [-r]

Combine multiple excel files with a single excel spreadsheet into one excel
file with multiple sheets.

optional arguments:
  -h, --help            show this help message and exit

  -i INPUT_PATH, --input_path INPUT_PATH
  
                        File path where excel files are located, can be folder
                        
                        or individual file

  -o OUTPUT_FILE, --output_file OUTPUT_FILE

                        File path to output excel file

  -g, --glob            Use glob to find files specified by input_path

  -r, --recursive       Perform glob search recursively
