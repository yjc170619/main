import streamlit as st
from math import *

def main():
    st.header('原神伤害计算器')

    #分成两列，左列选择乘区，右列是便携计算器
    col_cq,col_cal=st.columns([0.7,0.3])

    #左列开始
    with col_cq:
        #分成6页，每页放置一个乘区
        tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['基准*倍率+附加','增伤','抗性','防御','双爆','增幅'])
        with tab1:
            #基准（jz）*倍率（bl）乘区,gjl攻击力，smz生命值，fyl防御力，ysjt元素精通，cs乘数
            if st.toggle('攻击力倍率'):
                gjl=st.number_input('请输入攻击力',min_value=0,value=2000,step=1)
                bl_gjl=st.number_input('请输入攻击力倍率',min_value=0.0,value=1.0,step=0.001)
                #攻击力倍率乘数
                if st.toggle('攻击力倍率乘数'):
                    gjlblcs=st.number_input('请输入攻击力倍率乘数',min_value=0.0,value=1.0,step=0.001)
                    gjlbl=gjl*bl_gjl*gjlblcs
                else:    
                    gjlbl=gjl*bl_gjl
            else:
                gjlbl=0

            if st.toggle('生命值倍率'):
                smz=st.number_input('请输入生命值',min_value=0,value=20000,step=1)
                bl_smz=st.number_input('请输入生命值倍率',min_value=0.0,value=1.0,step=0.001)
                smzbl=smz*bl_smz
            else:
                smzbl=0

            if st.toggle('防御力倍率'):
                fyl=st.number_input('请输入防御力',min_value=0,value=2000,step=1)
                bl_fyl=st.number_input('请输入防御力倍率',min_value=0.0,value=1.0,step=0.001)  
                fylbl=fyl*bl_fyl
            else:
                fylbl=0

            if st.toggle('元素精通倍率'):
                ysjt=st.number_input('请输入元素精通',min_value=0,value=200,step=1)
                bl_ysjt=st.number_input('请输入参与倍率计算的元素精通',min_value=0.0,value=1.0,step=0.001) 
                ysjtbl=ysjt*bl_ysjt
            else:
                ysjtbl=0
            #基准倍率求和
            jzbl=gjlbl+smzbl+fylbl+ysjtbl

            #附加倍率，fj附加
            if st.toggle('附加倍率'):
                if st.toggle('附加攻击力倍率'):
                    fjgjl=st.number_input('请输入附加攻击力',min_value=0,value=2000,step=1)
                    bl_fjgjl=st.number_input('请输入附加攻击力倍率',min_value=0.0,value=1.0,step=0.001)
                    fj_gjlbl=fjgjl*bl_fjgjl
                else:
                    fj_gjlbl=0

                if st.toggle('附加生命值倍率'):
                    fjsmz=st.number_input('请输入附加生命值',min_value=0,value=20000,step=1)
                    bl_fjsmz=st.number_input('请输入附加生命值倍率',min_value=0.0,value=1.0,step=0.001)
                    fj_smzbl=fjsmz*bl_fjsmz
                else:
                    fj_smzbl=0

                if st.toggle('附加防御力倍率'):
                    fjfyl=st.number_input('请输入附加防御力',min_value=0,value=2000,step=1)
                    bl_fjfyl=st.number_input('请输入附加防御力倍率',min_value=0.0,value=1.0,step=0.001)  
                    fj_fylbl=fjfyl*bl_fjfyl
                else:
                    fj_fylbl=0

                if st.toggle('附加元素精通倍率'):
                    fjysjt=st.number_input('请输入附加元素精通',min_value=0,value=200,step=1)
                    bl_fjysjt=st.number_input('请输入附加元素精通倍率',min_value=0.0,value=1.0,step=0.001) 
                    fj_ysjtbl=fjysjt*bl_fjysjt
                else:
                    fj_ysjtbl=0
                #附加倍率求和
                fjbl=fj_gjlbl+fj_fylbl+fj_smzbl+fj_ysjtbl
            else:
                fjbl=0

        with tab2:
            #增伤（zs）乘区
            zs=st.number_input('请输入增伤系数',min_value=0.0,value=1.0,step=0.001)

        with tab3:
            #抗性（kx）乘区，gwkx怪物抗性
            gwkx=st.number_input('请输入怪物抗性',value=1.0,step=0.001)
            if gwkx<0:
                kx=1-gwkx/2
            if gwkx>0.75:
                kx=1/(1+4*gwkx)
            else:
                kx=1-gwkx

        with tab4:
            #防御（fy）乘区,jsdj角色等级，gwdj怪物等级，jf减防，wsfy无视防御
            jsdj=st.slider('请选择角色等级',1,90,90)
            gwdj=st.slider('请选择怪物等级',1,100,100)
            jf=st.number_input('请输入减防量',min_value=0.0,value=0.0,step=0.01)
            wsfy=st.number_input('请输入无视防御量',min_value=0.0,value=0.0,step=0.01)
            #计算防御区乘数
            fy=(jsdj+100)/((gwdj+100)*(1-jf)*(1-wsfy)+(jsdj+100))

        with tab5:
            #暴击乘区，bjl暴击率，bjsh暴击伤害，qw期望
            bjl=st.number_input('请输入暴击率',min_value=0.0,max_value=1.0,value=0.05,step=0.001)
            bjsh=st.number_input('请输入暴击伤害',min_value=0.0,value=0.5,step=0.001)
            #暴击期望乘数计算
            qw=1+bjl*bjsh

        with tab6:
            #增幅（zf）乘区，jczf基础增幅
            jczf=st.slider('请选择基础增幅系数',1.0,2.0,1.0,0.5)
            if jczf>1:
                ysjt_r=st.number_input('请输入用于反应的元素精通',min_value=0,value=200,step=1)
                zf=jczf+278*ysjt_r/(ysjt_r+1400)
    #左列结束

    #右列开始
    with col_cal:
        def calculate(expression):  
            try:  
                result = eval(expression)  
                return result  
            except:  
                st.error('等待输入')  
                return None
            
        st.subheader('便携计算器')    
        expression = st.text_input('请输入表达式')
        result = calculate(expression)
        if st.button('='):
            st.write('结果是：',result)  

    #伤害计算,result伤害结果，_b暴击伤害，_qw暴击期望伤害，_r反应伤害
    if st.button('计算'):
        result=(jzbl+fjbl)*zs*kx*fy
        result_b=result*(1+bjsh)
        result_qw=result*qw
        st.write('无反应未暴击伤害是：',round(result))
        st.write('无反应暴击伤害是：',round(result_b))
        st.write('无反应期望伤害是：',round(result_qw))
        if jczf>1:
            result_r=result*zf
            result_r_b=result_r*(1+bjsh)
            result_r_qw=result_r*qw
            st.write('反应未暴击伤害是：',round(result_r))
            st.write('反应暴击伤害是：',round(result_r_b))
            st.write('反应期望伤害是：',round(result_r_qw))
    
if __name__ == '__main__':  
    main()