
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Consumer Complaints Clustering Dashboard")

# Load Data
clusters_df = pd.read_csv("clustered_output.csv")
pca_df = pd.read_csv("pca_projection.csv")
sentiment_df = pd.read_csv("cluster_sentiment_summary.csv")
narratives_df = pd.read_csv("cluster_sentiment_narratives.csv")

# Cluster selection
cluster_list = sorted(clusters_df['cluster'].unique())
selected_cluster = st.sidebar.selectbox("Select Cluster", cluster_list)

# PCA Scatter Plot
st.subheader("PCA Cluster Projection")
fig_pca = px.scatter(pca_df, x="x", y="y", color=pca_df["cluster"].astype(str),
                     title="PCA Projection of Clusters")
st.plotly_chart(fig_pca)

# Top issues in selected cluster
st.subheader(f"Top Issues in Cluster {selected_cluster}")
filtered = clusters_df[clusters_df['cluster'] == selected_cluster]
top_issues = filtered['issue'].value_counts().nlargest(10).reset_index()
top_issues.columns = ["Issue", "Count"]
fig_issues = px.bar(top_issues, x="Issue", y="Count", title="Top Issues")
st.plotly_chart(fig_issues)

# Sentiment Breakdown
st.subheader("Sentiment Distribution")
sent_filtered = sentiment_df[sentiment_df['cluster'] == selected_cluster]
fig_sentiment = px.pie(sent_filtered, values='count', names='sentiment', title="Sentiment by Cluster")
st.plotly_chart(fig_sentiment)

# Sample narratives
st.subheader("Sample Complaint Narratives")
sample_narratives = narratives_df[narratives_df['cluster'] == selected_cluster].head(10)
st.write(sample_narratives[['complaint_what_happened', 'sentiment']])
