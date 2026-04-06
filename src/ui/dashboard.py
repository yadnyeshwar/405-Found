import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
import json
import tempfile
from src.pipeline.run_pipeline import run_pipeline


st.title("MEP Guard AI")

st.subheader("AI-Based MEP Clash Detection & Rerouting")

uploaded_file = st.file_uploader(
    "Upload IFC Model",
    type=["ifc"]
)


if uploaded_file:

    st.success("IFC file uploaded")

    with tempfile.NamedTemporaryFile(delete=False) as tmp:

        tmp.write(uploaded_file.read())

        ifc_path = tmp.name


    if st.button("Run Clash Detection"):

        with st.spinner("Running pipeline..."):

            run_pipeline(ifc_path)

        st.success("Pipeline finished")


        with open("clash_results.json") as f:

            data = json.load(f)


        st.subheader("Clash Results")

        st.write("Total Clashes:", len(data["clashes"]))

        st.dataframe(data["clashes"])


        st.subheader("Rerouting Suggestions")

        st.dataframe(data["reroutes"])


        st.download_button(
            label="Download JSON for Revit Plugin",
            data=json.dumps(data, indent=4),
            file_name="clash_results.json"
        )