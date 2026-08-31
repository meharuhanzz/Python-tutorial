"""Generates PDF_Generator_Mentoring_Guide.pdf from this file's content
using reportlab -- the same library the app itself uses to build the
user's PDF. Not part of the app itself -- run once to (re)build the guide
after editing the text below.

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

OUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "PDF_Generator_Mentoring_Guide.pdf")

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
h1("PDF Generator -- Mentoring Guide")
body("A Streamlit app that builds a real PDF file from user-entered content "
     "blocks, entirely in memory, and offers it back as a download. This "
     "guide walks through the moving pieces, then a real bug this project's "
     "own build surfaced, then closes with exercises.")

# --------------------------------------------------------------- 1. why
h2("1. Two different PDF-building jobs in one project")
body("This app actually uses reportlab <i>twice</i>, for two unrelated "
     "purposes: <font face='Courier'>app.py</font> builds whatever PDF the "
     "<i>user</i> designs through the UI, and this very script, "
     "<font face='Courier'>build_guide.py</font>, builds the mentoring "
     "guide PDF you're reading right now. Same library, same underlying "
     "API (<font face='Courier'>SimpleDocTemplate</font> + a list of "
     "\"flowable\" elements like <font face='Courier'>Paragraph</font> and "
     "<font face='Courier'>ListFlowable</font>) -- worth noticing since it "
     "means reading this guide's own source is a second, real example of "
     "everything Section 3 explains.")

# --------------------------------------------------------- 2. in-memory
h2("2. Building a PDF in memory: io.BytesIO")
body("reportlab's <font face='Courier'>SimpleDocTemplate</font> normally "
     "writes to a file path on disk. This app never touches disk at all -- "
     "it hands <font face='Courier'>SimpleDocTemplate</font> an "
     "<font face='Courier'>io.BytesIO()</font> object instead, which "
     "behaves like a file (it has <font face='Courier'>.write()</font>) but "
     "just holds bytes in memory:")
code(
"""buffer = io.BytesIO()
doc = SimpleDocTemplate(buffer, pagesize=A4, title=title)
doc.build(story)
return buffer.getvalue()   # the raw PDF bytes"""
)
body("This matters on a server: temp files need cleanup, can collide "
     "between concurrent users, and are slower than memory. "
     "<font face='Courier'>io.BytesIO</font> sidesteps all of that -- the "
     "PDF exists only as bytes in a Python variable, for exactly as long as "
     "this function call needs it.")

# --------------------------------------------------------- 3. flowables
h2("3. reportlab's model: a list of flowables")
body("reportlab doesn't think in terms of x/y coordinates for a document "
     "like this. You build a Python list -- called the <i>story</i> -- of "
     "\"flowable\" objects (<font face='Courier'>Paragraph</font>, "
     "<font face='Courier'>Spacer</font>, <font face='Courier'>ListFlowable</font>), "
     "and <font face='Courier'>doc.build(story)</font> lays them out "
     "top to bottom, wrapping text and adding page breaks automatically.")
code(
"""story = [Paragraph(title, styles["Title"])]
for block in blocks:
    if block["type"] == "Heading":
        story.append(Paragraph(block["text"], styles["Heading2"]))
    elif block["type"] == "Bullet list":
        items = [line.strip() for line in block["text"].splitlines() if line.strip()]
        story.append(ListFlowable([ListItem(Paragraph(i, styles["Normal"])) for i in items]))
    else:
        story.append(Paragraph(block["text"], styles["Normal"]))"""
)
body("<font face='Courier'>getSampleStyleSheet()</font> is a ready-made set "
     "of named paragraph styles (<font face='Courier'>\"Title\"</font>, "
     "<font face='Courier'>\"Heading2\"</font>, "
     "<font face='Courier'>\"Normal\"</font>) -- reused as-is here rather "
     "than hand-building fonts and sizes.")

# --------------------------------------------------- 4. download_button
h2("4. Serving the bytes: st.download_button")
body("<font face='Courier'>st.download_button</font> takes the finished "
     "bytes directly and hands them to the browser as a file download -- no "
     "separate route or static file needed, unlike a typical web "
     "framework:")
code(
"""st.download_button(
    "⬇️ Download PDF",
    data=pdf_bytes,
    file_name=f"{doc_title}.pdf",
    mime="application/pdf",
)"""
)
body("Notice the PDF is rebuilt from <font face='Courier'>st.session_state.blocks</font> "
     "on <i>every</i> rerun, not just when a \"Generate\" button is clicked -- "
     "cheap enough for a document this size, and it means the download "
     "button always offers the current state of the document, with no "
     "extra \"did you forget to regenerate\" step for the user to trip on.")

# ------------------------------------------------------------- 5. bug
h2("5. A real bug this project's own build found: widget identity inside a form")
body("The block-type selector offers three kinds of content "
     "(<font face='Courier'>Paragraph</font>, "
     "<font face='Courier'>Bullet list</font>, "
     "<font face='Courier'>Heading</font>), and the first version of this "
     "app tried to change the text box's label depending on which one was "
     "picked -- \"One item per line\" for a bullet list, something more "
     "generic otherwise:")
code(
"""# THE BUGGY VERSION -- do not copy this
with st.form("add_block_form", clear_on_submit=True):
    block_type = st.selectbox("Block type", BLOCK_TYPES)
    if block_type == "Bullet list":
        text = st.text_area("One item per line")
    else:
        text = st.text_area("Text")"""
)
body("This looks reasonable, and would work fine <i>outside</i> a form. "
     "Inside <font face='Courier'>st.form(...)</font>, though, widgets "
     "deliberately don't trigger a rerun when a sibling field changes -- "
     "that's the whole point of a form, batching input until submit. So in "
     "the browser, picking \"Bullet list\" from the selectbox never "
     "actually reruns the script, which means the text box the user is "
     "typing into is still the one from whichever branch rendered on the "
     "<i>previous</i> run.")
body("The real damage happens at submit time: the script finally reruns, "
     "now sees <font face='Courier'>block_type == \"Bullet list\"</font>, "
     "and executes <font face='Courier'>st.text_area(\"One item per "
     "line\")</font> for the first time this run. Because neither call had "
     "an explicit <font face='Courier'>key=</font>, Streamlit auto-derives "
     "one partly from the label -- and a <i>different label</i> means a "
     "<i>different widget identity</i> as far as Streamlit is concerned. "
     "The text the user had already typed, stored under the old label's "
     "auto-key, doesn't transfer. It's silently discarded, and "
     "<font face='Courier'>text</font> comes back empty.")
body("This was caught automatically: an automated test that filled in the "
     "form and submitted a bullet-list block got back an empty "
     "<font face='Courier'>st.session_state.blocks</font> where it expected "
     "one new entry -- exactly the silent-data-loss signature this class of "
     "bug produces, with no exception or error message anywhere.")
body("The fix in the shipped <font face='Courier'>app.py</font>: one "
     "single, statically-labelled <font face='Courier'>st.text_area</font>, "
     "given an explicit fixed <font face='Courier'>key=\"block_text\"</font>, "
     "so its identity never depends on anything that can change mid-form:")
code(
"""text = st.text_area(
    "Text",
    placeholder="A paragraph or heading's text, or one bullet item per line for a bullet list",
    key="block_text",
)"""
)
body("The general lesson, useful well beyond this app: <b>inside a "
     "st.form, never let a widget's label, or anything else that "
     "influences its auto-generated key, depend on another field in that "
     "same form.</b> Give it an explicit, fixed "
     "<font face='Courier'>key=</font> instead, and keep any "
     "value-dependent text (a caption, a hint) separate from the widget "
     "itself.")

# --------------------------------------------------------- 6. exercises
h2("6. Exercises")
bullets([
    "<b>Reorder blocks.</b> Add ↑/↓ buttons next to each block "
    "that swap it with its neighbour in "
    "<font face='Courier'>st.session_state.blocks</font> (same index-based "
    "mutation pattern as the delete button).",
    "<b>Edit in place.</b> Let the user click a block to edit its text, "
    "instead of only being able to delete and re-add it.",
    "<b>Images.</b> Add an <font face='Courier'>st.file_uploader</font> for "
    "an image, and a fourth block type that embeds it (reportlab's "
    "<font face='Courier'>platypus.Image</font> flowable, fed the "
    "uploaded file's bytes via <font face='Courier'>io.BytesIO</font> -- "
    "the same in-memory-file idea as the PDF itself).",
    "<b>Page numbers.</b> reportlab supports a page-template callback for "
    "headers/footers -- add page numbers to the generated document.",
    "<b>Save/load a draft.</b> Persist "
    "<font face='Courier'>st.session_state.blocks</font> to a local JSON "
    "file (same pattern as the to-do list and expense tracker projects), "
    "so a half-built document survives closing the browser tab.",
])

story.append(Spacer(1, 0.6 * cm))
body("<i>Written as a teaching companion to app.py -- read this guide with "
     "the code open side by side.</i>")

doc = SimpleDocTemplate(
    OUT_FILE, pagesize=A4,
    leftMargin=2.2 * cm, rightMargin=2.2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
    title="PDF Generator -- Mentoring Guide",
)
doc.build(story)
print("Wrote", OUT_FILE)
