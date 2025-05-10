import pickle
import streamlit as st
import pandas as pd
model=pickle.load(open("loan_approval.pkl","rb"))

st.header("Loan Approval Project")

col1,col2,col3,col4=st.columns(4)
with col1:
    gender=st.selectbox("Gender",["Male","Female"])
    st.text(" ")
    emply=st.selectbox("Self_Employed or not",["No","Yes"])
    st.text(" ")
    loanamterm=st.number_input("enter Loan_Amount_Term")
    st.text(" ")
   
with col2:
    marriage=st.selectbox("Married or not",["No","Yes"])
    st.text(" ")
    applica=st.number_input("Enter Applicant Income")
    st.text(" ")
    crd_his=st.selectbox("select credit history",[1,0])

with col3:
    depends=st.selectbox("select dependents",[1,0])
    st.text(" ")
    co_app=st.number_input("Enter Coapplicant Income")
    st.text(" ")
    pry_area=st.selectbox("select area",["Semiurban","Urban","Rural"])


with col4:
    educa=st.selectbox("education",["Graduate","Not Graduate"])
    st.text(" ")
    loanamt=st.number_input("enter loan amount")
    st.text(" ")
    
    
st.text(" ")

if st.button("Predict Loan"):
    data=pd.DataFrame([[gender,marriage,depends,educa,emply,applica,co_app,loanamt,loanamterm,crd_his,pry_area]],columns=["Gender","Married","Dependents","Education",
                                    "Self_Employed","ApplicantIncome","CoapplicantIncome",
                                    "LoanAmount","Loan_Amount_Term","Credit_History","Property_Area"])
    
    prediction=model.predict(data)[0]
    if prediction==1:
        st.write("Loan appproved")
    else:
        st.write("Sorry loan not approved")
