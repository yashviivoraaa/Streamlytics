import streamlit as st
import pandas as pd
import glob
import time

# Wide layout
st.set_page_config(layout="wide")

# Page title
st.markdown("<h1 style='text-align: center; color: white;'>📊 CFPB Live Streaming Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# Placeholders for charts
product_placeholder = st.empty()
company_placeholder = st.empty()
channel_placeholder = st.empty()

while True:
    try:
        # --- Product-Level Dashboard ---
        folder = "dashboard_output/agg.csv"
        part_files = glob.glob(f"{folder}/part-*.csv")

        if part_files:
            df_product = pd.read_csv(part_files[0])
            with product_placeholder.container():
                st.markdown("### 📦 Live Complaint Count by Product")
                st.bar_chart(df_product.set_index("product")["count"])
                st.markdown("---")
        else:
            product_placeholder.warning("Waiting for product data...")

        # --- Company & Channel Dashboards ---
        stream_files = sorted(glob.glob("streaming_data/data_*.json"))
        if stream_files:
            dfs = [pd.read_json(f, lines=True) for f in stream_files]
            df_all = pd.concat(dfs, ignore_index=True)

            # Company Chart
            company_counts = df_all["company"].value_counts().head(10).reset_index()
            company_counts.columns = ["company", "count"]
            with company_placeholder.container():
                st.markdown("### 🏢 Top Companies by Complaint Volume")
                st.bar_chart(company_counts.set_index("company"))
                st.markdown("---")

            # Submission Method Chart
            if "submitted_via" in df_all.columns:
                via_counts = df_all["submitted_via"].value_counts().reset_index()
                via_counts.columns = ["submitted_via", "count"]
                with channel_placeholder.container():
                    st.markdown("### 📨 Complaint Submission Methods")
                    st.bar_chart(via_counts.set_index("submitted_via"))
                    st.markdown("---")
            else:
                channel_placeholder.warning("submitted_via column not available.")
        else:
            company_placeholder.warning("Waiting for streamed JSON data...")
            channel_placeholder.warning("Waiting for streamed JSON data...")

        time.sleep(5)

    except Exception as e:
        st.error(f"Error updating dashboards: {e}")
        time.sleep(5)
