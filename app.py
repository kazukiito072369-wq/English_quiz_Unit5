import streamlit as st
import random

questions = [
    {
        "question": "In this way, we can develop a fair and ( ) system of production.",
        "answer": "sustainable"
    },
    {
        "question": "Look at this picture ( ) I found on the internet.",
        "answer": "which"
    },
    {
        "question": "We can start to ( ) the world by making smart choices.",
        "answer": "change"
    },
    {
        "question": "Today, I would like to make a ( ) about T-shirts for the contest.",
        "answer": "suggestion"
    },
    {
        "question": "Fair trade is one of the ways to ( ) that problem.",
        "answer": "solve"
    },
    {
        "question": "If we choose fair trade products, farmers can ( ) enough money to live.",
        "answer": "earn"
    },
    {
        "question": "T-shirts are made of cotton, and they’re mainly ( ) in developing countries.",
        "answer": "produced"
    },
    {
        "question": "I will ( ) the reason.",
        "answer": "explain"
    },

    {
        "question": "What ( ) you interested in fair trade?",
        "answer": "made"
    },
    {
        "question": "What do you want to do in the ( )?",
        "answer": "future"
    },
    {
        "question": "One ( ), I want to work with her.",
        "answer": "day"
    },
    {
        "question": "My aunt ( ) a fair trade shop in New York.",
        "answer": "runs"
    },
    {
        "question": "I want to ( ) playing basketball and become a professional basketball player.",
        "answer": "keep"
    },
    {
        "question": "I’m sure your dream will ( ) true.",
        "answer": "come"
    },
    {
        "question": "She says her job is challenging but ( ).",
        "answer": "rewarding"
    },
    {
        "question": "Yes, I was ( ), too.",
        "answer": "impressed"
    },
    {
        "question": "The presentation ( ) you gave was great!",
        "answer": "that"
    },

    {
        "question": "That might ( ) to my future career.",
        "answer": "lead"
    },
    {
        "question": "I’m not ( ) about my future, but I have some ideas.",
        "answer": "sure"
    },
    {
        "question": "Being a puppy walker was another great experience I ( ).",
        "answer": "had"
    },
    {
        "question": "In the ( ) three years, I’ve had a lot of memorable experiences.",
        "answer": "past"
    },
    {
        "question": "I learned about life from the ( ) of a person in a wheelchair.",
        "answer": "viewpoint"
    },
    {
        "question": "If I keep doing that, I’ll ( ) across something that will interest me.",
        "answer": "come"
    },
    {
        "question": "Now I feel that I ( ) to be open to new experiences and ideas.",
        "answer": "want"
    },
    {
        "question": "In ( ), meeting and getting to know David was an eye-opener for me.",
        "answer": "particular"
    },

    {
        "question": "There are many girls ( ) marry under the age of 18 in those countries.",
        "answer": "who"
    },
    {
        "question": "I think all girls should be ( ) to go to school.",
        "answer": "able"
    },
    {
        "question": "For that, we have to solve the problems of poverty and child ( ).",
        "answer": "marriage"
    },
    {
        "question": "( ) don’t many girls go to school?",
        "answer": "why"
    },
    {
        "question": "First, it’s ( ) of poverty.",
        "answer": "because"
    },
    {
        "question": "( ) of going to school, many girls have to do housework or help with work.",
        "answer": "instead"
    },
    {
        "question": "We can’t do that quickly, but I’d like to do the things ( ) I can do.",
        "answer": "that"
    },
    {
        "question": "You’ll ( ) the percentage is very large in Sub-Saharan African countries.",
        "answer": "find"
    }
]


all_answers = list(set(q["answer"] for q in questions))


st.title("3年生 Unit 5 まとめ")


if "question_list" not in st.session_state:

    st.session_state.question_list = random.sample(
        questions,
        min(10, len(questions))
    )

    st.session_state.number = 0
    st.session_state.results = []
    st.session_state.finished = False
    st.session_state.show_results = False
    st.session_state.choices = {}


if st.session_state.finished:

    st.success("10問終了！")

    score = 0

    for result in st.session_state.results:

        if result["answer"] == result["correct"]:
            score += 1

    st.write(
        "あなたの得点は",
        score,
        "/",
        len(st.session_state.results)
    )


    if st.button("今回の結果を見る"):

        st.session_state.show_results = True
        st.rerun()


    if st.session_state.show_results:

        st.write("### 今回の問題と結果")

        for i, result in enumerate(st.session_state.results):

            st.write("第", i + 1, "問")
            st.write("問題:", result["question"])
            st.write("あなたの答え:", result["answer"])
            st.write("正解:", result["correct"])

            if result["answer"] == result["correct"]:

                st.success("○ 正解")

            else:

                st.error("× 不正解")


    if st.button("もう一度挑戦"):

        st.session_state.question_list = random.sample(
            questions,
            min(10, len(questions))
        )

        st.session_state.number = 0
        st.session_state.results = []
        st.session_state.finished = False
        st.session_state.show_results = False
        st.session_state.choices = {}

        st.rerun()


else:

    question_data = st.session_state.question_list[
        st.session_state.number
    ]

    question = question_data["question"]
    correct = question_data["answer"]


    st.write(
        "第",
        st.session_state.number + 1,
        "問"
    )

    st.write(question)


    if st.session_state.number not in st.session_state.choices:

        choices = [correct]

        while len(choices) < 4:

            choice = random.choice(all_answers)

            if choice not in choices:
                choices.append(choice)

        random.shuffle(choices)

        st.session_state.choices[
            st.session_state.number
        ] = choices


    choices = st.session_state.choices[
        st.session_state.number
    ]


    answer = st.radio(
        "正しい答えを選んでください",
        choices,
        key="choice_" + str(st.session_state.number)
    )


    if st.button("回答"):

        if answer == correct:

            st.success("正解！")

        else:

            st.error(
                "不正解。正解は " + correct
            )


        st.session_state.results.append({
            "question": question,
            "answer": answer,
            "correct": correct
        })


        if st.session_state.number < 9:

            st.session_state.number += 1
            st.rerun()

        else:

            st.session_state.finished = True
            st.rerun()