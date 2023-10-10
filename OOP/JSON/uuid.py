import uuid
import pandas as pd

data = pd.DataFrame({
    "id": [uuid.uuid4() for n in range(6)],
    "value1": [40, 20, 50, 12, 25, 19,],
    "value2": [45, 41, 85, 96, 12, 33, 54, 18]
    })

data = data.set_index("id")
existing = pd.readcsv("existing_data.csv")
existing = existing.set_index("id")

combined = pd.concat([existing, data], verify_integrity=True)
print(combined)
