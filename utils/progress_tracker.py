def track_progress(user_data):
    avg_steps = sum([int(row['steps']) for row in user_data]) / len(user_data)
    return f"Average steps this week: {avg_steps}"