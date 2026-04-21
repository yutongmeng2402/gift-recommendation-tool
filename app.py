import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Gift Retail Recommendation Tool", layout="wide")

st.title("Gift Retail Interactive Recommendation Tool")
st.subheader("Recommend optimal product bundles to increase customer willingness to pay")

# Load recommendations
df_rec = pd.read_csv('recommendations.csv')

# Make sure column names are English
if '用户群体' in df_rec.columns:
    df_rec = df_rec.rename(columns={
        '用户群体': 'Customer Segment',
        '推荐商品组合': 'Recommended Bundle',
        '出现次数': 'Frequency',
        '平均支付金额': 'Average Payment Amount'
    })

st.sidebar.header("Filter")
selected_segment = st.sidebar.selectbox(
    "Select Customer Segment",
    options=sorted(df_rec['Customer Segment'].unique())
)

st.subheader(f"Recommended Bundles for {selected_segment}")

filtered = df_rec[df_rec['Customer Segment'] == selected_segment]

st.dataframe(
    filtered[['Recommended Bundle', 'Frequency', 'Average Payment Amount']],
    use_container_width=True,
    hide_index=True
)

st.subheader("Predicted Revenue Impact After Targeted Recommendation")

current_mean = filtered['Average Payment Amount'].mean()

uplift_rates = {
    "High Value Loyal Customers": 0.25,
    "Potential Customers": 0.20,
    "General Customers": 0.15,
    "Price Sensitive / New Customers": 0.10
}

rate = uplift_rates.get(selected_segment, 0.20)
predicted_mean = current_mean * (1 + rate)
uplift = predicted_mean - current_mean

compare_df = pd.DataFrame({
    'Scenario': ['Current (No Recommendation)', 'After Targeted Bundle Recommendation'],
    'Average Payment Amount ($)': [current_mean, predicted_mean]
})

fig = px.bar(
    compare_df,
    x='Scenario',
    y='Average Payment Amount ($)',
    text='Average Payment Amount ($)',
    title=f"Revenue Comparison for {selected_segment}",
    color='Scenario',
    color_discrete_sequence=['#99CCFF', '#FF9966']
)
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(yaxis_title="Average Payment Amount per Transaction ($)")
st.plotly_chart(fig, use_container_width=True)

st.success(f"Predicted uplift: +${uplift:.2f} per transaction (+{rate*100:.0f}%)")

insights = {
    "High Value Loyal Customers": "High-value loyal customers respond strongly to premium bundles. Prioritizing JUMBO BAG RED RETROSPOT and REGENCY CAKESTAND can significantly boost revenue.",
    "Potential Customers": "Potential customers show strong interest in decorative items. Bundles featuring WHITE HANGING HEART T-LIGHT HOLDER are highly effective at converting them into loyal buyers.",
    "General Customers": "General customers buy occasionally. PARTY BUNTING and ASSORTED COLOUR BIRD ORNAMENT bundles can effectively lift their average order value.",
    "Price Sensitive / New Customers": "Price-sensitive and new customers prefer affordable entry points. WHITE HANGING HEART T-LIGHT HOLDER is the best starting bundle to increase willingness to pay."
}

st.info(insights.get(selected_segment, "Targeted recommendations can increase customer willingness to pay."))