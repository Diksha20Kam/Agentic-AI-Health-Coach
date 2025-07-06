def track_progress(user_data):
    last_7_days = user_data.tail(7)
    avg_steps = last_7_days["steps"].mean()
    avg_calories = last_7_days["calories_burned"].mean()
    weight_change = last_7_days["weight_kg"].iloc[-1] - last_7_days["weight_kg"].iloc[0]

    return {
        "Average Steps (7 days)": int(avg_steps),
        "Average Calories Burned (7 days)": int(avg_calories),
        "Weight Change (7 days)": round(weight_change, 2)
    }