import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import streamlit as st
def show_firebase_page():

    st.subheader('FireBase Test Page')
    #save data
    ref = db.reference('py/')
    user_ref = ref.child('users')
    user_ref.set({
        'Ishu':{
            'dob':'Dec 12,2002',
            'full_name':'Sparsh'
        },
        'Isha':{
            'dob':'July 15,2002',
            'full_name':'Maggie'
        }
    })

    #update data

    hopper_ref = user_ref.child('Ishu')
    hopper_ref.update({
        'nickname':'Suru'
    })

    # read data
    handle = db.reference('py/users/Ishu')

    # read data and post the refeerence
    st.write('full name: ',user_ref.child('Ishu').child('full_name').get())
    st.write('dob: ',user_ref.child('Ishu').child('dob').get())

    st.write('full name: ',user_ref.child('Isha').child('full_name').get())
    st.write('dob: ',user_ref.child('Isha').child('dob').get())

    # print(ref.get())
    