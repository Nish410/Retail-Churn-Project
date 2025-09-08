import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

# Set the page configuration for the Streamlit app
st.set_page_config(layout="wide", page_title="Customer Churn Prediction", initial_sidebar_state="expanded")

# --- Load Our Saved Model and Data ---
model = joblib.load('churn_model.joblib')
rfm_data = pd.read_csv('rfm_data.csv')


# --- App Title ---
st.title('Retail Customer Analytics & Churn Prediction 🔮')
st.markdown("---")


# --- INTERACTIVE CHURN PREDICTION SECTION ---
st.header('Interactive Churn Prediction')
st.write("Adjust the sliders to reflect a customer's behavior and click 'Predict' to see the result.")

col1, col2 = st.columns([1, 2]) # Make the input column narrower

with col1:
    st.subheader('Customer Input Features')
    recency = st.slider('Recency (Days since last purchase)', 0, 365, 50)
    frequency = st.slider('Frequency (Total number of purchases)', 1, 100, 5)
    monetary = st.slider('Monetary Value (Total spend in $)', 0, 10000, 500)
    
    # Convert inputs to scores
    r_labels = range(4, 0, -1)
    f_labels = range(1, 5)
    m_labels = range(1, 5)
    
    try:
        r_score = pd.qcut(pd.Series([recency] + list(rfm_data['Recency'])), q=4, labels=r_labels)[0]
        f_score = pd.qcut(pd.Series([frequency] + list(rfm_data['Frequency'])), q=4, labels=f_labels)[0]
        m_score = pd.qcut(pd.Series([monetary] + list(rfm_data['MonetaryValue'])), q=4, labels=m_labels)[0]

        prediction_df = pd.DataFrame({'R_score': [r_score], 'F_score': [f_score], 'M_score': [m_score]})

        if st.button('Predict Churn', type="primary", use_container_width=True):
            prediction = model.predict(prediction_df)
            prediction_proba = model.predict_proba(prediction_df)
            churn_status = 'YES' if prediction[0] == 1 else 'NO'

            with col2:
                st.subheader('Prediction Result')
                if churn_status == 'YES':
                    st.error(f'This customer is likely to CHURN.', icon="🚨")
                else:
                    st.success(f'This customer is likely to STAY.', icon="✅")
                
                # Display probability scores with a gauge-like visualization
                st.write("Confidence Score:")
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = prediction_proba[0][1] * 100,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "Churn Probability"},
                    gauge = {'axis': {'range': [None, 100]},
                             'steps' : [
                                 {'range': [0, 50], 'color': "gray"},
                                 {'range': [50, 100], 'color': "#303138"}], # Adjusted for dark theme
                             'threshold' : {'line': {'color': "#F63366", 'width': 4}, 'thickness': 0.75, 'value': prediction_proba[0][1]*100}}))
                fig.update_layout(height=250, paper_bgcolor="#0E1117", font={'color': 'white'})
                st.plotly_chart(fig, use_container_width=True)

    except ValueError as e:
        st.error(f"Error: Could not calculate scores. The input values might be outside the typical range of the data.")

st.markdown("---")

# --- CUSTOMER ANALYTICS SECTION ---
st.header('Overall Customer Analytics 📊')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue by Customer Segment")
    # Pie chart showing monetary value contribution by segment
    segment_monetary = rfm_data.groupby('Segment_Name')['MonetaryValue'].sum().reset_index()
    fig_pie = px.pie(segment_monetary, 
                     values='MonetaryValue', 
                     names='Segment_Name', 
                     title='Contribution to Total Revenue by Segment',
                     # THIS IS THE CORRECTED LINE:
                     color_discrete_sequence=px.colors.sequential.Plasma_r)
    fig_pie.update_layout(paper_bgcolor="#0E1117", font={'color': 'white'})
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("Customer Segment Counts")
    fig_bar = px.bar(rfm_data['Segment_Name'].value_counts().reset_index(), 
                     x='Segment_Name', 
                     y='count',
                     title='Number of Customers by Segment',
                     color_discrete_sequence=px.colors.sequential.Viridis_r)
    fig_bar.update_layout(xaxis_title="Segment", yaxis_title="Number of Customers", paper_bgcolor="#0E1117", font={'color': 'white'})
    st.plotly_chart(fig_bar, use_container_width=True)

# Interactive Scatter Plot
st.subheader("Recency vs. Frequency Scatter Plot")
fig_scatter = px.scatter(rfm_data, 
                         x='Recency', 
                         y='Frequency', 
                         color='Segment_Name',
                         size='MonetaryValue',
                         hover_name='Customer ID',
                         title='Recency vs. Frequency colored by Segment',
                         size_max=60)
fig_scatter.update_layout(paper_bgcolor="#0E1117", font={'color': 'white'})
st.plotly_chart(fig_scatter, use_container_width=True)