#!/usr/bin/env python3

import time
import argparse, hashlib

if __name__ == '__main__':
  argp = argparse.ArgumentParser()
  argp.add_argument('-k', '--key', required=True)
  argp.add_argument('-s', '--secret', required=True)
  args = argp.parse_args()

  now = int(time.time())
  data = args.key + args.secret + str(now)
  md5 = hashlib.md5()
  md5.update(bytes(data, 'utf-8'))
  print(md5.hexdigest())
