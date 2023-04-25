import weaviate
import json
import time

if __name__ == "__main__":
    start_time = time.time()

    client = weaviate.Client(
        url="http://localhost:8080/",  # Replace with your endpoint

        # additional_headers = {
        #     "X-OpenAI-Api-Key": "<THE-KEY>"  # Replace with your API key
        # }

    )


    nearText = {"concepts": ["the ethics of computing social sciences "]}

    result = (
        client.query
        .get(class_name="Paper", properties=["text", "title"])
        .with_near_text(nearText)
        .with_limit(4)
        .do()
    )

    result_titles = [result["data"]["Get"]["Paper"][i]["title"] for i in range(len(result["data"]["Get"]["Paper"]))]

    print(json.dumps(result_titles, indent=4))

    print("--- %s seconds ---" % (time.time() - start_time))



    # result = (
    #     client.query
    #     .get("Question", ["question", "answer", "category"])
    #     .with_near_text(nearText)
    #     .with_limit(4)
    #     .do()
    # )