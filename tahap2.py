def stage2_page():

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import networkx as nx
    import random
    from PIL import Image
# =========================
    # BANNER HTML (pengganti image1)
    # =========================
    st.markdown("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Barlow+Condensed:wght@700;900&display=swap');

      .s2-root {
        font-family: 'Space Mono', monospace;
        background: #0a0800;
        border: 1px solid #2a1f00;
        border-radius: 4px;
        overflow: hidden;
        position: relative;
        width: 100%;
        user-select: none;
        margin-bottom: 1.5rem;
      }
      .s2-topbar {
        display: flex; align-items: center; justify-content: space-between;
        padding: 6px 14px; border-bottom: 0.5px solid #2a1f00; background: #060500;
      }
      .s2-topbar-left { display: flex; align-items: center; gap: 10px; }
      .s2-dot {
        width: 6px; height: 6px; border-radius: 50%; background: #c8a416;
        animation: s2-pulse 2s ease-in-out infinite;
      }
      @keyframes s2-pulse {
        0%,100% { opacity:1; box-shadow: 0 0 0 0 #c8a41640; }
        50% { opacity:0.5; box-shadow: 0 0 0 4px #c8a41600; }
      }
      .s2-sys { font-size: 12px; letter-spacing: 3px; color: #c8a416; opacity: 0.6; text-transform: uppercase; }
      .s2-classify {
        font-size: 12px; letter-spacing: 2px; color: #e85a16;
        border: 0.5px solid #e85a1680; padding: 2px 8px; text-transform: uppercase; opacity: 0.7;
      }
      .s2-main {
        position: relative; height: 260px; overflow: hidden;
        display: flex; align-items: stretch;
      }
      .s2-data-stream { position: absolute; inset: 0; pointer-events: none; overflow: hidden; }
      .s2-stream-col {
        position: absolute; top: 0; bottom: 0; display: flex;
        flex-direction: column; gap: 3px;
        animation: s2-stream-fall linear infinite; opacity: 0.07;
      }
      .s2-stream-char { font-size: 8px; color: #c8a416; line-height: 1.2; }
      @keyframes s2-stream-fall {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(100%); }
      }
      .s2-scanline {
        position: absolute; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, transparent 0%, #c8a41630 20%, #c8a41660 50%, #c8a41630 80%, transparent 100%);
        animation: s2-scan 3s linear infinite; pointer-events: none; z-index: 5;
      }
      @keyframes s2-scan {
        0% { top: -2px; }
        100% { top: 260px; }
      }
      .s2-left-bar {
        width: 3px; background: #c8a416; flex-shrink: 0; position: relative; z-index: 2;
      }
      .s2-left-bar::after {
        content: ''; position: absolute; inset: 0;
        background: linear-gradient(180deg, transparent, #c8a41690, transparent);
        animation: s2-bar-glow 2s ease-in-out infinite;
      }
      @keyframes s2-bar-glow {
        0%,100% { opacity: 0.3; }
        50% { opacity: 1; }
      }
      .s2-vert-label {
        writing-mode: vertical-rl; transform: rotate(180deg); font-size: 13px;
        letter-spacing: 3px; color: #c8a416; opacity: 0.5; text-transform: uppercase;
        padding: 12px 6px; flex-shrink: 0; position: relative; z-index: 2;
        border-right: 0.5px solid #2a1f0080;
      }
      .s2-center {
        flex: 1; display: flex; flex-direction: column; justify-content: center;
        padding: 0 20px; position: relative; z-index: 2;
      }
      .s2-chapter {
        font-size: 15px; letter-spacing: 4px; color: #c8a416; opacity: 0.55;
        text-transform: uppercase; margin-bottom: 5px;
        display: flex; align-items: center; gap: 8px;
      }
      .s2-chapter::before {
        content: ''; display: inline-block; width: 20px; height: 0.5px;
        background: #c8a416; opacity: 0.5;
      }
      .s2-title {
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 72px;
        line-height: 0.88; letter-spacing: -1.5px; color: #f5f0e0;
        text-transform: uppercase; margin-bottom: 6px;
      }
      .s2-title .s2-accent { color: #c8a416; display: block; }
      .s2-meta {
        font-size: 12px; letter-spacing: 1.5px; color: #2a2200;
        text-transform: uppercase; display: flex; align-items: center; gap: 8px;
      }
      .s2-meta-sep { color: #c8a41440; }
      .s2-right {
        display: flex; flex-direction: column; align-items: flex-end;
        justify-content: center; padding: 0 18px; gap: 6px;
        position: relative; z-index: 2; border-left: 0.5px solid #2a1f0060;
      }
      .s2-hex {
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 72px;
        line-height: 1; color: #c8a416; opacity: 0.06; letter-spacing: -3px;
      }
      .s2-badge {
        font-size: 12px; letter-spacing: 2px; padding: 3px 10px;
        border: 0.5px solid #c8a41660; color: #c8a416; opacity: 0.7;
        text-transform: uppercase; margin-top: -20px;
      }
      .s2-uptime { font-size: 12px; color: #3a2e00; letter-spacing: 1px; opacity: 0.8; }
      .s2-corners span { position: absolute; width: 10px; height: 10px; }
      .s2-tl { top: 8px; left: 8px; border-top: 1px solid #c8a41440; border-left: 1px solid #c8a41440; }
      .s2-tr { top: 8px; right: 8px; border-top: 1px solid #c8a41440; border-right: 1px solid #c8a41440; }
      .s2-bl { bottom: 8px; left: 8px; border-bottom: 1px solid #c8a41440; border-left: 1px solid #c8a41440; }
      .s2-br { bottom: 8px; right: 8px; border-bottom: 1px solid #c8a41440; border-right: 1px solid #c8a41440; }
      .s2-glitch-bar {
        position: absolute; height: 1px; left: 0; right: 0; background: #c8a416;
        opacity: 0; animation: s2-glitch 7s ease-in-out infinite;
      }
      @keyframes s2-glitch {
        0%,100% { opacity: 0; }
        48% { opacity: 0; top: 60px; }
        50% { opacity: 0.15; top: 62px; }
        51% { opacity: 0; top: 58px; }
        52% { opacity: 0.08; top: 64px; }
        53% { opacity: 0; }
      }
      .s2-bottombar {
        display: flex; align-items: stretch;
        border-top: 0.5px solid #2a1f00; background: #060500;
      }
      .s2-ticker-wrap { flex: 1; overflow: hidden; position: relative; }
      .s2-ticker {
        display: flex; align-items: center; gap: 0;
        animation: s2-tick 18s linear infinite; white-space: nowrap; padding: 7px 0;
      }
      @keyframes s2-tick {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
      }
      .s2-tick-item {
        font-size: 12px; letter-spacing: 1.5px; color: #2a2200; text-transform: uppercase;
        padding: 0 18px; border-right: 0.5px solid #2a1f00; flex-shrink: 0;
      }
      .s2-tick-item.hot { color: #c8a416; opacity: 0.8; }
      .s2-tick-item.warn { color: #e85a16; opacity: 0.7; }
      .s2-status-right {
        display: flex; align-items: center; gap: 12px;
        padding: 6px 14px; border-left: 0.5px solid #2a1f00; flex-shrink: 0;
      }
      .s2-led {
        width: 5px; height: 5px; border-radius: 50%; background: #c8a416;
        opacity: 0.8; animation: s2-led-blink 1.2s step-end infinite;
      }
      @keyframes s2-led-blink {
        0%,100% { opacity: 0.8; }
        50% { opacity: 0.2; }
      }
      .s2-ok { font-size: 12px; letter-spacing: 2px; color: #c8a416; opacity: 0.6; text-transform: uppercase; }
    </style>

    <div class="s2-root">
      <div class="s2-topbar">
        <div class="s2-topbar-left">
          <div class="s2-dot"></div>
          <span class="s2-sys">SYS::FINCORE · NODE_B · CROSS-BORDER ACTIVE</span>
        </div>
        <span class="s2-classify">RESTRICTED</span>
      </div>

      <div class="s2-main">
        <div class="s2-data-stream" id="s2-stream"></div>
        <div class="s2-scanline"></div>
        <div class="s2-glitch-bar"></div>
        <div class="s2-corners">
          <span class="s2-tl"></span><span class="s2-tr"></span>
          <span class="s2-bl"></span><span class="s2-br"></span>
        </div>
        <div class="s2-left-bar"></div>
        <div class="s2-vert-label">Stage 02 · Convergence</div>
        <div class="s2-center">
          <div class="s2-chapter">Chapter <strong style="color:#c8a416;opacity:1;font-size:10px;">02</strong></div>
          <div class="s2-title">
            Bayangan
            <span class="s2-accent">Di Langit</span>
          </div>
          <div class="s2-meta">
            <span>semua jalur → satu titik</span>
            <span class="s2-meta-sep">·</span>
            <span>sistem bayangan</span>
            <span class="s2-meta-sep">·</span>
            <span>tidak tercatat</span>
          </div>
        </div>
        <div class="s2-right">
          <div class="s2-hex">02</div>
          <div class="s2-badge">Converge</div>
          <div class="s2-uptime" id="s2-uptime">00:00:00</div>
        </div>
      </div>

      <div class="s2-bottombar">
        <div class="s2-ticker-wrap">
          <div class="s2-ticker">
            <span class="s2-tick-item hot">NODE_MERGE ████→█</span>
            <span class="s2-tick-item">CONVERGENCE: 99.7%</span>
            <span class="s2-tick-item warn">SHADOW_SYSTEM ACTIVE</span>
            <span class="s2-tick-item">SIM:CROSS-BORDER</span>
            <span class="s2-tick-item hot">ALL PATHS → ONE NODE</span>
            <span class="s2-tick-item">TXN_LOOP ∞</span>
            <span class="s2-tick-item warn">UNREGISTERED</span>
            <span class="s2-tick-item">ENDPOINT: 0x0001</span>
            <span class="s2-tick-item hot">SYS_SHADOW</span>
            <span class="s2-tick-item">NODE_ID: —</span>
            <span class="s2-tick-item warn">ANOMALY_FLAGGED</span>
            <span class="s2-tick-item">▓▓░░▓▓░░▓▓░░</span>
            <span class="s2-tick-item hot">NODE_MERGE ████→█</span>
            <span class="s2-tick-item">CONVERGENCE: 99.7%</span>
            <span class="s2-tick-item warn">SHADOW_SYSTEM ACTIVE</span>
            <span class="s2-tick-item">SIM:CROSS-BORDER</span>
            <span class="s2-tick-item hot">ALL PATHS → ONE NODE</span>
            <span class="s2-tick-item">TXN_LOOP ∞</span>
            <span class="s2-tick-item warn">UNREGISTERED</span>
            <span class="s2-tick-item">ENDPOINT: 0x0001</span>
            <span class="s2-tick-item hot">SYS_SHADOW</span>
            <span class="s2-tick-item">NODE_ID: —</span>
            <span class="s2-tick-item warn">ANOMALY_FLAGGED</span>
            <span class="s2-tick-item">▓▓░░▓▓░░▓▓░░</span>
          </div>
        </div>
        <div class="s2-status-right">
          <div class="s2-led"></div>
          <span class="s2-ok">ONLINE</span>
        </div>
      </div>
    </div>

    <script>
      (function() {
        var chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノ';
        var stream = document.getElementById('s2-stream');
        if (stream) {
          var cols = 28;
          for (var i = 0; i < cols; i++) {
            var col = document.createElement('div');
            col.className = 's2-stream-col';
            col.style.left = (i / cols * 100) + '%';
            col.style.animationDuration = (6 + Math.random() * 8) + 's';
            col.style.animationDelay = (-Math.random() * 10) + 's';
            col.style.opacity = (0.03 + Math.random() * 0.06).toString();
            for (var j = 0; j < 20; j++) {
              var c = document.createElement('div');
              c.className = 's2-stream-char';
              c.textContent = chars[Math.floor(Math.random() * chars.length)];
              col.appendChild(c);
            }
            stream.appendChild(col);
          }
          setInterval(function() {
            var allCols = stream.querySelectorAll('.s2-stream-col');
            var idx = Math.floor(Math.random() * allCols.length);
            var chars2 = allCols[idx].querySelectorAll('.s2-stream-char');
            chars2.forEach(function(c) {
              c.textContent = '01アイウエオカキクケコ'[Math.floor(Math.random()*11)];
            });
          }, 200);
        }
        var uptime = document.getElementById('s2-uptime');
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
    df = pd.read_csv("./data/stage2_network.csv")

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

    .stCodeBlock { border-radius: 20px; }

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
        <div class="main-title">🧩 Stage 2</div>
        <div class="subtitle">Convergence</div>
        <div class="story-text">
Awalnya tidak ada yang aneh.

Transaksi internasional berjalan seperti biasa.

Tidak ada pola yang mencurigakan.

Tidak ada pusat yang terlihat.

<hr>

Namun ketika data divisualisasikan ulang…

struktur mulai berubah.

<hr>

Bukan karena data berubah.

Tapi karena cara melihatnya yang berbeda.

<hr>

Beberapa node terlihat lebih "berat" dari yang lain.

Bukan secara volume.

Tapi secara koneksi.

<hr>

Dan semakin lama diamati,

semakin jelas satu hal:

<hr>

Sistem ini tidak tersebar.

Sistem ini <b>tertarik ke satu titik.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # DATA SECTION
    # =========================
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">📂 Full Transaction Data</div>', unsafe_allow_html=True)

    st.dataframe(df, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # =========================
    # ANALYSIS SECTION
    # =========================
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">🔍 Analisis Jaringan</div>
    <div class="story-text">
Seorang analis mencoba memvisualisasikan jaringan transaksi.

Namun…

kode yang digunakan tidak lengkap.
    </div>
    """, unsafe_allow_html=True)

    st.code("""
import networkx as nx
import matplotlib.pyplot as plt

G = nx.from_pandas_edgelist(df, '...[A]...', '...[B]...')

pos = nx.spring_layout(G, seed=42)

degree = dict(G.degree())
node_sizes = [degree[n]*60 for n in G.nodes()]

nx.draw(
    G, pos,
    with_labels=True,
    node_size=node_sizes
)

plt.show()
""", language="python")

    st.markdown('<div class="section-title">💻 Lengkapi Kode</div>', unsafe_allow_html=True)

    A = st.text_input("Isi A (source):")
    B = st.text_input("Isi B (destination):")

    if st.button("Run Code"):

        if A.strip() == "source_country" and B.strip() == "destination_country":

            st.success("✅ Visualisasi berhasil dijalankan...")

            G = nx.from_pandas_edgelist(df, "source_country", "destination_country")

            fig, ax = plt.subplots(figsize=(12, 10))

            pos = nx.spring_layout(G, seed=42)

            node_colors = [
                (random.random(), random.random(), random.random())
                for _ in G.nodes()
            ]

            degree = dict(G.degree())
            node_sizes = [degree[n] * 80 for n in G.nodes()]

            fig.patch.set_facecolor("#0B1120")
            ax.set_facecolor("#0B1120")

            nx.draw(
                G,
                pos,
                ax=ax,
                with_labels=True,
                node_color=node_colors,
                node_size=node_sizes,
                font_size=8,
                edge_color="gray",
                alpha=0.7,
            )

            st.pyplot(fig)

            st.markdown("""
            <div class="terminal">
💡 HINT ANALISIS

• Node terbesar = pusat aliran
• Perhatikan koneksi terbanyak
• Sistem selalu kembali ke titik yang sama
            </div>
            """, unsafe_allow_html=True)

        else:

            st.error("❌ Code Error! Periksa kembali nama kolom.")

    st.markdown('</div>', unsafe_allow_html=True)

    # =========================
    # FINAL ANSWER SECTION
    # =========================
    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">🎯 Identifikasi Pusat Sistem</div>
    <div class="story-text">
Ke mana semua jalur ini sebenarnya mengarah?
    </div>
    """, unsafe_allow_html=True)

    answer = st.text_input("Masukkan jawaban:")

    if st.button("Kirim Jawaban"):

        if "UNITED STATES" in answer.strip().upper() or "US" in answer.strip().upper():

            st.success("✅ Benar. Semua jalur mengarah ke sana.")

            st.session_state.current_stage = 3
            st.rerun()

        else:

            st.error("❌ Salah. Perhatikan pola koneksi.")

    st.markdown('</div>', unsafe_allow_html=True)