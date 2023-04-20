import os
import json

data = {}

for class_ in range(7, 12):
    id = 1
    for filename in os.listdir("Text files"):
        data[filename[:-5]] = f"{class_}_{id}"
        os.rename(os.path.join(f"Text files/{class_}/", filename), os.path.join(f"Text files/{class_}/", f"{class_}_{id}.docx"))
        id += 1

with open("dict.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)