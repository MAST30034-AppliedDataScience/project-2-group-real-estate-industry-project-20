# Real Estate Consulting Project

## Team members:
• Ngoc Minh Pham - 1312628

• Ngoc Minh Vu - 1375708

• Duy Thinh Tran - 1369324

• Khanh Nam Nguyen - 1367184

• Tung Lam Le - 1374374


## Research Goal:
• Predict rental price in Victoria, and decide the most important features for prediction

• Predict top 10 suburbs with highest median rental price in Victoria for 2025, 2026 and 2027

• Suggest most liveable and affordable suburbs in Victoria.


## Project Pipeline:
0. Run the `requirements.txt` to install all the necessary libraries
1. Run the `m_scrape.py` in `scripts` to scrape data from *domain.com.au*
2. Run the `hospital_record` in `scripts` to get dataset for public hospital.
3. Run the `groceries_record` in `scripts` to get dataset for shop records.
4. Run the `preprocess_current_rent.ipynb` in `notebooks` to preprocess the scraped rental data for modelling
5. Obtain your API_KEY from openrouteservice `https://openrouteservice.org` to run the notebook below
6. Run the `point_of_interest.ipynb` in `notebooks` to add features about transportations, shops and hospitals
7. Run the `income.ipynb` then `population_and_migrants.ipynb` in `notebooks` to add features about income, migrants, jobs and estimated resident populations
8. Run the `historical_rent.ipynb` in `notebooks` to extract historical rental data for visualisation and records of individual suburbs
9. Run the `predict.ipynb` in `notebooks` to run the models for rental price predictions and future median rental price predictions


## Visualisation:
1. Run `poi_visualisation` in `notebooks` for *points of interest* geospatial visualisation, plots can be found in `point_of_interest` in `plots`
2. Geospatial visualisation for *median rental prices in June 2024* can be found in `june 2024 median` in `plots`
3. Geospatial visualisation for *estimated resident populations* and  can be found in `erp`, `erp_per_km2` and `erp_increase` in `plots`
4. Geospatial visualisation for *income across suburbs* and *jobs accross suburbs* can be found in `income` and `jobs` in `plots`
5. Geospatial visualisation for *migrants across suburbs* can be found in `net_migrants` in `plots`
6. Geospatial visualisation for *suburbs' areas* can be found in `area` in `plots`

