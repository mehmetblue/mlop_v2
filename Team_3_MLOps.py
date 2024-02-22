
#Import libraries
from multiprocessing import parent_process
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import joblib
from io import BytesIO
import base64
import xlsxwriter

# import locale

# # Display the GitHub link at the beginning of the app
# st.markdown('[GitHub Repository](https://github.com/mehmetblue/Final_Project_MLOps/tree/main)')

#load the model from disk
filename = "catb_model_24outbaski.sav"
model = joblib.load(filename)

#Setting Application title
st.title('Developer Salary Prediction Model App Team-3')

#Setting Application description
st.markdown("""
This Streamlit app is made to predict Developers Salaries based on Stack Overflow 2018 Developers Survey.
The application is functional for both online prediction and batch data prediction. \n
""")
st.markdown("<h3></h3>", unsafe_allow_html=True)

#Setting Application sidebar default
image = Image.open("App.png")
add_selectbox = st.sidebar.selectbox(
"How would you like to predict?", ("Online", "Batch"))
st.sidebar.info('This app is created to predict Developers Salaries based on Stack Overflow 2018 Developers Survey')
st.sidebar.image(image)

# Adding the GitHub Repo link at the bottom of the sidebar
# st.sidebar.markdown('[Project GitHub Repo](https://github.com/mehmetblue/Final_Project_MLOps)')
st.sidebar.info('[Project GitHub Repo](https://github.com/mehmetblue/Final_Project_MLOps)')

if add_selectbox == "Online":
    st.info("Please Input data below")

    #Based on our optimal features selection
    st.subheader("Developer's Informations")


    Country_list = ['Afghanistan',  'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
                    'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana',
                    'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic',
                    'Chile', 'China', 'Colombia', 'Congo, Republic of the...', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', "Côte d'Ivoire",
                    "Democratic People's Republic of Korea", 'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
                    'Egypt', 'El Salvador', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece',
                    'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong (S.A.R.)', 'Hungary', 'Iceland', 'India', 'Indonesia',
                    'Iran, Islamic Republic of...', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyzstan',
                    'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libyan Arab Jamahiriya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia',
                    'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia, Federated States of...', 'Monaco', 'Mongolia',
                    'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
                    'North Korea', 'Norway', 'Oman', 'Other Country (Not Listed Above)', 'Pakistan', 'Palau', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland',
                    'Portugal', 'Qatar', 'Republic of Korea', 'Republic of Moldova', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Lucia', 'San Marino',
                    'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
                    'South Korea', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan', 'Tajikistan',
                    'Thailand', 'The former Yugoslav Republic of Macedonia', 'Timor-Leste', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                    'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United Republic of Tanzania', 'United States', 'Uruguay', 'Uzbekistan',
                    'Venezuela, Bolivarian Republic of...', 'Viet Nam', 'Yemen', 'Zambia', 'Zimbabwe']

    YearsCodingProf_list = ["0-2 years", "3-5 years", "6-8 years", "9-11 years", "12-14 years", "15-17 years", 
                            "18-20 years", "21-23 years", "24-26 years", "27-29 years", "30 or more years"]

    RaceEthnicity_list = ["White or of European descent", "South Asian", "Hispanic or Latino/Latina", "East Asian", "Middle Eastern",
                            "Black or of African descent", "Native American, Pacific Islander, or Indigenous Australian"]

    Age_list = ["Under 18 years old", "18 - 24 years old", "25 - 34 years old", "35 - 44 years old", "45 - 54 years old", "55 - 64 years old", "65 years or older"]

    Employment_list = ["Employed full-time", "Independent contractor, freelancer, or self-employed", "Not employed, but looking for work",
                        "Employed part-time", "Not employed, and not looking for work", "Retired"]

    FormalEducation_list = ["I never completed any formal education", "Primary/elementary school", "Secondary school", 
                            "Some college/university study without earning a degree", "Associate degree", "Bachelor's degree",
                            "Master's degree", "Professional degree", "Doctoral degree"]

    CommunicationTools_list = ["Office / productivity suite (Microsoft Office, Google Suite, etc.)", "Slack ", "Confluence ", "Jira "
                                "Other chat system (IRC, proprietary software, etc.) ", "Other wiki tool (Github, Google Sites, proprietary software, etc.)",
                                "Trello ", "Google Hangouts/Chat ", "HipChat ", "Facebook ", "Stack Overflow Enterprise"]

    NumberMonitors_list = ["1", "2", "3"," 4", "More than 4"]

    DevType_list = ["Back-end developer", "Full-stack developer", "Front-end developer", "Mobile developer", "Desktop or enterprise applications developer",
                    "Student", "Database administrator", "Designer", "System administrator", "DevOps specialist", "Data or business analyst",
                    "Data scientist or machine learning specialist", "QA or test developer", "Engineering manager", "Embedded applications or devices developer",
                    "Game or graphics developer", "Product manager", "Educator or academic researcher", "C-suite executive (CEO, CTO, etc.)", 
                    "Marketing or sales professional"]

    LastNewJob_list = ["I've never had a job", "Less than a year ago", "Between 1 and 2 years ago", "Between 2 and 4 years ago", "More than 4 years ago"]

    Student_list = ["No", "Yes, part-time", "Yes, full-time"]

    ide_list = ["Visual Studio Code", "Visual Studio", "Notepad++", "Sublime Text", "Vim", "IntelliJ", "Android Studio", "Eclipse", "Atom", "PyCharm",
                "Xcode", "PHPStorm", "NetBeans", "IPython / Jupyter", "Emacs", "RStudio", "RubyMine", "TextMate", "Coda", "Komodo", "Zend", "Light Table"]


    country = st.selectbox(label = "Choose a country", options = Country_list)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    yearsCodingProf = st.selectbox(label = "For how many years have you coded professionally (as a part of your work)?", options = YearsCodingProf_list)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    raceEthnicity = st.selectbox(label = "Which of the following do you identify as?", options = RaceEthnicity_list)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    age = st.selectbox(label = "Age", options = Age_list)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    employment = st.selectbox(label = "Which of the following best describes your current employment status?", options = Employment_list)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    formalEducation = st.selectbox(label = "Which of the following best describes the highest level of formal education that you have completed?", options = FormalEducation_list)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    assessBenefits6 = st.number_input(label = "Please rank the 'Retirement or pension savings matching' aspects of a job's benefits package, where 1 is most important and 11 is least important.", min_value=1, max_value=11, value=1)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    communicationTools = st.selectbox(label = "Which of the following tools do you use to communicate, coordinate, or share knowledge with your coworkers?", options = CommunicationTools_list)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    numberMonitors = st.selectbox(label = "How many monitors are set up at your workstation?", options = NumberMonitors_list)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    devType = st.selectbox(label = "Which of the following describe you?", options = DevType_list)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    assessBenefits3 = st.number_input(label = "Please rank the 'Health insurance' aspects of a job's benefits package, where 1 is most important and 11 is least important.", min_value=1, max_value=11, value=1)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    lastNewJob = st.selectbox(label = "When was the last time that you took a job with a new employer?", options = LastNewJob_list)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    student = st.selectbox(label = "Are you currently enrolled in a formal, degree-granting college or university program?", options = Student_list)
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    ide = st.selectbox(label = "Which development environment(s) do you use regularly?", options= ide_list)


    data = {
            'Country_LE': country,
            'YearsCodingProf' : yearsCodingProf,
            'RaceEthnicity_LE' : raceEthnicity,
            'Age' : age,
            'Employment_LE' : employment,
            'FormalEducation' : formalEducation,
            'CommunicationTools_LE' : communicationTools,
            'AssessBenefits6' : assessBenefits6,
            'NumberMonitors' : numberMonitors,
            'DevType_LE' : devType,
            'AssessBenefits3' : assessBenefits3,
            'LastNewJob' : lastNewJob,
            'Student_LE' : student,
            'IDE_LE' : ide  
        
                        }

    features_df = pd.DataFrame.from_dict([data])

    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.write('Overview of input is shown below')
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    st.write(features_df)


    dictionary = {
        'Afghanistan' : 0,
        'Albania' : 1,
        'Algeria' : 2,
        'Andorra' : 3,
        'Angola' : 4,
        'Antigua and Barbuda' : 5,
        'Argentina' : 6,
        'Armenia' : 7,
        'Australia' : 8,
        'Austria' : 9,
        'Azerbaijan' : 10,
        'Bahamas' : 11,
        'Bahrain' : 12,
        'Bangladesh' : 13,
        'Barbados' : 14,
        'Belarus' : 15,
        'Belgium' : 16,
        'Belize' : 17,
        'Benin' : 18,
        'Bhutan' : 19,
        'Bolivia' : 20,
        'Bosnia and Herzegovina' : 21,
        'Botswana' : 22,
        'Brazil' : 23,
        'Brunei Darussalam' : 24,
        'Bulgaria' : 25,
        'Burkina Faso' : 26,
        'Burundi' : 27,
        'Cambodia' : 28,
        'Cameroon' : 29,
        'Canada' : 30,
        'Cape Verde' : 31,
        'Central African Republic' : 32,
        'Chile' : 33,
        'China' : 34,
        'Colombia' : 35,
        'Congo Republic of the...' : 36,
        'Costa Rica' : 37,
        'Croatia' : 38,
        'Cuba' : 39,
        'Cyprus' : 40,
        'Czech Republic' : 41,
        "Côte d'Ivoire" : 42,
        "Democratic People's Republic of Korea" : 43,
        'Democratic Republic of the Congo' : 44,
        'Denmark' : 45,
        'Djibouti' : 46,
        'Dominica' : 47,
        'Dominican Republic' : 48,
        'Ecuador' : 49,
        'Egypt' : 50,
        'El Salvador' : 51,
        'Eritrea' : 52,
        'Estonia' : 53,
        'Ethiopia' : 54,
        'Fiji' : 55,
        'Finland' : 56,
        'France' : 57,
        'Gabon' : 58,
        'Gambia' : 59,
        'Georgia' : 60,
        'Germany' : 61,
        'Ghana' : 62,
        'Greece' : 63,
        'Grenada' : 64,
        'Guatemala' : 65,
        'Guinea' : 66,
        'Guinea-Bissau' : 67,
        'Guyana' : 68,
        'Haiti' : 69,
        'Honduras' : 70,
        'Hong Kong (S.A.R.)' : 71,
        'Hungary' : 72,
        'Iceland' : 73,
        'India' : 74,
        'Indonesia' : 75,
        'Iran Islamic Republic of...' : 76,
        'Iraq' : 77,
        'Ireland' : 78,
        'Israel' : 79,
        'Italy' : 80,
        'Jamaica' : 81,
        'Japan' : 82,
        'Jordan' : 83,
        'Kazakhstan' : 84,
        'Kenya' : 85,
        'Kuwait' : 86,
        'Kyrgyzstan' : 87,
        'Latvia' : 88,
        'Lebanon' : 89,
        'Lesotho' : 90,
        'Liberia' : 91,
        'Libyan Arab Jamahiriya' : 92,
        'Liechtenstein' : 93,
        'Lithuania' : 94,
        'Luxembourg' : 95,
        'Madagascar' : 96,
        'Malawi' : 97,
        'Malaysia' : 98,
        'Maldives' : 99,
        'Mali' : 100,
        'Malta' : 101,
        'Marshall Islands' : 102,
        'Mauritania' : 103,
        'Mauritius' : 104,
        'Mexico' : 105,
        'Micronesia Federated States of...' : 106,
        'Monaco' : 107,
        'Mongolia' : 108,
        'Montenegro' : 109,
        'Morocco' : 110,
        'Mozambique' : 111,
        'Myanmar' : 112,
        'Namibia' : 113,
        'Nauru' : 114,
        'Nepal' : 115,
        'Netherlands' : 116,
        'New Zealand' : 117,
        'Nicaragua' : 118,
        'Niger' : 119,
        'Nigeria' : 120,
        'North Korea' : 121,
        'Norway' : 122,
        'Oman' : 123,
        'Other Country (Not Listed Above)' : 124,
        'Pakistan' : 125,
        'Palau' : 126,
        'Panama' : 127,
        'Paraguay' : 128,
        'Peru' : 129,
        'Philippines' : 130,
        'Poland' : 131,
        'Portugal' : 132,
        'Qatar' : 133,
        'Republic of Korea' : 134,
        'Republic of Moldova' : 135,
        'Romania' : 136,
        'Russian Federation' : 137,
        'Rwanda' : 138,
        'Saint Lucia' : 139,
        'San Marino' : 140,
        'Saudi Arabia' : 141,
        'Senegal' : 142,
        'Serbia' : 143,
        'Sierra Leone' : 144,
        'Singapore' : 145,
        'Slovakia' : 146,
        'Slovenia' : 147,
        'Solomon Islands' : 148,
        'Somalia' : 149,
        'South Africa' : 150,
        'South Korea' : 151,
        'Spain' : 152,
        'Sri Lanka' : 153,
        'Sudan' : 154,
        'Suriname' : 155,
        'Swaziland' : 156,
        'Sweden' : 157,
        'Switzerland' : 158,
        'Syrian Arab Republic' : 159,
        'Taiwan' : 160,
        'Tajikistan' : 161,
        'Thailand' : 162,
        'The former Yugoslav Republic of Macedonia' : 163,
        'Timor-Leste' : 164,
        'Togo' : 165,
        'Trinidad and Tobago' : 166,
        'Tunisia' : 167,
        'Turkey' : 168,
        'Turkmenistan' : 169,
        'Uganda' : 170,
        'Ukraine' : 171,
        'United Arab Emirates' : 172,
        'United Kingdom' : 173,
        'United Republic of Tanzania' : 174,
        'United States' : 175,
        'Uruguay' : 176,
        'Uzbekistan' : 177,
        'Venezuela Bolivarian Republic of...' : 178,
        'Viet Nam' : 179,
        'Yemen' : 180,
        'Zambia' : 181,
        'Zimbabwe' : 182,
        
        "0-2 years" : 0, 
        "3-5 years" : 1,
        "6-8 years" : 2,
        "9-11 years" : 3,
        "12-14 years" : 4, 
        "15-17 years" : 5,          
        "18-20 years" : 6,
        "21-23 years" : 7,
        "24-26 years" : 8,
        "27-29 years" : 9,
        "30 or more years": 10,

        "White or of European descent" : 0, 
        "South Asian" : 1, 
        "Hispanic or Latino/Latina" : 2, 
        "East Asian" : 3, 
        "Middle Eastern" : 4, 
        "Black or of African descent" : 5, 
        "Native American, Pacific Islander, or Indigenous Australian" : 6,

        "Under 18 years old" : 0, 
        "18 - 24 years old" : 1, 
        "25 - 34 years old" : 2, 
        "35 - 44 years old" : 3, 
        "45 - 54 years old" : 4, 
        "55 - 64 years old" : 5, 
        "65 years or older" : 6,


        "Employed full-time" : 0, 
        "Independent contractor, freelancer, or self-employed" : 1, 
        "Not employed, but looking for work" : 2,
        "Employed part-time" : 3, 
        "Not employed, and not looking for work" : 4, 
        "Retired" : 5,

        "I never completed any formal education" : 0, 
        "Primary/elementary school" : 1, 
        "Secondary school" : 2, 
        "Some college/university study without earning a degree" : 3, 
        "Associate degree" : 4, 
        "Bachelor's degree" : 5,
        "Master's degree" : 6, 
        "Professional degree" : 7, 
        "Doctoral degree" : 8,

        "Office / productivity suite (Microsoft Office, Google Suite, etc.)" : 0, 
        "Slack " : 1, 
        "Confluence " : 2, 
        "Jira " : 3,
        "Other chat system (IRC, proprietary software, etc.) " : 4, 
        "Other wiki tool (Github, Google Sites, proprietary software, etc.)" : 5,
        "Trello " : 6, 
        "Google Hangouts/Chat " : 7, 
        "HipChat " : 8, 
        "Facebook " : 9, 
        "Stack Overflow Enterprise" : 10,

        "1" : 0, 
        "2" : 1, 
        "3" : 2, 
        "4" : 3, 
        "More than 4" : 4,

        "Back-end developer" : 0, 
        "Full-stack developer" : 1, 
        "Front-end developer" : 2, 
        "Mobile developer" : 3, 
        "Desktop or enterprise applications developer" : 4,
        "Student" : 5, 
        "Database administrator" :6, 
        "Designer" : 7, 
        "System administrator" : 8, 
        "DevOps specialist" : 9, 
        "Data or business analyst" : 10,
        "Data scientist or machine learning specialist" : 11, 
        "QA or test developer" : 12, 
        "Engineering manager" : 13, 
        "Embedded applications or devices developer" : 14,
        "Game or graphics developer" : 15, 
        "Product manager" : 16, 
        "Educator or academic researcher" : 17, 
        "C-suite executive (CEO, CTO, etc.)" : 18, 
        "Marketing or sales professional" : 19,

        "I've never had a job" : 0, 
        "Less than a year ago" : 1, 
        "Between 1 and 2 years ago" : 2, 
        "Between 2 and 4 years ago" : 3, 
        "More than 4 years ago" : 4,

        "No" : 0, 
        "Yes, part-time" : 1, 
        "Yes, full-time" : 2,

        "Visual Studio Code" : 0, 
        "Visual Studio" : 1, 
        "Notepad++" : 2, 
        "Sublime Text" : 3, 
        "Vim" : 4, 
        "IntelliJ" : 5,
        "Android Studio" : 6, 
        "Eclipse" : 7, 
        "Atom" : 8, 
        "PyCharm" : 9,
        "Xcode" : 10, 
        "PHPStorm" : 11, 
        "NetBeans" : 12, 
        "IPython / Jupyter" : 13, 
        "Emacs" : 14, 
        "RStudio" : 15, 
        "RubyMine" : 16, 
        "TextMate" : 17, 
        "Coda" : 18, 
        "Komodo" : 19, 
        "Zend" : 20, 
        "Light Table" : 21

    }


    binary_list = ['Country_LE', 'YearsCodingProf', 'RaceEthnicity_LE', 'Age', 
                    'Employment_LE', 'FormalEducation', 'CommunicationTools_LE', 
                    'NumberMonitors', 'DevType_LE', 'LastNewJob', 'Student_LE', 'IDE_LE']

    numeric_list = ['AssessBenefits6', 'AssessBenefits3']

    column_list_to_map = ['Country_LE', 'YearsCodingProf', 'RaceEthnicity_LE', 'Age', 'Employment_LE', 'FormalEducation', 
                'CommunicationTools_LE', 'AssessBenefits6', 'NumberMonitors', 'DevType_LE', 'AssessBenefits3', 
                'LastNewJob', 'Student_LE', 'IDE_LE']


    for i in column_list_to_map:
        if i in binary_list: 
            features_df[i][0] = dictionary.get(features_df[i][0])
        else:
            pass

    st.markdown("<h3></h3>", unsafe_allow_html=True)

    for j in column_list_to_map:
        features_df[j] = pd.to_numeric(features_df[j], downcast='float')

    # locale.setlocale(locale.LC_ALL, 'en_US')

    if st.button('Predict'):
        prediction = model.predict(features_df)

        prediction_df = pd.DataFrame(prediction, columns=["Prediction"])

        st.markdown("<h3></h3>", unsafe_allow_html=True)
        # result_value = locale.format("%d",prediction_df['Prediction'][0], grouping=True)
        # st.success(result_value, icon="💰")
        # st.success(prediction_df["Prediction"][0])
        # st.write('$', round(prediction_df["Prediction"][0]))
        # st.info(round(prediction_df["Prediction"][0]))


        # Prediction değerini yuvarla ve string formatında göster
        prediction_value = round(prediction_df["Prediction"][0])
        prediction_value = f"{prediction_value:,}".replace(",", ".")
        info_message = f"Predicted value: $ {prediction_value}"
        st.info(info_message)

else:
    st.subheader("Dataset upload")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df_batch = pd.read_csv(uploaded_file,encoding= 'utf-8', low_memory=False, index_col=False)
        #Get overview of data
        # st.write(df_batch.head())
        st.write(df_batch)
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        #Preprocess inputs
                
        dictionary = {
        'Afghanistan' : 0,
        'Albania' : 1,
        'Algeria' : 2,
        'Andorra' : 3,
        'Angola' : 4,
        'Antigua and Barbuda' : 5,
        'Argentina' : 6,
        'Armenia' : 7,
        'Australia' : 8,
        'Austria' : 9,
        'Azerbaijan' : 10,
        'Bahamas' : 11,
        'Bahrain' : 12,
        'Bangladesh' : 13,
        'Barbados' : 14,
        'Belarus' : 15,
        'Belgium' : 16,
        'Belize' : 17,
        'Benin' : 18,
        'Bhutan' : 19,
        'Bolivia' : 20,
        'Bosnia and Herzegovina' : 21,
        'Botswana' : 22,
        'Brazil' : 23,
        'Brunei Darussalam' : 24,
        'Bulgaria' : 25,
        'Burkina Faso' : 26,
        'Burundi' : 27,
        'Cambodia' : 28,
        'Cameroon' : 29,
        'Canada' : 30,
        'Cape Verde' : 31,
        'Central African Republic' : 32,
        'Chile' : 33,
        'China' : 34,
        'Colombia' : 35,
        'Congo Republic of the...' : 36,
        'Costa Rica' : 37,
        'Croatia' : 38,
        'Cuba' : 39,
        'Cyprus' : 40,
        'Czech Republic' : 41,
        "Côte d'Ivoire" : 42,
        "Democratic People's Republic of Korea" : 43,
        'Democratic Republic of the Congo' : 44,
        'Denmark' : 45,
        'Djibouti' : 46,
        'Dominica' : 47,
        'Dominican Republic' : 48,
        'Ecuador' : 49,
        'Egypt' : 50,
        'El Salvador' : 51,
        'Eritrea' : 52,
        'Estonia' : 53,
        'Ethiopia' : 54,
        'Fiji' : 55,
        'Finland' : 56,
        'France' : 57,
        'Gabon' : 58,
        'Gambia' : 59,
        'Georgia' : 60,
        'Germany' : 61,
        'Ghana' : 62,
        'Greece' : 63,
        'Grenada' : 64,
        'Guatemala' : 65,
        'Guinea' : 66,
        'Guinea-Bissau' : 67,
        'Guyana' : 68,
        'Haiti' : 69,
        'Honduras' : 70,
        'Hong Kong (S.A.R.)' : 71,
        'Hungary' : 72,
        'Iceland' : 73,
        'India' : 74,
        'Indonesia' : 75,
        'Iran Islamic Republic of...' : 76,
        'Iraq' : 77,
        'Ireland' : 78,
        'Israel' : 79,
        'Italy' : 80,
        'Jamaica' : 81,
        'Japan' : 82,
        'Jordan' : 83,
        'Kazakhstan' : 84,
        'Kenya' : 85,
        'Kuwait' : 86,
        'Kyrgyzstan' : 87,
        'Latvia' : 88,
        'Lebanon' : 89,
        'Lesotho' : 90,
        'Liberia' : 91,
        'Libyan Arab Jamahiriya' : 92,
        'Liechtenstein' : 93,
        'Lithuania' : 94,
        'Luxembourg' : 95,
        'Madagascar' : 96,
        'Malawi' : 97,
        'Malaysia' : 98,
        'Maldives' : 99,
        'Mali' : 100,
        'Malta' : 101,
        'Marshall Islands' : 102,
        'Mauritania' : 103,
        'Mauritius' : 104,
        'Mexico' : 105,
        'Micronesia Federated States of...' : 106,
        'Monaco' : 107,
        'Mongolia' : 108,
        'Montenegro' : 109,
        'Morocco' : 110,
        'Mozambique' : 111,
        'Myanmar' : 112,
        'Namibia' : 113,
        'Nauru' : 114,
        'Nepal' : 115,
        'Netherlands' : 116,
        'New Zealand' : 117,
        'Nicaragua' : 118,
        'Niger' : 119,
        'Nigeria' : 120,
        'North Korea' : 121,
        'Norway' : 122,
        'Oman' : 123,
        'Other Country (Not Listed Above)' : 124,
        'Pakistan' : 125,
        'Palau' : 126,
        'Panama' : 127,
        'Paraguay' : 128,
        'Peru' : 129,
        'Philippines' : 130,
        'Poland' : 131,
        'Portugal' : 132,
        'Qatar' : 133,
        'Republic of Korea' : 134,
        'Republic of Moldova' : 135,
        'Romania' : 136,
        'Russian Federation' : 137,
        'Rwanda' : 138,
        'Saint Lucia' : 139,
        'San Marino' : 140,
        'Saudi Arabia' : 141,
        'Senegal' : 142,
        'Serbia' : 143,
        'Sierra Leone' : 144,
        'Singapore' : 145,
        'Slovakia' : 146,
        'Slovenia' : 147,
        'Solomon Islands' : 148,
        'Somalia' : 149,
        'South Africa' : 150,
        'South Korea' : 151,
        'Spain' : 152,
        'Sri Lanka' : 153,
        'Sudan' : 154,
        'Suriname' : 155,
        'Swaziland' : 156,
        'Sweden' : 157,
        'Switzerland' : 158,
        'Syrian Arab Republic' : 159,
        'Taiwan' : 160,
        'Tajikistan' : 161,
        'Thailand' : 162,
        'The former Yugoslav Republic of Macedonia' : 163,
        'Timor-Leste' : 164,
        'Togo' : 165,
        'Trinidad and Tobago' : 166,
        'Tunisia' : 167,
        'Turkey' : 168,
        'Turkmenistan' : 169,
        'Uganda' : 170,
        'Ukraine' : 171,
        'United Arab Emirates' : 172,
        'United Kingdom' : 173,
        'United Republic of Tanzania' : 174,
        'United States' : 175,
        'Uruguay' : 176,
        'Uzbekistan' : 177,
        'Venezuela Bolivarian Republic of...' : 178,
        'Viet Nam' : 179,
        'Yemen' : 180,
        'Zambia' : 181,
        'Zimbabwe' : 182,

        "0-2 years" : 0, 
        "3-5 years" : 1,
        "6-8 years" : 2,
        "9-11 years" : 3,
        "12-14 years" : 4, 
        "15-17 years" : 5,          
        "18-20 years" : 6,
        "21-23 years" : 7,
        "24-26 years" : 8,
        "27-29 years" : 9,
        "30 or more years": 10,

        "White or of European descent" : 0, 
        "South Asian" : 1, 
        "Hispanic or Latino/Latina" : 2, 
        "East Asian" : 3, 
        "Middle Eastern" : 4, 
        "Black or of African descent" : 5, 
        "Native American, Pacific Islander, or Indigenous Australian" : 6,

        "Under 18 years old" : 0, 
        "18 - 24 years old" : 1, 
        "25 - 34 years old" : 2, 
        "35 - 44 years old" : 3, 
        "45 - 54 years old" : 4, 
        "55 - 64 years old" : 5, 
        "65 years or older" : 6,


        "Employed full-time" : 0, 
        "Independent contractor, freelancer, or self-employed" : 1, 
        "Not employed, but looking for work" : 2,
        "Employed part-time" : 3, 
        "Not employed, and not looking for work" : 4, 
        "Retired" : 5,

        "I never completed any formal education" : 0, 
        "Primary/elementary school" : 1, 
        "Secondary school" : 2, 
        "Some college/university study without earning a degree" : 3, 
        "Associate degree" : 4, 
        "Bachelor’s degree (BA, BS, B.Eng., etc.)" : 5,
        "Master’s degree (MA, MS, M.Eng., MBA, etc.)" : 6, 
        "Professional degree" : 7, 
        "Doctoral degree" : 8,

        "Office / productivity suite (Microsoft Office, Google Suite, etc.)" : 0, 
        "Slack " : 1, 
        "Confluence " : 2, 
        "Jira " : 3,
        "Other chat system (IRC, proprietary software, etc.) " : 4, 
        "Other wiki tool (Github, Google Sites, proprietary software, etc.)" : 5,
        "Trello " : 6, 
        "Google Hangouts/Chat " : 7, 
        "HipChat " : 8, 
        "Facebook " : 9, 
        "Stack Overflow Enterprise" : 10,

        1 : 0, 
        2 : 1, 
        3 : 2, 
        4 : 3, 
        "More than 4" : 4,

        "Back-end developer" : 0, 
        "Full-stack developer" : 1, 
        "Front-end developer" : 2, 
        "Mobile developer" : 3, 
        "Desktop or enterprise applications developer" : 4,
        "Student" : 5, 
        "Database administrator" :6, 
        "Designer" : 7, 
        "System administrator" : 8, 
        "DevOps specialist" : 9, 
        "Data or business analyst" : 10,
        "Data scientist or machine learning specialist" : 11, 
        "QA or test developer" : 12, 
        "Engineering manager" : 13, 
        "Embedded applications or devices developer" : 14,
        "Game or graphics developer" : 15, 
        "Product manager" : 16, 
        "Educator or academic researcher" : 17, 
        "C-suite executive (CEO, CTO, etc.)" : 18, 
        "Marketing or sales professional" : 19,

        "I've never had a job" : 0, 
        "Less than a year ago" : 1, 
        "Between 1 and 2 years ago" : 2, 
        "Between 2 and 4 years ago" : 3, 
        "More than 4 years ago" : 4,

        "No" : 0, 
        "Yes, part-time" : 1, 
        "Yes, full-time" : 2,

        "Visual Studio Code" : 0, 
        "Visual Studio" : 1, 
        "Notepad++" : 2, 
        "Sublime Text" : 3, 
        "Vim" : 4, 
        "IntelliJ" : 5,
        "Android Studio" : 6, 
        "Eclipse" : 7, 
        "Atom" : 8, 
        "PyCharm" : 9,
        "Xcode" : 10, 
        "PHPStorm" : 11, 
        "NetBeans" : 12, 
        "IPython / Jupyter" : 13, 
        "Emacs" : 14, 
        "RStudio" : 15, 
        "RubyMine" : 16, 
        "TextMate" : 17, 
        "Coda" : 18, 
        "Komodo" : 19, 
        "Zend" : 20, 
        "Light Table" : 21

        }

        binary_list = ['Country_LE', 'YearsCodingProf', 'RaceEthnicity_LE', 'Age', 
                        'Employment_LE', 'FormalEducation', 'CommunicationTools_LE', 
                        'NumberMonitors', 'DevType_LE', 'LastNewJob', 'Student_LE', 'IDE_LE',]

        numeric_list = ['AssessBenefits6', 'AssessBenefits3']

        column_list_to_map = ['Country_LE', 'YearsCodingProf', 'RaceEthnicity_LE', 'Age', 'Employment_LE', 'FormalEducation', 
                    'CommunicationTools_LE', 'AssessBenefits6', 'NumberMonitors', 'DevType_LE', 'AssessBenefits3', 
                    'LastNewJob', 'Student_LE', 'IDE_LE',]

        df_new_batch = pd.DataFrame(columns=column_list_to_map)
        # st.write('map oncesi')

        # st.write('df_batch.shape[0]: ', df_batch.shape[0])

        for i in column_list_to_map:
            if i in binary_list:
                df_new_batch[i] = df_batch[i].map(dictionary)
            
            else:
                counter = 0
                while counter < df_batch.shape[0]:                    
                    df_new_batch[i][counter] = df_batch[i][counter]
                    counter += 1

        # st.write('df_new_batch')
        # st.write(df_new_batch)

        for j in column_list_to_map:
            df_new_batch[j] = pd.to_numeric(df_new_batch[j], downcast='float')


        # print('df_new_batch.info(): ', df_new_batch.info())

        if st.button('Predict'):
            prediction = model.predict(df_new_batch)

            prediction_df = pd.DataFrame(prediction, columns=["Prediction_$"])

            result_df = pd.concat([df_batch, prediction_df], axis=1, ignore_index=False, sort=False)

            st.markdown("<h3></h3>", unsafe_allow_html=True)
            st.subheader('Prediction')
            st.write(result_df)

            # DataFrame'i CSV string'ine çevir
            csv = result_df.to_csv(index=False)
            # CSV string'ini indirme butonu ile kullanıcıya sun
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='prediction_results.csv',
                mime='text/csv',
            )

            # DataFrame'i Excel olarak indirme işlevi
            def to_excel(df):
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, sheet_name='Sheet1')
                processed_data = output.getvalue()
                return processed_data
            
            excel_data = to_excel(result_df)  # result_df DataFrame'ini Excel'e dönüştür
            st.download_button(
                label="Download data as Excel",
                data=excel_data,
                file_name="prediction_results.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

