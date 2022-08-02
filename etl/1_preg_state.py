"""
Amy Fan 7-2022

ETL for teen births by state

input:
_____

~/data/source/NCHS_-_U.S._and_State_Trends_on_Teen_Births.csv

    data from NCHS with teen birth data for each state for every year from 1990 - 2020


output:
______

~/data/processed/1_preg_state.csv

    cleaned data on teen birth rates for 2019 by state

"""

import pandas as pd
import numpy as np

input_loc = "data//source//"
output_loc = "data//processed//"

#######################
# READING IN THE FILE #
#######################

infilestr = input_loc + "NCHS_-_U.S._and_State_Trends_on_Teen_Births.csv"
df = pd.read_csv(infilestr) 

#############
# FILTERING #
#############

# only 2019 
df_2019 = df[df.Year==2019]

# only 15-19 
df_2019_age = df_2019[df_2019["Age Group (Years)"] == "15-19 years"]

# keep relevant columns
outfile = df_2019_age[["Year", "State", "Age Group (Years)", "State Rate", "State Births"]]

##########
# EXPORT #
##########

outfilestr = output_loc + "etl_1_preg_state.csv"
outfile.to_csv(outfilestr)