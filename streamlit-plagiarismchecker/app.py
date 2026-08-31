"""A simple text-similarity / plagiarism checker built with Streamlit.

Concepts this app demonstrates (useful as a teaching checklist):
  1. Comparing two texts with the standard-library `difflib` module --
     no machine-learning model or external API needed.
  2. Two different similarity ideas: character-sequence similarity
     (SequenceMatcher) vs. word-overlap similarity (a hand-written
     Jaccard-index function) -- and why they can disagree.
  3. Turning `difflib`'s matching blocks into a highlighted diff view.
  4. Basic widgets: two side-by-side text_area boxes, columns, a slider
     for the "flag as similar" threshold.

Run it with:  streamlit run app.py

IMPORTANT, for the guide and for anyone extending this app: this is a
teaching tool, not a real plagiarism-detection system. It only catches
near-identical wording. It cannot detect paraphrasing, translation, or
plagiarism of ideas without matching words -- see the mentoring guide for
why, and what a real system would need on top of this.
"""
import re
from difflib import SequenceMatcher

import streamlit as st

st.set_page_config(page_title="Plagiarism Checker", page_icon="🔍")
st.title("🔍 Plagiarism Checker")
st.caption("Compares two texts for overlap -- a teaching tool, not a research-grade detector "
           "(see the mentoring guide for why).")


def word_set(text):
    """Lowercase, alphanumeric 'words' only -- crude but good enough to
    teach the idea of comparing texts as sets of tokens."""
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def jaccard_similarity(text_a, text_b):
    """|intersection| / |union| of the two texts' word sets. 0.0 if both
    are empty (nothing to compare)."""
    words_a, words_b = word_set(text_a), word_set(text_b)
    if not words_a and not words_b:
        return 0.0
    return len(words_a & words_b) / len(words_a | words_b)


def sequence_similarity(text_a, text_b):
    """difflib's ratio: 2 * matching characters / total characters, using
    the longest-common-subsequence-style algorithm SequenceMatcher
    implements. Sensitive to word order, unlike Jaccard above."""
    return SequenceMatcher(None, text_a, text_b).ratio()


col1, col2 = st.columns(2)
with col1:
    text_a = st.text_area("Text A", height=220, placeholder="Paste the first text here...")
with col2:
    text_b = st.text_area("Text B", height=220, placeholder="Paste the second text here...")

threshold = st.slider("Flag as similar above", min_value=0, max_value=100, value=60, format="%d%%")

if text_a.strip() and text_b.strip():
    jaccard = jaccard_similarity(text_a, text_b)
    sequence = sequence_similarity(text_a, text_b)
    overall = (jaccard + sequence) / 2

    st.divider()
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Word overlap (Jaccard)", f"{jaccard * 100:.1f}%")
    col_m2.metric("Sequence similarity", f"{sequence * 100:.1f}%")
    col_m3.metric("Overall", f"{overall * 100:.1f}%")

    if overall * 100 >= threshold:
        st.error(f"⚠️ Flagged: {overall * 100:.1f}% similarity is at or above the {threshold}% threshold.")
    else:
        st.success(f"✅ Not flagged: {overall * 100:.1f}% similarity is below the {threshold}% threshold.")

    # ---- highlighted diff: which parts of Text A also appear in Text B ----
    st.divider()
    st.subheader("Matching passages in Text A")
    matcher = SequenceMatcher(None, text_a, text_b)
    matches = matcher.get_matching_blocks()

    highlighted = []
    pos = 0
    for match in matches:
        if match.size == 0:
            continue
        if match.a > pos:
            highlighted.append(text_a[pos:match.a])
        segment = text_a[match.a:match.a + match.size]
        if match.size >= 15:  # ignore tiny/incidental matches (single words, punctuation)
            highlighted.append(f"**:red[{segment}]**")
        else:
            highlighted.append(segment)
        pos = match.a + match.size
    if pos < len(text_a):
        highlighted.append(text_a[pos:])

    st.markdown("".join(highlighted) or "_(nothing to show)_")
    st.caption("Text highlighted in red also appears, verbatim, in Text B (matches of 15+ characters).")
else:
    st.info("Paste text into both boxes above to compare them.")
