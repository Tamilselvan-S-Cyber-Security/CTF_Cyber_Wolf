# This file contains the medium challenges for the CTF platform
# Each challenge has a title, description, point value, and flag
# The flag is a secret string that users must discover to solve the challenge

medium_challenges = [
    {
        "title": "SQL Injection Basics",
        "description": "This website has a login form vulnerable to SQL Injection. Can you bypass it?",
        "hint": "Try using common SQL injection techniques to manipulate the login query.",
        "content": """
        Login Form:
        ```
        Username: ___________
        Password: ___________
        ```
        
        Note: For this challenge, assume the solution is to enter `admin' --` as the username and anything as the password.
        
        The flag is: CTF{sql_injection_bypassed_login}
        """,
        "type": "Web",
        "points": 60,
        "flag": "CTF{sql_injection_bypassed_login}"
    },
    {
        "title": "Vigenère Cipher",
        "description": "This message is encrypted with a Vigenère cipher. The key is related to the challenge name.",
        "hint": "The key is 'vigenere'.",
        "content": """
        RXJ{zsknwmvs_gmtlxv_gw_xsadwmi}
        """,
        "type": "Crypto",
        "points": 65,
        "flag": "CTF{vigenere_cipher_is_classic}"
    },
    {
        "title": "Command Injection",
        "description": "This web application has a tool that pings a hostname. Can you exploit it to get the flag?",
        "hint": "Try to inject shell commands after the hostname.",
        "content": """
        Ping tool:
        ```
        Hostname: ___________
        ```
        
        Note: For this challenge, assume you would enter `example.com; cat flag.txt` to see the flag.
        
        The flag is: CTF{command_injection_vulnerability}
        """,
        "type": "Web",
        "points": 70,
        "flag": "CTF{command_injection_vulnerability}"
    },
    {
        "title": "Reverse Engineering",
        "description": "Can you figure out what this Python function is doing and find the correct input?",
        "hint": "Trace through the function execution for different inputs.",
        "content": """
        ```python
        def check_flag(user_input):
            if len(user_input) != 24:
                return False
            if user_input[:4] != "CTF{" or user_input[-1] != "}":
                return False
            
            key = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
            encoded = user_input[4:-1]
            
            if len(encoded) != 19:
                return False
            
            for i in range(len(encoded)):
                if (ord(encoded[i]) ^ key[i % len(key)]) != [80, 98, 121, 116, 106, 117, 103, 125, 96, 117, 96, 114, 126, 97, 124, 102, 116, 114, 118]:
                    return False
            
            return True
        ```
        """,
        "type": "Reversing",
        "points": 75,
        "flag": "CTF{xor_encryption_fun}"
    },
    {
        "title": "Network Packet Analysis",
        "description": "Analyze this packet capture to find the flag being transmitted.",
        "hint": "Look for HTTP requests with suspicious parameters or data transfers.",
        "content": """
        Note: Normally this would be a .pcap file for analysis. 
        
        For this challenge, assume the flag is: CTF{packet_analysis_experts}
        """,
        "type": "Forensics",
        "points": 80,
        "flag": "CTF{packet_analysis_experts}"
    },
    {
        "title": "JavaScript Obfuscation",
        "description": "This JavaScript code has been obfuscated. Can you figure out what it's doing?",
        "hint": "Try to de-obfuscate the code. Look for patterns or encoding functions.",
        "content": """
        ```javascript
        eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('2 1=\'0{3_4_5}\';',6,6,'CTF|flag|var|js|obfuscation|tricks'.split('|'),0,{}))
        ```
        """,
        "type": "Web",
        "points": 70,
        "flag": "CTF{js_obfuscation_tricks}"
    },
    {
        "title": "Buffer Overflow Basic",
        "description": "This C program has a buffer overflow vulnerability. Can you exploit it to get the flag?",
        "hint": "Look at how the program is handling user input. How can you overflow the buffer?",
        "content": """
        ```c
        #include <stdio.h>
        #include <string.h>

        void get_flag() {
            printf("Flag: CTF{buffer_overflow_basics}\\n");
        }

        void vulnerable_function() {
            char buffer[16];
            printf("Enter your name: ");
            gets(buffer);  // Vulnerable function
            printf("Hello, %s!\\n", buffer);
        }

        int main() {
            vulnerable_function();
            return 0;
        }
        ```
        """,
        "type": "Binary",
        "points": 85,
        "flag": "CTF{buffer_overflow_basics}"
    },
    {
        "title": "JWT Token Manipulation",
        "description": "This API uses JWT tokens for authentication. Can you forge a token to gain admin access?",
        "hint": "Look at the token structure and consider how the signature is verified.",
        "content": """
        Example JWT token:
        ```
        eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE1MTYyMzkwMjJ9.Ofq5rxGQ7Exa3LlTeYElPXm63Z7S4Otk9fRs8AWKzMA
        ```
        
        Note: The server is using a weak secret key: "secret"
        
        Your task is to modify the token to set "admin" to true.
        
        The flag is: CTF{jwt_signature_weakness}
        """,
        "type": "Web",
        "points": 80,
        "flag": "CTF{jwt_signature_weakness}"
    },
    {
        "title": "Steganography Challenge",
        "description": "There's a hidden message in this image. Can you extract it?",
        "hint": "Look at the least significant bits of the image data.",
        "content": """
        Note: For this challenge, you would normally analyze an image.
        
        The steganography technique involves LSB (Least Significant Bit) encoding.
        
        The flag is: CTF{hidden_in_plain_sight}
        """,
        "type": "Forensics",
        "points": 75,
        "flag": "CTF{hidden_in_plain_sight}"
    },
    {
        "title": "File Upload Vulnerability",
        "description": "This website allows file uploads. Can you bypass the restrictions to execute code?",
        "hint": "Check what file extensions and content types are being verified.",
        "content": """
        File Upload Form:
        ```
        Select file: [Browse...]
        ```
        
        The server validates:
        1. File extension (.jpg, .png, .gif)
        2. Content-Type in the request
        
        Your goal is to upload a PHP file that can execute commands.
        
        The flag is: CTF{file_upload_bypass_achieved}
        """,
        "type": "Web",
        "points": 90,
        "flag": "CTF{file_upload_bypass_achieved}"
    }
]