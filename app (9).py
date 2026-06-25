import streamlit as st
import streamlit.components.v1 as components
import os, pathlib

st.set_page_config(page_title="LifeSim 3D", page_icon="🌍", layout="wide")
st.title("🌍 LifeSim 3D")
st.caption("Realistic 3D life simulator • Online multiplayer • GitHub Pages ready")

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.header("📁 Download Files")
    st.info("Download all files and upload to GitHub for online play")

    FILES = {
        "index.html": ("🎮 Game (index.html)",  "text/html"),
        "app.py":     ("🐍 Streamlit (app.py)", "text/plain"),
        "server.py":  ("🌐 Server (server.py)", "text/plain"),
        "requirements.txt": ("📦 requirements.txt", "text/plain"),
    }

    for fname, (label, mime) in FILES.items():
        fpath = pathlib.Path(fname)
        if fpath.exists():
            with open(fpath, "rb") as f:
                data = f.read()
            st.download_button(f"⬇️ {label}", data=data,
                               file_name=fname, mime=mime, use_container_width=True)
        else:
            st.warning(f"{fname} not found")

    st.divider()
    st.header("🌐 Multiplayer Setup")
    st.markdown("""
**Free hosting options:**
1. **[Glitch](https://glitch.com)** — upload `server.py` + `requirements.txt`
2. **[Railway](https://railway.app)** — connect GitHub repo
3. **[Render](https://render.com)** — free web service

After deploying, add to `index.html` before `</script>`:
```js
window.LIFESIM_WS_URL = 'wss://your-server.glitch.me';
```
""")

    st.divider()
    st.header("🎮 Controls")
    st.markdown("""
| Key | Action |
|-----|--------|
| **WASD** | Move |
| **Shift** | Run |
| **Space** | Jump |
| **]** | Mouse lock |
| **1/2/3** | Camera |
| **E** | Wardrobe / Shop |
| **F** | Talk to NPC |
| **C** | Car |
| **T** | Chat |
| **/** | Actions menu |
""")

# ── Main game embed ───────────────────────────────────────────
game_path = pathlib.Path("index.html")
if game_path.exists():
    html_content = game_path.read_text(encoding="utf-8")
    components.html(html_content, height=700, scrolling=False)
else:
    st.error("❌ index.html not found — run the Game HTML Builder block first")

st.markdown("""
---
### 🚀 Deploy to GitHub Pages
1. Download `index.html`  
2. Create a GitHub repo and upload it  
3. **Settings → Pages → Source: main branch**  
4. Live at `https://yourusername.github.io/yourrepo/`
""")
