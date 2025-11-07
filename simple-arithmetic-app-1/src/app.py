import streamlit as st
from game import generate_question, check_answer, play_game

def main():
    st.title("간단한 덧셈과 뺄셈 연습")
    st.write("3문제를 풀고 맞춘 문제 수를 확인하세요!")

    score = 0
    total_questions = 3

    for _ in range(total_questions):
        question, answer = generate_question()
        user_answer = st.number_input(question, min_value=-100, max_value=100, step=1)

        if st.button("제출"):
            if check_answer(user_answer, answer):
                st.success("정답입니다!")
                score += 1
            else:
                st.error(f"틀렸습니다. 정답은 {answer}입니다.")

    st.write(f"총 {total_questions}문제 중 {score}문제를 맞췄습니다.")

if __name__ == "__main__":
    main()