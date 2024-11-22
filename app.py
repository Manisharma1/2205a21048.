import streamlit as st 
st.title("2205A21048-PS11")
st.title("efficiency of dc series motor")

def output(V, CL,IL, K, Rse, Ra):
    CUL=(K*IL**2)*(Rse+Ra)
    eff=((K*V*IL+CL+CUL)/(K*V*IL))*100
    return CUL,eff


col1,col2=st.columns(2)
with col1:
    V=st.number_input("V(volt)",value=10)
    IL=st.number_input("IL(amps)",value=10)
    Rse=st.number_input("Rse(ohms)",value=10)
    Ra=st.number_input("Ra(ohms)",value=10)
    K = st.number_input("k(watts)",value=10)
    CL=st.number_input("CL(watts)",value=10)
    compute=st.button("compute")

with col2:
    with st.container(border=True):
        if compute:
            eff,CUL=output(V, CL, IL, K, Rse, Ra)
            st.write(f"Effiiency:{eff:.2f} %")
            st.write(f"Copper losses:{CUL:.2f} W")

