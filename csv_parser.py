import csv

f = open("E:\HJ\UIUC\CS\CS467\proj_final\data.csv", "r")
data = csv.reader(f)

schema = []
for row in data:
    schema = row + []
    break

print schema

univ = set()
univ_bs = set()
univ_ms = set()
univ_phd = set()

univ_idx = schema.index('University')
univ_bs_idx = schema.index('Bachelors')
#univ_ms_idx = schema.index('Masters')
univ_phd_idx = schema.index('Doctorate')
fd_idx = schema.index('Subfield')

"""
for row in data:
    univ.add(row[univ_idx])
    univ_bs.add(row[univ_bs_idx])
    univ_ms.add(row[univ_ms_idx])
    univ_phd.add(row[univ_phd_idx])

print len(univ)
print len(univ_bs)
print len(univ_ms)
print len(univ_phd)
"""

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
bs_prof = {}
ms_prof = {}
phd_prof = {}
bs_phd = {}

bs_program = set()
phd_program = set()


for row in data:
    if row[univ_idx] in top_univ:
        bs_key = (row[univ_bs_idx], row[univ_idx], row[fd_idx])
        #ms_key = (row[univ_ms_idx], row[univ_idx], row[fd_idx])
        phd_key = (row[univ_phd_idx], row[univ_idx], row[fd_idx])
        bs_phd_key = (row[univ_bs_idx], row[univ_phd_idx], row[fd_idx])
        if bs_key in bs_prof:
            bs_prof[bs_key] += 1
        else:
            bs_prof[bs_key] = 1
        if phd_key in phd_prof:
            phd_prof[phd_key] += 1
        else:
            phd_prof[phd_key] = 1
        #if ms_key in ms_prof:
        #    ms_prof[ms_key] += 1
        #else:
        #    ms_prof[ms_key] = 1
        if bs_phd_key in bs_phd:
            bs_phd[bs_phd_key] += 1
        else:
            bs_phd[bs_phd_key] = 1

print len(bs_prof)
print len(ms_prof)
print len(phd_prof)

prof_data = []
for key in phd_prof:
    col0 = '1_' + key[2] + '_' + key[0]
    col1 = '2_'+ key[2] + '_' + key[1]
    prof_data.append([col0, col1, phd_prof[key]])

for key in bs_phd:
    col0 = '0_' + key[2] + '_' + key[0]
    col1 = '1_'+ key[2] + '_' + key[1]
    prof_data.append([col0, col1, bs_phd[key]])    


def writeCsvFile(fname, data, *args, **kwargs):
    """
    @param fname: string, name of file to write
    @param data: list of list of items

    Write data to file
    """
    mycsv = csv.writer(open(fname, 'wb'), *args, **kwargs)
    for row in data:
        mycsv.writerow(row)


writeCsvFile("E:\HJ\UIUC\CS\CS467\proj_final\prof_data.csv", prof_data)


f.close()
