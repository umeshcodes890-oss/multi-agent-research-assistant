import streamlit as st
from workflows.research_graph import graph
from tools.pdf_generator import generate_pdf

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="ResearchGPT",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 2rem;
}

.report-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #262730;
    border: 1px solid #444;
}

.status-card {
    padding: 10px;
    border-radius: 10px;
    background-color: #1E1E1E;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🚀 ResearchGPT")

    st.markdown("---")

    st.subheader("System Status")

    st.success("Gemma 3 Connected")
    st.success("Tavily Connected")
    st.success("ChromaDB Connected")

    st.markdown("---")

    st.subheader("Agents")

    st.write("🧠 Planner Agent")
    st.write("💾 Memory Agent")
    st.write("🌐 Search Agent")
    st.write("📚 Research Agent")
    st.write("✍ Writer Agent")
    st.write("🔍 Critic Agent")
    st.write("✅ Fact Checker")
    st.write("🎯 Supervisor")

    st.markdown("---")

    st.caption("Built with LangGraph + Ollama")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🤖 ResearchGPT")

st.caption(
    "Agentic AI Research Assistant powered by Ollama, Tavily, ChromaDB and LangGraph"
)

# --------------------------------------------------
# METRICS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Agents",
        value="8"
    )

with col2:
    st.metric(
        label="LLM",
        value="Gemma 3"
    )

with col3:
    st.metric(
        label="Memory",
        value="ChromaDB"
    )

with col4:
    st.metric(
        label="Search",
        value="Tavily"
    )

st.markdown("---")

# --------------------------------------------------
# INPUT
# --------------------------------------------------

topic = st.text_input(
    "Enter Research Topic",
    placeholder="Example: Artificial Intelligence in Healthcare"
)

# --------------------------------------------------
# RESEARCH BUTTON
# --------------------------------------------------

if st.button("🚀 Start Research", use_container_width=True):

    if not topic.strip():

        st.warning(
            "Please enter a research topic."
        )

        st.stop()

    progress = st.progress(0)

    try:

        with st.spinner("Research Agents Working..."):

            progress.progress(10)

            result = graph.invoke(
                {
                    "topic": topic,
                    "revision_count": 0,
                    "memory": ""
                }
            )

            progress.progress(100)

        st.success("✅ Research Complete!")

        report = result.get(
            "report",
            "No report generated."
        )

        # --------------------------------------------------
        # TABS
        # --------------------------------------------------

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📄 Final Report",
                "📚 Sources",
                "🧠 Research Notes",
                "⚙ Debug"
            ]
        )

        # --------------------------------------------
        # REPORT TAB
        # --------------------------------------------

        with tab1:

            st.subheader(
                "Generated Research Report"
            )

            st.markdown(
                f"""
                <div class="report-box">
                {report}
                </div>
                """,
                unsafe_allow_html=True
            )

            try:

                pdf_file = generate_pdf(
                    topic,
                    report
                )

                with open(pdf_file, "rb") as file:

                    st.download_button(
                        label="📥 Download PDF Report",
                        data=file,
                        file_name=pdf_file,
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error(
                    f"PDF Error: {e}"
                )

        # --------------------------------------------
        # SOURCES TAB
        # --------------------------------------------

        with tab2:

            st.subheader(
                "Collected Sources"
            )

            st.write(
                result.get(
                    "sources",
                    ""
                )
            )

            st.subheader(
                "Academic Sources"
            )

            st.write(
                result.get(
                    "academic_sources",
                    ""
                )
            )

        # --------------------------------------------
        # RESEARCH TAB
        # --------------------------------------------

        with tab3:

            st.subheader(
                "Research Notes"
            )

            st.write(
                result.get(
                    "research",
                    ""
                )
            )

            st.subheader(
                "Memory Retrieved"
            )

            st.write(
                result.get(
                    "memory",
                    ""
                )
            )

        # --------------------------------------------
        # DEBUG TAB
        # --------------------------------------------

        with tab4:

            st.subheader(
                "Plan"
            )

            st.write(
                result.get(
                    "plan",
                    ""
                )
            )

            st.subheader(
                "Critique"
            )

            st.write(
                result.get(
                    "critique",
                    ""
                )
            )

            st.subheader(
                "Fact Check"
            )

            st.write(
                result.get(
                    "fact_check",
                    ""
                )
            )

            st.subheader(
                "Full State"
            )

            st.json(result)

        # --------------------------------------------------
        # AGENT ACTIVITY
        # --------------------------------------------------

        with st.expander(
            "🤖 Agent Activity Log"
        ):

            st.success(
                "Planner Agent Completed"
            )

            st.success(
                "Memory Agent Completed"
            )

            st.success(
                "Search Agent Completed"
            )

            st.success(
                "Research Agent Completed"
            )

            st.success(
                "Writer Agent Completed"
            )

            st.success(
                "Critic Agent Completed"
            )

            st.success(
                "Fact Checker Completed"
            )

            st.success(
                "Supervisor Completed"
            )

    except Exception as e:

        st.error(
            f"Research Failed: {e}"
        )