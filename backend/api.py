from fastapi import FastAPI, Request, HTTPException
import uuid
from threading import Thread
from job_manager import jobs, jobs_lock, append_event, Event
from typing import List
from model import InputData
import json
from datetime import datetime

app = FastAPI()

# Issue: Backend never sends COMPLETE status to show the ouput on the front

def kickoff_crew(job_id: str, regions: List[str], subjects: List[str]):
    print(f"Running crew for {job_id} with {regions} and {subjects}")

    # Set up the crew
    results = None
    try:
        # Import and setup GeoPoliticsResearchCrew here
        from crew import GeoPoliticsResearchCrew
        geopolitics_research_crew = GeoPoliticsResearchCrew(job_id)
        geopolitics_research_crew.setup_crew(regions, subjects)
        results = geopolitics_research_crew.kickoff()


    except Exception as e:
        print(f"CREW FAILED: {e}")
        append_event(job_id, f"CREW FAILED: {e}")
        with jobs_lock:
            jobs[job_id].status = "ERROR"
            jobs[job_id].result = str(e)
        
    with jobs_lock:
        jobs[job_id].status = "COMPLETE"
        jobs[job_id].result = results
        jobs[job_id].events.append(Event(data="CREW COMPLETED", timestamp=datetime.now()))

@app.post("/api/crew/")
def run_crew(request: InputData):
    data = request.dict()

    if not data or "regions" not in data or "subjects" not in data:
        raise HTTPException(status_code=400, detail="Invalid input data. 'regions' and 'subjects' are required.")

    job_id = str(uuid.uuid4())
    regions = data["regions"]
    subjects = data["subjects"]

    # Run the crew in a thread
    thread = Thread(target=kickoff_crew, args=(job_id, regions, subjects))
    thread.start()
    return {"status": "sucess", "job_id": job_id}

@app.get("/api/crew/{job_id}")
def get_status(job_id: str):
    with jobs_lock:
        job = jobs.get(job_id)
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
    
    # Parse the JSON data
    try:
        result_json = json.loads(job.result)
    except:
        result_json = job.result
     
    result = {
        'job_id': job_id,
        'status': job.status,
        'result': result_json,
        'events': [{"timestamp": event.timestamp.isoformat(), "data": event.data} for event in job.events]
    }

    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8080)
