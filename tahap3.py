def stage3_page():

    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from PIL import Image
# =========================
    # BANNER HTML (pengganti image1)
    # =========================
    st.markdown("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Barlow+Condensed:wght@700;900&display=swap');

      .s3-root {
        font-family: 'Space Mono', monospace;
        background: #000d16;
        border: 1px solid #001a2a;
        border-radius: 4px;
        overflow: hidden;
        position: relative;
        width: 100%;
        user-select: none;
        margin-bottom: 1.5rem;
      }
      .s3-topbar {
        display: flex; align-items: center; justify-content: space-between;
        padding: 6px 14px; border-bottom: 0.5px solid #001a2a; background: #00080f;
      }
      .s3-topbar-left { display: flex; align-items: center; gap: 10px; }
      .s3-dot {
        width: 6px; height: 6px; border-radius: 50%; background: #4ab8e8;
        animation: s3-pulse 2s ease-in-out infinite;
      }
      @keyframes s3-pulse {
        0%,100% { opacity:1; box-shadow: 0 0 0 0 #4ab8e840; }
        50% { opacity:0.5; box-shadow: 0 0 0 4px #4ab8e800; }
      }
      .s3-sys { font-size: 12px; letter-spacing: 3px; color: #4ab8e8; opacity: 0.6; text-transform: uppercase; }
      .s3-classify {
        font-size: 12px; letter-spacing: 2px; color: #e85a16;
        border: 0.5px solid #e85a1680; padding: 2px 8px; text-transform: uppercase; opacity: 0.7;
      }
      .s3-main {
        position: relative; height: 260px; overflow: hidden;
        display: flex; align-items: stretch;
      }
      .s3-data-stream { position: absolute; inset: 0; pointer-events: none; overflow: hidden; }
      .s3-stream-col {
        position: absolute; top: 0; bottom: 0; display: flex;
        flex-direction: column; gap: 3px;
        animation: s3-stream-fall linear infinite; opacity: 0.07;
      }
      .s3-stream-char { font-size: 8px; color: #4ab8e8; line-height: 1.2; }
      @keyframes s3-stream-fall {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(100%); }
      }
      .s3-scanline {
        position: absolute; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, transparent 0%, #4ab8e830 20%, #4ab8e860 50%, #4ab8e830 80%, transparent 100%);
        animation: s3-scan 3s linear infinite; pointer-events: none; z-index: 5;
      }
      @keyframes s3-scan {
        0% { top: -2px; }
        100% { top: 260px; }
      }
      .s3-left-bar {
        width: 3px; background: #4ab8e8; flex-shrink: 0; position: relative; z-index: 2;
      }
      .s3-left-bar::after {
        content: ''; position: absolute; inset: 0;
        background: linear-gradient(180deg, transparent, #4ab8e890, transparent);
        animation: s3-bar-glow 2s ease-in-out infinite;
      }
      @keyframes s3-bar-glow {
        0%,100% { opacity: 0.3; }
        50% { opacity: 1; }
      }
      .s3-vert-label {
        writing-mode: vertical-rl; transform: rotate(180deg); font-size: 13px;
        letter-spacing: 3px; color: #4ab8e8; opacity: 0.5; text-transform: uppercase;
        padding: 12px 6px; flex-shrink: 0; position: relative; z-index: 2;
        border-right: 0.5px solid #001a2a80;
      }
      .s3-center {
        flex: 1; display: flex; flex-direction: column; justify-content: center;
        padding: 0 20px; position: relative; z-index: 2;
      }
      .s3-chapter {
        font-size: 15px; letter-spacing: 4px; color: #4ab8e8; opacity: 0.55;
        text-transform: uppercase; margin-bottom: 5px;
        display: flex; align-items: center; gap: 8px;
      }
      .s3-chapter::before {
        content: ''; display: inline-block; width: 20px; height: 0.5px;
        background: #4ab8e8; opacity: 0.5;
      }
      .s3-title {
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 72px;
        line-height: 0.88; letter-spacing: -1.5px; color: #e8f4f8;
        text-transform: uppercase; margin-bottom: 6px;
      }
      .s3-title .s3-accent { color: #4ab8e8; display: block; }
      .s3-meta {
        font-size: 12px; letter-spacing: 1.5px; color: #001a2a;
        text-transform: uppercase; display: flex; align-items: center; gap: 8px;
      }
      .s3-meta-sep { color: #4ab8e840; }
      .s3-right {
        display: flex; flex-direction: column; align-items: flex-end;
        justify-content: center; padding: 0 18px; gap: 6px;
        position: relative; z-index: 2; border-left: 0.5px solid #001a2a60;
      }
      .s3-hex {
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 72px;
        line-height: 1; color: #4ab8e8; opacity: 0.06; letter-spacing: -3px;
      }
      .s3-badge {
        font-size: 12px; letter-spacing: 2px; padding: 3px 10px;
        border: 0.5px solid #4ab8e860; color: #4ab8e8; opacity: 0.7;
        text-transform: uppercase; margin-top: -20px;
      }
      .s3-uptime { font-size: 12px; color: #002a40; letter-spacing: 1px; opacity: 0.8; }
      .s3-corners span { position: absolute; width: 10px; height: 10px; }
      .s3-tl { top: 8px; left: 8px; border-top: 1px solid #4ab8e840; border-left: 1px solid #4ab8e840; }
      .s3-tr { top: 8px; right: 8px; border-top: 1px solid #4ab8e840; border-right: 1px solid #4ab8e840; }
      .s3-bl { bottom: 8px; left: 8px; border-bottom: 1px solid #4ab8e840; border-left: 1px solid #4ab8e840; }
      .s3-br { bottom: 8px; right: 8px; border-bottom: 1px solid #4ab8e840; border-right: 1px solid #4ab8e840; }
      .s3-glitch-bar {
        position: absolute; height: 1px; left: 0; right: 0; background: #4ab8e8;
        opacity: 0; animation: s3-glitch 7s ease-in-out infinite;
      }
      @keyframes s3-glitch {
        0%,100% { opacity: 0; }
        48% { opacity: 0; top: 60px; }
        50% { opacity: 0.15; top: 62px; }
        51% { opacity: 0; top: 58px; }
        52% { opacity: 0.08; top: 64px; }
        53% { opacity: 0; }
      }
      .s3-bottombar {
        display: flex; align-items: stretch;
        border-top: 0.5px solid #001a2a; background: #00080f;
      }
      .s3-ticker-wrap { flex: 1; overflow: hidden; position: relative; }
      .s3-ticker {
        display: flex; align-items: center; gap: 0;
        animation: s3-tick 18s linear infinite; white-space: nowrap; padding: 7px 0;
      }
      @keyframes s3-tick {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
      }
      .s3-tick-item {
        font-size: 12px; letter-spacing: 1.5px; color: #001a2a; text-transform: uppercase;
        padding: 0 18px; border-right: 0.5px solid #001a2a; flex-shrink: 0;
      }
      .s3-tick-item.hot { color: #4ab8e8; opacity: 0.8; }
      .s3-tick-item.warn { color: #e85a16; opacity: 0.7; }
      .s3-status-right {
        display: flex; align-items: center; gap: 12px;
        padding: 6px 14px; border-left: 0.5px solid #001a2a; flex-shrink: 0;
      }
      .s3-led {
        width: 5px; height: 5px; border-radius: 50%; background: #4ab8e8;
        opacity: 0.8; animation: s3-led-blink 1.2s step-end infinite;
      }
      @keyframes s3-led-blink {
        0%,100% { opacity: 0.8; }
        50% { opacity: 0.2; }
      }
      .s3-ok { font-size: 12px; letter-spacing: 2px; color: #4ab8e8; opacity: 0.6; text-transform: uppercase; }
    </style>

    <div class="s3-root">
      <div class="s3-topbar">
        <div class="s3-topbar-left">
          <div class="s3-dot"></div>
          <span class="s3-sys">SYS::FINCORE · NODE_C · SHADOW ACCESS DETECTED</span>
        </div>
        <span class="s3-classify">RESTRICTED</span>
      </div>

      <div class="s3-main">
        <div class="s3-data-stream" id="s3-stream"></div>
        <div class="s3-scanline"></div>
        <div class="s3-glitch-bar"></div>
        <div class="s3-corners">
          <span class="s3-tl"></span><span class="s3-tr"></span>
          <span class="s3-bl"></span><span class="s3-br"></span>
        </div>
        <div class="s3-left-bar"></div>
        <div class="s3-vert-label">Stage 03 · Access</div>
        <div class="s3-center">
          <div class="s3-chapter">Chapter <strong style="color:#4ab8e8;opacity:1;font-size:10px;">03</strong></div>
          <div class="s3-title">
            Langkah Yang
            <span class="s3-accent">Terlupakan</span>
          </div>
          <div class="s3-meta">
            <span>id: null</span>
            <span class="s3-meta-sep">·</span>
            <span>akses: penuh</span>
            <span class="s3-meta-sep">·</span>
            <span>ada sejak awal</span>
            <span class="s3-meta-sep">·</span>
            <span>bukan penyusup</span>
          </div>
        </div>
        <div class="s3-right">
          <div class="s3-hex">03</div>
          <div class="s3-badge">Root</div>
          <div class="s3-uptime" id="s3-uptime">00:00:00</div>
        </div>
      </div>

      <div class="s3-bottombar">
        <div class="s3-ticker-wrap">
          <div class="s3-ticker">
            <span class="s3-tick-item hot">ACCESS_LOG: ID_NULL</span>
            <span class="s3-tick-item">DEPT: —</span>
            <span class="s3-tick-item warn">PRIV: ROOT</span>
            <span class="s3-tick-item">SINCE: DEPLOY_v1</span>
            <span class="s3-tick-item hot">ARCHIVE ✓ · DB_TXN ✓ · CORE_SRV ✓</span>
            <span class="s3-tick-item">BACKDOOR? NO.</span>
            <span class="s3-tick-item warn">BUILT-IN FROM ORIGIN</span>
            <span class="s3-tick-item">TIMESTAMP: [EPOCH]</span>
            <span class="s3-tick-item hot">INTRUDER: NONE</span>
            <span class="s3-tick-item">NODE_ID: —</span>
            <span class="s3-tick-item warn">SHADOW ACCESS</span>
            <span class="s3-tick-item">▓▓░░▓▓░░▓▓░░</span>
            <span class="s3-tick-item hot">ACCESS_LOG: ID_NULL</span>
            <span class="s3-tick-item">DEPT: —</span>
            <span class="s3-tick-item warn">PRIV: ROOT</span>
            <span class="s3-tick-item">SINCE: DEPLOY_v1</span>
            <span class="s3-tick-item hot">ARCHIVE ✓ · DB_TXN ✓ · CORE_SRV ✓</span>
            <span class="s3-tick-item">BACKDOOR? NO.</span>
            <span class="s3-tick-item warn">BUILT-IN FROM ORIGIN</span>
            <span class="s3-tick-item">TIMESTAMP: [EPOCH]</span>
            <span class="s3-tick-item hot">INTRUDER: NONE</span>
            <span class="s3-tick-item">NODE_ID: —</span>
            <span class="s3-tick-item warn">SHADOW ACCESS</span>
            <span class="s3-tick-item">▓▓░░▓▓░░▓▓░░</span>
          </div>
        </div>
        <div class="s3-status-right">
          <div class="s3-led"></div>
          <span class="s3-ok">ONLINE</span>
        </div>
      </div>
    </div>

    <script>
      (function() {
        var chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノ';
        var stream = document.getElementById('s3-stream');
        if (stream) {
          var cols = 28;
          for (var i = 0; i < cols; i++) {
            var col = document.createElement('div');
            col.className = 's3-stream-col';
            col.style.left = (i / cols * 100) + '%';
            col.style.animationDuration = (6 + Math.random() * 8) + 's';
            col.style.animationDelay = (-Math.random() * 10) + 's';
            col.style.opacity = (0.03 + Math.random() * 0.06).toString();
            for (var j = 0; j < 20; j++) {
              var c = document.createElement('div');
              c.className = 's3-stream-char';
              c.textContent = chars[Math.floor(Math.random() * chars.length)];
              col.appendChild(c);
            }
            stream.appendChild(col);
          }
          setInterval(function() {
            var allCols = stream.querySelectorAll('.s3-stream-col');
            var idx = Math.floor(Math.random() * allCols.length);
            var chars2 = allCols[idx].querySelectorAll('.s3-stream-char');
            chars2.forEach(function(c) {
              c.textContent = '01アイウエオカキクケコ'[Math.floor(Math.random()*11)];
            });
          }, 200);
        }
        var uptime = document.getElementById('s3-uptime');
        if (uptime) {
          var s = 0;
          setInterval(function() {
            s++;
            var h = String(Math.floor(s/3600)).padStart(2,'0');
            var m = String(Math.floor((s%3600)/60)).padStart(2,'0');
            var sec = String(s%60).padStart(2,'0');
            uptime.textContent = h+':'+m+':'+sec;
          }, 1000);
        }
      })();
    </script>
    """, unsafe_allow_html=True)
    # =========================
    # LOAD DATA
    # =========================
    df_access = pd.read_csv("./data/stage3_access.csv")
    df_system = pd.read_csv("./data/stage3_system.csv")

    df_access["timestamp"] = pd.to_datetime(df_access["timestamp"])
    df_system["timestamp"] = pd.to_datetime(df_system["timestamp"])

    # =========================
    # CUSTOM CSS
    # =========================
    st.markdown("""
    <style>

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #050816;
        color: #F8FAFC;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(37,99,235,0.12), transparent 30%),
            radial-gradient(circle at bottom right, rgba(124,58,237,0.16), transparent 30%),
            linear-gradient(180deg, #030712 0%, #050816 100%);
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    .glass-card {
        position: relative;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 28px;
        padding: 3rem;
        backdrop-filter: blur(16px);
        box-shadow:
            0 0 60px rgba(0,0,0,0.35),
            inset 0 0 20px rgba(255,255,255,0.02);
        margin-bottom: 3rem;
        overflow: hidden;
        animation: fadeUp 0.8s ease;
    }

    .glass-card::before {
        content: "";
        position: absolute;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(255,255,255,0.06), transparent 70%);
        top: -150px;
        right: -100px;
        pointer-events: none;
    }

    .hero { text-align: center; }

    .main-title {
        font-size: 4.5rem;
        font-weight: 900;
        line-height: 0.95;
        letter-spacing: -3px;
        margin-bottom: 1rem;
        text-align: center;
        background: linear-gradient(to bottom, #FFFFFF, #94A3B8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 40px rgba(255,255,255,0.08);
    }

    .subtitle {
        text-align: center;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 5px;
        color: #64748B;
        margin-bottom: 3rem;
    }

    .story-text {
        max-width: 760px;
        margin: auto;
        text-align: center;
        line-height: 2.2;
        font-size: 1.08rem;
        color: #CBD5E1;
        white-space: pre-line;
    }

    .section-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 2rem;
        color: white;
    }

    .stTextInput input {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        color: white;
        padding: 1rem;
        text-align: center;
        font-size: 1rem;
    }

    .stButton button {
        width: 100%;
        height: 58px;
        border-radius: 18px;
        border: none;
        font-weight: 700;
        font-size: 1rem;
        color: white;
        letter-spacing: 0.5px;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        box-shadow: 0 0 25px rgba(124,58,237,0.28);
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 40px rgba(124,58,237,0.45);
    }

    .stDataFrame { border-radius: 18px; overflow: hidden; }

    .terminal {
        background: #020617;
        border: 1px solid rgba(56,189,248,0.18);
        border-radius: 22px;
        padding: 2rem;
        max-width: 800px;
        margin: auto;
        text-align: center;
        box-shadow:
            inset 0 0 35px rgba(56,189,248,0.03),
            0 0 30px rgba(56,189,248,0.08);
        font-family: monospace;
        color: #67E8F9;
        line-height: 2;
        font-size: 1rem;
    }

    .streamlit-expanderHeader {
        font-size: 1rem;
        font-weight: 600;
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    hr {
        display: block;        /* ← tambahkan ini */
        border: none;
        height: 1px;
        width: 72%;
        margin: 2.8rem auto;
        background: linear-gradient(
            90deg,
            transparent 0%,
            rgba(255,255,255,0.04) 10%,
            rgba(148,163,184,0.35) 50%,
            rgba(255,255,255,0.04) 90%,
            transparent 100%
        );
        box-shadow:
            0 0 12px rgba(148,163,184,0.12),
            0 0 30px rgba(59,130,246,0.06);
        opacity: 0.9;
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # HERO SECTION
    # =========================
    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">🧩 Stage 3</div>
        <div class="subtitle">Shadow Access</div>
        <div class="story-text">
Semua jejak mengarah ke satu tempat.

Log akses dibuka.

Awalnya terlihat normal.

Namun…

<b>ada sesuatu yang tidak masuk akal.</b>

<hr>

"Semua user masuk lewat login..."

"...atau setidaknya, seharusnya begitu."
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # DATA SECTION
    # =========================
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">📂 Access & System Logs</div>', unsafe_allow_html=True)

    with st.expander("📂 Access Log"):
        st.dataframe(df_access, use_container_width=True)

    with st.expander("📂 System Log"):
        st.dataframe(df_system, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # =========================
    # VISUALIZATION SECTION
    # =========================
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">📊 Aktivitas User</div>', unsafe_allow_html=True)

    df_access["hour"] = df_access["timestamp"].dt.hour

    pivot = df_access.pivot_table(
        index="user_id",
        columns="hour",
        aggfunc="size",
        fill_value=0
    )

    fig, ax = plt.subplots(figsize=(12, 5))

    sns.heatmap(pivot, cmap="mako", ax=ax)

    fig.patch.set_facecolor("#0B1120")
    ax.set_facecolor("#0B1120")
    ax.tick_params(colors="white")
    
    st.pyplot(fig)

    st.markdown("""
    <div class="terminal">
💡 HINT ANALISIS

Tidak semua yang muncul di access log...

...pernah benar-benar login.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # =========================
    # FINAL CHALLENGE
    # =========================
    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">🎯 Identifikasi User</div>
    <div class="story-text">
Siapa user yang selalu muncul...

tanpa pernah benar-benar login?
    </div>
    """, unsafe_allow_html=True)

    answer = st.text_input("Masukkan user ID:")

    if st.button("Kirim"):

        if answer.strip().upper() == "XJ-9A":

            st.success(
                "...\n\n"
                '"Dia tidak pernah login..."\n\n'
                '"...tapi selalu ada."\n\n'
                "Itu bukan user.\n\n"
                "Itu sesuatu yang lain."
            )

            st.session_state.current_stage = 4
            st.rerun()

        else:

            st.error("❌ Salah.")

    st.markdown('</div>', unsafe_allow_html=True)