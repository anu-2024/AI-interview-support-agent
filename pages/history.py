# history page placeholder
import streamlit as st
import sqlite3


DB_NAME = "interview_agent.db"


def show_history():

    st.title(
        "📜 Interview History"
    )

    try:

        conn = sqlite3.connect(
            DB_NAME
        )

        query = """
        SELECT
        id,
        final_score,
        percentage,
        created_at
        FROM scores
        """

        history = conn.execute(
            query
        ).fetchall()

        conn.close()

        if len(history) == 0:

            st.info(
                "No History Available"
            )

        else:

            st.dataframe(
                history
            )

    except Exception as e:

        st.error(
            str(e)
        )
