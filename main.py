import streamlit as st
from predictor import predict

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Credit Risk Modelling",
    page_icon="📊",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("📊 Credit Risk Modelling Dashboard")
st.markdown("---")

# ---------------- INPUT SECTION ----------------
st.subheader("🧾 Applicant & Loan Details")

# Outer rows
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# -------- ROW 1 (Slim Inputs) --------
with row1[0]:
    c1, c2 = st.columns([2, 1])
    with c1:
        age = st.number_input("👤 Age", min_value=18, max_value=100, value=28)

with row1[1]:
    c1, c2 = st.columns([2, 1])
    with c1:
        income = st.number_input("💰 Annual Income", min_value=0, value=1200000)

with row1[2]:
    c1, c2 = st.columns([2, 1])
    with c1:
        loan_amount = st.number_input("🏦 Loan Amount", min_value=0, value=2560000)

# -------- Loan to Income Ratio --------
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.metric("📉 Loan to Income Ratio", f"{loan_to_income_ratio:.2f}")

# -------- ROW 2 --------
with row2[1]:
    c1, _ = st.columns([2, 1])
    with c1:
        loan_tenure_months = st.number_input(
            "📅 Loan Tenure (Months)", min_value=0, value=36
        )

with row2[2]:
    c1, _ = st.columns([2, 1])
    with c1:
        avg_dpd_per_delinquency = st.number_input(
            "⏱ Avg DPD", min_value=0, value=20
        )

# -------- ROW 3 --------
with row3[0]:
    c1, _ = st.columns([2, 1])
    with c1:
        delinquency_ratio = st.number_input(
            "⚠ Delinquency Ratio (%)", min_value=0, max_value=100, value=30
        )

with row3[1]:
    c1, _ = st.columns([2, 1])
    with c1:
        credit_utilization_ratio = st.number_input(
            "📊 Credit Utilization Ratio (%)", min_value=0, max_value=100, value=30
        )

with row3[2]:
    c1, _ = st.columns([2, 1])
    with c1:
        num_open_accounts = st.number_input(
            "📂 Open Loan Accounts", min_value=1, max_value=4, value=2
        )

# -------- ROW 4 --------
with row4[0]:
    c1, _ = st.columns([2, 1])
    with c1:
        residence_type = st.selectbox(
            "🏠 Residence Type", ["Owned", "Rented", "Mortgage"]
        )

with row4[1]:
    c1, _ = st.columns([2, 1])
    with c1:
        loan_purpose = st.selectbox(
            "🎯 Loan Purpose", ["Education", "Home", "Auto", "Personal"]
        )

with row4[2]:
    c1, _ = st.columns([2, 1])
    with c1:
        loan_type = st.selectbox(
            "🔒 Loan Type", ["Unsecured", "Secured"]
        )

st.markdown("---")

# ---------------- BUTTON & RESULTS ----------------
if st.button("🚀 Calculate Credit Risk"):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months,
        avg_dpd_per_delinquency, delinquency_ratio,
        credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.subheader("📈 Results")
    col1, col2, col3 = st.columns(3)

    col1.success(f"Default Probability\n\n{probability:.2%}")
    col2.info(f"Credit Score\n\n{credit_score}")
    col3.warning(f"Rating\n\n{rating}")

st.markdown("---")
st.caption("Developed by Aniruddha Moharir | Machine Learning project")
