
import streamlit as st

# App title
st.title("HydroFuel 💧")
st.subheader("Highlighting hydration as fuel for performance and recovery")

# Input fields
name = st.text_input("Enter your name:")
weight_unit = st.selectbox("Select your weight unit:", ["Kilograms (kg)", "Pounds (lb)"])
weight = st.number_input("Enter your weight:", min_value=1.0, step=0.1)
workout_minutes = st.number_input("Enter workout duration (in minutes):", min_value=0, step=10)
intensity = st.selectbox("Select workout intensity:", ["Low", "Moderate", "High"])

# Conversion factors
kg_to_lb = 2.205
oz_to_liters = 33.814
cups_to_oz = 8

# Dehydration performance loss factors
performance_loss_percentage = 25
fluid_loss_percentage_threshold = 2

# Calculate water intake
if name and weight > 0:
    # Convert weight to pounds if the input is in kilograms
    if weight_unit == "Kilograms (kg)":
        weight_lb = weight * kg_to_lb
    else:
        weight_lb = weight

    # Base water intake (2/3 of body weight in ounces)
    base_water_oz = weight_lb * (2 / 3)

    # Workout hydration (7–10 ounces every 10–20 minutes)
    workout_intervals = workout_minutes / 10
    workout_water_oz = workout_intervals * 7  # Minimum hydration
    max_workout_water_oz = workout_intervals * 10  # Maximum hydration

    # Post-workout hydration (2–3 cups)
    post_workout_water_oz = 2 * cups_to_oz  # Minimum
    max_post_workout_water_oz = 3 * cups_to_oz  # Maximum

    # Total daily water intake
    total_water_oz = base_water_oz + workout_water_oz + post_workout_water_oz
    total_water_liters = total_water_oz / oz_to_liters

    # Dehydration risk calculation
    fluid_loss_oz = weight_lb * (fluid_loss_percentage_threshold / 100)
    endurance_reduction = "from 121 to 55 minutes" if intensity == "High" else "minimal at lower intensities"

    # Display results
    st.subheader(f"Hello, {name}!")
    st.write(f"Based on your weight of **{weight:.2f} {weight_unit} ({weight_lb:.2f} lb)** and a workout duration of **{workout_minutes} minutes**:")

    st.write(f"- **Daily Water Intake (Base):** {base_water_oz:.2f} ounces ({base_water_oz / oz_to_liters:.2f} liters)")
    st.write(f"- **Workout Water Intake:** {workout_water_oz:.2f}–{max_workout_water_oz:.2f} ounces ({workout_water_oz / oz_to_liters:.2f}–{max_workout_water_oz / oz_to_liters:.2f} liters)")
    st.write(f"- **Post-Workout Hydration:** {post_workout_water_oz:.2f}–{max_post_workout_water_oz:.2f} ounces ({post_workout_water_oz / oz_to_liters:.2f}–{max_post_workout_water_oz / oz_to_liters:.2f} liters)")
    st.write(f"- **Total Daily Water Intake:** {total_water_oz:.2f} ounces ({total_water_liters:.2f} liters)")

    # Dehydration risk alert
    st.warning(f"⚠️ Losing 2% of your body weight in fluid ({fluid_loss_oz:.2f} ounces) can decrease performance by **{performance_loss_percentage}%**.")
    st.write(f"- **Impact on Endurance:** Your endurance may reduce {endurance_reduction} if dehydrated.")

    # Concentration improvement insights
    st.info("💡 Staying hydrated enhances concentration and nervous system efficiency, improving workout performance and recovery.")

    st.success(f"Stay hydrated and perform at your best, {name}!")
else:
    st.info("Please enter your name, weight, and workout duration to calculate your water intake.")

# Disclaimer
st.divider()
st.caption(
    "⚠️ **Disclaimer:** The hydration recommendations provided by HydroFuel are for general guidance only. "
    "Always consult with a healthcare professional or doctor to determine the most suitable hydration needs "
    "based on your specific health conditions, activity level, and other factors."
)
