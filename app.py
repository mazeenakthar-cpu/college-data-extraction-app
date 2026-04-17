import streamlit as st
import pandas as pd

st.set_page_config(page_title="College Data Explorer", layout="wide")

st.title("🎓 College Data Extraction & Analysis")

# Upload file
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    st.sidebar.header("Filters")

    # 🔍 Search by college name
    search = st.sidebar.text_input("Search College Name")

    # 📍 District filter
    district = st.sidebar.multiselect(
        "Select District",
        options=df["District"].unique()
    )

    # 🎓 Branch filter
    branch = st.sidebar.multiselect(
        "Select Branch",
        options=df["Branch"].unique()
    )

    # 🏫 College Type filter
    if "Type" in df.columns:
        college_type = st.sidebar.multiselect(
            "Select College Type",
            options=df["Type"].unique()
        )
    else:
        college_type = []

    # 🧠 Apply filters
    filtered_df = df.copy()

    if search:
        filtered_df = filtered_df[
            filtered_df["College_Name"].str.contains(search, case=False)
        ]

    if district:
        filtered_df = filtered_df[
            filtered_df["District"].isin(district)
        ]

    if branch:
        filtered_df = filtered_df[
            filtered_df["Branch"].isin(branch)
        ]

    if college_type:
        filtered_df = filtered_df[
            filtered_df["Type"].isin(college_type)
        ]

    st.subheader("Filtered Results")
    st.dataframe(filtered_df)

    # 📥 Download filtered data
    csv = filtered_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label=" Download Filtered CSV",
        data=csv,
        file_name="filtered_colleges.csv",
        mime="text/csv"
    )

else:
    st.info("Please upload a CSV file to start")
