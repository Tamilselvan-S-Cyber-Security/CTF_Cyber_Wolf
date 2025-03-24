import streamlit as st
import time
from datetime import datetime, timedelta

def initialize_timer(category, minutes):
    """Initialize the timer for a category challenge."""
    # Set the end time for the timer
    current_time = datetime.now()
    end_time = current_time + timedelta(minutes=minutes)
    st.session_state.timer_end = end_time.timestamp()
    st.session_state.timer_category = category
    st.session_state.timer_total_minutes = minutes

def get_remaining_time():
    """Get the remaining time in seconds."""
    if 'timer_end' not in st.session_state:
        return 0
    
    current_time = datetime.now().timestamp()
    remaining = st.session_state.timer_end - current_time
    
    return max(0, remaining)

def format_time(seconds):
    """Format seconds into a readable time string (HH:MM:SS)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def display_timer():
    """Display the countdown timer in the sidebar."""
    remaining_seconds = get_remaining_time()
    
    if remaining_seconds <= 0:
        st.error("Time's up!")
        return
    
    # Show remaining time
    formatted_time = format_time(remaining_seconds)
    
    # Calculate progress percentage
    if 'timer_total_minutes' in st.session_state:
        total_seconds = st.session_state.timer_total_minutes * 60
        progress = 1 - (remaining_seconds / total_seconds)
    else:
        progress = 0
    
    # Display timer with progress bar
    st.markdown("### Time Remaining")
    st.progress(progress)
    st.markdown(f"<h2 style='text-align: center;'>{formatted_time}</h2>", unsafe_allow_html=True)
    
    # Warning when time is running low
    if remaining_seconds < 300:  # Less than 5 minutes
        st.warning("⚠️ Less than 5 minutes remaining!")

def check_timer_expired():
    """Check if the timer has expired."""
    if 'timer_end' not in st.session_state:
        return False
    
    current_time = datetime.now().timestamp()
    return current_time >= st.session_state.timer_end
