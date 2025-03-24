import streamlit as st
import time
import json
import random
import string

def initialize_auth_state():
    """Initialize authentication-related session state variables if they don't exist."""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'user_info' not in st.session_state:
        st.session_state.user_info = {}
    if 'auth_error' not in st.session_state:
        st.session_state.auth_error = None
    if 'is_admin' not in st.session_state:
        st.session_state.is_admin = False

def check_authentication():
    """Check if the user is authenticated."""
    initialize_auth_state()
    return st.session_state.authenticated

def authenticate_user(auth):
    """Display login form and handle user authentication."""
    initialize_auth_state()
    
    st.markdown("## CTF Login")
    st.info("Enter your team name and password to start the CTF challenge.")
    
    with st.form("login_form"):
        team_name = st.text_input("Team Name", key="login_team")
        password = st.text_input("Password", type="password", key="login_password")
        submit_button = st.form_submit_button("Start CTF Challenge")
        
        if submit_button:
            if team_name and password:
                try:
                    # For CTF competitions, we can use Firebase or a simpler approach
                    # Here's the Firebase approach
                    try:
                        # Try to login with existing account
                        user = auth.sign_in_with_email_and_password(f"{team_name.lower().replace(' ', '_')}@ctf.com", password)
                    except:
                        # If login fails, create a new account for this team
                        # This allows new teams to register on the fly
                        try:
                            user = auth.create_user_with_email_and_password(
                                f"{team_name.lower().replace(' ', '_')}@ctf.com", 
                                password
                            )
                        except Exception as create_error:
                            if "EMAIL_EXISTS" in str(create_error):
                                st.error("Team exists but password is incorrect. Try again.")
                                return
                            else:
                                st.error(f"Registration error: {str(create_error)}")
                                return
                    
                    # Update session state - no history, fresh start every time
                    st.session_state.authenticated = True
                    
                    # Check if this is an admin login
                    is_admin = False
                    # Identify admin by special username and password
                    if team_name.lower() == "admin" and password == "ctfadmin123":
                        is_admin = True
                        
                    st.session_state.user_info = {
                        'uid': team_name.lower().replace(' ', '_'),
                        'name': team_name,
                        'team_id': ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)),
                        'is_admin': is_admin
                    }
                    
                    # Initialize fresh challenge progress for this session
                    st.session_state.solved_challenges = {}
                    
                    st.success(f"Welcome, Team {team_name}!")
                    time.sleep(1)
                    st.rerun()
                    
                except Exception as e:
                    st.session_state.auth_error = f"Login failed: {str(e)}"
                    st.error(st.session_state.auth_error)
            else:
                st.error("Team name and password are required.")

def logout_user():
    """Log out the current user."""
    # Reset authentication state
    st.session_state.authenticated = False
    st.session_state.user_info = {}
    
    # Clear solved challenges - no history preservation
    st.session_state.solved_challenges = {}
    
    # Reset active category and timer
    st.session_state.active_category = None
    if 'timer_end' in st.session_state:
        del st.session_state.timer_end
        
    # Reset admin state
    if 'is_admin' in st.session_state:
        st.session_state.is_admin = False
    
    # Reset any editing state for admin panel
    if 'editing_challenge' in st.session_state:
        del st.session_state.editing_challenge
    if 'editing_category' in st.session_state:
        del st.session_state.editing_category
