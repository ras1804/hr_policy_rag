"""run form here"""

from hr_assistant.pipeline import ask, build_hr_assistant
from hr_assistant.logger import get_logger


logger = get_logger(__name__)

def main():
    logger.info("Building the HR policy assistant")
    agent = build_hr_assistant()

    demo_questions = [
        "How many paid annual leaves do I get?",
        "What is the notice period during probation?",
        "Can I work form home every day?"
    ]

    for question in demo_questions:
        print("="*60)
        print(f'Question: {question}')
        print("-"*60)
        answer = ask(agent, question)
        print(f'ANSWER:', answer)
        print("="*60)


if __name__ == "__main__":
    main()