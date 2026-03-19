# 📊 Trader Performance vs Market Sentiment Analysis

## Objective
This project analyzes how market sentiment (Fear vs Greed) influences trader behavior and performance on Hyperliquid. The goal is to uncover patterns that can inform better trading strategies and decision-making.

---

## 📁 Folder Structure

Primetrade/
├── primetrade.ipynb   # Data preparation, analysis, insights
├── app.py             # Streamlit dashboard
└── README.md          # Documentation

---

##  Data Preparation (Part A)

- Loaded both datasets and inspected structure, missing values, and duplicates
- Converted timestamps into datetime format
- Aligned datasets using **nearest timestamp matching (`merge_asof`)** due to non-overlapping date ranges
- Extracted daily date for aggregation

### Feature Engineering:
- Created **sentiment groups**:
  - Greed / Extreme Greed → Greed
  - Others → Fear
- Created **win indicator**:
  - Profit > 0 → Win
- Computed key metrics:
  - Daily PnL
  - Win rate
  - Average trade size
  - Trade frequency (per day)
  - Long/Short distribution

### ⚠️ Note on Leverage
Leverage data was not available in the dataset.  
**Trade size (Size USD) was used as a proxy for risk exposure** to approximate leverage-related behavior.

---

## 📊 Methodology

The analysis focuses on comparing trader performance and behavior under different market sentiment conditions.

Approach:
1. Align sentiment data with trades
2. Aggregate metrics at sentiment level
3. Compare performance and behavior
4. Segment traders based on activity and risk
5. Derive actionable insights

---

## 📈 Analysis & Insights (Part B)

### 🔹 1. Performance vs Sentiment

- Traders show **higher average PnL during Greed periods**
- Greed also introduces **higher volatility (risk)**
- Fear periods result in **lower returns and more consistent losses**

**Insight**:  
Market sentiment directly impacts profitability and risk profile.

---

### 🔹 2. Behavioral Changes

#### Trade Frequency
- Higher during Greed → aggressive trading
- Lower during Fear → cautious behavior  

#### Position Size (Risk Proxy)
- Larger during Greed → higher risk-taking  
- Smaller during Fear → conservative strategy  

#### Long vs Short Bias
- Stronger **long bias during Greed**
- More balanced positioning during Fear  

**Insight**:  
Traders adapt behavior based on sentiment—becoming risk-seeking in Greed and defensive in Fear.

---

### 🔹 3. Trader Segmentation

#### High vs Low Risk (Size USD Proxy)
- High-risk traders:
  - Higher returns but larger losses  
- Low-risk traders:
  - More stable performance  

#### Frequent vs Infrequent Traders
- Frequent traders:
  - Higher activity but not consistently better performance  
- Infrequent traders:
  - More stable outcomes  

 **Insight**:  
Higher activity and risk do not guarantee better performance.

---

## 💡 Actionable Strategies (Part C)

### 🔹 Strategy 1: Risk Control Based on Sentiment
- Reduce position size by 30-50% during Fear 
- Avoid aggressive trading  
- Focus on capital preservation  

 Rule:  
> During Fear periods, traders should reduce risk exposure and limit trade frequency to minimize drawdowns.

---

### 🔹 Strategy 2: Control Overtrading During Greed
- Limit number of trades despite favorable conditions  
- Maintain disciplined execution  
- Avoid impulsive decisions  

 Rule:  
> During Greed periods, traders should control trade frequency and maintain consistent position sizing to prevent overtrading losses.

---

## 📊 Output (Charts & Tables)

The following visualizations were generated:

- PnL distribution (Fear vs Greed)
- Average trade size comparison
- Trade frequency comparison
- Long vs Short distribution

### 🖼️ Sample Outputs

#### PnL Distribution
<img width="449" height="535" alt="image" src="https://github.com/user-attachments/assets/dcb6afdf-6b70-41a1-a0e9-dd031f3858e5" />


#### Average Trade Size
<img width="462" height="546" alt="image" src="https://github.com/user-attachments/assets/fb2dbdcd-8e44-4851-a28a-df1d3e574d09" />


#### Average trades per day
<img width="435" height="507" alt="image" src="https://github.com/user-attachments/assets/1efb8718-5df5-474e-a86a-303fd926651b" />


#### Long vs Short
<img width="480" height="558" alt="image" src="https://github.com/user-attachments/assets/16da0d82-4cce-41cf-9877-c8937f9a9cb9" />


---

## 🖥️ Streamlit Dashboard

An interactive dashboard was built to explore results.

### Features:
- Sentiment-based filtering
- Key metrics (PnL, trade size, trade count)
- Visualizations for behavior analysis
- Data preview

### 🖼️ Dashboard Preview

<img width="920" height="692" alt="image" src="https://github.com/user-attachments/assets/047a98e2-3f9a-4cf5-b994-bbc5702ef327" />


---

## ⚙️ Setup & How to Run

### 1. Install Libraries
Make sure Python is installed, then run:

pip install pandas numpy matplotlib seaborn streamlit scikit-learn

---

### 2. Download Datasets

- Bitcoin Market Sentiment  
https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing  

- Historical Trader Data  
https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing  

---

### 3. Run Notebook

Open and run:

Primetrade.ipynb

This will generate:
merged.csv

---

### 4. Run Dashboard

In terminal, run:

streamlit run app.py

---

### 5. Open in Browser

http://localhost:8501

---

## 📊 Dashboard

- Select view: All / Greed / Fear  
- View charts:
  - PnL by Sentiment
  - Average Trade Size
  - Average Trades per Day
  - Long vs Short 

---
