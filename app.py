import streamlit as st
import time
from datetime import datetime, timedelta
import pyrebase
import pandas as pd
import json

# Import local modules
from auth import logout_user  # We only need logout functionality
from challenges import display_challenges, check_flag
from timer import display_timer, initialize_timer, check_timer_expired, auto_close_challenges
from utils import initialize_session_state, calculate_score, get_user_progress
from styles import apply_styles
from data.easy_challenges import easy_challenges
from data.medium_challenges import medium_challenges

# Page configuration
st.set_page_config(
    page_title="CTF Challenge Platform | Created by S.Tamilselvan",
    page_icon="🚩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styles
apply_styles()

# Initialize session state variables
initialize_session_state()

# Firebase configuration
firebase_config = {
    "apiKey": "AIzaSyBHvGu2v_2k7EXpCATDPjpNN3eTQFh6qRA",
    "authDomain": "cyber-wolf-0jkuwe.firebaseapp.com",
    "projectId": "cyber-wolf-0jkuwe",
    "storageBucket": "cyber-wolf-0jkuwe.firebasestorage.app",
    "messagingSenderId": "928367001088",
    "appId": "1:928367001088:web:13c28470f09863292fe2e5",
    "databaseURL": "https://cyber-wolf-0jkuwe-default-rtdb.firebaseio.com"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def main():
    # Display header with logo
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown(
            """
            <div style="text-align: center">
                <h1>🚩 CTF Challenge Platform</h1>
                <p>Created by S.Tamilselvan</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # Auto-authenticate the user (no login required)
    if not st.session_state.authenticated:
        # Set authentication status directly
        st.session_state.authenticated = True
        st.session_state.user_info = {
            'uid': 'player_123',
            'name': 'Player'
        }
        
        # Initialize user's challenge progress
        if 'solved_challenges' not in st.session_state:
            st.session_state.solved_challenges = {}
    
    # Display sidebar
    with st.sidebar:
        st.write(f"👋 Welcome, Player")
        
        # Display user score
        total_score = calculate_score()
        st.metric("Total Score", f"{total_score} pts")
        
        # Display timer for current category
        if st.session_state.active_category:
            display_timer()
            
            # Display challenge progress
            progress = get_user_progress()
            if st.session_state.active_category == "easy":
                total_challenges = len(easy_challenges)
            else:
                total_challenges = len(medium_challenges)
                
            st.write("---")
            st.markdown("### Progress")
            solved = progress['solved']
            attempted = progress['attempted']
            
            # Show progress metrics
            st.write(f"✅ Solved: {solved}/{total_challenges}")
            st.write(f"⚠️ Attempted: {attempted}")
            st.write(f"🔄 Remaining: {total_challenges - attempted}")
            
            # Progress bar
            st.progress(solved/total_challenges if total_challenges > 0 else 0)
        
        # Reset button instead of logout
        if st.button("Reset Game", key="reset_game"):
            logout_user()
            st.rerun()
    
    # Main content - Category selection
    if not st.session_state.active_category:
        st.markdown("## Challenge Categories")
        st.info("Select a category to begin. Once started, the timer will begin and you'll have limited time to solve the challenges.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                ### Easy Challenges
                - 10 beginner-friendly problems
                - 1 hour time limit
                - One attempt per challenge
                """
            )
            if st.button("Start Easy Challenges", key="start_easy"):
                st.session_state.active_category = "easy"
                initialize_timer("easy", 60)  # 60 minutes
                st.rerun()
        
        with col2:
            st.markdown(
                """
                ### Medium Challenges
                - 10 intermediate problems
                - 1 hour 40 minutes time limit
                - One attempt per challenge
                """
            )
            if st.button("Start Medium Challenges", key="start_medium"):
                st.session_state.active_category = "medium"
                initialize_timer("medium", 100)  # 100 minutes (1h40m)
                st.rerun()
    
    # Display challenges for the selected category
    elif st.session_state.active_category == "easy":
        # Check if timer expired
        if auto_close_challenges():
            st.error("⏰ Time's up! Your session has ended.")
            st.warning(f"Final Score: {calculate_score()} points")
            
            if st.button("Return to Categories"):
                st.session_state.active_category = None
                st.session_state.timer_end = None
                st.rerun()
        else:
            st.markdown("## Easy Challenges")
            st.info("⏱️ You have 1 hour to solve these challenges. Timer started when you selected this category.")
            display_challenges(easy_challenges)
    
    elif st.session_state.active_category == "medium":
        # Check if timer expired
        if auto_close_challenges():
            st.error("⏰ Time's up! Your session has ended.")
            st.warning(f"Final Score: {calculate_score()} points")
            
            if st.button("Return to Categories"):
                st.session_state.active_category = None
                st.session_state.timer_end = None
                st.rerun()
        else:
            st.markdown("## Medium Challenges")
            st.info("⏱️ You have 1 hour and 40 minutes to solve these challenges. Timer started when you selected this category.")
            display_challenges(medium_challenges)
        
        # Display leaderboard (if time permits)
        # This would require a database integration, which is not implemented in this demo

if __name__ == "__main__":
    main()
