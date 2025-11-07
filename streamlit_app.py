import random
import streamlit as st


def generate_questions(n=3, min_val=0, max_val=20):
    questions = []
    for _ in range(n):
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        op = random.choice(["+", "-"])
        # ensure non-negative result for subtraction
        if op == "-" and a < b:
            a, b = b, a
        answer = a + b if op == "+" else a - b
        questions.append({"a": a, "b": b, "op": op, "answer": answer})
    return questions


def reset_game():
    st.session_state.q_index = 0
    st.session_state.correct = 0
    st.session_state.questions = generate_questions(3)
    st.session_state.user_answer = 0


if "questions" not in st.session_state:
    reset_game()

st.title("간단한 덧셈·뺄셈 연습 앱")
st.write("3문제를 연속으로 풀고, 마지막에 몇 문제를 맞혔는지 알려줍니다.")

q_index = st.session_state.q_index
questions = st.session_state.questions

if q_index < len(questions):
    q = questions[q_index]
    st.markdown(f"### 문제 {q_index + 1} / {len(questions)}")
    st.markdown(f"**{q['a']} {q['op']} {q['b']} = ?**")

    # 숫자 입력 (정수)
    user_answer = st.number_input(
        "답을 입력하세요:", min_value=-1000, max_value=1000, step=1, value=st.session_state.get("user_answer", 0), key="user_answer_input"
    )

    if st.button("제출"):
        try:
            user_int = int(user_answer)
        except Exception:
            st.warning("정수를 입력해 주세요.")
        else:
            correct = q["answer"]
            if user_int == correct:
                st.success("정답입니다!")
                st.session_state.correct += 1
            else:
                st.error(f"틀렸습니다. 정답은 {correct} 입니다.")

            st.session_state.q_index += 1
            # reset temporary input storage
            st.session_state.user_answer = 0
            # 재렌더링을 위해 명시적으로 rerun 유도 (Streamlit가 자동으로 재실행함)
            st.experimental_rerun()
else:
    st.markdown("## 결과")
    st.write(f"총 {len(questions)}문제 중 {st.session_state.correct}문제 맞혔습니다.")
    if st.button("다시 하기"):
        reset_game()
        st.experimental_rerun()

