# The-Emergence-of-Rhymed-Meters-in-the-Indo-Aryan-Prosody
This repository encompasses codes and data pertaining to the survey in the paper titled 'The Emergence of Rhymed Meters in Indo-Aryan Prosody'.
The primary focuses of investigation are the differences in the diversity of word endings and in the easiness of the end rhyme between Old Indo-Aryan and Middle Indo-Aryan. 

# Test design
This Survey has two steps. 


First, I listed the final two syllables of all multisyllabic words in each text, except for the onset of the penultimate, namely -VC0VC0# (hereafter referred to as the 'rhyme pattern').


Then, I calculated the probability of a coincidental rhyme match in each text.  The probability {P(r1)} of (r1) occurring at any given word-final location in the text is acquired by dividing the frequency of (r1) by the total number of rhymes in the text. Hence, the probability of the same (r1) happening to occur at any two given word-final locations is {P(r1)}^2. By calculating this probability for all rhyme patterns and summing them, the probability that any given rhyme pattern will match at the two locations is obtained. This is Rhyme Match Probability.


In Apabhraṃśa rhyming texts, such as PC and PD, multiple identical rhyme patterns that arise due to the metrical rhyming rule were counted only once to avoid double-counting.

# Material Texts
This survey utilizes six texts: R̥gveda Saṃhitā (RV), Gāhā Sattasaī (SS), Setubandha (SB), Gaüḍavaho (GV), Paümacariu (PC), Pāhuḍadohā (PD).  



As an electronic text of RV, I used Lubotsky's (1997) text, which is available on Vedaweb. 

Kölligan, Daniel et al. (2017-2025) Vedaweb: Online Research Platform for Old Indic Texts.

  https://github.com/VedaWebProject/vedaweb-data
  
A file named 'lubotsky.csv' was downloaded and subsequently converted into a txt file. Notations of Hymn numbers, Pādas, and accent marks were removed. Metrical lengthened forms, marked by '+' or '+_-', were replaced with their short forms. Other notations such as '_' and '-' was removed except for '-' in the middle of the words meaning Āmredita, which was replaced by a space. In this way 'rv.txt' was prepared.



As electronic texts of SS and PC, I used GRETIL's texts.

Niedersächsische Staats- und Universitätsbibliothek (2010) GRETIL - Göttingen Register of Electronic Texts in Indian Languages. 

  https://gretil.sub.uni-goettingen.de/gretil.html
  
Htm files of the e-texts of SS and PC were downloaded and converted into text files.
For PC, lines which do not contain main texts were removed. This included blank lines, lines indicating the beginning of a chapter, lines stating 'ghattā:', lines indicating only the meter, such as 'jambheṭṭiẏā', etc. Words written in the gesperrt style, such as 'sa ẏaṃ bhu', were replaced with their normal forms ('saẏaṃbhu'). Blank lines were added after {Pc_49,2.1}, two lines after {Pc_74,5.8}, {Pc_74,6.10}, {Pc_74,7.10},  {Pc_74,8.10}, {Pc_74,9.10}, {Pc_74,10.10}, {Pc_74,11.10}, {Pc_74,12.10}, {Pc_74,13.10}, {Pc_74,14.10}, {Pc_74,15.10}, {Pc_74,16.8}, {Pc_74,17.10}. Thus, 'ss.txt' and 'pc.txt' were prepared.



As electronic texts of SB and GV, I used texts from Prakrit Digital Text Project.

Ollett, Andrew - Prakrit Digital Text Project. 

  https://github.com/aso2101/prakrit_texts
  
'Sētu.xml' and 'GaüḍVa.xml' were downloaded and converted into txt files. Then the main texts were extracted by removing tags and other extranious information. In this way 'sb.txt' and 'gv.txt' were prepared.



As for PD, I created the electronic text in the form of .txt file based on Śāstrī (1998).


# Data Files
Python files, such as 'sanskrit.py', contain the codes necessary for conducting this survey. These scripts are designed to automatically tabulate the rhyme patterns from the imput of a text file and calculate the rhyme match probability. The codes were executed using Python 3.9.6.

Rhyme pattern files, such as 'rv_rhymepattern.txt' exhibits all tokens of the rhyme patterns extracted from the source text.

List files, such as 'rvlist.txt', are generated with 'sort' and 'uniq' commands on the command line from the rhymepattern files. They display all types of the rhyme patterns and list them in ascending order. 

Result files, such as 'rv_result.txt' indicate token counts and type counts of the rhyme patterns as well as the rhyme match probability.

# Bibliography
Lubotsky, Alexander (1997) A R̥gvedic word concordance. American Oriental Series; v.82-83. 2.v. New Haven, Conn.: American Oriental Society. 
Muni Rāmasiṃha and Śāstrī, Devendrakumāra (ed.) (1998) Pāhuḍadohā (Apabhraṃśa kā rahasyavādī kāvya). Nayī Dillī: Bhāratīya Jñānapīṭha.

