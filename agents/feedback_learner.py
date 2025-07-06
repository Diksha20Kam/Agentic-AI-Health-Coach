def update_plan_based_on_feedback(goals, feedback):
    if "tired" in feedback.lower():
        if isinstance(goals, dict) and "daily_steps" in goals:
            goals["daily_steps"] = int(goals["daily_steps"] * 0.9)
    return goals