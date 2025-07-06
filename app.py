import streamlit as st
from agents.goal_planner import get_goals
from agents.diet_exercise_advisor import suggest_diet_and_workout
from agents.feedback_learner import update_plan_based_on_feedback

st.title("🏋️‍♀️ Agentic AI Health Coach")

user_input = st.text_input("Enter your health goal:", "I want to lose 5kg in 2 months")

if st.button("Generate Plan"):
    goals = get_goals(user_input)
    st.subheader("📋 Generated Plan")
    st.write(goals)

    today_plan = suggest_diet_and_workout(goals)
    st.subheader("💡 Today's Recommendation")
    st.write(today_plan)

    feedback = st.text_input("How did you feel about today's plan?")
    if st.button("Update Plan with Feedback"):
        updated = update_plan_based_on_feedback(goals, feedback)
        st.subheader("🔁 Updated Plan")
        st.write(updated)
