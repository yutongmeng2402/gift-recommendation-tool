# Gift Retail Interactive Recommendation Tool

## Project Overview
This interactive Streamlit application helps a gift and collectibles retail company segment customers using the RFM model and recommend optimal product bundles to maximize customer willingness to pay.

**Target Audience**: Retail managers and marketing teams looking for data-driven bundling and promotion strategies.

## How to Run the App
1. Clone or download this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
Run the application: 
   ```bash
   streamlit run app.py

## Data Source

Dataset: UCI Online Retail Dataset (real transaction records from a UK-based online gift retailer, 2010–2011)
Access Date: 20 April 2026
Link: https://www.kaggle.com/datasets/mysarahmadbhat/customersegmentation
Note: The original dataset (~40MB) is not uploaded to this repository due to size limit. Only the processed recommendations.csv is included.

## Key Features

RFM-based customer segmentation (4 segments)
Personalized product bundle recommendations
Before-After revenue impact visualization
Business insights for each customer segment

## Repository Structure

app.py – Main Streamlit interactive tool
online_retail_analysis.ipynb – Full data analysis workflow
recommendations.csv – Pre-computed recommendations
requirements.txt – Required Python packages

## Technologies

Python, Pandas
Streamlit (interactive dashboard)
Plotly (visualization)

## Demo Video

Watch the demo video
https://b23.tv/fLap3rb

## Author

[Yutong Meng]
ACC102 Mini Assignment – Track 4
Xi'an Jiaotong-Liverpool University
