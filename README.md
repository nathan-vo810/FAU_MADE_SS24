[![CC BY 4.0][cc-by-shield]][cc-by-4]

# Correlation Between Renewable Energy Consumption and CO2 Emissions in various countries

## Introduction
The combustion of fossil fuels such as coal, petroleum, and natural gas emits a significant amount of carbon dioxide (CO2), which is the largest contributor to greenhouse gases and global warming. To mitigate climate change, many countries are transitioning from fossil fuels to renewable, sustainable energy sources like solar and wind. This project aims to analyze global renewable energy consumption and assess its influence on CO2 emissions, exploring how renewable energy supports the fight against climate change. 

### Research Question
What is the correlation between renewable energy consumption and CO2 emissions in various countries?

## Data Sources
The data used in this analysis includes:

- **CO2 Emission Data:**
  - **Geographical Coverage:** 266 countries/associations
  - **Temporal Coverage:** 1990 - 2020
  - **Unit:** kt
  - **License:** [CC BY-NC 4.0][cc-by-nc-4]
  - **Source:** Climate Watch – Historical GHG Emissions (1990–2020)
  - **Provider:** [The World Bank][co2]

- **Renewable Energy Consumption Data:**
  - **Geographical Coverage:** 266 countries/associations
  - **Temporal Coverage:** 1990 - 2021
  - **Unit:** % of total final energy consumption
  - **License:** [CC BY-4.0][cc-by-4]
  - **Source:** IEA, IRENA, UNSD, World Bank, WHO (2023 Tracking SDG 7: The Energy Progress Report)
  - **Provider:** [The World Bank][rnew]

### Data Adaptation and Changes
- The time period for the Renewable Energy Consumption dataset is set to 1990 – 2020.
- Countries/associations without records have been excluded.
- Only countries/associations present in both datasets are selected.
- Missing values are filled using the first available value for each country/association.

### Final Dataset
- The final datasets encompass 236 countries and associations from 1990 – 2020.
- These datasets are stored in 2 tables within an SQLite database, saved locally.

## Analysis
The analysis follows a structured approach to examine the correlation between CO2 emissions and renewable energy consumption from 1990 to 2020. Key points include:

- **Global CO2 Emissions Trends:** 
  - Steady increase from 1990 to 2020, with a significant rise of 57.7% and a modest decline of about 5% towards the end of the period.
  
- **Global Renewable Energy Consumption Trends:**
  - Steady increase in renewable energy consumption, with noticeable fluctuations and a sharp rise towards 2020.
  
- **Top CO2 Emitters:**
  - Approximately 60% of global CO2 emissions originate from 10 countries, with China and the United States being the largest contributors.
  
- **Renewable Energy Consumption in Top Emitters:**
  - Significant decline in renewable energy consumption in China and India, while other top emitters showed a steady increase.

- **Countries with Largest CO2 Reductions:**
  - Estonia, Ukraine, Moldova, Lithuania, and Romania show significant increases in renewable energy usage and substantial decreases in CO2 emissions.
  
- **Emissions and Renewable Energy by Income Group:**
  - Middle-income countries have seen a significant rise in CO2 emissions, surpassing high-income countries.
  - Low-income countries lead in renewable energy consumption, while high-income countries show the lowest renewable energy usage.

## Conclusion
The correlation between renewable energy consumption and CO2 emissions varies significantly across different countries and economic groups. While global trends indicate an increase in renewable energy adoption and a beginning decline in CO2 emissions, other factors such as regulations and technologies may play more significant roles in limiting CO2 emissions. Further investigation into renewable energy output, country-specific regulations, and advanced energy technologies is necessary to answer the research question more definitively.

## License
This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by-4].

[![CC BY 4.0][cc-by-image]][cc-by-4]

[cc-by-4]: https://creativecommons.org/licenses/by/4.0/
[cc-by-nc-4]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
[co2]: https://data.worldbank.org/indicator/EN.ATM.CO2E.KT
[rnew]: https://data.worldbank.org/indicator/EG.FEC.RNEW.ZS
