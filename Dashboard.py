import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Fitness Dashboard",
                   page_icon=":chart_with_upwards_trend:",
                   layout="wide")

st.sidebar.title("🏋️‍♀️ Fitness Dashboard Navigation")

# Sidebar page selection
page = st.sidebar.radio("Go to", ["📊 Fitness Analysis", "🧮 BMI Calculator"])

# ---------------- Page 1: Overview ----------------
if page == "📊 Fitness Analysis":
    df = pd.read_csv("cleaned_data.csv")

    # Sidebar
    st.sidebar.header("Please Filter here:")
    Gender = st.sidebar.multiselect(
        "Select the Gender:",
        options=df["Gender"].unique(),
        default=df["Gender"].unique()
        )
    st.sidebar.header("Please Filter here:")
    Workout = st.sidebar.multiselect(
        "Select the Workout:",
        options=df["Workout_Type"].unique(),
        default=df["Workout_Type"].unique()
        )
    st.sidebar.header("Please Filter here:")
    Experience = st.sidebar.multiselect(
        "Select the Experience:",
        options=df["Experience_Level"].unique(),
        default=df["Experience_Level"].unique()
        )
    # Age range slider in sidebar
    st.sidebar.header("Please Select the Age Range:")
    age_range = st.sidebar.slider(
        "Select age range:",
        min_value=18,
        max_value=60,
        value=(18, 40),  # Default range (adjusted to fit within 0-60)
        step=1
        )

    st.sidebar.write(f"Age range: {age_range[0]} to {age_range[1]} years")

    # Correct way to filter age range
    df_selection = df.query(
        "Gender == @Gender & Workout_Type == @Workout & Experience_Level == @Experience & "
        "Age >= @age_range[0] & Age <= @age_range[1]"
        )
    # Main-page
    st.title(":bar_chart: Fitness Dashboard")
    st.markdown("##")

    # KPI cards
    Avg_BMI = round(df["BMI"].mean(),2)
    Avg_Resting_BPM = round(df["Resting_BPM"].mean(),2)
    Avg_Water_intake = round(df["Water_Intake (liters)"].mean(),2)

    left_column,middle_column,right_column = st.columns(3)
    with left_column:
        st.subheader("Average BMI:")
        st.subheader(f"{Avg_BMI:,}")
    with middle_column:
        st.subheader("Average Resting BPM:")
        st.subheader(f"{Avg_Resting_BPM:,}")
    with right_column:
        st.subheader("Average Water Intake:")
        st.subheader(f"{Avg_Water_intake:,}")

    st.markdown("---")
    st.markdown("###")
    st.dataframe(df_selection)

    # Bar chat
    workout_age_counts = df_selection.groupby(['Workout_Type', 'Age']).size().reset_index(name='Count')

    fig_workout_age = px.bar(
        workout_age_counts,
        y='Age',
        x='Count',
        color='Workout_Type',
        title="<b>Workout Distribution by Age</b>",
        color_discrete_sequence=px.colors.qualitative.Set3,
        template="plotly_white",
        orientation="h"
    )

    fig_workout_age.update_layout(
        yaxis_title="Age",
        xaxis_title="Number of People",
        height=400
    )

    st.plotly_chart(fig_workout_age)

    # Pie chart 
    gender_workout_counts = df_selection.groupby(['Workout_Type', 'Gender']).size().reset_index(name='Count')

    # giving manual colors
    color_map = {
        'Cardio': '#FF6B6B',
        'Strength': '#4ECDC4', 
        'Yoga': '#45B7D1',
        'HIIT': '#96CEB4',
    }

    fig_pie_workout_gender = px.pie(
        gender_workout_counts,
        values='Count',
        names='Workout_Type',
        title="<b>Workout Type Distribution by Gender</b>",
        color='Workout_Type',
        color_discrete_map=color_map,
        template="plotly_white",
        facet_col='Gender'  # Creates separate pies for each gender
    )

    fig_pie_workout_gender.update_traces(
        textposition='inside',
        textinfo='percent+label'
    )

    st.plotly_chart(fig_pie_workout_gender)

    # Simple line plot - Calories vs Duration
    calories_duration = df.groupby('Session_Duration (hours)')['Calories_Burned'].mean().reset_index()

    fig_calories_duration = px.line(
        calories_duration,
        x='Session_Duration (hours)',
        y='Calories_Burned',
        title="<b>Calories Burned vs Workout Duration</b>",
        markers=True,  # Add markers to data points
        template="plotly_white"
    )

    fig_calories_duration.update_layout(
        xaxis_title="Workout Duration (hours)",
        yaxis_title="Calories Burned",
        height=500
    )

    st.plotly_chart(fig_calories_duration)

    # Count occurrences of each workout type
    workout_popularity = df_selection['Workout_Type'].value_counts().reset_index()
    workout_popularity.columns = ['Workout_Type', 'Count']

    # Create bar chart
    fig_workout_popularity = px.bar(
        workout_popularity,
        x='Count',
        y='Workout_Type',
        title="<b>Most Popular Workout Types</b>",
        color='Count',
        color_continuous_scale='Viridis',
        orientation='h',
        template="plotly_white"
    )

    fig_workout_popularity.update_layout(
        xaxis_title="Number of Participants",
        yaxis_title="Workout Type",
        yaxis={'categoryorder': 'total ascending'},  # Sort by popularity
        height=400
    )

    st.plotly_chart(fig_workout_popularity)

    # Donut chart for experience levels
    experience_counts = df_selection['Experience_Level'].value_counts().reset_index()
    experience_counts.columns = ['Experience_Level', 'Count']

    # Custom colors for each experience level
    color_map = {
        'Beginner': '#FF6B6B',      # Red for beginners
        'Intermediate': '#4ECDC4',   # Teal for intermediate
        'Advanced': '#45B7D1',       # Blue for advanced
    }

    fig_experience = px.pie(
        experience_counts,
        values='Count',
        names='Experience_Level',
        title="<b>Experience Level Breakdown</b>",
        color='Experience_Level',
        color_discrete_map=color_map,
        template="plotly_white",
        hole=0.4  # Creates donut chart
    )

    fig_experience.update_traces(
        textposition='inside',
        textinfo='percent+label',
        textfont_size=14
    )

    fig_experience.update_layout(
        annotations=[dict(text='Experience', x=0.5, y=0.5, font_size=16, showarrow=False)]
    )

    st.plotly_chart(fig_experience)

# ---------------- Page 2: BMI Calculator ----------------
elif page == "🧮 BMI Calculator":
    st.title("BMI Calculator 🧍‍♀️🧍‍♂️")

    # --- Input fields ---
    name = st.text_input("Enter your Name:")
    age = st.number_input("Enter your Age:", min_value=1, max_value=120, step=1)
    weight = st.number_input("Enter your Weight (kg):", min_value=1.0, max_value=300.0, step=0.5)
    height = st.number_input("Enter your Height (m):", min_value=0.5, max_value=2.5, step=0.01)

    # --- Calculate BMI ---
    if height > 0:
        bmi = weight / (height ** 2)

        # --- Determine BMI Category ---
        if bmi < 18.5:
            category = "Underweight"
            highlight = st.warning("You are Underweight 😟\nTry to include more nutrients and balanced meals.")
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
            highlight = st.success("You are in the Normal weight range ✅\nKeep maintaining a balanced lifestyle!")
        elif 25 <= bmi < 30:
            category = "Overweight"
            highlight = st.warning("You are Overweight ⚠️\nTry moderate exercise and a healthy diet.")
        else:
            category = "Obese"
            highlight = st.error("You are in the Obese range 🚨\nPlease consult a doctor or nutritionist.")

        # --- Create DataFrame including category ---
        data = {
            "Name": [name],
            "Age": [age],
            "Height (m)": [height],
            "Weight (kg)": [weight],
            "BMI": [round(bmi, 2)],
            "Result": [category]
        }

        df_bmi = pd.DataFrame(data)
    

        # Download button for CSV
        csv = df_bmi.to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name="user_health_data.csv",
            mime="text/csv",
            help="Click to download the data as CSV file"
        )

        # --- Display Table ---
        st.subheader("📋 Your BMI Result")
        st.table(df_bmi)

    else:
        st.info("Please enter your height to calculate BMI.")
