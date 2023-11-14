#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open('logo-short.png')
st.set_page_config(
    page_title="Storage_Fee|LogiGeek", 
    page_icon=image,
    layout="wide")

st.header('N期制保管料のシミュレーションアプリ')
st.text('')
st.subheader('このアプリでできること')
st.text('倉庫保管料の単価設定には二期制（１５日単位）、三期制（１０日単位）、四期制（週単位）、日単位等があります。')
st.text('このアプリは具体的な入庫／出庫データを基に、単価設定の違いにより一ヶ月の保管料がどれだけ異なってくるかをシミュレーションします。')
st.text('詳細な使い方は下記のサイトを参照下さい↓')
st.link_button(":blue[【物流担当者必見！】三期制の保管料はこんなに損。アプリで簡単シミュレーション|ロジギーク]", 
               "https://rikei-logistics.com/app-storage1")
st.text('')

st.sidebar.header('◆変数設定画面◆')
st.sidebar.subheader('１．日々の入庫CBM変更')
in0 = 0
in1 = st.sidebar.number_input(label = '１日目', value = 0, label_visibility="visible")
in2 = st.sidebar.number_input(label = '２日目', value = 0, label_visibility="visible")
in3 = st.sidebar.number_input(label = '３日目', value = 0, label_visibility="visible")
in4 = st.sidebar.number_input(label = '４日目', value = 669, label_visibility="visible")
in5 = st.sidebar.number_input(label = '５日目', value = 0, label_visibility="visible")
in6 = st.sidebar.number_input(label = '６日目', value = 0, label_visibility="visible")
in7 = st.sidebar.number_input(label = '７日目', value = 0, label_visibility="visible")
in8 = st.sidebar.number_input(label = '８日目', value = 0, label_visibility="visible")
in9 = st.sidebar.number_input(label = '９日目', value = 0, label_visibility="visible")
in10 = st.sidebar.number_input(label = '１０日目', value = 0, label_visibility="visible")
in11 = st.sidebar.number_input(label = '１１日目', value = 773, label_visibility="visible")
in12 = st.sidebar.number_input(label = '１２日目', value = 0, label_visibility="visible")
in13 = st.sidebar.number_input(label = '１３日目', value = 0, label_visibility="visible")
in14 = st.sidebar.number_input(label = '１４日目', value = 0, label_visibility="visible")
in15 = st.sidebar.number_input(label = '１５日目', value = 0, label_visibility="visible")
in16 = st.sidebar.number_input(label = '１６日目', value = 0, label_visibility="visible")
in17 = st.sidebar.number_input(label = '１７日目', value = 678, label_visibility="visible")
in18 = st.sidebar.number_input(label = '１８日目', value = 0, label_visibility="visible")
in19 = st.sidebar.number_input(label = '１９日目', value = 0, label_visibility="visible")
in20 = st.sidebar.number_input(label = '２０日目', value = 0, label_visibility="visible")
in21 = st.sidebar.number_input(label = '２１日目', value = 0, label_visibility="visible")
in22 = st.sidebar.number_input(label = '２２日目', value = 0, label_visibility="visible")
in23 = st.sidebar.number_input(label = '２３日目', value = 0, label_visibility="visible")
in24 = st.sidebar.number_input(label = '２４日目', value = 703, label_visibility="visible")
in25 = st.sidebar.number_input(label = '２５日目', value = 0, label_visibility="visible")
in26 = st.sidebar.number_input(label = '２６日目', value = 0, label_visibility="visible")
in27 = st.sidebar.number_input(label = '２７日目', value = 0, label_visibility="visible")
in28 = st.sidebar.number_input(label = '２８日目', value = 0, label_visibility="visible")
in29 = st.sidebar.number_input(label = '２９日目', value = 0, label_visibility="visible")
in30 = st.sidebar.number_input(label = '３０日目', value = 778, label_visibility="visible")
ins = [in1, in2, in3, in4, in5, in6, in7, in8, in9, in10,
      in11, in12, in13, in14, in15, in16, in17, in18, in19, in20,
      in21, in22, in23, in24, in25, in26, in27, in28, in29, in30]

st.sidebar.text('')
st.sidebar.subheader('２．日々の出庫CBM変更')
out0 = 0
out1 = st.sidebar.number_input(label = '１日目', value = 95, label_visibility="visible")
out2 = st.sidebar.number_input(label = '２日目', value = 16, label_visibility="visible")
out3 = st.sidebar.number_input(label = '３日目', value = 36, label_visibility="visible")
out4 = st.sidebar.number_input(label = '４日目', value = 195, label_visibility="visible")
out5 = st.sidebar.number_input(label = '５日目', value = 170, label_visibility="visible")
out6 = st.sidebar.number_input(label = '６日目', value = 135, label_visibility="visible")
out7 = st.sidebar.number_input(label = '７日目', value = 126, label_visibility="visible")
out8 = st.sidebar.number_input(label = '８日目', value = 40, label_visibility="visible")
out9 = st.sidebar.number_input(label = '９日目', value = 13, label_visibility="visible")
out10 = st.sidebar.number_input(label = '１０日目', value = 74, label_visibility="visible")
out11 = st.sidebar.number_input(label = '１１日目', value = 201, label_visibility="visible")
out12 = st.sidebar.number_input(label = '１２日目', value = 168, label_visibility="visible")
out13 = st.sidebar.number_input(label = '１３日目', value = 183, label_visibility="visible")
out14 = st.sidebar.number_input(label = '１４日目', value = 147, label_visibility="visible")
out15 = st.sidebar.number_input(label = '１５日目', value = 37, label_visibility="visible")
out16 = st.sidebar.number_input(label = '１６日目', value = 19, label_visibility="visible")
out17 = st.sidebar.number_input(label = '１７日目', value = 113, label_visibility="visible")
out18 = st.sidebar.number_input(label = '１８日目', value = 137, label_visibility="visible")
out19 = st.sidebar.number_input(label = '１９日目', value = 154, label_visibility="visible")
out20 = st.sidebar.number_input(label = '２０日目', value = 97, label_visibility="visible")
out21 = st.sidebar.number_input(label = '２１日目', value = 177, label_visibility="visible")
out22 = st.sidebar.number_input(label = '２２日目', value = 130, label_visibility="visible")
out23 = st.sidebar.number_input(label = '２３日目', value = 35, label_visibility="visible")
out24 = st.sidebar.number_input(label = '２４日目', value = 97, label_visibility="visible")
out25 = st.sidebar.number_input(label = '２５日目', value = 207, label_visibility="visible")
out26 = st.sidebar.number_input(label = '２６日目', value = 133, label_visibility="visible")
out27 = st.sidebar.number_input(label = '２７日目', value = 130, label_visibility="visible")
out28 = st.sidebar.number_input(label = '２８日目', value = 134, label_visibility="visible")
out29 = st.sidebar.number_input(label = '２９日目', value = 101, label_visibility="visible")
out30 = st.sidebar.number_input(label = '３０日目', value = 24, label_visibility="visible")
outs = [out1, out2, out3, out4, out5, out6, out7, out8, out9, out10,
      out11, out12, out13, out14, out15, out16, out17, out18, out19, out20,
      out21, out22, out23, out24, out25, out26, out27, out28, out29, out30]

st.sidebar.text('')
st.sidebar.subheader('３．初期在庫CBM変更')
st0 = st.sidebar.number_input(label = '初期在庫CBM', value = 500, label_visibility="visible")

st1 = st0 + in1 - out1
st2 = st1 + in2 - out2
st3 = st2 + in3 - out3
st4 = st3 + in4 - out4
st5 = st4 + in5 - out5
st6 = st5 + in6 - out6
st7 = st6 + in7 - out7
st8 = st7 + in8 - out8
st9 = st8 + in9 - out9
st10 = st9 + in10 - out10
st11 = st10 + in11 - out11
st12 = st11 + in12 - out12
st13 = st12 + in13 - out13
st14 = st13 + in14 - out14
st15 = st14 + in15 - out15
st16 = st15 + in16 - out16
st17 = st16 + in17 - out17
st18 = st17 + in18 - out18
st19 = st18 + in19 - out19
st20 = st19 + in20 - out20
st21 = st20 + in21 - out21
st22 = st21 + in22 - out22
st23 = st22 + in23 - out23
st24 = st23 + in24 - out24
st25 = st24 + in25 - out25
st26 = st25 + in26 - out26
st27 = st26 + in27 - out27
st28 = st27 + in28 - out28
st29 = st28 + in29 - out29
st30 = st29 + in30 - out30
sts = [st0, st1, st2, st3, st4, st5, st6, st7, st8, st9,
      st10, st11, st12, st13, st14, st15, st16, st17, st18, st19,
      st20, st21, st22, st23, st24, st25, st26, st27, st28, st29]

st.sidebar.text('')
st.sidebar.subheader('４．保管料設定変更')
charge_30 = st.sidebar.number_input(label = '１日当たりの保管料（円/CBM･日）', value = 30, label_visibility="visible")
rate_2 = st.sidebar.number_input(label = '二期制の場合の保管料割引率（％）', value = 0, label_visibility="visible")
rate_3 = st.sidebar.number_input(label = '三期制の場合の保管料割引率（％）', value = 0, label_visibility="visible")
rate_4 = st.sidebar.number_input(label = '四期制の場合の保管料割引率（％）', value = 0, label_visibility="visible")

st.text('')
st.subheader('入出庫データ')
list1=[[in0,out0,st0],
    [in1,out1,st1], [in2,out2,st2], [in3,out3,st3], [in4,out4,st4], [in5,out5,st5], 
       [in6,out6,st6], [in7,out7,st7], [in8,out8,st8], [in9,out9,st9], [in10,out10,st10],
       [in11,out11,st11], [in12,out12,st12], [in13,out13,st13], [in14,out14,st14], [in15,out15,st15],
       [in16,out16,st16], [in17,out17,st17], [in18,out18,st18], [in19,out19,st19], [in20,out20,st20],
       [in21,out21,st21], [in22,out22,st22], [in23,out23,st23], [in24,out24,st24], [in25,out25,st25],
       [in26,out26,st26], [in27,out27,st27], [in28,out28,st28], [in29,out29,st29], [in30,out30,st30]]
index1 = ["０日目（初期値）",
        "１日目", "２日目", "３日目", "４日目", "５日目", "６日目", "７日目", "８日目", "９日目", "１０日目", 
          "１１日目", "１２日目", "１３日目", "１４日目", "１５日目", "１６日目", "１７日目", "１８日目", "１９日目", "２０日目", 
          "２１日目", "２２日目", "２３日目", "２４日目", "２５日目", "２６日目", "２７日目", "２８日目", "２９日目", "３０日目"]
columns1 =["入庫CBM", "出庫CBM", "在庫CBM"]
df = pd.DataFrame(data=list1, index=index1, columns=columns1)
st.table(df)

in_2_1 = sum(ins[:15])
in_2_2 = sum(ins[15:])
in_3_1 = sum(ins[:10])
in_3_2 = sum(ins[10:20])
in_3_3 = sum(ins[20:30])
in_4_1 = sum(ins[:7])
in_4_2 = sum(ins[7:14])
in_4_3 = sum(ins[14:21])
in_4_4 = sum(ins[21:28])

q_2_1 = st0 + in_2_1
q_2_2 = st15 + in_2_2
q_3_1 = st0 + in_3_1
q_3_2 = st10 + in_3_2
q_3_3 = st20 + in_3_3
q_4_1 = st0 + in_4_1
q_4_2 = st7 + in_4_2
q_4_3 = st14 + in_4_3
q_4_4 = st21 + in_4_4
q_30 = sts + ins

fee_30 = f'{int(sum(q_30) * charge_30 * 100 / 100):,}'
fee_2 = f'{int((q_2_1 + q_2_2) * charge_30 * 15 * (100 - rate_2) / 100):,}'
fee_3 = f'{int((q_3_1 + q_3_2 + q_3_3) * charge_30 * 10 * (100 - rate_3) / 100):,}'
fee_4 = f'{int((q_4_1 + q_4_2 + q_4_3 + q_4_4) * charge_30 * 7 * (100 - rate_4) / 100 /28 * 30):,}'

fee_30_int = int(sum(q_30) * charge_30 * 100 / 100)
fee_2_int = int((q_2_1 + q_2_2) * charge_30 * 15 * (100 - rate_2) / 100)
fee_3_int = int((q_3_1 + q_3_2 + q_3_3) * charge_30 * 10 * (100 - rate_3) / 100)
fee_4_int = int((q_4_1 + q_4_2 + q_4_3 + q_4_4) * charge_30 * 7 * (100 - rate_4) / 100 /28 * 30)

st.text('')
st.subheader('一ヶ月の保管料の比較')
list2 = [[fee_30, fee_2, fee_3, fee_4], [1, round(fee_2_int/fee_30_int,2), round(fee_3_int/fee_30_int,2), round(fee_4_int/fee_30_int,2)]]
index2 = ['一ヶ月の保管料（円）', '日単位制に対する比率']
columns2 = ['日単位制', '二期制', '三期制', '四期制']
df2 = pd.DataFrame(data=list2, index=index2, columns=columns2)
st.table(df2)

list3 = [[fee_30_int], [fee_2_int], [fee_3_int], [fee_4_int]]
index2 = ['一ヶ月の保管料（円）']
columns2 = ['1) 日単位制', '2) 二期制', '3) 三期制', '4) 四期制']
df3 = pd.DataFrame(data=list3, index=columns2, columns=index2)

st.text('')
st.bar_chart(df3)

