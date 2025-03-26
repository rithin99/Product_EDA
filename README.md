Product_EDA - Exploratory Data Analysis with Python and Power BI
-Project Overview
This project involves performing an Exploratory Data Analysis (EDA) on a product sales dataset. The goal is to clean and analyze the data to derive meaningful insights using Python and visualize the results using Power BI.

-Project Structure

Product_EDA/
├── data/
│   ├── sales_data.csv
│   ├── stores_data.csv
│   ├── features_data.csv
│   ├── processed_merget_dataset
├── notebooks/
│   ├── EDA_sales_data.ipynb
├── src/
│   ├── __init__.py
│   ├── data_load.py
│   ├── eda.py
│   ├── utils.py
├── reports/
│   ├── visual_reports.pbix
│   ├── summary_statistics
│   ├── datasets_info
├── README.md
└── requirements.txt

-Getting Started

Prerequisites
Ensure the following are installed:

Python 3.10+

Power BI Desktop

Jupyter Notebook

Git

Installation
Clone the repository:

git clone https://github.com/rithin99/Product_EDA.git
cd Product_EDA

Set up the virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

- Data Overview

The project uses three datasets:

Sales Data: Contains store-wise sales information, including weekly sales and dates.

Stores Data: Contains information about each store, including store type and size.

Features Data: Includes additional economic indicators like CPI, fuel price, and unemployment rate.

-EDA Process
The analysis follows these steps:

Data Loading: Load and explore data for initial understanding.

Data Cleaning: Handle missing values, outliers, and data type conversions.

Data Merging: Combine datasets for better analysis.

EDA & Visualization: Perform statistical analysis and visualize trends.

-Visualizations
The project visualizes:

Sales Distribution: Using histograms to understand sales distribution.

Store-wise Sales: Using bar charts and pie charts.

Trend Analysis: Using line charts to observe sales trends over time.

Sales vs. Store Size: Using scatter plots to analyze the relationship.

All visualizations are available in the Power BI dashboard (visual_reports.pbix).

How to Run
Run the Jupyter notebook:

run command from gitbash
jupyter notebook

Open and execute:

EDA_sales_data.ipynb 

Open Power BI:

Load the visual_report.pbix.

Review and interact with the reports.

-Key Insights
Some findings include:

Seasonal trends in sales during holidays.

Higher sales in larger stores.

Impact of economic factors like CPI and fuel price on sales.

-Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a branch (git checkout -b feature/your-feature).

Commit your changes (git commit -m "Add new feature").

Push to the branch (git push origin feature/your-feature).

Open a Pull Request.

-License
This project is licensed under the MIT License. See LICENSE for more information.

-Contact
Author: Rithin Varghese

GitHub: rithin99

Email: rithintoch@gmail.com