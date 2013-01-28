import sys
from time import strftime, strptime
from datetime import datetime, timedelta
import getopt
import csv

def usage(script_name):
    print "usage: python %s [-q<ferdous>]" % script_name
    print "       python %s [--query=<nobody likes you>]" % script_name
    print "       python %s [-h]" % script_name
    print "       python %s [--help]" % script_name
    return

def cli(cli_args, method, script_name):
    try:
        opts, args = getopt.getopt(cli_args, 'hq:', ['help', 'query='])
    except getopt.GetoptError:
        usage(script_name)
        sys.exit(2)

    if not opts:
        usage(script_name)
        sys.exit(2)

    for opt, arg in opts:

        if opt in ['-q', '--query']:
            method.__call__(arg)
            print 'Operation completed!'
            #print '\033[34;1mOperation Completed! \033[0m'
        elif opt in ['-h', '--help']:
            usage(script_name)
    return

def current_time(format="%Y-%m-%d %H:%M:%S"):
    return strftime(format, datetime.now().timetuple())

dashed_name = lambda name: name.lower().replace(' ', '-')

def get_items_from_csv(csv_src):
    try:
        #data = UnicodeReader(csv_src, encoding='utf-8')
        #data = unicode_csv_reader(csv_src)
        data = csv.reader(open(csv_src))
    except IOError:
        print "File not found => %s" % csv_src
        sys.exit(2)
    try:
        # Read the column names from the first line of the file
        fields = data.next()
        items = []
        for row in data:
            item = {}
            for (name, value) in zip(fields, row):
                item[name] = value.strip()
            items.append(item)
    except csv.Error, e:
        print "Error in file %s at line %d: %s" % (csv_src, data.line_num, e)
        sys.exit(2)
    return items