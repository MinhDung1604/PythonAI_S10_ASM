import streamlit as st

st.title('Trà sữa CoTAI')
col1, col2 = st.columns(2)
prize = 0
with col1:
    st.image('trasua.jpg')

with col2:
    size  = st.radio('Kích cỡ', ('Nhỏ (30k)', 'Vừa (40k)', 'Lớn (50k)'), horizontal = True)
    match size:
        case 'Nhỏ (30k)': size = 'Cỡ nhỏ'; prize += 30
        case 'Vừa (40k)': size  = 'Cỡ vừa'; prize += 40
        case 'Lớn (50k)': size = 'Cỡ lớn'; prize += 50
    
    st.text('Thêm')
    col2_1,col2_2 = st.columns(2)
    with col2_1:
        extra = []
        sua = st.checkbox('Sữa (5k)')
        if sua: prize += 5; extra.append('Sữa')
        kem = st.checkbox('Kem (10k)')
        if kem: prize += 10; extra.append('Kem')
        
    with col2_2:
        caphe = st.checkbox('Cà phê (8k)')
        if caphe: prize += 8; extra.append('Cà phê')
        trung = st.checkbox('Trứng (15k)')
        if trung: prize += 15; extra.append('Trứng')


col3,col4 = st.columns(2)
with col3:
        topping = st.multiselect('Topping', ('Trân châu trắng (5K)',
                                'Trân châu đen (5K)',
                                'Thạch rau câu (6K)',
                                'Vải (7K)',
                                'Nhãn (8K)',
                                'Đào (10K)'))
        if 'Trân châu trắng (5K)' in topping: prize += 5
        if 'Trân châu đen (5K)' in topping: prize += 5
        if 'Thạch rau câu (6K)' in topping: prize += 6
        if 'Vải (7K)' in topping: prize += 7
        if 'Nhãn (8K)' in topping: prize += 8
        if 'Đào (10K)' in topping: prize += 10
with col4:    
    amount = st.number_input('Số lượng', 0)

note = st.text_area('Ghi chú')

if st.button('Đặt hàng'):
    st.success(f'''
{size} \n
Thêm: {', '.join(extra)} \n
Topping: {', '.join(topping)} \n
Ghi chú: {note} \n
Số lượng: {amount} \n 
Thành tiền: {prize*amount}K \n
''')
    