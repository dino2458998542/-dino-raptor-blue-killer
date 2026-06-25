import streamlit as st
import os

st.set_page_config(page_title="LifeSim 3D", layout="wide", page_icon="🌍")

st.title("🌍 LifeSim 3D")
st.caption("A 3D life simulation game — play in browser or deploy to GitHub Pages")

# Read game HTML
html_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    game_html = f.read()

# Inject game
st.components.v1.html(game_html, height=700, scrolling=False)

# Sidebar
with st.sidebar:
    st.header("🎮 LifeSim 3D")
    st.markdown("""
### Controls
| Key | Action |
|---|---|
| **WASD** | Move |
| **Shift** | Run |
| **Space** | Jump |
| **]** | Lock/unlock mouse |
| **1/2/3** | Camera modes |
| **/** | Actions menu |
| **E** | Wardrobe / Shop |
| **F** | Talk to NPC |
| **C** | Car in/out |
| **T** | Chat |
""")
    st.divider()
    st.header("📥 Download Files")
    files = {
        "index.html": "text/html",
        "app.py": "text/plain",
        "server.py": "text/plain",
        "requirements.txt": "text/plain",
        "Procfile": "text/plain",
        "render.yaml": "text/plain",
    }
    for fname, mime in files.items():
        fpath = os.path.join(os.path.dirname(__file__), fname)
        if os.path.exists(fpath):
            with open(fpath, "rb") as f:
                st.download_button(f"⬇️ {fname}", f.read(), file_name=fname, mime=mime)
        else:
            st.caption(f"⚠️ {fname} not found")

    st.divider()
    st.header("🚀 Deploy Multiplayer Server (Render.com)")
    st.markdown("""
**Free WebSocket server on Render:**

1. Go to [render.com](https://render.com) and sign up free
2. Click **New → Web Service**
3. Connect your GitHub repo (push all files)
4. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python server.py`
   - **Environment:** Python 3
5. Copy your Render URL (e.g. `wss://lifesim.onrender.com`)
6. Open `index.html`, find `window.LIFESIM_WS_URL` and set:
   ```js
   window.LIFESIM_WS_URL = 'wss://lifesim.onrender.com';
   ```
7. Re-upload to GitHub Pages — done! 🎉

**Or use the render.yaml** — Render auto-detects it and configures everything!
""")

    st.divider()
    st.header("🌐 Deploy Game (GitHub Pages)")
    st.markdown("""
1. Create GitHub repo
2. Upload `index.html`
3. Settings → Pages → Source: **main branch**
4. Live at `https://yourusername.github.io/reponame/`
""")
