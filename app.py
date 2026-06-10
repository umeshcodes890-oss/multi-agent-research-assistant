import streamlit as st
from workflows.research_graph import graph

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

if st.button("Start Research"):

    with st.spinner("Agents are researching..."):

        result = graph.invoke({
            "topic": topic,
            "revision_count": 0
        })

    st.success("Research Complete!")

    st.markdown(result["report"])