# Streamlytics - CFPB Streaming Analytics Dashboard

A real-time analytics pipeline for monitoring Consumer Financial Protection Bureau (CFPB) complaint data using PySpark Structured Streaming and Streamlit.

---

## Overview

The Consumer Complaint Database published by the CFPB is a large, publicly available dataset containing complaints about financial products and services submitted by consumers across the United States.

This project builds a simulated real-time data pipeline on top of this dataset to demonstrate how streaming systems can process, aggregate, and visualize high-volume complaint data.

The system mimics a live ingestion environment and provides continuously updating insights through an interactive dashboard.

---

## Project Architecture

The project consists of three main components:

1. Streaming Simulator  
   Generates real-time data by reading a static dataset and emitting records in batches  

2. Streaming Processing Layer (PySpark)  
   Processes incoming data streams and performs aggregations in near real time  

3. Visualization Layer (Streamlit)  
   Displays continuously updating analytics through an interactive dashboard  

---

## Project Structure

├── simulate_stream.py
├── streaming_analysis.py
├── streamlit_app.py
├── cfpb_all_complaints.csv
├── labeled_narrative.csv
├── Project Report.pdf
├── streaming_data/            (generated during runtime)
└── dashboard_output/          (generated during runtime)

---

## Features

- Simulated real-time data ingestion from CFPB dataset  
- Streaming aggregation using PySpark Structured Streaming  
- Live dashboard updates using Streamlit  
- Product-level complaint analysis  
- Company-level complaint trends  
- Optional breakdown by submission channel  

---

## Tech Stack

- Python  
- PySpark Structured Streaming  
- Streamlit  
- Pandas  

---

## Dataset

The project uses the CFPB Consumer Complaint Database, which includes:

- Product type (e.g., credit card, loan, mortgage)  
- Complaint issue and sub-issue  
- Company name  
- Consumer complaint narrative  
- Submission method (web, phone, etc.)  
- Company response and resolution status  

This dataset is commonly used for analyzing consumer issues, financial trends, and company behavior.

---

## How It Works

### Step 1: Simulate Streaming Data

The simulator reads the dataset and writes records in small batches as JSON files to a streaming directory.

python simulate_stream.py

### Step 2: Run Streaming Aggregation

PySpark reads incoming data, performs aggregation (e.g., complaint count by product), and writes results to an output file.

python streaming_analysis.py

### Step 3: Launch Dashboard

The Streamlit app reads processed data and updates visualizations in real time.

streamlit run streamlit_app.py

---

## Output

The dashboard provides:

- Complaint count by product  
- Top companies receiving complaints  
- Complaint submission channel distribution  

---

## Use Cases

- Real-time complaint monitoring systems  
- Financial services analytics  
- Streaming data engineering demonstrations  
- Consumer behavior analysis  

---

## Future Improvements

- Integrate Kafka or real-time streaming sources  
- Store outputs in a database (e.g., PostgreSQL, BigQuery)  
- Add advanced aggregations (issue-level, time-series trends)  
- Improve dashboard interactivity and filtering  
- Deploy as a cloud-based analytics system  

---

## Author

Yashvi Vora
