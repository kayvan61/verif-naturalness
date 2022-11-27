import os
import subprocess

with open("verilog-repos.txt") as f:
    for line in f:
        url = line.split(' ')[0]
        subprocess.run(["git", "clone", url])