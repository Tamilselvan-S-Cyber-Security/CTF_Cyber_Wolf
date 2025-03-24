import streamlit as st
import time
import hashlib

def display_challenges(challenges):
    """Display all challenges for a specific category."""
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
    
    # Create the challenge card
    with st.expander(
        f"{challenge['title']} ({challenge['points']} pts) " + ("✅" if solved else ""),
        expanded=not solved
    ):
        st.markdown(f"**Description:** {challenge['description']}")
        
        if 'hint' in challenge and not solved:
            with st.expander("Show Hint"):
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
                        
                        # Save the solved challenge to session state
                        st.session_state.solved_challenges[challenge_id] = {
                            'title': challenge['title'],
                            'points': challenge['points'],
                            'time': time.time()
                        }
                        
                        # Wait briefly to show the success message
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("Incorrect flag. Try again!")
        else:
            st.success(f"You've solved this challenge! (+{challenge['points']} points)")

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
