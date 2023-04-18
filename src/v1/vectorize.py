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
review_class = {
    "class": "CustomerReview",
    "description": "A customer review of a restaurant",
    "vectorizer": "text2vec-transformers",
    "properties": [
        {"dataType": ["string"], "name": "review"},
        {"dataType": ["boolean"], "name": "sentiment"}]
}

client.schema.create_class(review_class)

# ===== import data =====

import csv, json

reviews_file_loc = "data/reviews.tsv"

rows = []

# open the TSV file for reading
with open(reviews_file_loc, 'r') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')

    # convert each row to a dictionary and append to a list

    for row in reader:
        rows.append(dict(row))


print(rows)

#
# # Configure a batch process
# with client.batch as batch:
#     batch.batch_size = 100
#     # Batch import all Questions
#     for i, d in enumerate(data):
#         print(f"importing question: {i + 1}")
#
#         properties = {
#             "answer": d["Answer"],
#             "question": d["Question"],
#             "category": d["Category"],
#         }
#
#         client.batch.add_data_object(properties, "Question")
