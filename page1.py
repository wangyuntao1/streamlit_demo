import streamlit as st
import pandas as pd

st.title("我的个人网站 💡")

"### 早上好！！"
a = 789 * 3
a

[11, 22, 33]

{"a": "1", "b": "2", "c": "3"}

st.image(r"D:\streamlit-demo\t01bc04a86021958639.jpg", width = 200)
df = pd.DataFrame({"学号": ["01", "02", "03", "04", "05"],
              "班级": ["二班", "一班", "二班", "三班", "一班"],
              "成绩": [92, 67, 70, 88, 76]})

st.dataframe(df)
st.divider()
st.table(df)