from typing import List
from agents import GeoPoliticsResearchAgents
from job_manager import append_event
from tasks import GeoPoliticsResearchTasks

from crewai import Crew

class GeoPoliticsResearchCrew:
    def __init__(self, job_id):
        self.job_id = job_id
        self.crew = None
    
    def setup_crew(self, regions: List[str], subjects: List[str]):
        print(f"Setting up crew for job {self.job_id} with {regions} Regions and {subjects} Subjects")
 
        # SETUP AGENTS
        agents = GeoPoliticsResearchAgents()
        research_manager = agents.research_manager(regions, subjects)
        geopolitics_research_agent = agents.geopolitics_research_agent()
        # SETUP TASKS
        tasks = GeoPoliticsResearchTasks(self.job_id)

        Geopolitics_research_tasks = [
            tasks.geopolitics_research(geopolitics_research_agent, region, subjects) for region in regions
        ]

        manage_research = tasks.manage_research(research_manager, regions, subjects, Geopolitics_research_tasks)

        self.crew = Crew(
            agents=[research_manager, geopolitics_research_agent],
            tasks=[*Geopolitics_research_tasks, manage_research],
            verbose=2,
        )

    def kickoff(self):
        if not self.crew:
            print("Crew not found for id {self.job_id}")
            return
        append_event(self.job_id, "CREW STARTED")
        try:
            print(f"Kicking off job {self.job_id}")
            append_event(self.job_id, "CREW WORKING")
            result = self.crew.kickoff()
            filename = "geopolitics_research_crew_result.md"
            print(f"Prrinting final result {result}")
            with open(filename, 'w') as file:
                file.write(result)
            return result
        
        except Exception as e:
            print(f"Error kicking off job {self.job_id}: {e}")
            append_event(self.job_id, "CREW FAILED")
            return str(e)

if __name__ == "__main__":  
    filename = "geopolitics_research_crew_result.md"
    job = GeoPoliticsResearchCrew(664)
    job.setup_crew(regions=["Palestine", "Israel"], subjects=["war"])
    result = job.kickoff()
    with open(filename, 'w') as file:
        file.write(result)