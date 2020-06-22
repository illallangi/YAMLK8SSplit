#!/usr/bin/env python3

import os
import sys
import yaml
import six

def main():
  files = sys.argv[1:]
  if not files:
      files = ["/dev/stdin"]
  for file in files:
    f = open(file)
    for i in yaml.load_all(f, Loader=yaml.FullLoader):
      for r in i['items'] if (i.get('kind') or '') == "List" else [i]:
        os.makedirs(os.path.join(os.path.realpath('.'), *[x for x in [r['metadata'].get('namespace')] if x is not None]), exist_ok=True)
        filename = os.path.join(os.path.realpath('.'), *[x for x in [r['metadata'].get('namespace'), f"{r['kind'].lower()}-{r['metadata']['name']}.yaml"] if x is not None]).replace(':','-')
        with open(filename, "w") as file:
          print('---', file=file)
          yaml.dump(r, file)
        print(f"Wrote {filename}")

# Get around pyyaml removing leading 0s
# https://github.com/yaml/pyyaml/issues/98
def string_representer(dumper, data):
  if data.startswith("0"):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="'")
  try:
      dlen = len(data.splitlines())
      if (dlen > 1):
          return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
  except TypeError as ex:
      return dumper.represent_scalar('tag:yaml.org,2002:str', data)
  return dumper.represent_scalar('tag:yaml.org,2002:str', data)
yaml.Dumper.add_representer(six.text_type, string_representer)

if __name__ == "__main__":
  main()
