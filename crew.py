from agents import GeoPoliticsResearchAgents
from tasks import GeoPoliticsResearchTasks

from crewai import Crew

class GeoPoliticsResearchCrew:
    def __init__(self):
        self.crew = None
    
    def setup_crew(self, regions: list[str], subjects: list[str]):
 
        # SETUP AGENTS
        agents = GeoPoliticsResearchAgents()
        research_manager = agents.research_manager(regions, subjects)
        geopolitics_research_agent = agents.geopolitics_research_agent()
        # SETUP TASKS
        tasks = GeoPoliticsResearchTasks()

        Geopolitics_research_tasks = [
            tasks.geopolitics_research(geopolitics_research_agent, region, subjects) for region in regions
        ]

        manage_research = tasks.manage_research(research_manager, regions, subjects, Geopolitics_research_tasks)

        self.crew = Crew(
            agents=[research_manager, geopolitics_research_agent],
            tasks=[*Geopolitics_research_tasks, manage_research],
            verbose=2,
        )
    
        return self.crew.kickoff()

if __name__ == "__main__":  
    filename = "geopolitics_research_crew_result.md"
    job = GeoPoliticsResearchCrew(664)
    job.setup_crew(regions=["Palestine", "Israel"], subjects=["war"])
    result = job.kickoff()
    with open(filename, 'w') as file:
        file.write(result)