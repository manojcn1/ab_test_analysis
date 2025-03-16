# ab_test_analysis
This repository contains a comprehensive A/B testing analysis where I evaluate the performance of a new marketing campaign using real-world data science techniques
This project analyzes an A/B test conducted to measure the effectiveness of a new marketing campaign compared to the existing one. Using data science techniques, we evaluate whether the new campaign drives higher conversion rates and revenue per user.

The analysis covers data preprocessing, exploratory data analysis (EDA), statistical testing, and business insights, providing a data-driven recommendation on whether to adopt the new campaign.

📂 Project Structure
📁 Data Files:
ab_testing_dataset.csv → Raw dataset with imperfections (missing values, duplicates)
ab_test_analysis.ipynb → Jupyter Notebook with full A/B test analysis

📁 Project Documentation:
README.md → This documentation

🔹 Dataset Details
The dataset contains user interactions with two marketing campaigns:

Group A (Control) → Users exposed to the existing campaign
Group B (Treatment) → Users exposed to the new campaign

🔢 Features in the Dataset
Column	Description
User_ID	Unique identifier for each user
Group	A (Control) or B (Treatment)
Impressions	Number of times the ad was shown
Clicks	Number of times the ad was clicked
Conversions	Whether the user converted (1 = Yes, 0 = No)
Revenue	Revenue generated per user
Timestamp	Date and time of interaction


📊 Analysis Workflow

1️⃣ Data Cleaning & Preprocessing
Handled missing values (e.g., missing clicks, conversions)
Identified duplicate rows and removed inconsistencies
Created new features for deeper insights

2️⃣ Exploratory Data Analysis (EDA)
Visualized conversion rates & revenue trends
Compared Click-Through Rate (CTR) and Conversion Rate (CR) for A vs. B
Checked for seasonality trends in user behavior

3️⃣ Hypothesis Testing: Is the New Campaign Better?
Chi-Square Test → Did the new campaign significantly improve conversion rates?
T-Test → Is the revenue per user significantly different between A & B?
Lift Calculation → By what percentage did the new campaign improve performance?

4️⃣ Business Recommendation
Should the company switch to the new campaign, or keep the existing one?
Interpreted results beyond statistics to guide real-world decision-making.
