import os

def main():
  os.system("""
#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: drsize <directory>"
    exit 1
fi

du -hs "$1"

"""

main()
