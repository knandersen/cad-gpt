from rhino3dm import *
import requests  # pip install requests

req = requests.get("https://files.mcneel.com/TEST/Rhino Logo.3dm")
model = File3dm.FromByteArray(req.content)
print(model.Objects)
for obj in model.Objects:
    print(obj)
    geometry = obj.Geometry
    bbox = geometry.GetBoundingBox()
    print("{}, {}".format(bbox.Min, bbox.Max))
