import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="LifeSim 3D",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load game HTML from file
_dir = os.path.dirname(os.path.abspath(__file__))
_html_path = os.path.join(_dir, "index.html")

with open(_html_path, "r", encoding="utf-8") as f:
    GAME_HTML = f.read()

# ── Sidebar
with st.sidebar:
    st.title("🌍 LifeSim 3D")
    st.caption("Full 3D life simulator for GitHub Pages")
    st.divider()

    st.subheader("🎮 Controls")
    controls = {
        "Move":               "WASD",
        "Run":                "Shift + WASD",
        "Jump":               "Space",
        "Look around":        "Move Mouse",
        "Lock / Unlock Mouse":"] key",
        "Camera 1st person":  "Key 1",
        "Camera 2nd person":  "Key 2",
        "Camera 3rd person":  "Key 3",
        "Wardrobe / Interact":"E  (near wardrobe)",
        "Talk to NPC":        "F  (near NPC)",
        "Actions menu":       "/ key",
        "Enter / Exit car":   "C",
    }
    for k, v in controls.items():
        st.markdown(f"**{k}** → `{v}`")

    st.divider()
    st.subheader("📥 Download Files")
    st.caption("Put these in your GitHub repo to deploy on GitHub Pages.")

    # Download index.html
    with open(_html_path, "rb") as f:
        st.download_button(
            label="⬇️ Download index.html  (game)",
            data=f.read(),
            file_name="index.html",
            mime="text/html",
            use_container_width=True
        )

    # Download app.py
    _app_path = os.path.abspath(__file__)
    with open(_app_path, "rb") as f:
        st.download_button(
            label="⬇️ Download app.py  (Streamlit)",
            data=f.read(),
            file_name="app.py",
            mime="text/plain",
            use_container_width=True
        )

    # Download requirements.txt
    _req_path = os.path.join(_dir, "requirements.txt")
    if os.path.exists(_req_path):
        with open(_req_path, "rb") as f:
            st.download_button(
                label="⬇️ Download requirements.txt",
                data=f.read(),
                file_name="requirements.txt",
                mime="text/plain",
                use_container_width=True
            )

    st.divider()
    st.subheader("🚀 GitHub Pages Deploy")
    st.markdown("""
1. Create a GitHub repo
2. Upload **index.html** to the root
3. Go to **Settings → Pages**
4. Source: **main branch / root**
5. Visit `https://yourusername.github.io/reponame/`
""")
    st.subheader("🐍 Streamlit Cloud Deploy")
    st.markdown("""
1. Push **app.py**, **index.html**, **requirements.txt** to a repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repo, set `app.py` as entry point
4. Deploy!
""")

# ── Main area: render game
st.markdown("## 🌍 LifeSim 3D")
st.caption("Press **]** to lock mouse for free-look. Use **WASD** to move. Press **/** for the actions menu.")
components.html(GAME_HTML, height=700, scrolling=False)
