# sử dụng streamlit
import streamlit as st


def main():
    st.title("Word correction using Levenshtein Distance")
    word = st.text_input("Word:")
    st.button("Correct"):  # type: ignore
        distances = dict()
        for vocab in vocabs:
            distances[vocab] = distance(word, vocab)

        sorted
