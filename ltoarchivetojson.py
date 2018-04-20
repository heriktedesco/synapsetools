'''
        LTO ARCHIVE TO JSON
        LICENSE: CREATIVE COMMONS Attribution 4.0 International
        CREATOR: HERIK BATISTA TEDESCO http://github.com/heriktedesco
        SUPERVISOR: GUSTAVO H. M. SILVA http://github.com/gustavohmsilva
'''
#!/usr/bin/env python3
import csv
import sys

csv_f = csv.reader(open(str(sys.argv[1])))
n = "\n"
nt = "\n\t"
ntt = "\n\t\t"
nttt = "\n\t\t\t"
for row in csv_f:
    for i, _ in enumerate(row):
        if _ == "":
            row[i] = "NO DESCRIPTION"
    codigo = '"Codigo de Programa":"'+row[0]+'"'
    description = '"Description":"'+row[1]+'"'
    bitrate = '"Overall bit rate":"'+row[5]+'"'
    lto = '"TAPE Number":"'+row[7]+'"'
    codec = '"Format":"'+row[2]+'"'
    height = '"Height":"'+row[3]+'"'
    display = '"Display aspect ratio":"'+row[4]+'"'
    fps = '"Frame rate":"'+row[6]+'"'

    general = '{'+nt+codigo+','+nt+description+','+nt+bitrate+','+nt+lto+','+n
    video = '\t"Video":'+ntt+'[{'+nttt+codec+','+nttt+height+','+nttt+display+','+nttt+fps+ntt+'}]'+n+'}'
    arquivo = open(row[0]+"_"+row[1]+".json", 'w')
    arquivo.write(general+video)
    arquivo.close()
