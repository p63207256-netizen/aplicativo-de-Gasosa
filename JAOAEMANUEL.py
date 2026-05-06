import streamlit as st
st.title("Caculadora De Combustivel")
st.subheader("Escolha Entre Gasolina Ou Etanol")
gasosa = st.number_input("Digite O Valor Da Gasolina",min_value=0.0)
etanol = st.number_input("Digite O Valor Da Etanol",min_value=0.0)

if gasosa >0:

    resultdo = etanol/gasosa
    if resultdo <0.7:
        mgs = "abastaça com Etanol"
    else:
        mgs = "abastaça com Gasosa"
else:
    st.warning("Os valores não podem ser 0") 


if st.button("calcular"):
    st.info(mgs)
    st.balloons
