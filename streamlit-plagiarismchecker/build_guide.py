"""Generates Plagiarism_Checker_Mentoring_Guide.pdf from this file's
content using reportlab. Not part of the app itself -- run once to
(re)build the guide after editing the text below.

Run it with:  python3 build_guide.py
"""
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, Preformatted
)

OUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Plagiarism_Checker_Mentoring_Guide.pdf")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="H1", fontSize=20, leading=24, spaceAfter=14, textColor=colors.HexColor("#1a1a2e")))
styles.add(ParagraphStyle(name="H2", fontSize=14, leading=18, spaceBefore=16, spaceAfter=8, textColor=colors.HexColor("#16213e")))
styles.add(ParagraphStyle(name="Body", fontSize=10.5, leading=15, spaceAfter=8))
styles.add(ParagraphStyle(name="CodeBlock", fontName="Courier", fontSize=8.5, leading=11, backColor=colors.HexColor("#f4f4f8"),
                           borderPadding=6, spaceAfter=10))

story = []


def h1(text):
    story.append(Paragraph(text, styles["H1"]))


def h2(text):
    story.append(Paragraph(text, styles["H2"]))


def body(text):
    story.append(Paragraph(text, styles["Body"]))


def code(text):
    story.append(Preformatted(text, styles["CodeBlock"]))


def bullets(items):
    story.append(ListFlowable(
        [ListItem(Paragraph(i, styles["Body"])) for i in items],
        bulletType="bullet", start="•", leftIndent=16,
    ))


# ---------------------------------------------------------------- title ----
h1("Plagiarism Checker -- Mentoring Guide")
body("A Streamlit app that compares two texts and reports how similar "
     "they are, using only the Python standard library. This guide "
     "explains the two similarity measures it uses, why they can "
     "disagree, how the highlighted diff view is built, and -- "
     "importantly -- what this app can't actually detect.")

# ------------------------------------------------- 1. what this is NOT
h2("1. Read this before anything else")
body("<b>This is not a real plagiarism detector.</b> It only measures "
     "surface-level text overlap: shared words and shared character "
     "sequences. It will correctly flag copy-pasted or lightly-edited "
     "text. It will <b>not</b> catch:")
bullets([
    "<b>Paraphrasing</b> -- rewording the same ideas in different words "
    "shares almost no character sequences or exact words, so both "
    "measures below score it as dissimilar.",
    "<b>Translation</b> -- the same content in a different language shares "
    "essentially zero surface overlap.",
    "<b>Idea plagiarism without matching wording</b> -- copying an "
    "argument, structure, or dataset while writing entirely original "
    "sentences.",
])
body("A production-grade system needs semantic comparison -- typically "
     "sentence embeddings (turning text into vectors that capture "
     "<i>meaning</i>, not just characters) plus a large reference corpus to "
     "compare against. That's a materially bigger project; see the "
     "exercises for a pointer on how you'd start extending this one in "
     "that direction. What this app <i>is</i> good for: a clear, honest "
     "example of how far you can get with nothing but "
     "<font face='Courier'>difflib</font> -- and where that approach "
     "runs out.")

# ------------------------------------------------- 2. two measures
h2("2. Two different notions of \"similar\"")
body("The app computes two independent scores and averages them, because "
     "each one catches something the other misses.")
h2("2a. Word overlap: a hand-written Jaccard index")
code(
"""def word_set(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def jaccard_similarity(text_a, text_b):
    words_a, words_b = word_set(text_a), word_set(text_b)
    return len(words_a & words_b) / len(words_a | words_b)"""
)
body("Each text becomes a <i>set</i> of lowercase words (word order and "
     "repetition both thrown away). The Jaccard index is "
     "|shared words| / |all words in either text| -- a classic, simple "
     "way to compare two sets. Because order doesn't matter here, two "
     "texts that say the same things in a different order can still score "
     "highly.")
h2("2b. Sequence similarity: difflib.SequenceMatcher")
code(
"""def sequence_similarity(text_a, text_b):
    return SequenceMatcher(None, text_a, text_b).ratio()"""
)
body("<font face='Courier'>SequenceMatcher</font> (standard library, no "
     "install needed) finds the longest matching runs of "
     "<i>characters</i> between the two texts, recursively, and reports "
     "a ratio based on how much of both texts is covered by matches. "
     "Unlike Jaccard, this <i>is</i> sensitive to order -- rearranging the "
     "same sentences into a different sequence lowers this score even "
     "though every word is still shared.")
body("Averaging the two gives a single number that's reasonably hard to "
     "game with just one trick (shuffling word order, or scrambling "
     "individual characters) -- though, again, neither is remotely hard "
     "to fool with real paraphrasing.")

# ------------------------------------------------- 3. diff highlighting
h2("3. Highlighting the matching passages")
body("<font face='Courier'>SequenceMatcher.get_matching_blocks()</font> "
     "returns the actual matching runs as "
     "<font face='Courier'>(start_in_a, start_in_b, length)</font> "
     "triples. The app walks Text A once, alternating between "
     "un-highlighted gaps and matched segments, and wraps each matched "
     "segment 15 characters or longer in Streamlit's "
     "<font face='Courier'>:red[...]</font> markdown-colouring syntax:")
code(
"""for match in matcher.get_matching_blocks():
    if match.size == 0:
        continue
    ...
    segment = text_a[match.a:match.a + match.size]
    if match.size >= 15:
        highlighted.append(f"**:red[{segment}]**")"""
)
body("The 15-character minimum matters: without it, single shared words "
     "like \"the\" or \"is\" would get highlighted individually, burying "
     "the genuinely meaningful matches (whole shared phrases or "
     "sentences) in noise.")
body("A known rough edge, worth knowing about rather than hiding: if the "
     "pasted text itself contains markdown-special characters "
     "(<font face='Courier'>*</font>, <font face='Courier'>_</font>, "
     "<font face='Courier'>#</font>), <font face='Courier'>st.markdown</font> "
     "will interpret them as formatting rather than literal text, since "
     "the highlighting itself relies on real markdown syntax being "
     "injected around the matched segments. Fine for a teaching demo; a "
     "hardened version would need to escape the user's text first and use "
     "a different highlighting mechanism (e.g. raw HTML with "
     "<font face='Courier'>&lt;mark&gt;</font> tags via "
     "<font face='Courier'>st.iframe</font> instead of markdown).")

# ------------------------------------------------- 4. exercises
h2("4. Exercises")
bullets([
    "<b>Ignore case and punctuation properly.</b> Try comparing "
    "\"Hello, World!\" against \"hello world\" -- the sequence-similarity "
    "score is dragged down by the punctuation/casing difference even "
    "though a human would call these identical. Normalize both texts "
    "(lowercase, strip punctuation) before running "
    "<font face='Courier'>SequenceMatcher</font>, and see how the score "
    "changes.",
    "<b>Sentence-level comparison.</b> Instead of comparing whole blocks "
    "of text at once, split both texts into sentences (the stdlib "
    "<font face='Courier'>re</font> module, splitting on "
    "<font face='Courier'>. ! ?</font>) and report a "
    "per-sentence-in-A similarity against the best-matching sentence in "
    "B -- much more useful for finding exactly which sentences were "
    "copied.",
    "<b>Multiple documents.</b> Add "
    "<font face='Courier'>st.file_uploader(accept_multiple_files=True)</font> "
    "and compare one document against many at once, showing a ranked "
    "table of which one it's most similar to.",
    "<b>N-gram overlap.</b> Instead of single-word Jaccard, build the word "
    "sets out of overlapping 3-word phrases (\"n-grams\") instead of "
    "single words -- a stronger signal for detecting copied phrasing "
    "specifically, rather than just shared vocabulary.",
    "<b>Semantic similarity (the real next step).</b> Look up "
    "\"sentence embeddings\" and a library like "
    "<font face='Courier'>sentence-transformers</font> -- turning each "
    "text into a vector and comparing vectors with cosine similarity is "
    "the actual technique that lets a checker catch paraphrasing, at the "
    "cost of a much heavier dependency and needing a pretrained model.",
])

story.append(Spacer(1, 0.6 * cm))
body("<i>Written as a teaching companion to app.py -- read this guide with "
     "the code open side by side.</i>")

doc = SimpleDocTemplate(
    OUT_FILE, pagesize=A4,
    leftMargin=2.2 * cm, rightMargin=2.2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
    title="Plagiarism Checker -- Mentoring Guide",
)
doc.build(story)
print("Wrote", OUT_FILE)
