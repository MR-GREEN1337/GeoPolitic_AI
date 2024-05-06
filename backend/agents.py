from crewai import Agent
from crewai_tools import SerperDevTool
from typing import List
from langchain_groq import ChatGroq
import os

class GeoPoliticsResearchAgents():
    def __init__(self):
        print("Setting up GeoPoltics Agents")
        self.tools = [SerperDevTool()]

        os.environ["SERPER_API_KEY"] = "8f67df02cc87f1fc8315f46f3b9eb95798b6f002"  # serper.dev API key

        os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
        os.environ["OPENAI_MODEL_NAME"] = "llama3-70b-8192"
        os.environ["OPENAI_API_KEY"] = "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"

    def research_manager(self, regions: List[str], subjects: List[str]) -> Agent:
        print("Research Agent of GeoPoltics")
        print(f"Regions of interest: {' '.join([region for region in regions])}")
        print(f"Subject of interest: {' '.join([subject for subject in subjects])}")
        return Agent(
            role="Geopolitics Research Manager",
            goal = f"""Generate me an extensive markdown file covering all the recent information on the latest news around the world.
                    Regions of interest: {regions}
                    Subjects of interest: {subjects}
                    THE MOMENT YOU GENERATE MARKDOWN FILE, STOP GENERATING, JUST STOP WORKING.
                    Important: I want you to summarize first the main events in a well-written few paragraphs, then list the resources the final markdown paper must be extensive and cover all the information you have retrieved.
                    DON'T DIVERGE FROM THE RETRIEVED INFORMATION. AND BE WISE!
            """,
            backstory="As a Geopolitics Research Manager, your main goal is to summarize given information and convey them wisely",
            tools = self.tools,
            verbose = True,
            max_iter = 6,
            memory=True,
            max_rpm=2000
        )

    def geopolitics_research_agent(self) -> Agent:
       return Agent(
        role="Geopolitics Research Agent",
        goal=""" The goal is to find RECENT resources about the given subjects and regions. THE MOMENT YOU GENERATE MARKDOWN FILE, STOP GENERATING, JUST STOP WORKING""",
        backstory="""As a Geopolitics Research Agent, you are responsable for Searching for VALID, RECENT INFO ABOUT GIVEN SUBJECTS AND REGIONS.""",
        tools = self.tools,
        verbose = True,
        max_iter = 6,
        memory=True,
        max_rpm=2000


    )
