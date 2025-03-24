import streamlit as st
import time
import json

def initialize_auth_state():
    """Initialize authentication-related session state variables if they don't exist."""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'user_info' not in st.session_state:
        st.session_state.user_info = {}
    if 'auth_error' not in st.session_state:
        st.session_state.auth_error = None

def check_authentication():
    """Check if the user is authenticated."""
    initialize_auth_state()
    return st.session_state.authenticated

def authenticate_user(auth):
    """Display login form and handle user authentication."""
    initialize_auth_state()
    
    st.markdown("## Login to CTF Platform")
    st.warning("Note: Only login is available, no signup option as per requirements.")
    
    with st.form("login_form"):
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            if email and password:
                try:
                    # Authenticate user with Firebase
                    user = auth.sign_in_with_email_and_password(email, password)
                    
                    # Get user info
                    user_info = auth.get_account_info(user['idToken'])
                    
                    # Update session state
                    st.session_state.authenticated = True
                    st.session_state.user_info = {
                        'uid': user['localId'],
                        'email': user['email'],
                        'name': email.split('@')[0]  # Simple way to get a display name
                    }
                    
                    # Initialize user's challenge progress
                    if 'solved_challenges' not in st.session_state:
                        st.session_state.solved_challenges = {}
                    
                    st.success("Login successful!")
                    time.sleep(1)
                    st.rerun()
                    
                except Exception as e:
                    st.session_state.auth_error = f"Login failed: {str(e)}"
                    st.error(st.session_state.auth_error)
            else:
                st.error("Email and password are required.")
    
    # Add a direct login option for demo purposes
    st.markdown("---")
    st.markdown("#### Demo Login")
    if st.button("Login as Demo User"):
        # For simplicity, we'll simulate a successful login
        st.session_state.authenticated = True
        st.session_state.user_info = {
            'uid': 'demo_user_123',
            'email': 'demo@example.com',
            'name': 'Demo User'
        }
        
        # Initialize user's challenge progress
        if 'solved_challenges' not in st.session_state:
            st.session_state.solved_challenges = {}
        
        st.success("Demo login successful!")
        time.sleep(1)
        st.rerun()

def logout_user():
    """Log out the current user."""
    # Reset authentication state
    st.session_state.authenticated = False
    st.session_state.user_info = {}
    
    # Keep solved challenges for the session
    # In a real application, this would be stored in a database
    
    # Reset active category and timer
    st.session_state.active_category = None
    if 'timer_end' in st.session_state:
        del st.session_state.timer_end
