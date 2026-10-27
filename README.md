# ECHO — Adaptive Deep Learning Tutor

ECHO is a student learning prototype designed to help learners practise Deep Learning concepts through quizzes, performance analysis, and targeted revision recommendations.

## Current Features

- Interactive Deep Learning quizzes
- Automatic answer checking and scoring
- Concept-wise performance dashboard
- Visual performance chart
- Targeted revision recommendations
- Downloadable learning report

## Technology Stack

- Python
- Streamlit
- Pandas
- Plotly

## Run Locally

1. Install Python.
2. Install the required packages:

   ```bash
   python -m pip install streamlit pandas plotly
   ```

3. Start the application:

   ```bash
   python -m streamlit run web_app.py
   ```

## Current Limitations

ECHO currently uses predefined questions and rule-based recommendations. It does not yet use a trained AI model. Quiz results are preliminary indicators of performance, not definitive measures of mastery.

## Planned Improvements

- Persistent student progress
- Improved adaptive question selection
- Concept dependency visualization
- Testing and evaluation of recommendation logic
