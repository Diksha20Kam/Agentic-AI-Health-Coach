def update_plan_based_on_feedback(goals, feedback):
    if not isinstance(goals, dict):
        return goals

    adjustments = ""
    if "tired" in feedback.lower():
        adjustments += "Reduced steps by 10%. "
        if "daily_steps" in goals:
            goals["daily_steps"] = int(goals["daily_steps"] * 0.9)
    if "easy" in feedback.lower():
        adjustments += "Increased steps by 10%. "
        if "daily_steps" in goals:
            goals["daily_steps"] = int(goals["daily_steps"] * 1.1)
    goals["feedback_notes"] = feedback
    goals["adjustments"] = adjustments or "No changes made."

    return goals

