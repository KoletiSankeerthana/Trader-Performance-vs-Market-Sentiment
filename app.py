import streamlit as st
import pandas as pd

# -------------------------------
# LOAD DATA
# -------------------------------
merged = pd.read_csv(r"C:\Users\saipa\Downloads\merged.csv")

# -------------------------------
# TITLE
# -------------------------------
st.title("📊 Trader Behavior Dashboard")

# -------------------------------
# PREPROCESSING
# -------------------------------
merged['sentiment_group'] = merged['classification'].astype(str).apply(
    lambda x: 'Greed' if 'Greed' in x else 'Fear'
)

merged['date'] = pd.to_datetime(merged['Timestamp']).dt.date

# -------------------------------
# FILTER
# -------------------------------
st.sidebar.header("Filter")
selected_sentiment = st.sidebar.selectbox(
    "Select Sentiment",
    merged['sentiment_group'].unique()
)

filtered = merged[merged['sentiment_group'] == selected_sentiment]

# -------------------------------
# KPI SECTION
# -------------------------------
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg PnL", round(filtered['Closed PnL'].mean(), 2))
col2.metric("Avg Trade Size", round(filtered['Size USD'].mean(), 2))
col3.metric("Total Trades", len(filtered))

# -------------------------------
# PnL
# -------------------------------
st.subheader("📈 PnL by Sentiment")
pnl = merged.groupby('sentiment_group')['Closed PnL'].mean()
st.bar_chart(pnl)

st.write("Insight: Greed periods show higher profitability but also increased volatility compared to Fear periods.")

# -------------------------------
# TRADE SIZE (RISK)
# -------------------------------
st.subheader("💰 Average Trade Size (Risk Proxy)")
size = merged.groupby('sentiment_group')['Size USD'].mean()
st.bar_chart(size)

st.write("Insight: Traders take larger positions during Greed periods, indicating higher risk-taking behavior.")

# -------------------------------
# TRADE FREQUENCY
# -------------------------------
st.subheader("🔁 Average Trades per Day")
freq = merged.groupby(['sentiment_group', 'date']).size().reset_index(name='trades')
freq_avg = freq.groupby('sentiment_group')['trades'].mean()

st.bar_chart(freq_avg)

st.write("Insight: Trade frequency increases during Greed periods, suggesting overconfidence and aggressive trading.")

# -------------------------------
# LONG VS SHORT
# -------------------------------
st.subheader("⚖️ Long vs Short Positions")
bias = pd.crosstab(merged['sentiment_group'], merged['Side'])
st.bar_chart(bias)

st.write("Insight: Traders show a stronger long bias during Greed periods, while Fear periods show more balanced positioning.")

# -------------------------------
# DATA PREVIEW
# -------------------------------
st.subheader("🔍 Data Preview")
st.dataframe(filtered.head(20))