import os
import streamlit as st
from workflows.research_graph import graph
from tools.pdf_generator import generate_pdf

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Multi-Agent Research Assistant")

topic = st.text_input(
    "Enter a research topic",
    placeholder="AI Agents in Healthcare"
)

if "result" not in st.session_state:
    st.session_state.result = None

if st.button("Start Research"):
    with st.spinner("Agents are researching..."):
        st.session_state.result = graph.invoke({
            "topic": topic,
            "revision_count": 0
        })
    st.success("Research Complete!")

if st.session_state.result:
    result = st.session_state.result

    st.subheader("Plan")
    st.write(result.get("plan"))

    st.subheader("Research")
    st.write(result.get("research"))

    st.subheader("Critique")
    st.write(result.get("critique"))

    st.subheader("Final Report")
    st.write(result.get("report"))

    report = result.get("report", "")
    if report:
        pdf_file = generate_pdf(topic or "research_report", report)
        file_name = os.path.basename(pdf_file)

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="Download PDF Report",
                data=file,
                file_name=file_name,
                mime="application/pdf"
            )
else:
    st.info("Enter a research topic and click Start Research to begin.")