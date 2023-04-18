import weaviate
import json

client = weaviate.Client(
    url="http://localhost:8080/",  # Replace with your endpoint

    # additional_headers = {
    #     "X-OpenAI-Api-Key": "<THE-KEY>"  # Replace with your API key
    # }

)


# nearText = {"concepts": ["wait staff sentiment and overall restaurant ambience"]}
nearText = {"concepts": ["portion size"]}

result = (
    client.query
    .get(class_name="CustomerReview", properties=["review"])
    .with_near_text(nearText)
    .with_limit(9)
    .do()
)

print(json.dumps(result, indent=4))



# result = (
#     client.query
#     .get("Question", ["question", "answer", "category"])
#     .with_near_text(nearText)
#     .with_limit(4)
#     .do()
# )