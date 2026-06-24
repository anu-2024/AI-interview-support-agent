# dashboard page placeholder
import streamlit as st
import pandas as pd
import plotly.express as px

from database.db import db


def show_dashboard():

    st.title(
        "📊 Performance Dashboard"
    )

    stats = (
        db.get_dashboard_stats()
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Interviews",
        stats[
            "total_interviews"
        ]
    )

    col2.metric(
        "Average Score",
        stats[
            "average_score"
        ]
    )

    col3.metric(
        "Highest Score",
        stats[
            "highest_score"
        ]
    )

    scores = db.get_scores()

    score_values = []

    for row in scores:

        try:
            score_values.append(
                row[0]
            )
        except:
            pass

    if len(score_values) > 0:

        df = pd.DataFrame(
            {
                "Attempt":
                list(
                    range(
                        1,
                        len(
                            score_values
                        ) + 1
                    )
                ),

                "Score":
                score_values
            }
        )

        fig = px.line(
            df,
            x="Attempt",
            y="Score",
            title="Score Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "No interview data available"
        )
