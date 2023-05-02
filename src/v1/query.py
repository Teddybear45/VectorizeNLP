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

    nearText = {"concepts": ["""
    
Job brief

We are looking for an experienced IT Director to oversee all IT (Information Technology) functions in our company. You will be in charge of a team of IT managers and manage the company’s technology operations and the implementation of new IT systems and policies.

An excellent IT director is very knowledgeable in IT and computer systems. They have a solid technical background while able to manage and motivate people. The ideal candidate will be experienced in creating and implementing IT policies and systems that will meet objectives.

The goal is to ensure IT systems and people are effective and functioning within the limits of budget, time and specifications of the company.
Responsibilities

    Oversee all technology operations (e.g. network security) and evaluate them according to established goals
    Devise and establish IT policies and systems to support the implementation of strategies set by upper management
    Analyze the business requirements of all departments to determine their technology needs
    Purchase efficient and cost effective technological equipment and software
    Inspect the use of technological equipment and software to ensure functionality and efficiency
    Identify the need for upgrades, configurations or new systems and report to upper management
    Coordinate IT managers and supervise computer scientists, technicians and other professionals to provide guidance
    Control budget and report on expenditure
    Assist in building relationships with vendors and creating cost-efficient contracts

Requirements and skills

    Proven experience as IT director or similar role
    Experience in analysis, implementation and evaluation of IT systems and their specifications
    Sound understanding of computer systems (hardware/software), networks etc.
    Experience in controlling information technology budget
    Excellent organizational and leadership skills
    Outstanding communication abilities
    BSc/BA in computer science, engineering or relevant field; MSc/MA will be a plus

Frequently asked questions
What does an IT Director do?

IT Directors make sure that employees can meet all the technology needs of an organization. In addition, they provide strategic leadership on projects, directing their team's efforts towards successful completion while meeting organizational goals along the way.
What are the duties and responsibilities of an IT Director?

The IT Director is responsible for assessing an organization's technology needs and making upgrade recommendations. Their role includes setting short-term goals, such as providing a list of new equipment installed in the next fiscal year or two.
What makes a good IT Director?

A successful IT director needs to have technical knowledge, communication, and leadership skills. They'll interact with employees on every level, from executive-level managers all way down. Whether in marketing or accounting, communicating can help sway opinions when making critical decisions about how things should run within an organization.
Who does an IT Director work with?

As IT Directors fulfill their proper duties throughout their day, most report to their CIO or Cheif Informant Officer. The CIO oversees the use of information throughout a company and monitors an IT team's progress as time goes on. 
    """

    ]}

    result = (
        client.query
        .get(class_name="Resume", properties=["text"])
        .with_near_text(nearText)
        .with_limit(1)
        .with_additional(['certainty'])
        .do()
    )

    result_resumes = [(r["text"], "CERTAINTY: {}".format(r['_additional']['certainty'])) for r in
                      result["data"]["Get"]["Resume"]]
    print(json.dumps(result_resumes, indent=4))

    print("--- %s seconds ---" % (time.time() - start_time))

    # result = (
    #     client.query
    #     .get("Question", ["question", "answer", "category"])
    #     .with_near_text(nearText)
    #     .with_limit(2)
    #     .do()
    # )
