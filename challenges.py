import streamlit as st
import time
import hashlib
from timer import start_challenge_timer, get_challenge_solving_time, format_solving_time, auto_close_challenges

def display_challenges(challenges):
    """Display all challenges for a specific category."""
    # Check if timer has expired and auto-close if needed
    if auto_close_challenges():
        st.error("⏰ Time's up! The challenges are now closed.")
        st.warning("Your final score has been recorded.")
        return
    
    # Create tabs for different challenge types
    tabs = st.tabs(["Web", "Crypto", "Forensics", "Reversing", "Misc"])
    
    # Group challenges by type
    challenge_types = {}
    for idx, challenge in enumerate(challenges):
        challenge_type = challenge.get("type", "Misc")
        if challenge_type not in challenge_types:
            challenge_types[challenge_type] = []
        challenge_types[challenge_type].append((idx, challenge))
    
    # Display challenges by type in respective tabs
    for i, tab_name in enumerate(["Web", "Crypto", "Forensics", "Reversing", "Misc"]):
        with tabs[i]:
            if tab_name in challenge_types:
                for idx, challenge in challenge_types[tab_name]:
                    display_challenge_card(idx, challenge)
            else:
                st.info(f"No {tab_name} challenges available in this category.")

def display_challenge_card(idx, challenge):
    """Display a single challenge card with submission form."""
    # Generate a unique key for this challenge
    challenge_id = f"{challenge['title']}_{idx}"
    
    # Check if challenge has been solved
    solved = challenge_id in st.session_state.solved_challenges
    
    # Start timing this challenge when it's opened and not solved
    if not solved:
        start_challenge_timer(challenge_id)
    
    # Create the challenge card
    with st.expander(
        f"{challenge['title']} ({challenge['points']} pts) " + ("✅" if solved else ""),
        expanded=not solved
    ):
        st.markdown(f"**Description:** {challenge['description']}")
        
        if 'hint' in challenge and not solved:
            # Use a collapsible container with button instead of nested expander
            if st.button(f"Show Hint", key=f"hint_{challenge_id}"):
                st.markdown(f"*{challenge['hint']}*")
        
        # Display any challenge-specific content
        if 'content' in challenge:
            st.markdown(challenge['content'])
        
        # If challenge is not solved yet, show submission form
        if not solved:
            with st.form(f"flag_submission_{challenge_id}"):
                flag_input = st.text_input("Enter flag:", key=f"flag_input_{challenge_id}")
                submitted = st.form_submit_button("Submit Flag")
                
                if submitted:
                    if check_flag(challenge_id, flag_input, challenge['flag']):
                        st.success("Correct flag! 🎉")
                        
                        # Calculate solving time
                        solving_time = get_challenge_solving_time(challenge_id)
                        solving_time_formatted = format_solving_time(solving_time)
                        
                        # Save the solved challenge to session state with timing information
                        st.session_state.solved_challenges[challenge_id] = {
                            'title': challenge['title'],
                            'points': challenge['points'],
                            'time': time.time(),
                            'solving_time': solving_time,
                            'solving_time_formatted': solving_time_formatted
                        }
                        
                        # Show solving time
                        st.info(f"Solved in: {solving_time_formatted}")
                        
                        # Wait briefly to show the success message
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("Incorrect flag. Try again!")
        else:
            solved_info = st.session_state.solved_challenges[challenge_id]
            solving_time_display = solved_info.get('solving_time_formatted', 'N/A')
            st.success(f"You've solved this challenge! (+{challenge['points']} points)")
            st.info(f"Solved in: {solving_time_display}")

def check_flag(challenge_id, submitted_flag, correct_flag):
    """Check if the submitted flag is correct."""
    # If this is not the user's first attempt at this challenge, reject
    attempt_key = f"attempt_{challenge_id}"
    
    if attempt_key in st.session_state:
        st.warning("You've already attempted this challenge. Only one attempt is allowed per challenge.")
        return False
    
    # Mark this challenge as attempted
    st.session_state[attempt_key] = True
    
    # Clean and normalize flags before comparison
    submitted_flag = submitted_flag.strip()
    
    # If the flag is a hash (for extra security), compare hashed values
    if len(correct_flag) == 64 and all(c in '0123456789abcdef' for c in correct_flag):
        # This appears to be a SHA-256 hash, so hash the input for comparison
        hashed_input = hashlib.sha256(submitted_flag.encode()).hexdigest()
        return hashed_input == correct_flag
    else:
        # Direct comparison
        return submitted_flag == correct_flag
