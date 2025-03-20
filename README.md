# The-Emergence-of-Rhymed-Meters-in-the-Indo-Aryan-Prosody
This repository contains codes and data of the survey in a paper 'The Emergence of Rhymed Meters in Indo-Aryan Prosody'.
The primary focuses of investigation are the differences in the diversity of word endings and in the easiness of the end rhyme between Old Indo-Aryan and Middle Indo-Aryan. 

# Test design

(R)= ∑_(k = 1)^m▒〖{P(r_k)}〗^2 
The codes were executed on Python 3.9.6.

# Material Texts
This survey utilizes six texts: R̥gveda Saṃhitā (RV), Gāhā Sattasaī (SS), Setubandha (SB), Gaüḍavaho (GV), Paümacariu (PC), Pāhuḍadohā (PD).  

As an electronic text of RV, I used Lubotsky's (1997) text, which is available on Vedaweb. 
  https://github.com/VedaWebProject/vedaweb-data
A file named 'lubotsky.csv' was downloaded and converted into a txt file. Notations of Hymn numbers and Pādas as well as accent notation were removed. Metrical lengthened forms marked by '+' or '+_-' were replaced by short forms. Other notations such as '_' and '-' was removed except for '-' in the middle of the words meaning Āmredita, which was replaced by ' '. In this way 'rv.txt' was prepared.

As electronic texts of SS and PC, I used GRETIL's texts.
  https://gretil.sub.uni-goettingen.de/gretil.html
I downloaded html files of the e-texts of SS and PC and converted into a txt file.
As for PC, I removed lines which do not contain main texts. Blank lines, lines which only indicates the beginning of a chapter, lines which say 'ghattā:', and lines which indicates only the meter like 'jambheṭṭiẏā' were removed for example. Words written in the gesperrt style, such as 'sa ẏaṃ bhu', were replaced by the normal form ('saẏaṃbhu'). Blank lines were added after {Pc_49,2.1}, two lines after {Pc_74,5.8}, {Pc_74,6.10}, {Pc_74,7.10},  {Pc_74,8.10}, {Pc_74,9.10}, {Pc_74,10.10}, {Pc_74,11.10}, {Pc_74,12.10}, {Pc_74,13.10}, {Pc_74,14.10}, {Pc_74,15.10}, {Pc_74,16.8}, {Pc_74,17.10}. In this way 'ss.txt' and 'pc.txt' were prepared.

As electronic texts of SB and GV, I used texts from Prakrit Digital Text Project.
  https://github.com/aso2101/prakrit_texts
'Sētu.xml' and 'GaüḍVa.xml' were downloaded and converted into txt files. Then I extracted the main texts removing tags and other information. In this way 'sb.txt' and 'gv.txt' were prepared.

As for PD, I created the electronic text in the form of .txt file based on Śāstrī (1998).

# Data Files

# Bibliography
