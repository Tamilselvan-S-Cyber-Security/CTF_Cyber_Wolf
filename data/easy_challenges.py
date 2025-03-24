# This file contains the easy challenges for the CTF platform
# Each challenge has a title, description, point value, and flag
# The flag is a secret string that users must discover to solve the challenge

easy_challenges = [
    {
        "title": "Warm Up",
        "description": "Your first challenge! The flag is hidden in plain sight. Inspect the source code of this page.",
        "hint": "Right-click and select 'View Page Source' or press Ctrl+U in most browsers.",
        "content": """
        <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
        Welcome to the CTF! Can you find the hidden flag?
        <!-- The flag is: CTF{welcome_to_the_game} -->
        </div>
        """,
        "type": "Web",
        "points": 10,
        "flag": "CTF{welcome_to_the_game}"
    },
    {
        "title": "Base Knowledge",
        "description": "Decoding is essential in CTF challenges. Can you decode this?",
        "hint": "This is a common encoding used for binary data on the web. Think about the name of the challenge.",
        "content": "Q1RGe2Jhc2U2NF9kZWNvZGluZ19pcl9mdW59",
        "type": "Crypto",
        "points": 15,
        "flag": "CTF{base64_decoding_ir_fun}"
    },
    {
        "title": "Hidden Message",
        "description": "There's a hidden message in this text. Can you find it?",
        "hint": "Look at the first letter of each word.",
        "content": """
        Carefully Take Freaky Great Big Underwater Turtles Hunting Innocent Seagulls In Nearly Totally Hidden Environment
        """,
        "type": "Crypto",
        "points": 20,
        "flag": "CTF{BUTHISINTH}"
    },
    {
        "title": "HTTP Headers",
        "description": "The server admin likes to hide flags in HTTP response headers. Can you find it?",
        "hint": "You might need to use browser developer tools or a tool like curl to view HTTP headers.",
        "content": """
        The flag is contained within one of the HTTP response headers. 
        
        Note: For this challenge, assume the flag is CTF{http_headers_are_useful}
        """,
        "type": "Web",
        "points": 25,
        "flag": "CTF{http_headers_are_useful}"
    },
    {
        "title": "Simple Cipher",
        "description": "This message has been encrypted with a simple substitution cipher where each letter is shifted by a fixed number.",
        "hint": "This is a classic Caesar cipher. Try different shift values.",
        "content": "FYK{fdhjdu_flskhu_lv_fodvvlf}",
        "type": "Crypto",
        "points": 30,
        "flag": "CTF{caesar_cipher_is_classic}"
    },
    {
        "title": "Find the Password",
        "description": "Can you find the password in this JavaScript code?",
        "hint": "Look carefully at variable assignments and what they might evaluate to.",
        "content": """
        ```javascript
        function checkPassword() {
            var p = "CTF{";
            p += "j4v4scr1pt_"
            p += "1s_fun}"
            return p;
        }
        ```
        """,
        "type": "Web",
        "points": 35,
        "flag": "CTF{j4v4scr1pt_1s_fun}"
    },
    {
        "title": "Binary Basics",
        "description": "Can you convert this binary code to text?",
        "hint": "Convert binary to ASCII text. Each 8 bits represents one character.",
        "content": """
        01000011 01010100 01000110 01111011 01100010 01101001 01101110 01100001 01110010 01111001 
        01011111 01110100 01101111 01011111 01110100 01100101 01111000 01110100 01111101
        """,
        "type": "Crypto",
        "points": 40,
        "flag": "CTF{binary_to_text}"
    },
    {
        "title": "Hexadecimal Mystery",
        "description": "This hex string contains a hidden message. Decode it to find the flag.",
        "hint": "Convert the hex characters to ASCII text.",
        "content": "4354467b6865785f69735f6576657279776865726521207d",
        "type": "Crypto",
        "points": 45,
        "flag": "CTF{hex_is_everywhere! }"
    },
    {
        "title": "Reversing Basics",
        "description": "Can you reverse this string to find the flag?",
        "hint": "The flag is written backwards.",
        "content": "}gnisrever_gnirts_cisab{FTC",
        "type": "Reversing",
        "points": 50,
        "flag": "CTF{basic_string_reversing}"
    },
    {
        "title": "Hidden in Plain Sight",
        "description": "The flag is hidden in this image. Can you find it?",
        "hint": "Look for patterns or hidden text in the image. Focus on contrast and colors.",
        "content": """
        Note: Since we cannot include actual images, imagine there's a QR code here that says 'CTF{steganography_101}'
        """,
        "type": "Forensics",
        "points": 55,
        "flag": "CTF{steganography_101}"
    },
    {
        "title": "Cookie Monster",
        "description": "The flag is stored in a browser cookie. Can you find it?",
        "hint": "Use the browser's developer tools to examine cookies for this page.",
        "content": """
        Note: In a real scenario, you'd find the flag stored in a cookie called 'secret-flag'.
        
        The flag is: CTF{cookies_are_delicious}
        """,
        "type": "Web",
        "points": 40,
        "flag": "CTF{cookies_are_delicious}"
    }
]
