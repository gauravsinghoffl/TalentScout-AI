import streamlit as st
from utils.resume_processing import generate_motivation_message
from config.settings import CONFIDENCE_THRESHOLDS


def create_assessment_guidelines():
    """Create consistent assessment guidelines for sidebar"""
    guidelines = {
        "steps": [
            "📋 Initial Information Collection",
            "📎 Resume Analysis & Verification",
            "🔍 Technical Skills Assessment",
            "📈 Final Report Generation"
        ],
        "rules": [
            "Answer each question thoroughly and precisely",
            "Take time to structure your responses clearly",
            "Focus on practical experience and examples",
            "Be honest about knowledge limitations",
            "Maintain professional communication"
        ]
    }
    return guidelines


def render_sidebar(stage, resume_analysis=None):
    """Render consistent sidebar content across all stages"""

    with st.sidebar:

        st.title("🧠 TalentScout")
        st.header('Assessment Guide 📚')

        # Map sidebar stages to index in the steps list
        stage_to_index = {
            "info": 0,
            "resume": 1,
            "interview": 2,
            "report": 3  # adjust if you want "Performance Evaluation" as 3
        }
        current_index = stage_to_index.get(stage, -1)

        # Display current stage
        stages = {
            'info': '📋 Information Collection',
            'resume': '📎 Resume Analysis',
            'interview': '🔍 Technical Assessment',
            'report': '📈 Final Report'
        }
        current_stage = stages.get(stage, '')
        st.subheader(f"Current Stage: {current_stage}")

        guidelines = create_assessment_guidelines()

        # -----------------------------
        # Assessment Steps with block highlight
        # -----------------------------
        with st.expander("📝 Assessment Steps", expanded=True):
            for idx, step in enumerate(guidelines['steps']):
                if idx == current_index:
                    # Highlight current step as a block
                    st.markdown(
                        f'<div style="padding:8px; margin-bottom:5px; background-color:#d9edf7; border-radius:5px; font-weight:bold;">→ {idx+1}. {step}</div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(f"{idx+1}. {step}")

        # -----------------------------
        # Assessment Rules
        # -----------------------------
        with st.expander("📋 Assessment Rules", expanded=True):
            for rule in guidelines['rules']:
                st.markdown(f"• {rule}")

        # -----------------------------
        # Optional: Resume Motivation
        # -----------------------------
        if resume_analysis and 'consistency_score' in resume_analysis:
            st.markdown("---")
            st.subheader("💫 Your Assessment Journey")
            motivation = generate_motivation_message(resume_analysis)
            st.markdown(f"*{motivation}*")

        st.markdown("---")

        # -----------------------------
        # Reset Button
        # -----------------------------
        if st.button('Reset Assessment 🔄'):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
