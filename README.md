# Gemini Self-Refining AI Agent

This project is a simple **AI agent using Google Gemini** that generates an initial answer to a user query and then **iteratively critiques and refines it** to produce a more polished final response.  

The workflow follows a **Writer → Critic → Refiner** loop:
1. **Writer**: Generates the first draft answer.  
2. **Critic**: Evaluates the answer for clarity, accuracy, and beginner-friendliness, then gives feedback and a score.  
3. **Refiner**: Rewrites the answer to address the critique.  

This loop repeats for a user-defined number of rounds, ensuring the final answer is improved step by step.  

---

## 🚀 Features
- Uses **Google Gemini (1.5-flash)** via the official SDK.  
- Supports **iterative self-critique and refinement**.  
- User can define:
  - Query (e.g., *“Explain black holes in simple terms”*)  
  - Number of refinement rounds.  
- Produces a **final polished answer** after all iterations.  

---

## 📦 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/gemini-self-refining-agent.git
   cd gemini-self-refining-agent
   ```

2. Install dependencies:
   ```bash
   pip install google-generativeai
   ```

3. Get your **Gemini API key** from [Google AI Studio](https://aistudio.google.com/).

---

## ⚡ Usage
1. Add your API key inside the script:
   ```python
   genai.configure(api_key="YOUR_API_KEY_HERE")
   ```

2. Run the script:
   ```bash
   python agent.py
   ```

3. Enter your query and number of refinement rounds when prompted:
   ```
   enter your query : Explain quantum computing in simple terms
   enter number of rounds : 3
   ```

4. The program will show:
   - Initial Draft  
   - Critiques for each round  
   - Refined answers for each round  
   - ✅ Final polished answer  

---

## 📖 Example Run
**Input:**
```
Query: Explain black holes simply
Rounds: 2
```

**Output (shortened):**
```
Initial Draft:
A black hole is a region of space where gravity is so strong that nothing can escape.

Critique 1:
The answer is clear but lacks analogy and beginner explanation. Score: 6/10.

Refined Answer 1:
A black hole is a place in space with gravity so strong that even light cannot escape. Imagine it like a cosmic vacuum cleaner pulling in everything nearby.

✅ Final Polished Answer:
[... improved text ...]
```

---

## 🛠️ How It Works
- Built with **Python** + **Google Generative AI SDK**.  
- Uses Gemini’s **chat mode** for context and history.  
- Alternates between:
  - Asking Gemini to critique its own output.  
  - Asking Gemini to refine the output based on that critique.  

---

 




