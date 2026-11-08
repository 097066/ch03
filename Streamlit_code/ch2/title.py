# 第二章/title.py
import streamlit as st # 導入Streamlit並用st代表它
# 這裡為了示範創建了多個標題展示元素

# 建立一個標題展示元素，內容是全英文的，預設錨點為first-title
st.title("first title")

# 建立一個標題展示元素，內容是全中文的
# 如不定義anchor參數，則無錨點
st.title("標題")

# 建立一個標題展示元素，內容是中英文混雜的
# 預設的錨點是英文部分的，即chinese
st.title("這是chinese標題")

# 第四個標題展示元素,並增加了錨點
st.title('這是第四個標題',anchor='fourth')

# 第五個標題展示元素,並增加了錨點和工具提示
st.title('這是第五個標題',anchor='fifth', help='工具提示')

# 第六個標題展示元素,內容使用了Markdown語法和表情符號,並增加了錨點和工具提示
st.title('這是第*六*個標題 :sunglasses:',anchor='sixth')
