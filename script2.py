"""
Author : Edmond Ghislain Makolle

Script to generate CEA, CTA, CPA files for each file cleaned,
for wikidata and foodon.

"""
import pandas as pd
import os
import argparse

from pathlib import Path


CEA_HEADERS = ['file', 'col', 'row', 'URI']
CTA_HEADERS = ['file', 'col', 'URI']
CPA_HEADERS = ['file', 'col0', 'colx', 'URI']


def generate_cea_file(filename: str, _from: pd.DataFrame, _for: str):
    """
    Function to generate the CEA file.
    
    Parameters
    ----------
    filename : str 
        The name of the file for which we want to generate the CEA.
    
    _from : DataFrame
        The data of the file for which we want to generate the CEA.
    
    _for : str
        This value is for define if the file is for ``wikidata`` or ``foodon``
    
    Returns
    -------
    Generate the file.
    """
    if _for not in ('wikidata', 'foodon'):
        print("Enter a good value for the parameter _for. It's ``wikidata`` or ``foodon``")
    
    else:
        cea_list = []
        for col in range(len(_from.columns)):
            for row in range(len(_from.index)):
                line = [filename, col, row, '']
                cea_list.append(line)

        cea = pd.DataFrame(cea_list, columns=CEA_HEADERS)
        cea.to_csv(f'cea_{_for}.csv', index=False)
        
        print(f"CEA of the file <{filename}> for {_for} generated !")


def generate_cta_file(filename: str, _from: pd.DataFrame, _for: str):
    """
    Function to generate the CTA file.
    
    Parameters
    ----------
    filename : str 
        The name of the file for which we want to generate the CTA.
    
    _from : DataFrame
        The data of the file for which we want to generate the CTA.
    
    _for : str
        This value is for define if the file is for ``wikidata`` or ``foodon``
    
    Returns
    -------
    Generate the file.
    """
    if _for not in ('wikidata', 'foodon'):
        print("Enter a good value for the parameter _for. It's ``wikidata`` or ``foodon``")
    
    else:
        cta_list = []
        for col in range(len(_from.columns)):
            line = [filename, col, '']
            cta_list.append(line)

        cta = pd.DataFrame(cta_list, columns=CTA_HEADERS)
        cta.to_csv(f'cta_{_for}.csv', index=False)
        
        print(f"CTA of the file <{filename}> for {_for} generated !")


def generate_cpa_file(filename: str, _from: pd.DataFrame, _for: str):
    """
    Function to generate the CPA file.
    
    Parameters
    ----------
    filename : str 
        The name of the file for which we want to generate the CPA.
    
    _from : DataFrame
        The data of the file for which we want to generate the CPA.
    
    _for : str
        This value is for define if the file is for ``wikidata`` or ``foodon``
    
    Returns
    -------
    Generate the file.
    """
    if _for not in ('wikidata', 'foodon'):
        print("Enter a good value for the parameter _for. It's ``wikidata`` or ``foodon``")
    
    else:
        cpa_list = []
        for col_0 in range(len(_from.columns)-1):
            for col_x in range(col_0+1, len(_from.columns)):
                line = [filename, col_0, col_x, '']
                cpa_list.append(line)

        cpa = pd.DataFrame(cpa_list, columns=CPA_HEADERS)
        cpa.to_csv(f'cpa_{_for}.csv', index=False)
        
        print(f"CPA of the file <{filename}> for {_for} generated !")


###################################################################################################

def generate_files(args):
    # Directory where we have all cleaned directories of files
    folders = Path(args.dir)

    for folder in folders.iterdir():
        # print(folder.name)
        
        os.chdir(f"{folder}/output/")
        # print(f"We are here ==> {os.getcwd()}")
        data = pd.read_csv((f"{folder.name}_clean.csv"))
        
        os.chdir(f"{folder}/output/wikidata/")
        # print(f"We are here ==> {os.getcwd()}")
        generate_cea_file(folder.name, data, "wikidata")
        generate_cpa_file(folder.name, data, "wikidata")
        generate_cta_file(folder.name, data, "wikidata")
        
        os.chdir(f"{folder}/output/foodon/")
        # print(f"We are here ==> {os.getcwd()}")
        generate_cea_file(folder.name, data, "foodon")
        generate_cpa_file(folder.name, data, "foodon")
        generate_cta_file(folder.name, data, "foodon")
        
        print("\n")


parser = argparse.ArgumentParser(
    description='''Generate CEA, CTA, CPA files for each file cleaned, for 
    wikidata and foodon.'''
)

parser.add_argument(
    '-d', 
    '--directory', 
    type=str, 
    dest='dir',
    required=True,
    help='The directory where we have all cleaned directories of files.'
)

args = parser.parse_args()
generate_files(args)
