# Project Plan

## Title
<!-- Give your project a short title. -->
Assessing the relationship between renewable energy consumption and CO<sub>2</sub> emissions across nations

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
What is the correlation between the renewable energy consumpion and CO<sub>2</sub> emissions in various countries?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The combustion of fossil fuels such as coal, petroleum and natural gas emits a significant amount of carbon dioxide (CO<sub>2</sub>), account for the largest share of greenhouse gases, which are associated with global warming. In an attempt to reverse or at least mitigating climate change, many countries are shifting their main energy source away from fossil fuels and towards renewable, sustainable alternatives such as solar or wind energy. 

Consequently, this project aims to analyze the global consumption of renewable energy and assess its influence on the total CO<sub>2</sub> emissions, exploring how renewable energy supports in the fight against climate change. Additionally, the progress on adopting renewable energy across nations will also be compared.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource 1: CO2 emission (kt)
* Metadata URL: https://databank.worldbank.org/reports.aspx?source=2&type=metadata&series=EN.ATM.CO2E.KT
* Data URL: https://data.worldbank.org/indicator/EN.ATM.CO2E.KT
* Data Type: CSVs inside a ZIP archive

This dataset contains CO2 emissions across nations from 1990 - 2020.

### Datasource 2: Renewable energy consumption (% of total final energy consumption)
* Metadata URL: https://databank.worldbank.org/reports.aspx?source=2&type=metadata&series=EG.FEC.RNEW.ZS
* Data URL: https://data.worldbank.org/indicator/EG.FEC.RNEW.ZS
* Data Type: CSVs inside a ZIP archive

This dataset contains renewable energy consumption with regarding to total final energy consumption across nations from 1990 - 2021.

### Datasource 3: Renewable electricity output (% of total electricity output)
* Metadata URL: https://databank.worldbank.org/reports.aspx?source=2&type=metadata&series=EG.ELC.RNEW.ZS
* Data URL: https://data.worldbank.org/indicator/EG.ELC.RNEW.ZS
* Data Type: CSVs inside a ZIP archive

This dataset contains renewable electricy output with regarding to total electricity output across nations from 1990 - 2015.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Extract, Load, and Transform (ETL) of Datasets [#1][i1]
2. Data Cleaning and Preprocessing [#2][i2]
3. Exploratory Data Analysis (EDA) [#3][i3]
4. Correlation Analysis [#4][i4]
5. Report on Intepretations and Insights [#5][i5]

[i1]: https://github.com/nathan-vo810/FAU_MADE_SS24/issues/1
[i2]: https://github.com/nathan-vo810/FAU_MADE_SS24/issues/2
[i3]: https://github.com/nathan-vo810/FAU_MADE_SS24/issues/3
[i4]: https://github.com/nathan-vo810/FAU_MADE_SS24/issues/4
[i5]: https://github.com/nathan-vo810/FAU_MADE_SS24/issues/5
