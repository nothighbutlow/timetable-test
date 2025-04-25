import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, DAILY

TERM_1_START = datetime(2025, 1, 6)
TERM_2_START = datetime(2025, 3, 24)
WEEKS_PER_TERM = 10
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
TIME_SLOTS = [
    "7:30 - 8:00", "8:00 - 8:30", "8:30 - 9:00", "9:00 - 9:30", "9:30 - 10:00",
    "10:00 - 10:30", "10:30 - 11:00", "11:00 - 11:30", "11:30 - 12:00",
    "12:00 - 12:30", "12:30 - 13:00", "13:00 - 13:30", "13:30 - 14:00",
    "14:00 - 14:30", "14:30 - 15:00", "15:00 - 15:30", "15:30 - 16:00",
    "16:00 - 16:30", "16:30 - 17:00", "17:00 - 17:30", "17:30 - 18:00",
    "18:00 - 18:30"
]

def generate_weeks(start_date):
    weeks = []
    for i in range(WEEKS_PER_TERM):
        week_start = start_date + timedelta(weeks=i)
        week_label = f"Week {i+1} ({week_start.strftime('%d %b')})"
        week_days = [(week_start + timedelta(days=j)).strftime('%a %d %b') for j in range(5)]
        weeks.append((week_label, week_days))
    return weeks

st.title("📘 AISS Semester Timetable Viewer")

term = st.radio("Select Term", ["Term 1", "Term 2"], horizontal=True)
weeks = generate_weeks(TERM_1_START if term == "Term 1" else TERM_2_START)

week_labels = [w[0] for w in weeks]
selected_week = st.selectbox("Select Week", week_labels)
selected_dates = dict(weeks)[selected_week]

st.subheader(f"🗓️ {selected_week}")

# Display table
st.write("### Timetable")

columns = st.columns(len(DAYS) + 1)
columns[0].markdown("**Time**")
for i, day in enumerate(selected_dates):
    columns[i + 1].markdown(f"**{day}**")

for slot in TIME_SLOTS:
    row = st.columns(len(DAYS) + 1)
    row[0].markdown(f"{slot}")
    for i in range(1, len(row)):
        row[i].markdown("\u200b")  # Empty cell placeholder
