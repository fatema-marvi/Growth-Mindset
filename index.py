import streamlit as st
import random

# Title and Introduction
st.title("🌱 Growth Mindset Challenge")
st.subheader("Empower Yourself to Learn and Grow!")

# Introduction Section
st.markdown("""
A **growth mindset** is the belief that your abilities can be developed through dedication, hard work, and learning from mistakes.

**Adopt the growth mindset and unlock your potential!**
""")

# Motivational Quotes
growth_quotes = [
    "Mistakes are proof that you are trying.",
    "Every expert was once a beginner.",
    "Success is the sum of small efforts repeated day in and day out.",
    "It’s not about being the best, it’s about being better than you were yesterday."
]

if st.button("💡 Inspire Me!"):
    st.success(random.choice(growth_quotes))

# Daily Goal Tracker
st.header("🎯 Daily Goal Tracker")
daily_goal = st.text_input("Set your learning goal for today:")

if daily_goal:
    st.success(f"Great goal! Stay focused on: {daily_goal}")

# Interactive Quiz
st.header("🧠 Quick Quiz: Do You Have a Growth Mindset?")
question = st.radio(
    "How do you handle failure?",
    ("I give up", "I try to learn from my mistakes", "I ignore it and move on")
)

if question == "I try to learn from my mistakes":
    st.success("That's the spirit of a growth mindset!")
else:
    st.warning("Consider viewing failures as opportunities to learn.")

# Reflection Section
st.header("📝 Reflect on Your Learning")
reflection = st.text_area("What did you learn today?")
if st.button("Save Reflection"):
    st.success("Reflection saved! Keep learning and growing.")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and UV.")
