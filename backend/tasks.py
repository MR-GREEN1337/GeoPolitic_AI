from job_manager import append_event
from typing import List
from crewai import Task, Agent
from textwrap import dedent

class GeoPoliticsResearchTasks():
    def __init__(self, job_id: str):
        self.job_id = job_id

    def append_event_callback(self, task_output: str):
        print(f"Appending event for {self.job_id} with output {task_output}")
        append_event(self.job_id, task_output)
    
    def geopolitics_research(self, agent: Agent, region: str, subjects: list[str]):
        return Task(
        description=dedent(f"""Given the region '{region}' and the subjects {subjects},
            instruct the geopolitics research agent to gather current, LATEST LATEST LATEST LATEST news data from this REGION, focusing on the specified subjects, 
            and summarize the findings."""),
        agent=agent,
        expected_output=dedent(
            """A json object containing the URLs for blog articles talking about the subject"""
        ),
        callback=self.append_event_callback,
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
            callback=self.append_event_callback,
            context=tasks
        )
