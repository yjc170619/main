import streamlit as st
import numpy as np 

def calculate(expression):  
    try:  
        result = eval(expression)  
        return result  
    except:  
        st.error('等待输入')  
        return None
  
def main():
    #标题
    st.header('科学计算器')  
    # 输入表达式  
    expression = st.text_input('请输入表达式')
    # 计算结果  
    result = calculate(expression)
    if st.button('计算'):
        st.write('结果是：',result)  
      
  
if __name__ == '__main__':  
    main()