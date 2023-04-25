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
papers_class = {
    "class": "Paper",
    "description": "A research paper",
    "vectorizer": "text2vec-transformers",
    "properties": [
        {"dataType": ["string"], "name": "title", "description": "The title of the paper"},
        {"dataType": ["string"], "name": "text", "description": "The text body of the paper"},

    ],
}

# client.schema.create_class(papers_class)

# ===== import data =====

import csv, json, os

reviews_folder_loc = "data/papers/"

reviews = []


for filename in os.listdir(reviews_folder_loc):
    f = os.path.join(reviews_folder_loc, filename)

    # open the TSV file for reading
    with open(f, 'r') as text_file:
        print(f"reading file: {f}")
        reader = text_file.readlines()
        text = " ".join(reader)

        # convert each row to a dictionary and append to a list

        reviews.append({
            "title": filename,
            "text": text
        })




# Configure a batch process
with client.batch as batch:
    batch.batch_size = 4
    # Batch import all Questions
    for i, d in enumerate(reviews):
        print(f"importing paper: {i + 1}")

        properties = {
            "title": reviews[i]["title"],
            "text": reviews[i]["text"],
        }

        client.batch.add_data_object(properties, "Paper")
