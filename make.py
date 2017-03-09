import os
import argparse
from argparse import RawTextHelpFormatter
import glob

def clean():
    print('Cleaning up files.')
    cleanups = [glob.glob(x) for x in ['*.log', '*.bbl',  '*.blg', '*.aux', '*.synctex.gz']]
    cleanups = [item for sublist in cleanups for item in sublist]
    for f in cleanups:
        os.system("rm {0}".format(f))

def make_bib():
    print('Making bibtex file.')
    os.system("cp /Users/tlschol/Documents/bibtex/Model\ Selection\ Paper.bib modelselectionpaper.bib")
    os.system('python bib_mutate.py')

def compile():
    print('Compiling pdf.')
    source = 'wilkspaper'
    os.system("pdflatex -interaction=batchmode {0}.tex".format(source))
    os.system("bibtex {0}.aux".format(source))
    os.system("pdflatex -interaction=batchmode {0}.tex".format(source))
    os.system("pdflatex -interaction=batchmode {0}.tex".format(source))
    os.system("bibtex {0}.aux".format(source))
    os.system("pdflatex -interaction=batchmode {0}.tex".format(source))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Helper file for generating paper.", formatter_class=RawTextHelpFormatter,)

    parser.add_argument('action',  type=str,
                       help='The action to perform')
    args = parser.parse_args()

    action = args.action

    if action == 'clean':
        clean()
    elif action == 'compile':
        compile()
    elif action == 'bib':
        make_bib()
    else:
        print('Action {0} not understood.'.format(action))