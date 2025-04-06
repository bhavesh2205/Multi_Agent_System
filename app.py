import streamlit as st
from IPython.display import Markdown
from crewai import Crew, Process
from tasks import plan, write, edit
from agents import planner, writer, editor

# from config import llm
# from crewai import LLM
# Create CrewAI Workflow
crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    process=Process.sequential,
    verbose=True,
)

# Streamlit UI
st.set_page_config(page_title="AI Multi-Agent Blog Writer", layout="wide")
st.title("AI Multi-Agent Blog Writer")

# User Input for Topic
topic = st.text_input(
    "Enter a topic for the article:", placeholder="e.g., Future of AI in Healthcare"
)

# Run CrewAI Workflow
if st.button("Generate Blog"):
    if topic.strip():
        st.write(" **Generating blog... Please wait.**")

        # Execute Multi-Agent Workflow
        with st.spinner("AI Agents are working..."):
            result = crew.kickoff(inputs={"topic": topic})

        # Retrieve final content (from Editor)
        final_blog = result.raw

        st.success("Blog generated successfully!")
        st.markdown(final_blog, unsafe_allow_html=True)
    else:
        st.warning(" Please enter a topic before generating the blog.")
