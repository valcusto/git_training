import pandas as pd
import streamlit as st

import src.answers as asw
from src.extraction import load_data

st.set_page_config(layout="wide")


def create_dataframe_section(df):
    st.title("Sections - Database Description")

    col_1, col_2 = st.columns(2)

    col_1.header("Database")
    col_1.dataframe(df, height=530)

    col_2.header("Data Description")

    data_description = """
                        | Column | Description |
                        | :----- | --------: |
                        | ID | Identification row/register |
                        | name | Manufacturer and Motorcycle Model |
                        | selling_price | Selling price |
                        | year | Year of Manufacture of the Motorcycle |
                        | seller_type | Type of Seller - Whether it is a private seller or a dealer |
                        | owner | Whether the motorcycle has had a first, second, third, or fourth owner |
                        | km_driven | Total kilometers traveled by the motorcycle |
                        | ex_showroom_price | Price of the motorcycle excluding insurance and registration fees |
                        | age | Number of years the motorcycle has been in use |
                        | km_class | Classification of motorcycles based on kilometers traveled |
                        | km_per_year | Kilometers traveled per year |
                        | km_per_month | Kilometers traveled per month |
                        | company | Motorcycle manufacturer |
    """

    col_2.markdown(data_description)


def create_answers_section(df):
    st.title("Main Questions Answers")

    st.header("First Round")
    st.subheader(
        "How many bikes are being sold by their owners and how many bikes are being sold by distributors?"
    )
    asw.rd1_question_9(df)

    st.subheader("How many bikes are being sold are bikes from a unique owner?")
    asw.rd1_question_13(df)

    st.subheader(
        "Are high kilometer bikes more expensive than bikes with lower kilometer?"
    )
    asw.rd1_question_14(df)

    st.subheader(
        "Are the bikes with a unique owner more expense on avarege than the other bikes?"
    )
    asw.rd2_question_1(df)

    st.subheader(
        "Are the bikes that have more owners also the bikes with more kilometers traveled on avarege?"
    )
    asw.rd2_question_2(df)

    st.subheader("Which company has the most bikes registered?")
    asw.rd2_question_7(df)

    st.subheader("Which company has the most expensive bikes on avarege?")
    asw.rd3_question_2(df)

    st.subheader(
        "Are the company that has the most expensive bikes registered also the company with the most bikes registered?"
    )
    asw.rd3_question_5(df)

    st.subheader("Which bikes are good for buying?")
    asw.rd3_question_7(df)


def create_main_layout():
    df = load_data()

    create_dataframe_section(df)

    create_answers_section(df)

if __name__ == "__main__":
    create_main_layout()
