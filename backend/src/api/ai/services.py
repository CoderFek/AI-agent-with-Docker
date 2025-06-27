from api.ai.llms import get_openai_llm
from api.ai.schemas import EmailMessageSchema


def generate_email_message(query:str) -> EmailMessageSchema:
    llm_base = get_openai_llm()
    llm = llm_base.with_structured_output(EmailMessageSchema)

    messages = [
        (
            "system",
            "You are a helpful assistant for research and composing plaintext emails. Structure your response like this: {\"subject\": \"...\", \"contexts\": \"...\", \"invalid_request\": false}. Your reply must be pure JSON.",

        ),
        (
            "human", f"{query}. Do not use markdown in your response only plaintext."
        )
    ]

    response = llm.invoke(messages)
    return response