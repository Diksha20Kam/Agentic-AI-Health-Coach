from agents.goal_planner import get_goals
from agents.diet_exercise_advisor import suggest_diet_and_workout
from agents.feedback_learner import update_plan_based_on_feedback

if __name__ == "__main__":
    print("Welcome to your Agentic Health Coach!")

    user_input = input("Describe your health goal (e.g., I want to lose 5kg in 2 months):\n")
    goals = get_goals(user_input)
    print("\nGenerated Plan:", goals)

    today_plan = suggest_diet_and_workout(goals)
    print("\nToday's Plan:", today_plan)

    feedback = input("\nHow did you feel about today's plan?\n")
    new_plan = update_plan_based_on_feedback(goals, feedback)
    print("\nUpdated Plan:", new_plan)