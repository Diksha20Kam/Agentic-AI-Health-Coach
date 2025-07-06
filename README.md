# Agentic AI Personal Health Coach

## 🧠 Overview
A proactive AI agent system to guide users in achieving their health goals using autonomous planning and feedback-driven adaptation.

## 🚀 Features
- Goal planning agent (LLM-based using LLaMA 2)
- Meal & exercise planner
- Feedback learning loop
- Tracks user progress

## 🛠️ Tech Stack
- Python, Hugging Face Transformers (LLaMA 2)
- LangChain, Streamlit/CLI

## 📦 How to Run
```bash
conda create -n agentic_ai python=3.10 -y
conda activate agentic_ai
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Project Structure
```
agentic-health-coach/
├── app.py
├── agents/
│   ├── goal_planner.py
│   ├── diet_exercise_advisor.py
│   └── feedback_learner.py
├── utils/
│   └── progress_tracker.py
├── data/
│   └── user_data.csv
├── prompts/
│   └── base_prompt.txt
└── README.md
```

