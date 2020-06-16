#! /usr/bin/env python3

import argparse
import json
import os

if __name__ == "__main__":
  args_parse = argparse.ArgumentParser(description='Converts a list in a JSON file to a CSV file, where each list item is a new line in the CSV.')
  args_parse.add_argument('json_file', help='The file containing the JSON list to transform to a CSV file.')
  args_parse.add_argument('csv_file', help='The file to write the list to.')
  args_parse.add_argument('--path', help='The dot separated path to the JSON list to convert.')
  args = args_parse.parse_args()

  if not os.path.exists(args.json_file):
    print('File not found')
    exit(1)

  with open(args.json_file) as data:
    json_data = json.load(data)

  node = json_data
  if args.path is not None:
    for path_node in args.path.split('.'):
      if not path_node in node:
        print(f'No node : {path_node}')
        exit(2)
      node = node[path_node]

  with open(args.csv_file, 'w') as out:
    lines = [ f'{item}\n' for item in node ] 
    out.writelines(lines)
