from typing import List
from crewai import Task, Agent
from textwrap import dedent

class GeoPoliticsResearchTasks():
    def geopolitics_research(self, agent: Agent, region: str, subjects: list[str]):
        return Task(
        description=dedent(f"""Given the region '{region}' and the subjects {subjects},
            instruct the geopolitics research agent to gather current, LATEST LATEST LATEST LATEST news data from this REGION, focusing on the specified subjects, 
            and summarize the findings."""),
        agent=agent,
        expected_output=dedent(
            """A json object containing the URLs for blog articles talking about the subject"""
        ),
        async_exection=True,
    )

    def manage_research(self, agent: Agent, regions: List[str], subjects: List[str], tasks: list[str]):
        return Task(
            description=dedent(f"""For the given regions {regions} and subjects {subjects}, 
            coordinate with the Geopolitics research agent to compile data on each region and subject combination. 
            Utilize the collected information to MAKE SENSE OF NEWS AROUND REGIONS, AND GIVE WHAT'S HAPPENING IN A POISED WAY, WISE WISE WISE WISE WISE WISE, 
            consolidating the findings into a comprehensive report."""),
            agent=agent,
            expected_output=dedent(
                """A markdown object containing the geopolitics new of the this week"""
            ),
            context=tasks
        )
