from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Tuple, Dict
from Geofence import Geofence 

app = FastAPI()

# In-memory storage for geofences
geofences: Dict[int, Geofence] = {}

@app.post("/geofences/", response_model=Geofence)
def create_geofence(geofence: Geofence):
	if geofence.id in geofences:
		raise HTTPException(status_code=400, detail="Geofence with this ID already exists")
	geofences[geofence.id] = geofence
	return geofence

@app.get("/geofences/{geofence_id}", response_model=Geofence)
def read_geofence(geofence_id: int = Path(..., description="The ID of the geofence to read")):
	if geofence_id not in geofences:
		raise HTTPException(status_code=404, detail="Geofence not found")
	return geofences[geofence_id]

@app.put("/geofences/{geofence_id}", response_model=Geofence)
def update_geofence(geofence_id: int, geofence: Geofence):
	if geofence_id not in geofences:
		raise HTTPException(status_code=404, detail="Geofence not found")
	if geofence.id != geofence_id:
		raise HTTPException(status_code=400, detail="Geofence ID mismatch")
	geofences[geofence_id] = geofence
	return geofence

@app.delete("/geofences/{geofence_id}", response_model=Geofence)
def delete_geofence(geofence_id: int):
	if geofence_id not in geofences:
		raise HTTPException(status_code=404, detail="Geofence not found")
	deleted_geofence = geofences.pop(geofence_id)
	return deleted_geofence

@app.get("/geofences/", response_model=List[Geofence])
def list_geofences():
    return list(geofences.values())