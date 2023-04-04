# web-semantic-csv-generator

Help in generating CSV files (Clean, CEA, CTA, CPA) for Web Semantic work.

## Setup

### Create a virtual environment

```bash
    python3 -m venv .venv || virtualenv .venv
```

### Activate the virtual environment

```bash
    source .venv/bin/activate
```

### Install dependencies

```bash
    pip install -r requirements.txt
```

## Usage

### For the script1

This script generate directories from files to clean, with the wikidata and foodon directories.
So you need to pass `the path of the directory where the files to clean are` and `the path of the directory where you want to create folder for each file`.

```bash
    python3 script1.py -i <path of the directory where the files to clean are> -o <path of the directory where you want to create folder for each file>
``` 

<b>Attention</b>: The script will create a folder for each file in the input directory. So if you have 10 files in the input directory, you will have 10 folders in the output directory.

### For the script2

This script generate the CEA, CTA and CPA files from the directories created by the script1. So you need to pass `the path of the directory where the directories created by the script1 are`. But before that, you need to clean the file in the output directory, otherwise the CTA, CEA and CPA files will be erroneous

```bash
    python3 script2.py -d <path of the directory where the directories created by the script1 are>
```

### Example

In this project directory, we have a folder named `the-test`, this folder contains a file to clean. So we can use the script1 to create a directory for this file. The result of the script1 need to be in the `DONE` directory.

```bash
    python3 script1.py -i <path of the directory the-test> -o <path of the directory DONE>
```

For the script2, we need to pass the path of the directory `DONE` as argument.

```bash
    python3 script2.py -d <path of the directory DONE>
```

<center>
<h4>
<i><p>It's all, make an issue if you have a problem.</p> One star ⭐ is enough for me, if you like it, thank you.
</i>
</h4>
</center>
