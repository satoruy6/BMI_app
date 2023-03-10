import streamlit as  st
import pandas as pd
from various import Person

st.set_page_config(
  page_title="BMI app",
  page_icon="ð",
)

st.title('ä½æ ¼ææ°BMIç­ãç®åºããã¢ããª')
height = st.text_input('èº«é·(cm)ãå¥åãã¦ãã ãã', 164)
weight = st.text_input('ä½é(kg)ãå¥åãã¦ãã ãã', 64.1)
if st.button('ç®åºéå§'):
    try:
        comment = st.empty()
        comment.write('ç®åºãéå§ãã¾ããã')
        height = float(height)
        weight = float(weight)
        person = Person(height, weight)
        bmi = person.bmi()
        appropriate_body_weight = person.appropriate_body_weight()
        body_mass_index = person.body_mass_index()
        st.write(f'BMIã¯{str(bmi)}ã§ãã')
        st.write(f'é©æ­£ä½éã¯{str(appropriate_body_weight)}kgã§ãã')
        st.write(f'è¥æºåº¦ã¯ã{body_mass_index}ã§ãã')
        data = {
            'BMIã®ç¯å²':['18.5æªæº', '18.5ãã25æªæº', '25ãã30æªæº', '30ãã35æªæº', '35ãã40æªæº', '40ä»¥ä¸'],
            'è¥æºåº¦':['ä½ä½é', 'æ®éä½é', 'è¥æºï¼ï¼åº¦ï¼', 'è¥æºï¼ï¼åº¦ï¼', 'è¥æºï¼ï¼åº¦ï¼', 'è¥æºï¼ï¼åº¦ï¼']
        }
        df = pd.DataFrame(data, columns = ['BMIã®ç¯å²','è¥æºåº¦'])
        st.table(df)
        comment.write('å®äºãã¾ããï¼')
    except:
        st.error('ã¨ã©ã¼ãçºçãã¾ãããèº«é·(cm)åã³ä½é(kg)ãå¥åãã¦ãååº¦å®è¡ãã¦ãã ããã')
