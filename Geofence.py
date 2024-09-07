from pydantic import BaseModel
from typing import List, Optional, Tuple

class Geofence(BaseModel):
    id: int
    name: str
    coordinates: List[Tuple[float, float]]

# Example usage
geofence = Geofence(
    id=1,
    name="Test Geofence",
    coordinates=[(12.9715987, 77.594566), (12.2958104, 76.6393805)]
)
print(geofence)