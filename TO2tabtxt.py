#    TO2TBX   
#    Copyright (C) 2020  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import xml.etree.ElementTree as etree
from xml.sax.saxutils import escape
import codecs

fentrada=sys.argv[1]
fsortida=sys.argv[2]
langs=sys.argv[3:]

print(langs)

sortida=codecs.open(fsortida,"w",encoding="utf-8")
subject=""
term={}
ident={}
for event, elem in etree.iterparse(fentrada):
    if event=='end':
        if elem.tag=="titol":
                titol="".join(elem.itertext()).lstrip().rstrip()
        if elem.tag=="fitxa":
                num=elem.attrib["num"]
                ident=titol+"-"+str(num)
                print(ident,term,subject)
                #escrivim la informacio
                llengues=list(term.keys())
                llengues.sort()
                termes={}
                for llengua in list(set(langs).intersection(llengues)):
                    termes[llengua]=[]
                    for termdenomin in term[llengua].split("|"):
                        termes[llengua].append(escape(termdenomin.lstrip().rstrip()))
                cadena=[]
                for l in langs:
                    cadena.append("|".join(termes[l]))
                sortida.write("\t".join(cadena)+"\n")
                subject=""
                term={}
        elif elem.tag=="areatematica":
            area="".join(elem.itertext()).lstrip().rstrip()
        elif elem.tag=="denominacio":
            llengua=elem.attrib["llengua"]
            pos=elem.attrib["categoria"]
            denominacio="".join(elem.itertext()).lstrip().rstrip()
            if llengua in langs and not llengua in term:
                term[llengua]=denominacio
            elif llengua in langs:
                term[llengua]+="|"+denominacio
print(langs)
