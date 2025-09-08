# Retail Customer Analytics & Churn Prediction 📈

This is a complete, end-to-end data analytics project developed as part of my 4th-year studies. The application analyzes transactional data from an online retailer to segment customers using RFM analysis and predicts customer churn with a machine learning model. The entire project is presented in a live, interactive Streamlit dashboard.

---

## 🚀 Key Features

- Interactive UI: Built with Streamlit for a user-friendly experience.
- **Exploratory Data Analysis (EDA):** In-depth analysis of sales, products, and customer behavior in the Jupyter Notebook.
- **RFM Customer Segmentation:** Customers are dynamically segmented into groups like "Best Customers," "Loyal," and "At Risk" based on their purchasing patterns.
- **Machine Learning Model:** A Random Forest Classifier trained to predict churn.
- **Critical Analysis:** Identified and explained the concept of data leakage, which led to the model's 100% accuracy on this dataset.
- **Interactive Prediction:** Allows users to input hypothetical customer data via sliders and get a real-time churn prediction.
- **Data Visualization:** Includes multiple interactive charts (pie charts, bar charts, scatter plots) built with Plotly to visualize customer segments and revenue.

---

## Tech Stack

- **Language:** Python
- **Data Manipulation:** Pandas
- **Machine Learning:** Scikit-learn (Logistic Regression, Random Forest)
- **Data Visualization:** Plotly, Seaborn, Matplotlib
- **Web Framework:** Streamlit
- **Version Control:** Git & GitHub

---

## How to Run Locally

1.  Clone the repository:**
    ```bash
    git clone [https://github.com/Nish410/Retail-Churn-Project.git](https://github.com/Nish410/Retail-Churn-Project.git)
    cd Retail-Churn-Project
    ```
2.  Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
The application will be available at `http://localhost:8501`.
