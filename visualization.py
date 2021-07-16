import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    st.markdown("## Display Dataframe")
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.dataframe(df)
    st.table(df[:10])

    st.markdown("## Line Chart")
    st.line_chart(df)

    st.markdown("## Bar Chart")
    st.bar_chart(df)

    st.markdown("## Scatter Plot")
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(df["a"], df["b"])
    ax.set_xlabel("a")
    ax.set_ylabel("b")
    st.pyplot(fig)
