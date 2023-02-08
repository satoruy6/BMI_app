#身長(cm)と体重(kg)から体格指数BMIをfloat形式で小数点２桁まで返す関数
def bmi(height_cm, weight_kg):
    bmi_raw = weight_kg/((height_cm/100)*(height_cm/100))
    bmi_2digit = round(bmi_raw, 2)
    return bmi_2digit

#身長(cm)と体重(kg)から体格指数BMIをfloat形式で生値で返す関数
def bmi_raw(height_cm, weight_kg):
    bmi_raw = weight_kg/((height_cm/100)*(height_cm/100))
    return bmi_raw

#身長(cm)から適正体重(kg)をfloat形式で返す関数
def appropriate_body_weight(height_cm):
    appropriate_body_weight = (height_cm/100)*(height_cm/100)*22
    appropriate_body_weight = round(appropriate_body_weight, 1)
    return appropriate_body_weight

#BMIから肥満度(body_mass_index)をstring形式で返す関数
def body_mass_index(bmi):
    bmi = float(bmi)
    body_mass_index = None
    if bmi < 18.5:
        body_mass_index = "低体重"
    elif bmi >=18.5 and bmi < 25:
        body_mass_index ="普通体重"
    elif bmi >= 25 and bmi < 30:
        body_mass_index = "肥満（１度）"
    elif bmi >=30 and bmi < 35:
        body_mass_index = "肥満（2度）"
    elif bmi >= 35 and bmi <40:
        body_mass_index = "肥満（3度）"
    elif bmi >= 40:
        body_mass_index = "肥満（4度）"
    return body_mass_index
