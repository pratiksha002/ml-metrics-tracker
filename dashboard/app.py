import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from src.tracker import load_experiments, get_best_experiment

st.title("📊 ML Metrics Tracking Dashboard")
experiments = load_experiments()
st.subheader("All Experiments")

if not experiments:
    st.warning("No experiments found!")
else:
    for exp in experiments:
        st.markdown(f"""
        ### 🔹 Run ID: {exp['run_id']}
        - **Model:** {exp['model_version']}
        - **MAE:** {exp['metrics']['mae']}
        - **RMSE:** {exp['metrics']['rmse']}
        - **R2:** {exp['metrics']['r2']}
        - **Timestamp:** {exp['timestamp']}
        ---
        """)

st.subheader("Best Experiment")

metric = st.selectbox("Select metric", ["mae", "rmse", "r2"])

best_exp = get_best_experiment(metric)

if best_exp:
    st.markdown(f"""
    ###  Best Based on {metric.upper()}
    
    - **Run ID:** {best_exp['run_id']}
    - **Model:** {best_exp['model_version']}
    - **MAE:** {best_exp['metrics']['mae']}
    - **RMSE:** {best_exp['metrics']['rmse']}
    - **R2:** {best_exp['metrics']['r2']}
    - **Timestamp:** {best_exp['timestamp']}
    """)
else:
    st.warning("No best experiment found!")