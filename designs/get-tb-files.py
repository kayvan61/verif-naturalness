import os
import subprocess
import glob
from pathlib import Path

dir_files = [
    '1-tbs-dir',
    '1-test-dir',
    '1-verif-dir'
]

corpus_files = open('./corp_paths', 'w')

for cur_dir in dir_files:
    print(cur_dir)
    with open(cur_dir) as f:
        for line in f:
            line = line.strip()
            cur_dir_path = os.path.join(os.getcwd(), line) 
            v_res = Path(cur_dir_path).rglob('*.v')
            sv_res = Path(cur_dir_path).rglob('*.sv')
            for path in v_res:
                print(path,file=corpus_files)
            for path in sv_res:
                print(path,file=corpus_files)