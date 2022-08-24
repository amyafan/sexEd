# sexEd

looking at the relationship between state sex ed policies and public health outcomes

*Created by Amy Fan (<amy.a.fan@gmail.com>)*

*Reporter: Amy Fan (<amy.a.fan@gmail.com>)*

## Project goal

Do states with more restrictive sex ed curriculum or laws have worse public health outcomes (Like teen pregnancy or HIV/STDs) 

## Data sources


### /source

* **NCHS\_-\_U.S.\_and\_State\_Trends\_on\_Teen\_Births.csv**
    * Teen births by state
    * [Source](https://www.cdc.gov/nchs/data-visualization/teen-births/index.htm) 
* **Natality, 2016-2020 expanded.txt**
    * Teen births by state, only has fertility rates for Hispanic or Latino, any race
    * queried from [CDC Wonder](https://wonder.cdc.gov/controller/datarequest/D149)
* **Natality, 2016-2020 expanded(1).txt**
    * Teen births by state and race, (not Hispanic or Latino)
    * queried from [CDC Wonder](https://wonder.cdc.gov/controller/datarequest/D149), 
* **AtlasPlusTableData.csv**
    * HIV/STD rates by state
    * queried from [AtlasPlus](https://www.cdc.gov/nchhstp/atlas/index.htm)
    * The specific queries are at the top of the file
* **AtlasPlusTableData(1).csv**
    * HIV/STD rates by state and race 
    * queried from [AtlasPlus](https://www.cdc.gov/nchhstp/atlas/index.htm)
    * The specific queries are at the top of the file. 
    
* ****
https://www.cdc.gov/healthyyouth/data/yrbs/data.htm

* ****
https://www.cdc.gov/healthyyouth/data/yrbs/data.htm


### /manual 

* **Sex_Ed_Policy.csv**
    * Tracking sex ed policies
    * Taken almost exclusively from the [SIECUS 2022 Sex Ed State Law and Policy Chart](https://siecus.org/wp-content/uploads/2021/09/2022-04-Sex-Ed-State-Law-and-Policy-Chart.pdf)
    * The sex ed req and consent req columns were both manually edited after an email conversation with SIECUS where they pointed out the following differences (the state chart was only updated after **all** state legislatures were done, as opposed to the state profiles, which were updated more frequently) 
        1) The Scripps chart lists California as requiring instruction on consent, however the state profile reads: "Curriculum is not required to include instruction on consent. However, curriculum must include instruction that provides students with “knowledge and skills they need to form healthy relationships that are based on mutual respect and affection, and are free from violence, coercion, and intimidation.” The updated Health Education Curriculum Framework also includes instruction on affirmative consent."
        2) It does not list Maine or Rhode Island as requiring consent. According to their SIECUS state profiles, both do.  
        3) South Carolina is listed as requiring consent, according to the SIECUS South Carolina state profile, it does not. 
        4) Florida is listed as requiring sex education, but the SIECUS Florida profile says it does not require sex education, rather that schools are required to teach comprehensive health education that includes instruction on teenage pregnancy.
        5) Texas is listed as requiring sex education, but the SIECUS Texas profile says it does not require sex education.
        6) Virginia is listed as not requiring sex education, but the SIECUS Texas profile says it does require sex education.

### /processed

* **etl_1_preg_state.csv**
    * teen births by state
* **etl_2_HIV_STD_state.csv**
    * HIV/STDs by state
* **etl_3_preg_state_race.csv**
    * teen births by state and race/ethnicity
* **etl_4_HIV_STD_state_race.csv**
    * HIV/STDs by state and race/ethnicity

## Data notes

CDC data is from 2019 because the pandemic affected the quality of 2020 and 2021 data. 