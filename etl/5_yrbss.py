"""
Amy Fan 7-2022

ETL for the YRBS survey data

input:
_____

~/data/source/sadc_2019_state_a_m.dat

    Survey data for states beginning with A-M
    
~/data/source/sadc_2019_state_n_z.dat

    Survey data for states beginning with N-Z


output:
______

~/data/processed/etl_5_yrbs.csv

    cleaned data on teen birth rates for 2019 by state

"""

##############
# SETTING UP #
##############

import pandas as pd
import numpy as np

input_loc = "data//source//"
output_loc = "data//processed//"

infile_a_m_str = input_loc + "sadc_2019_state_a_m.dat"
infile_n_z_str = input_loc + "sadc_2019_state_n_z.dat"

colspecs_infile = [(0,5),  (5,55), (55,105), (105,113), (113,121), (121,124), (124,134), (134,142), (142,150), (150,158), (158,161), (161,164), (164,167), (167,170), (170,173), (173,181), (181,189), (189,197), (197,205), (205,208), (208,211), (211,212), (212,213), (213,221), (221,229), (229,237), (237,245), (245,246), (246,247), (247,248), (248,249), (249,250), (250,251), (251,252), (252,253), (253,254), (254,255), (255,256), (256,257), (257,258), (258,259), (259,260), (260,261), (261,262), (262,263), (263,264), (264,265), (265,266), (266,267), (267,268), (268,269), (269,270), (270,271), (271,272), (272,273), (273,274), (274,275), (275,276), (276,277), (277,278), (278,279), (279,280), (280,281), (281,282), (282,283), (283,284), (284,285), (285,286), (286,287), (287,288), (288,289), (289,290), (290,291), (291,292), (292,293), (293,294), (294,295), (295,296), (296,297), (297,298), (298,299), (299,300), (300,301), (301,302), (302,303), (303,304), (304,305), (305,306), (306,307), (307,308), (308,309), (309,310), (310,311), (311,312), (312,313), (313,314), (314,315), (315,316), (316,317), (317,318), (318,319), (319,320), (320,321), (321,322), (322,323), (323,324), (324,325), (325,328), (328,331), (331,334), (334,337), (337,340), (340,343), (343,346), (346,349), (349,352), (352,355), (355,358), (358,361), (361,364), (364,367), (367,370), (370,373), (373,376), (376,379), (379,382), (382,385), (385,388), (388,391), (391,394), (394,397), (397,400), (400,403), (403,406), (406,409), (409,412), (412,415), (415,418), (418,421), (421,424), (424,427), (427,430), (430,433), (433,436), (436,439), (439,442), (442,445), (445,448), (448,451), (451,454), (454,457), (457,460), (460,463), (463,466), (466,469), (469,472), (472,475), (475,478), (478,481), (481,484), (484,487), (487,490), (490,493), (493,496), (496,499), (499,502), (502,505), (505,508), (508,511), (511,514), (514,517), (517,520), (520,523), (523,526), (526,529), (529,532), (532,535), (535,538), (538,541), (541,544), (544,547), (547,550), (550,553), (553,556), (556,559), (559,562), (562,565), (565,568), (568,571), (571,574), (574,577), (577,585), (585,593), (593,596), (596,599), (599,602), (602,605), (605,608), (608,611), (611,614), (614,617), (617,620), (620,623), (623,626), (626,629), (629,632), (632,635), (635,638), (638,641), (641,644), (644,647), (647,650), (650,653), (653,656), (656,659), (659,662), (662,665), (665,666), (666,667), (667,668), (668,669), (669,670), (670,671), (671,672), (672,673), (673,674), (674,675), (675,676), (676,677), (677,678), (678,679), (679,680), (680,681), (681,682), (682,683), (683,684), (684,685), (685,686), (686,687), (687,688), (688,689), (689,690), (690,691), (691,692), (692,693), (693,694), (694,695), (695,696), (696,697), (697,698), (698,699), (699,700), (700,701), (701,702), (702,703), (703,704), (704,705), (705,706), (706,707), (707,708), (708,709), (709,712), (712,715), (715,718), (718,721), (721,724), (724,727), (727,730), (730,733), (733,736), (736,739), (739,742), (742,745), (745,748), (748,751), (751,754), (754,757), (757,760), (760,763), (763,766), (766,769), (769,772), (772,775), (775,778), (778,781), (781,784), (784,787), (787,790), (790,793), (793,796), (796,799), (799,802), (802,805), (805,808), (808,811), (811,814), (814,817), (817,820), (820,823), (823,826), (826,829), (829,832), (832,835), (835,838), (838,841), (841,844), (844,847), (847,850), (850,853), (853,856), (856,859)]

colnames_infile = ['sitecode',  'sitename',  'sitetype',  'sitetypenum',  'year',  'survyear',  'weight',  'stratum',  'PSU',  'record',  'age',  'sex',  'grade',  'race4',  'race7',  'stheight',  'stweight',  'bmi',  'bmipct',  'qnobese',  'qnowt',  'q66',  'q65',  'sexid',  'sexid2',  'sexpart',  'sexpart2',  'q8',  'q9',  'q10',  'q11',  'q12',  'q13',  'q14',  'q15',  'q16',  'q17',  'q18',  'q19',  'q20',  'q21',  'q22',  'q23',  'q24',  'q25',  'q26',  'q27',  'q28',  'q29',  'q30',  'q31',  'q32',  'q33',  'q34',  'q35',  'q36',  'q37',  'q38',  'q39',  'q40',  'q41',  'q42',  'q43',  'q44',  'q45',  'q46',  'q47',  'q48',  'q49',  'q50',  'q51',  'q52',  'q53',  'q54',  'q55',  'q56',  'q57',  'q58',  'q59',  'q60',  'q61',  'q62',  'q63',  'q64',  'q67',  'q68',  'q69',  'q70',  'q71',  'q72',  'q73',  'q74',  'q75',  'q76',  'q77',  'q78',  'q79',  'q80',  'q81',  'q82',  'q83',  'q84',  'q85',  'q86',  'q87',  'q88',  'q89',  'qn8',  'qn9',  'qn10',  'qn11',  'qn12',  'qn13',  'qn14',  'qn15',  'qn16',  'qn17',  'qn18',  'qn19',  'qn20',  'qn21',  'qn22',  'qn23',  'qn24',  'qn25',  'qn26',  'qn27',  'qn28',  'qn29',  'qn30',  'qn31',  'qn32',  'qn33',  'qn34',  'qn35',  'qn36',  'qn37',  'qn38',  'qn39',  'qn40',  'qn41',  'qn42',  'qn43',  'qn44',  'qn45',  'qn46',  'qn47',  'qn48',  'qn49',  'qn50',  'qn51',  'qn52',  'qn53',  'qn54',  'qn55',  'qn56',  'qn57',  'qn58',  'qn59',  'qn60',  'qn61',  'qn62',  'qn63',  'qn64',  'qn67',  'qn68',  'qn69',  'qn70',  'qn71',  'qn72',  'qn73',  'qn74',  'qn75',  'qn76',  'qn77',  'qn78',  'qn79',  'qn80',  'qn81',  'qn82',  'qn83',  'qn84',  'qn85',  'qn86',  'qn87',  'qn88',  'qn89',  'qnfrcig',  'qndaycig',  'qnfrevp',  'qndayevp',  'qnfrcgr',  'qndaycgr',  'qntb2',  'qntb3',  'qntb4',  'qntb5',  'qniudimp',  'qnothhpl',  'qndualbc',  'qnbcnone',  'qnfr0',  'qnfr1',  'qnfr2',  'qnveg0',  'qnveg1',  'qnveg2',  'qnveg3',  'qnsoda1',  'qnsoda2',  'qnmilk1',  'qnmilk3',  'qnbk7day',  'qnpa0day',  'qnpa7day',  'qndlype',  'qnnodnt',  'qbikehelmet',  'qdrivemarijuana',  'qcelldriving',  'qpropertydamage',  'qbullyweight',  'qbullygender',  'qbullygay',  'qchokeself',  'qcigschool',  'qchewtobschool',  'qalcoholschool',  'qtypealcohol2',  'qhowmarijuana',  'qmarijuanaschool',  'qcurrentopioid',  'qcurrentcocaine',  'qcurrentheroin',  'qcurrentmeth',  'qhallucdrug',  'qprescription30d',  'qgenderexp',  'qtaughtHIV',  'qtaughtsexed',  'qtaughtstd',  'qtaughtcondom',  'qtaughtbc',  'qdietpop',  'qcoffeetea',  'qsportsdrink',  'qenergydrink',  'qsugardrink',  'qwater',  'qfastfood',  'qfoodallergy',  'qwenthungry',  'qmusclestrength',  'qsunscreenuse',  'qindoortanning',  'qsunburn',  'qconcentrating',  'qcurrentasthma',  'qwheresleep',  'qspeakenglish',  'qtransgender',  'qnbikehelmet',  'qndrivemarijuana',  'qncelldriving',  'qnpropertydamage',  'qnbullyweight',  'qnbullygender',  'qnbullygay',  'qnchokeself',  'qncigschool',  'qnchewtobschool',  'qnalcoholschool',  'qntypealcohol2',  'qnhowmarijuana',  'qnmarijuanaschool',  'qncurrentopioid',  'qncurrentcocaine',  'qncurrentheroin',  'qncurrentmeth',  'qnhallucdrug',  'qnprescription30d',  'qnillict',  'qngenderexp',  'qntaughtHIV',  'qntaughtsexed',  'qntaughtstd',  'qntaughtcondom',  'qntaughtbc',  'qndietpop',  'qncoffeetea',  'qnsportsdrink',  'qnspdrk1',  'qnspdrk2',  'qnenergydrink',  'qnsugardrink',  'qnwater',  'qnwater1',  'qnwater2',  'qnwater3',  'qnfastfood',  'qnfoodallergy',  'qnwenthungry',  'qnmusclestrength',  'qnsunscreenuse',  'qnindoortanning',  'qnsunburn',  'qnconcentrating',  'qncurrentasthma',  'qnwheresleep',  'qnspeakenglish',  'qntransgender']

variables = ["sitecode", "year","survyear", "weight", "stratum", "PSU", "age", "q19", "q20", "q21", "q22", "qtaughtsexed", "qtaughtstd", "qtaughtcondom", "qtaughtbc", "qn19", "qn20", "qn21", "qn22", "qntaughtsexed", "qntaughtstd", "qntaughtcondom", "qntaughtbc"]

###########################
# READING IN INITIAL FILE #
###########################

survey_am = pd.read_fwf(infile_a_m_str, colspecs=colspecs_infile,header=None)
survey_nz = pd.read_fwf(infile_n_z_str, colspecs=colspecs_infile,header=None)

# change column names 
survey_am.columns = colnames_infile
survey_nz.columns = colnames_infile

########################
# SUBSET + APPEND DATA #
########################

# keep relevant variables 
survey_am_subset = survey_am[variables]
survey_nz_subset = survey_nz[variables]

# append dataframes to each other 

outfile = pd.concat([survey_am_subset, survey_nz_subset])

print(outfile.head())

####################
# WRITE FINAL FILE #
####################

outfilestr = output_loc + "etl_5_yrbs.csv"
outfile.to_csv(outfilestr)