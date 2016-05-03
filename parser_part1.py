import csv

DATA_IN = 'data_orig.csv'
DATA_OUT = 'data.csv'

top_univ = set(['University of Illinois at Urbana-Champaign',
                'Stanford University',
                'University of California - Berkeley',
                'Cornell University',
                'Massachusetts Institute of Technology',
                'University of Texas - Austin',
                'Georgia Institute of Technology',
                'University of Washington',
                'Carnegie Mellon University',
                'Princeton University',
                ])


def check_valid(row):
    if row['Bachelors'] == "":
        return False
    #if row['Masters'] == "":
    #    return False
    if row['Doctorate'] == "":
        return False
    #if row['PostDoc'] == "":
    #    return False
    return True


def parse(original):
    pos = original.rfind(' - ')
    if (pos == -1):
        parsed = original
    else:
        parsed = original[:pos]
    return parsed


def refactor(input,output):
    header = "Name,University,JoinYear,Rank,Subfield,Bachelors,Doctorate\n"

    with open(input) as infile:
        csvdata = csv.DictReader(infile)
        with open(output,'w') as outfile:
            outfile.write(header)
            for row in csvdata:
                if (check_valid(row) == True):
                    result = row['Name']+ "," + \
                             row['University'] + "," + \
                             row['JoinYear'] + "," + \
                             row['Rank'] + "," + \
                             row['Subfield']  + "," + \
                             parse(row['Bachelors']) + "," + \
                             parse(row['Doctorate']) + "\n"
                    outfile.write(result)
    return

refactor(DATA_IN,DATA_OUT)