import streamlit as st
import time

def initialize_session_state():
    """Initialize all required session state variables if they don't exist."""
    # Authentication state
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'user_info' not in st.session_state:
        st.session_state.user_info = {}
    
    # Challenge tracking
    if 'solved_challenges' not in st.session_state:
        st.session_state.solved_challenges = {}
    
    # Category state
    if 'active_category' not in st.session_state:
        st.session_state.active_category = None

def calculate_score():
    """Calculate the total score from solved challenges."""
    total_score = 0
    
    if 'solved_challenges' in st.session_state:
        for challenge_id, challenge_data in st.session_state.solved_challenges.items():
            if 'points' in challenge_data:
                total_score += challenge_data['points']
    
    return total_score

def get_user_progress():
    """Get statistics about user's progress."""
    if 'solved_challenges' not in st.session_state:
        return {
            'total_solved': 0,
            'easy_solved': 0,
            'medium_solved': 0,
            'total_score': 0
        }
    
    # Count challenges by category
    easy_solved = 0
    medium_solved = 0
    
    for challenge_id in st.session_state.solved_challenges:
        if challenge_id.startswith('easy'):
            easy_solved += 1
        elif challenge_id.startswith('medium'):
            medium_solved += 1
    
    return {
        'total_solved': len(st.session_state.solved_challenges),
        'easy_solved': easy_solved,
        'medium_solved': medium_solved,
        'total_score': calculate_score()
    }
