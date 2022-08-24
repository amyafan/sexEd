"""
Amy Fan 7-2022

ETL for HIV_STD by state

input:
_____

~/data/source/AtlasPlusTableData.csv

    State level data on HIV/STDs

output:
______

~/data/processed/2_HIV_STD_state.csv

    cleaned data on HIV_STD rates for 2019 by state for people 13-24 

"""

import pandas as pd
import numpy as np

input_loc = "data//source//"
output_loc = "data//processed//"

#######################
# READING IN THE FILE #
#######################

infilestr = input_loc + "AtlasPlusTableData.csv"
df = pd.read_csv(infilestr, header = 8) 

# Get rid of \^ in state names
df.Geography = df.Geography.str.replace("\^", "")

#############
# RESHAPING #
#############

pivot =  pd.pivot_table(df, values='Rate per 100000', index=['Geography'], columns=['Indicator'], aggfunc=np.sum)

# replace "data suppressed" with nan value and convert column to float 
outfile = pivot.replace("Data suppressed", np.nan).astype(float)

##########
# EXPORT #
##########

outfilestr = output_loc + "etl_2_HIV_STD_state.csv"
outfile.to_csv(outfilestr)