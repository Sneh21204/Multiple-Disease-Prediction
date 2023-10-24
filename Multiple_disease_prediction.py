import pickle
import streamlit as st 
from streamlit_option_menu import option_menu

# loading the saved model
diabetes_model = pickle.load(open("C:/Users/LENOVO/OneDrive/Desktop/Multiple disease prediction system/diabetes_model.sav" , 'rb'))

parkinsons_model = pickle.load(open("C:/Users/LENOVO/OneDrive/Desktop/Multiple disease prediction system/parkinsons_model.sav" , 'rb'))

heart_model = pickle.load(open("C:/Users/LENOVO/OneDrive/Desktop/Multiple disease prediction system/Heart_model.sav" , 'rb'))

# sidebar for navigation 
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           default_index=0)

# Function to make predictions
def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
    prediction = diabetes_model.predict(data)
    return prediction

def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    prediction = heart_model.predict(data)
    return prediction

def predict_parkinsons(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE):
    data = [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]]
    prediction = parkinsons_model.predict(data)
    return prediction

# Main page content
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    if st.button('Diabetes Test Result'):
        try:
            Pregnancies = float(Pregnancies)
            Glucose = float(Glucose)
            BloodPressure = float(BloodPressure)
            SkinThickness = float(SkinThickness)
            Insulin = float(Insulin)
            BMI = float(BMI)
            DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
            Age = float(Age)
            diab_prediction = predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
            
            if diab_prediction[0] == 1:
                st.success('The person is diabetic')
            else:
                st.success('The person is not diabetic')
        except ValueError:
            st.error('Please enter valid numeric values for the input fields.')

elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    if st.button('Heart Disease Test Result'):
        try:
            age = float(age)
            sex = float(sex)
            cp = float(cp)
            trestbps = float(trestbps)
            chol = float(chol)
            fbs = float(fbs)
            restecg = float(restecg)
            thalach = float(thalach)
            exang = float(exang)
            oldpeak = float(oldpeak)
            slope = float(slope)
            ca = float(ca)
            thal = float(thal)
            
            heart_prediction = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
            
            if heart_prediction[0] == 1:
                st.success('The person is having heart disease')
            else:
                st.success('The person does not have any heart disease')
        except ValueError:
            st.error('Please enter valid numeric values for the input fields.')

elif selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")
    
    fo = st.text_input('MDVP:Fo(Hz)')
    fhi = st.text_input('MDVP:Fhi(Hz)')
    flo = st.text_input('MDVP:Flo(Hz)')
    Jitter_percent = st.text_input('MDVP:Jitter(%)')
    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    RAP = st.text_input('MDVP:RAP')
    PPQ = st.text_input('MDVP:PPQ')
    DDP = st.text_input('Jitter:DDP')
    Shimmer = st.text_input('MDVP:Shimmer')
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    APQ3 = st.text_input('Shimmer:APQ3')
    APQ5 = st.text_input('Shimmer:APQ5')
    APQ = st.text_input('MDVP:APQ')
    DDA = st.text_input('Shimmer:DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')
    
    if st.button("Parkinson's Test Result"):
        try:
            fo = float(fo)
            fhi = float(fhi)
            flo = float(flo)
            Jitter_percent = float(Jitter_percent)
            Jitter_Abs = float(Jitter_Abs)
            RAP = float(RAP)
            PPQ = float(PPQ)
            DDP = float(DDP)
            Shimmer = float(Shimmer)
            Shimmer_dB = float(Shimmer_dB)
            APQ3 = float(APQ3)
            APQ5 = float(APQ5)
            APQ = float(APQ)
            DDA = float(DDA)
            NHR = float(NHR)
            HNR = float(HNR)
            RPDE = float(RPDE)
            DFA = float(DFA)
            spread1 = float(spread1)
            spread2 = float(spread2)
            D2 = float(D2)
            PPE = float(PPE)
            
            parkinsons_prediction = predict_parkinsons(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE)
            
            if parkinsons_prediction[0] == 1:
                st.success("The person has Parkinson's disease")
            else:
                st.success("The person does not have Parkinson's disease")
        except ValueError:
            st.error('Please enter valid numeric values for the input fields.')
