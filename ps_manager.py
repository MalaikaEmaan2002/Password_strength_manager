import re
import streamlit as st
# page styling
st.set_page_config(page_title="Password Strength Checker", layout="centered")
# applied css
st.markdown(
    """
<style>
    .main{
        text-align: center;
    }
    .title {
        background: linear-gradient(45deg, #800080 50%, #006400 50%);
        -webkit-background-clip: text;  
        color: transparent;  
        font-size: 45px;
        font-weight: bold;
        display: inline; 
         font-style: italic;
    }
    .stTextInput{
        width: 60% !important; margin:auto;
    }
    .stButton button{
        width: 50%;
        background: linear-gradient(45deg, purple, black);
        color: white;
        font-size: 18px
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #808080);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 18px;
        color: black;
        font-style: italic;

    }
</style>    
""", unsafe_allow_html=True
)

# title & description

st.markdown(
    """
     <div class= "title"> ˙⋆✮ Password Strength Generator✯</div>
""", unsafe_allow_html=True
)
st.write("Enter your password below to assess its security level.")

# function 
def check_password_strength(password):
    score = 0
    feedback = []

    if len (password) >= 8:
        score += 1 
    else:
        feedback.append("❌ Password should be **atleast 8 character long**.")  

    if re.search(r"[A-Z]", password )and re.search(r"[a-z]", password):
        score += 1 
    else:
        feedback.append("❌ Password should include **both uppercase and lowercase letters**.")
    if re.search(r"/d", password):
        score += 1 
    else:
        feedback.append("❌ Password should include **atleast one number (0-9)**.")

        # special character
    if re.search(r"[!@#$%*&^]", password):
        score += 1 
    else:
        feedback.append("❌ Include **atleast one special character (!@#$%*&^)**.") 

  # display password strength result
    if score == 4:
        st.success(" ✔️ **Strong Password** your password is secure.")
    elif score == 3:
        st.info(" ⚠️ **Moderate Password** - Consider improving security by adding more feature.") 
    else:
        st.error(" ❗ **Weak Password** - Follow the suggestion below the strength it.")      

# feedback
    if feedback:
        with st.expander("**Improve your password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Enter your password is strong 🔐") 

# button
if st.button ("Check Stength"):
    if password:
        check_password_strength(password)
    else:
        st.warning(" ⚠️ Please enter a password first!")     


st.markdown("<div class='footer'>Created by Malaika Emaan💞</div>", unsafe_allow_html=True)