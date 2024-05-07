from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

class GeoPoliticsResearchAgents():
    def __init__(self):
        print("Setting up GeoPoltics Agents")
        self.tools = [SerperDevTool()]

        os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")  # serper.dev API key

        os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
        os.environ["OPENAI_MODEL_NAME"] = "llama3-70b-8192"
        os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY")

    def research_manager(self, regions: list[str], subjects: list[str]) -> Agent:
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
            max_iter = 1,
            memory=True,
            max_rpm=3000
        )

    def geopolitics_research_agent(self) -> Agent:
       return Agent(
        role="Geopolitics Research Agent",
        goal=""" The goal is to find RECENT resources about the given subjects and regions. THE MOMENT YOU GENERATE MARKDOWN FILE, STOP GENERATING, JUST STOP WORKING""",
        backstory="""As a Geopolitics Research Agent, you are responsable for Searching for VALID, RECENT INFO ABOUT GIVEN SUBJECTS AND REGIONS.""",
        tools = self.tools,
        verbose = True,
        max_iter = 1,
        memory=True,
        max_rpm=3000


    )
