import sys

import weaviate
import json

client = weaviate.Client(
    url="http://localhost:8080/",  # Replace with your endpoint

    # additional_headers = {
    #     "X-OpenAI-Api-Key": "<THE-KEY>"
    # }
)

# ===== add schema =====
resume_class = {
    "class": "Resume",
    "description": "A resume of a person",
    "vectorizer": "text2vec-transformers",
    "properties": [
        {"dataType": ["string"], "name": "text", "description": "The content body of the resume"},

    ],
}

# client.schema.create_class(resume_class)

# ===== import data =====

import csv, json, os

resume_file_loc = "data/resumes.json"


resumes = []


# open the csv file for reading
with open(resume_file_loc, 'r') as text_file:
    print(f"reading file: {resume_file_loc}")
    for line in text_file:
        resumes.append(json.loads(line)["content"])


print(resumes[0])



# Configure a batch process
with client.batch as batch:
    batch.batch_size = 3
    # Batch import all Questions
    for i, d in enumerate(resumes):
        print(f"importing resume: {i + 1}")

        properties = {
            "text": resumes[i],
        }

        client.batch.add_data_object(properties, "Resume")
