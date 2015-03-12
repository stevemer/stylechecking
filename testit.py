"""style183.

Usage:
  naval_fate.py <zipfile>

Options:
  -h --help     Show this screen.
"""

from docopt import docopt
import sys, os, re, glob, time, subprocess
from cStringIO import StringIO
import sys

CHECKED = [
    'whitespace',
    'build/include',
    'readability/casting',
    'legal/copyright',
    'Done processing',
    'Total errors'
]

def header(student, fname):
    fname.write('=' * 80 + '\n')
    fname.write('Grading Student: {0}\n'.format(student))
    fname.write('=' * 80 + '\n')

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    #Grab a zipfile
    #Open the zipfile
    os.system('unzip ' + arguments['<zipfile>'] + ' -d student_files')

    final = open('output', 'w+')
    #For each file, run cpplint and save the output
    for student_filename in glob.glob('student_files/*'):
        header(student_filename.split('.')[0].split('/')[-1], final)
        print "grading student file:", student_filename 
        print "checking:", os.path.abspath(student_filename)
        os.system('cpplint ' + os.path.abspath(student_filename) + ' &> result')
        result = open('result', 'rU').readlines()
        for line in result:
            for check in CHECKED:
                if check in line:
                    final.write(line)

    #Filter the output down to the ones we want

    #Log the output to a logfile and save the student score in a CSV file


