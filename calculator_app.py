import streamlit as st
st.title(""Retail Business Dashboard"")
st.header(""Manager Input Section"")
st.write(""Please enter the monthly sales target and select the region."")


monthly_sales = st.number_input(""Enter Monthly Sales Target (in USD):"",
                      min_value=0,
                      max_value=50000,
                      value=50000)


region = st.selectbox(""Select Region:"",
                      [""North"", ""South"", ""East"", ""West""])

if st.button(""Submit""):
    st.write(f""Monthly sales target is {monthly_sales} and current region is {region}."")
    st.success(""Dashboard completed successfully!"")
