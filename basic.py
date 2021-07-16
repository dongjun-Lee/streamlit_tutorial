import streamlit as st
import pandas as pd


def main():
    st.markdown("## Display Text")
    st.write("Hello World!")
    st.markdown("**Hello World!**")
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.code('for i in range(8): foo()')

    st.markdown("## Interactive Widgets")
    st.markdown("### Get input")
    text_input = st.text_input("Text input:")
    if text_input:
        st.write(text_input)

    text_area = st.text_area("Text area:", height=300)
    if text_area:
        st.write(text_area)

    number_input = st.number_input("Number input:")
    if number_input:
        st.write("{} ({})".format(number_input, type(number_input)))

    st.markdown("### File input")
    f = st.file_uploader('Text File', type=["txt"])
    if f:
        raw_text = str(f.read(), "utf-8")
        st.write(raw_text)

    f2 = st.file_uploader("CSV File", type=["csv"])
    if f2:
        df = pd.read_csv(f2)
        st.write(df)

    st.markdown("### Set options")
    is_checked = st.checkbox("Checkbox", value=False)
    st.markdown("```is_checked: {}```".format(is_checked))

    radio = st.radio('Radio', ["Option 1", "Option 2", "Option 3"])
    st.write("```radio: {}```".format(radio))

    multiselect = st.multiselect('Multiselect', [1, 2, 3])
    st.write("```multiselect: {}```".format(multiselect))

    st.markdown("## Sidebar")
    slider = st.sidebar.slider("num_outputs", 3, 10, 5, 1)
    selectbox = st.sidebar.selectbox("from", [2010, 2018, 2019, 2020], index=0)
    st.write("```slider: {}```".format(slider))
    st.write("```selectbox: {}```".format(selectbox))
