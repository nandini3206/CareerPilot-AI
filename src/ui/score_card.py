import streamlit as st
import plotly.graph_objects as go


def show_score_card(score):

    score = float(score)

    fig = go.Figure()

    fig.add_trace(

        go.Pie(

            values=[score,100-score],

            hole=.82,

            sort=False,

            direction="clockwise",

            marker=dict(

                colors=[

                    "#8B5CF6",

                    "#27272A"

                ]

            ),

            textinfo="none"

        )

    )

    fig.update_layout(

        margin=dict(

            l=0,

            r=0,

            t=0,

            b=0

        ),

        height=320,

        showlegend=False,

        paper_bgcolor="rgba(0,0,0,0)",

        annotations=[

            dict(

                text=f"""

                <span style='font-size:15px'>

                Overall Match Score

                </span>

                <br><br>

                <span style='font-size:54px;font-weight:bold;'>

                {int(score)}%

                </span>

                <br>

                <span style='color:#22C55E;font-size:18px;'>

                Good Match

                </span>

                """,

                showarrow=False,

                x=.5,

                y=.5

            )

        ]

    )

    st.markdown(
        "<div class='score-wrapper'>",
        unsafe_allow_html=True
    )

    st.plotly_chart(
        fig,
        config={
            "displayModeBar":False
        },
        use_container_width=True
    )

    st.button(

        "View Full Analysis",

        use_container_width=True

    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )