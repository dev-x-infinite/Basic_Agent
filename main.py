import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="")

# Start chat for history + context
chat = genai.GenerativeModel("gemini-1.5-flash").start_chat(history=[])

def refine_with_critique(query, rounds=3):
    # Step 1: Initial draft (Writer)
    chat.send_message(query)
    current_answer = chat.last.text
    print(f"Initial Draft:\n{current_answer}\n")

    # Step 2: Loop with critic + refiner
    for i in range(rounds):
        # Critic step
        critique_prompt = f"""
Here is the current answer:
\"\"\"{current_answer}\"\"\"

Critique this answer in terms of clarity, accuracy, and beginner-friendliness. 
List weaknesses and give it a score out of 10.
"""
        chat.send_message(critique_prompt)
        critique = chat.last.text

        print(f"Critique {i+1}:\n{critique}\n")

        # Refiner step
        refinement_prompt = f"""
Here is the current answer:
\"\"\"{current_answer}\"\"\"

Here is the critique:
\"\"\"{critique}\"\"\"

Task: Rewrite the answer to address the critique. 
Make it clearer, more accurate, and more beginner-friendly.
"""
        chat.send_message(refinement_prompt)
        current_answer = chat.last.text

        print(f"Refined Answer {i+1}:\n{current_answer}\n")

    return current_answer


# Test the self-critique loop
n = input("enter your query :")
y = int(input("enter number of rounds :"))
final = refine_with_critique(n, y)
print("✅ Final Polished Answer:\n", final)
