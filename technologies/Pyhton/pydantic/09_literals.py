from pydantic import BaseModel
from typing import Literal, Annotated

DeliveryMethod = Literal["ground", "air", "sea"]
PackageStatus = Annotated[str, Literal["in_transit", "retained", "delivered"]]

class DeliveryTask(BaseModel):
    track_id: int
    method: DeliveryMethod
    status: PackageStatus
    priority_level: Literal[1, 2, 3]

if __name__ == "__main__":
    info = {
        "track_id": 1,
        "method": "ground",
        "status": "retained",
        "priority_level": 1
    }
    data = DeliveryTask.model_validate(info)
    print(data) # track_id=1 method='ground' status='retained' priority_level=1