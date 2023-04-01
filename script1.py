"""
Author : Edmond Ghislain Makolle

Script to generate directories from files to clean, with the wikidata
and foodon directories.

"""
import os
import shutil
import argparse

from pathlib import Path
    

def generate_directories(args):
    """Generate directories from files to clean, with the wikidata and foodon"""    
    # Directory where are files to clean
    # dir1 = '/home/edghi/Web.Semantic/37'
    files = Path(args.input_dir)

    # Directory where we want to create folder for each file
    # dir2 = '/home/edghi/Web.Semantic'
    out = Path(args.output_dir)
    i = 1
    for file in files.iterdir():
        print(f"{i} - {file.name}")
        i += 1
        
        name = file.name.split('.')[0]
        os.chdir(out)
        os.mkdir(name)
        os.chdir(name)
        os.mkdir('input')
        os.mkdir('output')
        
        ori = Path(f'{args.input_dir}/{name}{file.suffix}')
        tar1 = Path(f'{args.output_dir}/{name}/input/{name}{file.suffix}')
        shutil.copyfile(ori, tar1)
        
        tar2 = Path(f'{args.output_dir}/{name}/output/{name}{file.suffix}')
        shutil.copyfile(ori, tar2)
        os.chdir(f'{args.output_dir}/{name}/output')
        os.rename(f'{name}{file.suffix}', f'{name}_clean{file.suffix}')
        
        os.mkdir('wikidata')
        os.mkdir('foodon') 


parser = argparse.ArgumentParser(
    description='''Script to generate directories from files to clean, with
    the wikidata and foodon directories.''',
)

parser.add_argument(
    '-i', 
    '--input-dir',
    dest='input_dir',
    type=str,
    required=True,
    help='Directory where are files to clean.',
)
parser.add_argument(
    '-o',
    '--output-dir',
    dest='output_dir',
    type=str,
    required=True,
    help='Directory where we want to create folder for each file.',
)

args = parser.parse_args()
generate_directories(args)
