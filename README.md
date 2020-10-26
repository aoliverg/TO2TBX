= TO2TBX and TO2tabtxt =

== Introduction ==

Simple scripts to transform XML files from Termcat's Terminologia Oberta glossaries to TBX or tab delimited files.

Terminologia oberta can be reached at: ([https://www.termcat.cat/ca/terminologia-oberta](https://www.termcat.cat/ca/terminologia-oberta))

== Usage ==

Download the desired terminological glossary in XML format and then follow the instrucions:

=== TO2TBX ===

To transform glossary1.xml to glossary1.tbx, taking the eng, spa and cat terms do:

```
python3 TO2TBX glossary1.xml glossary1.tbx en es ca
``` 

 
=== TO2tabtxt ===

To transform glossary1.xml to glossary1.txt, taking the eng, spa and cat terms (in this order) do:

```
python3 TO2TBX glossary1.xml glossary1.txt en es ca
``` 

=== License ===

This is free software released under GNU GPL v3 or later (at your choice).


