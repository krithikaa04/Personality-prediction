import pickle

import numpy as np
import pandas as pd
import streamlit as st

# a44a3f f19c79 cbdfbd f6f4d2 d4e09b
print("hello")

def main():
    st.markdown(
    """
    <style>
        body {
        background-color: #c9cba3  ;
    }
    .header {
        font-size: 36px;
        font-weight: bold;
        color: #472d30;
        text-align: center;
        margin-top: 0px;
        justify-content: center;
    }

        .sub-header {
            font-size: 36px;
            font-weight: bold;
            color: #472d30;
            text-align: center;
            margin-top: 10px;
        }

        .description {
            font-size: 18px;
            color: #000000;
            text-align: center;
            margin-top: 20px;
        }

        .questions{
            font-size: 18px;
            color: #472d30;
            margin-top: 50px;
        }

        .notes{
            font-size: 20px;
            font-weight: bold;
            color: #e26d5c;
        }
        
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Main header
    st.write('<div class="header">PERSONALITY QUESTIONAIRRE</div>', unsafe_allow_html=True)
    st.image("personalities.png", use_column_width=True)
    st.write('<div class="description">Comprehending and predicting personality is an interesting study into the individuality of every person. The intricate combination of traits, and features make up our personalities. It affects our inclinations, social interactions, professional decisions, and even how we respond to challenges in life.',unsafe_allow_html=True)
    st.write("<div class='description'>The science of identifying these characteristics is the focus of personality prediction, which offers insights about a person's inclinations, preferences, and responses to diverse circumstances. Welcome to the Personality Assessment. This quick questionnaire will help you gain insights into your personality traits.",unsafe_allow_html=True)
    st.write("<div class='description'>This page is a questionnaire, each focusing on a specific personality trait: Openness, Neuroticism, Conscientiousness, Agreeableness, and Extraversion.<br><br>",unsafe_allow_html=True)
    st.image("personalities2.png", use_column_width=True)
    
    
    st.write("<br>" * 5, unsafe_allow_html=True)
    st.write('<div class="sub-header"> Lets get started!!!</div>', unsafe_allow_html=True)
    st.write("<div class='description notes'>For every question move the slider to your desired value with 10 being the most agreeable to the question and 1 being the least agreeable.",unsafe_allow_html=True)
    # Input sliders for personality scores

    st.write("<div class='questions'>How willing are you to understand and empathize with others' viewpoints, even if they differ from your own?</div>", unsafe_allow_html=True)
    agreeableness_1 = st.slider("", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How much do you enjoy working in team settings and collaborative environments?</div>", unsafe_allow_html=True)
    extraversion_1 = st.slider(" ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>Are you usually punctual and strive to meet deadlines?</div>", unsafe_allow_html=True)
    conscientiousness_1 = st.slider("   ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'> Are you drawn to adventures and travel to unfamiliar places?",unsafe_allow_html=True)
    openness_1 = st.slider("    ",min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How well do you generally react to unexpected challenges or stress in your life?</div>", unsafe_allow_html=True)
    neuroticism_1 = st.slider("     ", min_value=1, max_value=10, value=0)  
    st.write("<div class='questions'>How much do you tend to be methodical and detail-oriented in your work or projects?</div>", unsafe_allow_html=True)
    conscientiousness_2 = st.slider("      ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>In group situations, do you often go along with what the majority wants to avoid conflict?</div>", unsafe_allow_html=True)
    agreeableness_2 = st.slider("       ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How comfortable are you with unconventional or avant-garde ideas and art forms?</div>", unsafe_allow_html=True)
    openness_2 = st.slider("        ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How often are you prone to mood swings or emotional fluctuations?</div>", unsafe_allow_html=True)
    neuroticism_2 = st.slider("         ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>Do you feel energized and recharged after spending time with others?</div>", unsafe_allow_html=True)
    extraversion_2 = st.slider("          ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How well do you handle conflicts and disagreements in your relationships?</div>", unsafe_allow_html=True)
    agreeableness_3 = st.slider("           ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>Do you frequently find yourself worrying about things that might go wrong?</div>", unsafe_allow_html=True)
    neuroticism_3 = st.slider("            ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How often do you actively seek out and embrace new experiences or viewpoints in your life?</div>", unsafe_allow_html=True)
    openness_3 = st.slider("             ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How much do you enjoy socializing with new people and being the center of attention in a group?</div>", unsafe_allow_html=True)
    extraversion_3 = st.slider("              ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How important is it for you to keep your living and working spaces neat and well-organized?</div>", unsafe_allow_html=True)
    conscientiousness_3 = st.slider("               ", min_value=1, max_value=10, value=0)
        
    conscientiousness = int(conscientiousness_1+conscientiousness_2+conscientiousness_3/3)
    openness = int(openness_1+openness_2+openness_3/3)
    neuroticism = int(neuroticism_2+neuroticism_1+neuroticism_3/3)
    agreeableness = int(agreeableness_3+agreeableness_1+agreeableness_2/3)
    extraversion = int(extraversion_3+extraversion_2+extraversion_1/3)
    


    if st.button("Predict"):
        personality = get_personality_description(openness, neuroticism, conscientiousness, agreeableness, extraversion)
        personality =personality.lower()
        if(personality=='dependable'):
                st.write('<div class="header">You are a DEPENDANT person</div>', unsafe_allow_html=True)
                st.write('<div class="description">Individuals with a dependable personality are pillars of reliability and consistency. They are trustworthy and take their commitments seriously, often going the extra mile to ensure that tasks are completed efficiently and on time. ',unsafe_allow_html=True)
                st.write("<div class='description'>Dependable people are valued for their steadfastness, attention to detail, and the sense of security they provide in both personal and professional relationships.",unsafe_allow_html=True)
        if(personality=='serious'):
                st.write('<div class="header">You are a SERIOUD person</div>', unsafe_allow_html=True)
                st.write('<div class="description">Those with a serious personality type approach life with a sense of purpose and determination. They are often meticulous planners, setting clear goals and working diligently to achieve them.',unsafe_allow_html=True)
                st.write("<div class='description'>Serious individuals tend to be disciplined, focused, and may exhibit a strong sense of duty.",unsafe_allow_html=True)
                st.write("<div class='description'>Their practical mindset and ability to stay composed under pressure make them effective problem-solvers.<br><br>",unsafe_allow_html=True)
        elif(personality=='extraverted'):
                st.write('<div class="header">You are an EXTRAVERTED person</div>', unsafe_allow_html=True)
                st.write('<div class="description">Extraverted individuals thrive in social environments, drawing energy from interactions with others. They are outgoing, expressive, and often the life of the party. Extraverts enjoy being the center of attention and are skilled communicators. ',unsafe_allow_html=True)
                st.write("<div class='description'>Their spontaneity and openness make them approachable, and they contribute to the vibrancy of social situations with their lively and engaging presence.<br><br>",unsafe_allow_html=True)
        elif(personality=='responsible'):
                st.write('<div class="header">You are a RESPONSIBLE person</div>', unsafe_allow_html=True)
                st.write('<div class="description">Responsible individuals are characterized by their conscientious nature and commitment to fulfilling obligations. They take pride in their work, paying close attention to details and delivering results with a high degree of accuracy. ',unsafe_allow_html=True)
                st.write("<div class='description'>Responsible people are often seen as dependable team members who can be relied upon to meet deadlines and uphold the standards of excellence in their tasks.<br><br>",unsafe_allow_html=True)
        elif(personality=='lively'):
                st.write('<div class="header">You are a LIVELY person</div>', unsafe_allow_html=True)
                st.write('<div class="description">Lively individuals bring energy and enthusiasm to every aspect of life. They possess a zest for living, often seeking out new experiences and embracing spontaneity. ',unsafe_allow_html=True)
                st.write("<div class='description'> Lively people enjoy socializing, making them natural connectors in various social circles. Their optimistic outlook, sense of humor, and willingness to try new things make them enjoyable companions and contribute to a dynamic and exciting atmosphere.<br><br>",unsafe_allow_html=True)
            
        st.write(" <div class='description notes'>THANK YOU FOR YOUR TIME!",unsafe_allow_html=True)

def get_personality_description(openness, neuroticism, conscientiousness, agreeableness, extraversion):
    result = np.array([openness, neuroticism, conscientiousness, agreeableness, extraversion], ndmin=2)
    df1 = pd.DataFrame(result)
    testdf = df1[[0, 1, 2, 3, 4]]
    maintestarray = testdf.valuesstrea

    # Load the model from the pickle file
    with open('multiNomialLogisticRegression.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    print(maintestarray)
    # Make predictions
    y_pred = loaded_model.predict(maintestarray)
    #print(accuracy_score(y_pred,maintestarray[-1])*100)
    # Post-process predictions
    y_pred = [str(pred) for pred in y_pred]

    # Create DataFrame with predictions
    DF = pd.DataFrame(y_pred, columns=["Predicted Personality"])
    DF.index = DF.index + 1
    DF.index.names = ["Person No"]

    print("Predicted Personality:", DF["Predicted Personality"].tolist()[0])
    personality = DF["Predicted Personality"].tolist()[0]
    return personality

if __name__ == '__main__':
    main()
