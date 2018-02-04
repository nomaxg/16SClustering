import os
import subprocess

def main():
    for root, dirs, files in os.walk("."):  
        for filename in files:
            pos = filename.find('fastq')
            if pos != -1:
                merge_files(filename[:pos])

def merge_files(filename):
    command = 'join_paired_ends.py -f ./trimmed_files/{} -r ./trimmed_files/{} -o ./joined_files'.format(
        filename + "fastq.forward.trimmed.fastq", filename + 'fastq.reverse.trimmed.fastq')
    subprocess.call([command])

if __name__ == '__main__':
    main()


