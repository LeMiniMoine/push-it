#!/bin/sh
# pushit-launcher.sh
# navigate to Pi main user directory, find script, execute it, back to pi user directory

cd ~
dir_path=$(find ~ -type d -name pushit)
cd ${dir_path}
python3 src/pushit.py
cd ~