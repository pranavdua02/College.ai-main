import streamlit as st
from menu.signup import sign_up
import sqlite3
from streamlit_authenticator.utilities.hasher import Hasher
import bcrypt


user_conn = sqlite3.connect('users.db',check_same_thread=False)
user_cursor = user_conn.cursor()
user_cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        email TEXT UNIQUE,
        password TEXT
    )
''')
user_conn.commit()




if 'is_logged' not in st.session_state: 
    st.session_state['is_logged'] = False

def main():
    st.write("<h1><center>Account</center></h1>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Login", "SignUp"])

    def get_user_emails():
        user_cursor.execute('SELECT email FROM users')
        email_list=[]
        em=user_cursor.fetchall()
        for row in em:
            email_list.append(row[0])
        user_conn.commit()
        return email_list

    def login():
        with st.form(key='login', clear_on_submit=True):
            st.subheader(':green[Login]')
            email = st.text_input(':blue[Email]', placeholder='Enter Your Email')
            password1 = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
            btn1, bt2, btn3, btn4, btn5 = st.columns(5)
            btn3=st.form_submit_button('Login')
            
            if btn3:
                email_lst=get_user_emails()
                if email in email_lst:
                    user_cursor.execute('SELECT email,password FROM users WHERE email=?',(email,))
                    records = user_cursor.fetchall()
                    # print("Printing ID ", records)
                    saved_pass=eval(records[0][1])
                    password=str.encode(password1)
                    if bcrypt.checkpw(password, saved_pass):
                        st.success("Logged In")
                        st.session_state['is_logged'] = True
                        st.session_state['user']=email
                    else:
                        st.warning("Wrong Password")                
                    
                else:
                    st.warning('Email is not correct')
            
    with tab1:
        login()
    with tab2:
        sign_up()
if __name__=="__main__":
    main()


