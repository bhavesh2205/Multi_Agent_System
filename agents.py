from crewai import Agent
from config import llm

planner = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on a given topic.",
    backstory="You are responsible for planning a blog article "
              "by gathering relevant information and structuring an outline. "
              "Your work serves as the foundation for the Content Writer "
              "to develop a well-researched article.",
    allow_delegation=True,  
    verbose=True,
    llm=llm
)

writer = Agent(
    role="Content Writer",
    goal="Write an insightful and factually accurate article based on the provided outline.",
    backstory="You are responsible for turning the Content Planner's outline "
              "into a well-written article. You must ensure accuracy, "
              "back up claims with evidence, and clearly distinguish between "
              "facts and opinions.",
    allow_delegation=False,  
    verbose=True,
    llm=llm
)

editor = Agent(
    role="Editor",
    goal="Refine and edit the article to match the organization's writing standards.",
    backstory="As an editor, you review the article written by the Content Writer, "
              "ensuring clarity, neutrality, and adherence to journalistic standards. "
              "You refine the structure and eliminate controversial elements where necessary.",
    allow_delegation=False, 
    verbose=True,
    llm=llm
)
