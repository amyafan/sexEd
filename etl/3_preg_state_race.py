"""
Amy Fan 7-2022

ETL for teen births by state and by race

input:
_____

~/data/source/Natality, 2016-2020 expanded.txt

    fertility rates for Hispanic or Latino, any race 


~/data/source/Natality, 2016-2020 expanded(1).txt

    fertility rates for all races, not Hispanic or Latino
    
    

output:
______

~/data/processed/3_preg_state_race.csv

    cleaned data on teen birth rates for 2019 by state and race 

"""

import pandas as pd
import numpy as np

input_loc = "data//source//"
output_loc = "data//processed//"

#######################
# READING IN THE FILE #
#######################

# Just hispanic/latino
infilestr1 = input_loc + "Natality, 2016-2020 expanded.txt"
df1 = pd.read_csv(infilestr1, sep = "\t", nrows = 50) 


# all races, non-hispanic/latino
infilestr2 = input_loc + "Natality, 2016-2020 expanded(1).txt"
df2 = pd.read_csv(infilestr2, sep = "\t", nrows = 213) 

#############
# FILTERING #
#############

# keeping only relevant columns + rename columns so there's a combined race/ethnicity column
hl = df1[["State of Residence", "Mother's Hispanic Origin", "Fertility Rate"]]
hl.columns = ["State", "Race/Ethnicity", "Fertility Rate"]

others = df2[["State of Residence", "Mother's Single Race 6", "Fertility Rate"]]
others.columns = ["State", "Race/Ethnicity", "Fertility Rate"]


# concatenate the two files together
outfile = pd.concat([hl, others])

##########
# EXPORT #
##########

outfilestr = output_loc + "etl_3_preg_state_race.csv"
outfile.to_csv(outfilestr)