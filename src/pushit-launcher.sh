#!/bin/sh
# pushit-launcher.sh
# navigate to Pi main user directory, find script, execute it, back to pi user directory

cd ~
script_path=$(find ~ -type f -name pushit.py)
python3 ${script_path}
cd ~