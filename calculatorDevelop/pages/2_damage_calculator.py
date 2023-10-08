import streamlit as st

def main():
    st.header('原神伤害计算器')
    sd=st.number_input('请输入基准量',min_value=0,step=1)
    mp=st.number_input('请输入倍率',min_value=0.0,step=0.001)
    ex=st.number_input('请输入附加量',min_value=0.0,value=0.0,step=0.001)
    db=st.number_input('请输入增伤系数',min_value=0.0,value=1.0,step=0.001)
    rq=st.number_input('请输入抗性系数',min_value=0.0,value=1.0,step=0.001)
    cl=st.slider('请选择角色等级',1,90,90)
    ml=st.slider('请选择怪物等级',1,100,100)
    dr1=st.number_input('请输入减防量',min_value=0.0,value=1.0,step=0.01)
    dr2=st.number_input('请输入无视防御量',min_value=0.0,value=1.0,step=0.01)
    cr=st.number_input('请输入暴击率',min_value=0.0,max_value=1.0,value=0.5,step=0.001)
    cd=st.number_input('请输入暴击伤害',min_value=0.0,value=1.0,step=0.001)
    ic=st.slider('请输入增幅系数',1.0,2.0,1.0,0.5)
    if ic>1:
        em=st.number_input('请输入元素精通',min_value=0,value=0,step=1)

    dc=(cl+100)/((ml+100)*(1-dr1)*(1-dr2)+(cl+100))
    cp=1+cr*cd
    if ic>1:
        rc=ic+278*em/(em+1400)

    if st.button('计算'):
        result=(sd*mp+ex)*db*rq*dc
        result_c=result*(1+cd)
        result_cp=result*cp
        st.write('无反应未暴击伤害是：',result)
        st.write('无反应暴击伤害是：',result_c)
        st.write('无反应期望伤害是：',result_cp)
        if ic>1:
            result_r=result*rc
            result_r_c=result_r*(1+cd)
            result_r_cp=result_r*cp
            st.write('反应未暴击伤害是：',result_r)
            st.write('反应暴击伤害是：',result_r_c)
            st.write('反应期望伤害是：',result_r_cp)
    


if __name__ == '__main__':  
    main()