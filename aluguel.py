import streamlit as st
#----------------------------------------------------------sidebar
st.sidebar.image('movida_logo.png')
st.sidebar.title('movida-aluguel de carros')
st.sidebar.write('seja bem vindo(a)')

carros =[ 'BMW','MUSTANG','HB20','FUSCA','civic']
carro = st.sidebar.selectbox('selecione um carro',carros)
if carro=='BMW':
    valor_do_dia=200
elif carro=='MUSTANG':
    valor_do_dia=500
elif carro=='HB20':
    valor_do_dia=150
elif carro== 'FUSCA':
    valor_do_dia=300
elif carro=='civic':
    valor_do_dia=200
else:
    valor_do_dia=60
#---------------------------------------------------------principal
st.title('movido aluguel de carros')
st.write('seja bem vindo(a)')
st.image(f'{carro}.png')

dias=st.text_input('informe a quantidade de dias')
km=st.text_input('informe a  quantidade de kilometros percorridos')
if st.button('calcular'):
    dias=int(dias)
    km=float(km)

    valor_dias=dias*valor_do_dia
    valor_km=km*0.15
    total=valor_dias+valor_km

    st.warning(f'você rodou{km}km por{dias} dias. o valor total a pagar será{total}.')
    
