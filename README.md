# Health-Fitness-Tracker-Dashboard

# Project Overview
This project provides an end-to-end pipeline for preparing a fitness dataset, cleaning it, and presenting it through a fully interactive analytics dashboard.
It includes:

A data-cleaning notebook (Cleaning.ipynb)
A Streamlit dashboard application (Dashboard.py)
The raw dataset used for analysis(Fitness.csv)
The cleaned dataset (cleaned_data.csv) generated after preprocessing

The goal is to ensure a clean dataset and provide an intuitive interface to explore fitness-related metrics such as BMI, workout types, session duration, calories burned, and more.

# Objectives
## Data Cleaning — Cleaning.ipynb
Load the raw dataset
Inspect structure, data types, and missing values
Fix invalid or inconsistent entries
Remove duplicates and zero-value anomalies
Standardize categorical columns
Prepare final clean dataset: cleaned_data.csv

## Dashboard — Dashboard.py
Provide sidebar filters (Gender, Workout Type, Experience, Age Range)
Display summary metrics (Average BMI, Resting BPM, Water Intake)
Visualize patterns using interactive charts
Offer a BMI calculator with category interpretation
Allow users to download their BMI report as CSV

# Data Processing Summary (Cleaning.ipynb)
1. Load Dataset
The notebook reads the raw fitness dataset provided by the user.
2. Data Inspection
Missing values
Zero or out-of-range values
Inconsistent text in categorical fields
Duplicated rows
3. Data Cleaning Steps
Replace/handle missing values
Normalize text (Gender, Workout Type, Experience Level)
Fix unrealistic values (like Age = 0, Height = 0, etc.)
Remove duplicate rows
Reformat numeric columns
4. Export
The final cleaned dataset is saved as:
cleaned_data.csv
This cleaned file is required for the dashboard.

# Dashboard Application Summary (Dashboard.py)
The dashboard contains two pages:
## Fitness Analysis Page
1.Filters Available
2.Gender
3.Workout Type
4.Experience Level
5.Age Range Slider
6.All charts update instantly based on selections.
7.KPIs Shown
8.Average BMI
9.Average Resting BPM
10.Average Water Intake
11.Charts Included
12.Workout Distribution by Age (Horizontal Bar Chart)
13.Workout Type Distribution by Gender (Side-by-Side Pie Charts)
14.Calories Burned vs Duration (Line Chart)
15.Most Popular Workouts (Horizontal Popularity Bar Chart)
16.Experience Level Breakdown (Donut Chart)
17.Data Table
18.Filtered dataset is shown as an interactive table.

## BMI Calculator Page
Allows users to:
Enter name, age, height, and weight
Automatically compute BMI
Receive category feedback:
Underweight
Normal
Overweight
Obese
Download results as CSV
View results in table format

# Requirements
## Install required libraries:
pandas
numpy
plotly
streamlit
matplotlib

# How to Run
Step 1: Run Cleaning Notebook
Open Cleaning.ipynb
Run all cells
Ensure cleaned_data.csv is generated in the same directory
Step 2: Launch the Dashboard
Run: streamlit run Dashboard.py

# Results Produced
## From Cleaning.ipynb
Clean, well-structured CSV file
Summary of cleaned values
A dataset ready for visualization

## From Dashboard.py
Interactive charts
KPI comparison
Age-, gender-, and workout-based insights
Downloadable BMI report
Clean UI for exploring fitness data

# Conclusion
## This project demonstrates a complete, reproducible workflow:
Data Cleaning
Preprocessing
Interactive Visualization
User-Friendly Fitness Tools
