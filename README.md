# Real Estate Consulting Project

## Team members:
• Ngoc Minh Pham - 1312628
• Ngoc Minh Vu - 
• Duy Thinh Tran - 
• Khanh Nam Nguyen - 
• Tung Lam Le - 

## Research Goal:
• Predict rental price in Victoria, and decide the most important features for prediction

• Predict top 10 suburbs with highest median rental price in Victoria for 2025, 2026 and 2027

• Suggest most liveable and affordable suburbs in Victoria 

## Datasets:
• Rental properties dataset acquired from scraping *domain.com.au*

• Historical dataset acquired from *Department of Families, Fairness and Housing*

• GDA2020 shapefile acquired from *data.gov.au*

• PTV 

• Population

• Australian postcodes 


## Project Pipeline:
1. Run the `m_scrape.py` in `scripts` to scrape data from *domain.com.au*
2. Run the `preprocess_current_rent.ipynb` in `notebooks` to preprocess the scraped rental data for modelling 
3. Run the `point_of_interest.ipynb` in `notebooks` to add features about transportations, shops and hospitals
4. Run the ` ` in `notebooks` to add features about income, migrants, jobs and estimated resident populations
5. Run the `historical_rent.ipynb` in `notebooks` to extract historical rental data for visualisation and records of individual suburbs
6. Run the `predict.ipynb` in `notebooks` to run the models for rental price predictions and future median rental price predictions

## Visualisation:
1. Run `poi_visualisation` in `notebooks` for *points of interest* geospatial visualisation, plots can be found in `point_of_interest` in `plots`
2. Geospatial visualisation for *median rental prices in March 2024* can be found in `march 2024 median` in `plots`
3. Geospatial visualisation for *estimated resident populations* and  can be found in `erp`, `erp_per_km2` and `erp_increase` in `plots`
4. Geospatial visualisation for *income across suburbs* and *jobs accross suburbs* can be found in `income` and `jobs` in `plots`
5. Geospatial visualisation for *migrants across suburbs* can be found in `net_migrants` in `plots`
6. Geospatial visualisation for ** can be found in `area` in `plots`
