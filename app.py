import streamlit as  st
import pandas as pd
from various import bmi, appropriate_body_weight, body_mass_index

st.title('体格指数BMI等を算出するアプリ')
height = st.text_input('身長(cm)を入力してください', 164)
weight = st.text_input('体重(kg)を入力してください', 64.1)
if st.button('算出開始'):
    try:
        comment = st.empty()
        comment.write('算出を開始しました。')
        height = float(height)
        weight = float(weight)
        bmi = bmi(height, weight)
        appropriate_body_weight = appropriate_body_weight(height)
        body_mass_index = body_mass_index(bmi)
        st.write(f'BMIは{str(bmi)}です。')
        st.write(f'適正体重は{str(appropriate_body_weight)}kgです。')
        st.write(f'肥満度は、{body_mass_index}です。')
        data = {
            'BMIの範囲':['18.5未満', '18.5から25未満', '25から30未満', '30から35未満', '35から40未満', '40以上'],
            '肥満度':['低体重', '普通体重', '肥満（１度）', '肥満（２度）', '肥満（３度）', '肥満（４度）']
        }
        df = pd.DataFrame(data, columns = ['BMIの範囲','肥満度'])
        st.table(df)
        comment.write('完了しました！')
    except:
        st.error('エラーが発生しました。身長(cm)及び体重(kg)を入力して、再度実行してください。')
