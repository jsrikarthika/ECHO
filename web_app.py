import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------
# ECHO: Adaptive Deep Learning Tutor
# ---------------------------------------

st.set_page_config(
    page_title="ECHO | Smart Learning",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 ECHO")
st.subheader("Adaptive Deep Learning Learning System")
st.write(
    "Learn Deep Learning through quizzes, concept mastery "
    "tracking, and personalized revision recommendations."
)

st.divider()

# Question bank
questions = [
    {
        "concept": "Neural Networks",
        "question": "What is the main purpose of an activation function?",
        "options": [
            "A. Store data",
            "B. Introduce non-linearity",
            "C. Delete neurons",
            "D. Increase dataset size"
        ],
        "answer": "B. Introduce non-linearity",
        "explanation": (
            "Activation functions introduce non-linearity, "
            "allowing neural networks to learn complex patterns."
        )
    },
    {
        "concept": "Backpropagation",
        "question": "What is the main purpose of backpropagation?",
        "options": [
            "A. Load a dataset",
            "B. Visualize images",
            "C. Calculate gradients for updating weights",
            "D. Remove hidden layers"
        ],
        "answer": "C. Calculate gradients for updating weights",
        "explanation": (
            "Backpropagation calculates gradients of the loss "
            "with respect to model parameters."
        )
    },
    {
        "concept": "Loss Functions",
        "question": "What does a loss function measure?",
        "options": [
            "A. Model prediction error",
            "B. Number of training files",
            "C. Screen resolution",
            "D. Number of users"
        ],
        "answer": "A. Model prediction error",
        "explanation": (
            "A loss function measures how different predictions "
            "are from the target values."
        )
    },
    {
        "concept": "Gradient Descent",
        "question": "What is the purpose of gradient descent?",
        "options": [
            "A. Increase every weight",
            "B. Sort the training data",
            "C. Create labels",
            "D. Minimize the loss by updating parameters"
        ],
        "answer": "D. Minimize the loss by updating parameters",
        "explanation": (
            "Gradient descent updates model parameters in a "
            "direction intended to reduce the loss."
        )
    },
    {
        "concept": "Overfitting",
        "question": "What is overfitting?",
        "options": [
            "A. The model cannot load data",
            "B. The model performs well on training data but poorly on unseen data",
            "C. The model has no parameters",
            "D. The dataset contains no labels"
        ],
        "answer": "B. The model performs well on training data but poorly on unseen data",
        "explanation": (
            "An overfit model learns training-specific patterns "
            "that do not generalize well to unseen examples."
        )
    },
    {
        "concept": "CNNs",
        "question": "What is a convolutional neural network commonly used for?",
        "options": [
            "A. Image-related tasks",
            "B. Only sorting numbers",
            "C. Managing computer folders",
            "D. Replacing every database"
        ],
        "answer": "A. Image-related tasks",
        "explanation": (
            "CNNs learn spatial features and are commonly used "
            "for image classification and other vision tasks."
        )
    }
]
# Additional questions for adaptive practice
adaptive_questions = {
    "Neural Networks": {
        "easy": {
            "question": "Which part of a neuron applies an activation function?",
            "options": [
                "A. The activation stage",
                "B. The dataset filename",
                "C. The computer monitor",
                "D. The file extension"
            ],
            "answer": "A. The activation stage",
            "explanation": (
                "The activation function transforms a neuron's "
                "weighted input and bias."
            )
        },
        "hard": {
            "question": (
                "Why are nonlinear activation functions important "
                "in multilayer neural networks?"
            ),
            "options": [
                "A. They eliminate all training data",
                "B. They allow networks to learn nonlinear relationships",
                "C. They guarantee zero training error",
                "D. They remove the need for weights"
            ],
            "answer": (
                "B. They allow networks to learn nonlinear relationships"
            ),
            "explanation": (
                "Without nonlinear activations, stacking ordinary "
                "linear layers would still produce a linear transformation."
            )
        }
    },
    "Backpropagation": {
        "easy": {
            "question": "What does backpropagation calculate?",
            "options": [
                "A. Screen brightness",
                "B. File size",
                "C. Gradients of the loss with respect to parameters",
                "D. The number of folders"
            ],
            "answer": "C. Gradients of the loss with respect to parameters",
            "explanation": (
                "Backpropagation calculates gradients used to update "
                "the network's parameters during training."
            )
        },
        "hard": {
            "question": (
                "In standard backpropagation, what is propagated "
                "backward through the network?"
            ),
            "options": [
                "A. Only the training images",
                "B. The loss gradients using the chain rule",
                "C. The file directory",
                "D. Random labels"
            ],
            "answer": "B. The loss gradients using the chain rule",
            "explanation": (
                "The chain rule is used to calculate how the loss "
                "changes with respect to parameters in earlier layers."
            )
        }
    },
    "Loss Functions": {
        "easy": {
            "question": "What does a loss function help measure?",
            "options": [
                "A. Prediction error",
                "B. Keyboard speed",
                "C. Monitor size",
                "D. Internet speed"
            ],
            "answer": "A. Prediction error",
            "explanation": (
                "A loss function quantifies the discrepancy between "
                "predictions and target values."
            )
        },
        "hard": {
            "question": (
                "Which loss function is commonly used for multiclass "
                "classification with mutually exclusive classes?"
            ),
            "options": [
                "A. Mean absolute error in every situation",
                "B. File compression loss",
                "C. Cross-entropy loss",
                "D. Image resizing loss"
            ],
            "answer": "C. Cross-entropy loss",
            "explanation": (
                "Cross-entropy loss is commonly used to evaluate "
                "predicted class probabilities against target classes."
            )
        }
    },
    "Gradient Descent": {
        "easy": {
            "question": "What does gradient descent update during training?",
            "options": [
                "A. The computer wallpaper",
                "B. Model parameters",
                "C. The Python installation",
                "D. The student's name"
            ],
            "answer": "B. Model parameters",
            "explanation": (
                "Gradient descent updates model parameters to reduce "
                "the objective being optimized."
            )
        },
        "hard": {
            "question": (
                "What can happen if the learning rate is excessively high?"
            ),
            "options": [
                "A. The model always becomes perfect",
                "B. The dataset disappears",
                "C. The loss is guaranteed to be zero",
                "D. Optimization may overshoot or diverge"
            ],
            "answer": "D. Optimization may overshoot or diverge",
            "explanation": (
                "An excessively high learning rate can cause unstable "
                "updates and prevent convergence."
            )
        }
    },
    "Overfitting": {
        "easy": {
            "question": "Which is a common sign of overfitting?",
            "options": [
                "A. High training performance but poor validation performance",
                "B. No training data",
                "C. No model parameters",
                "D. A computer with a large monitor"
            ],
            "answer": (
                "A. High training performance but poor validation performance"
            ),
            "explanation": (
                "Overfitting often appears when training performance "
                "is strong but performance on unseen data is poor."
            )
        },
        "hard": {
            "question": (
                "Which approach can help reduce overfitting?"
            ),
            "options": [
                "A. Memorize the test labels",
                "B. Always increase model complexity",
                "C. Use regularization and validation-based model selection",
                "D. Remove all validation checks"
            ],
            "answer": (
                "C. Use regularization and validation-based model selection"
            ),
            "explanation": (
                "Regularization and validation-based model selection "
                "can help improve generalization."
            )
        }
    },
    "CNNs": {
        "easy": {
            "question": "What does a convolutional layer learn?",
            "options": [
                "A. Computer passwords",
                "B. Visual patterns and features",
                "C. Folder names",
                "D. Internet addresses"
            ],
            "answer": "B. Visual patterns and features",
            "explanation": (
                "Convolutional layers learn spatial patterns such as "
                "edges, textures, and more complex visual features."
            )
        },
        "hard": {
            "question": (
                "What is a key benefit of weight sharing in a convolutional layer?"
            ),
            "options": [
                "A. It removes all computation",
                "B. It guarantees perfect predictions",
                "C. It eliminates the need for training",
                "D. It reduces parameters by reusing filters across spatial positions"
            ],
            "answer": (
                "D. It reduces parameters by reusing filters across spatial positions"
            ),
            "explanation": (
                "A convolutional filter uses shared weights across "
                "different spatial locations."
            )
        }
    }
}

# Initialize session data
if "results" not in st.session_state:
    st.session_state.results = {}

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

# Student profile
st.header("👩‍🎓 Student Profile")

name = st.text_input(
    "Enter your name",
    value=st.session_state.student_name,
    placeholder="Your name"
)

st.session_state.student_name = name

st.divider()

# Quiz
st.header("📝 Deep Learning Assessment")
st.write("Answer the questions below to assess your current understanding.")

with st.form("quiz_form"):
    answers = {}

    for index, question in enumerate(questions):
        st.markdown(f"### Question {index + 1}")
        st.caption(f"Concept: {question['concept']}")

        answers[question["concept"]] = st.radio(
            question["question"],
            question["options"],
            index=None,
            key=f"answer_{index}"
        )

    submitted = st.form_submit_button(
        "Submit Assessment",
        type="primary"
    )

if submitted:
    if not name.strip():
        st.warning("Please enter your name before submitting.")
    elif any(value is None for value in answers.values()):
        st.warning("Please answer every question before submitting.")
    else:
        st.session_state.results = {
            concept: {
                "correct": answer == next(
                    q["answer"] for q in questions
                    if q["concept"] == concept
                ),
                "selected": answer
            }
            for concept, answer in answers.items()
        }

        st.success("Assessment submitted successfully!")

# Results
if st.session_state.results:
    results = st.session_state.results

    score = sum(
        result["correct"] for result in results.values()
    )
    total = len(results)
    percentage = score / total * 100

    st.divider()
    st.header("📊 Your Learning Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Correct Answers", f"{score}/{total}")
    col2.metric("Assessment Score", f"{percentage:.1f}%")
    col3.metric(
        "Concepts to Revise",
        sum(not r["correct"] for r in results.values())
    )

    st.progress(percentage / 100)

    # Concept mastery table
    st.subheader("🎯 Concept-wise Mastery")

    mastery_data = []

    for question in questions:
        concept = question["concept"]
        correct = results[concept]["correct"]

        mastery_data.append({
            "Concept": concept,
            "Status": "Mastered in this quiz" if correct else "Needs revision",
            "Score (%)": 100 if correct else 0
        })

    mastery_df = pd.DataFrame(mastery_data)

    st.dataframe(
        mastery_df,
        use_container_width=True,
        hide_index=True
    )
        # Interactive concept performance chart
    st.subheader("📈 Concept Performance Overview")

    fig = px.bar(
        mastery_df,
        x="Concept",
        y="Score (%)",
        color="Status",
        range_y=[0, 100],
        text="Score (%)",
        title="Your Performance Across Deep Learning Concepts",
        labels={
            "Concept": "Deep Learning Concept",
            "Score (%)": "Performance (%)"
        }
    )

    fig.update_layout(
        xaxis_tickangle=-30,
        yaxis_title="Performance (%)",
        xaxis_title="Concept",
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)
    # Personalized recommendations
    st.subheader("💡 Your Revision Recommendations")

    weak_concepts = [
        concept for concept, result in results.items()
        if not result["correct"]
    ]

    if weak_concepts:
        st.write(
            "Based on your incorrect answers, start by revising:"
        )

        for concept in weak_concepts:
            explanation = next(
                q["explanation"] for q in questions
                if q["concept"] == concept
            )

            with st.expander(f"📚 Revise: {concept}"):
                st.write(explanation)

        st.info(
            "These recommendations are based on your answers "
            "to this assessment, not on a trained AI model."
        )
    else:
        st.success(
            "Excellent! You answered every question correctly. "
            "Try a more advanced assessment next."
        )

    # Download results
    report = mastery_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Your Learning Report",
        data=report,
        file_name="echo_learning_report.csv",
        mime="text/csv"
    )

st.divider()

st.caption(
    "ECHO | Adaptive Learning Prototype | Python + Streamlit + Pandas"
)
# ---------------------------------------
# ECHO ADAPTIVE PRACTICE ENGINE
# ---------------------------------------

st.divider()
st.header("🎯 Adaptive Practice Engine")

st.write(
    "ECHO uses your assessment results to recommend "
    "a follow-up question for concepts that need revision."
)

if st.session_state.results:

    results = st.session_state.results

    weak_concepts = [
        concept
        for concept, result in results.items()
        if not result["correct"]
    ]

    strong_concepts = [
        concept
        for concept, result in results.items()
        if result["correct"]
    ]

    if weak_concepts:
        st.subheader("📚 Recommended Practice")

        selected_concept = st.selectbox(
            "Choose a concept to practise",
            weak_concepts,
            key="adaptive_concept"
        )

        st.info(
            f"ECHO recommends reviewing {selected_concept} "
            "because your initial answer was incorrect."
        )

        difficulty = st.radio(
            "Choose practice difficulty",
            ["Easy", "Hard"],
            horizontal=True,
            key="adaptive_difficulty"
        )

        question_data = adaptive_questions[selected_concept][
            difficulty.lower()
        ]

        st.markdown(f"### {question_data['question']}")

        practice_answer = st.radio(
            "Select your answer",
            question_data["options"],
            index=None,
            key="adaptive_practice_answer"
        )

        if st.button("Check Practice Answer"):

            if practice_answer is None:
                st.warning("Please select an answer first.")

            elif practice_answer == question_data["answer"]:
                st.success("Correct! 🎉")
                st.write(question_data["explanation"])

            else:
                st.error("Not quite. Let's review the concept.")
                st.write(
                    f"Correct answer: {question_data['answer']}"
                )
                st.write(question_data["explanation"])

    else:
        st.success(
            "You answered all initial questions correctly! "
            "Try harder practice questions to challenge yourself."
        )

        selected_concept = st.selectbox(
            "Choose a concept for advanced practice",
            strong_concepts,
            key="advanced_concept"
        )

        question_data = adaptive_questions[selected_concept]["hard"]

        st.markdown(f"### {question_data['question']}")

        advanced_answer = st.radio(
            "Select your answer",
            question_data["options"],
            index=None,
            key="advanced_practice_answer"
        )

        if st.button("Check Advanced Answer"):

            if advanced_answer is None:
                st.warning("Please select an answer first.")

            elif advanced_answer == question_data["answer"]:
                st.success("Correct! 🎉")
                st.write(question_data["explanation"])

            else:
                st.error("Not quite. Review the explanation below.")
                st.write(
                    f"Correct answer: {question_data['answer']}"
                )
                st.write(question_data["explanation"])

else:
    st.info(
        "Complete and submit the initial assessment to receive "
        "personalized practice recommendations."
    )