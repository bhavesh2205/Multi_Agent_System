from crewai import Task
from agents import planner, writer, editor

plan = Task(
    description=(
        "1. Research and analyze the latest trends, key players, "
        "and noteworthy news related to the given topic.\n"
        "2. Identify the target audience and their key pain points.\n"
        "3. Develop a structured content outline with an introduction, "
        "key points, and a compelling conclusion.\n"
        "4. Include SEO-friendly keywords and credible sources for reference."
    ),
    expected_output=(
        "A structured content plan document containing:\n"
        "- Topic analysis with key trends and references.\n"
        "- Target audience breakdown.\n"
        "- A detailed content outline with sections.\n"
        "- SEO keywords and recommended sources."
    ),
    agent=planner,
)

write = Task(
    description=(
        "1. Use the provided content plan to write a compelling blog post.\n"
        "2. Integrate SEO keywords naturally into the text.\n"
        "3. Ensure sections/subtitles are engaging and relevant.\n"
        "4. Maintain a clear structure: introduction, detailed body, "
        "and a well-summarized conclusion.\n"
        "5. Proofread for grammatical correctness and alignment "
        "with the brand's tone and style."
    ),
    expected_output=(
        "A well-structured blog post in markdown format, with:\n"
        "- Engaging introduction.\n"
        "- Informative body sections (2-3 paragraphs per section).\n"
        "- Strong, well-rounded conclusion.\n"
        "- SEO-optimized writing and error-free grammar."
    ),
    agent=writer,
)

edit = Task(
    description=(
        "1. Review the provided blog post for grammatical errors "
        "and ensure clarity in writing.\n"
        "2. Adjust the tone to align with the brand's style and voice.\n"
        "3. Ensure that the article follows journalistic best practices.\n"
        "4. Remove any unnecessary fluff or controversial opinions."
    ),
    expected_output=(
        "A polished, publication-ready blog post with:\n"
        "- Refined language and grammar.\n"
        "- Improved sentence structure and clarity.\n"
        "- Consistency in tone and voice.\n"
        "- Proper formatting and final proofreading."
    ),
    agent=editor,
)
