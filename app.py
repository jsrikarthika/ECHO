# ==========================================
# PROJECT ECHO
# Adaptive Learning System for Deep Learning
# ==========================================

print("=" * 45)
print("       WELCOME TO PROJECT ECHO")
print("=" * 45)

student_name = input("\nEnter your name: ")

print(f"\nHello, {student_name}!")
print("Welcome to your personalized learning journey.")

print("\nToday's topic: Artificial Neural Networks")

print("\nLet's test your knowledge!")

print("\nQuestion 1:")
print("What is the main purpose of an activation function?")

print("\nA. To store data")
print("B. To introduce non-linearity")
print("C. To delete neurons")
print("D. To increase dataset size")

answer = input("\nEnter your answer (A/B/C/D): ").strip().upper()

if answer == "B":
    print("\nCorrect! Great job!")
    print("You understand the basic purpose of activation functions.")
else:
    print("\nNot quite! The correct answer is B.")
    print("Activation functions introduce non-linearity into neural networks.")

print("\nThank you for using PROJECT ECHO!")