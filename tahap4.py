def stage4_page():
    
    import streamlit as st
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import networkx as nx
    from PIL import Image
# =========================
    # BANNER HTML (pengganti image1)
    # =========================
    st.markdown("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Barlow+Condensed:wght@700;900&display=swap');

      .s4-root {
        font-family: 'Space Mono', monospace;
        background: #160800;
        border: 1px solid #2a0a00;
        border-radius: 4px;
        overflow: hidden;
        position: relative;
        width: 100%;
        user-select: none;
        margin-bottom: 1.5rem;
      }
      .s4-topbar {
        display: flex; align-items: center; justify-content: space-between;
        padding: 6px 14px; border-bottom: 0.5px solid #2a0a00; background: #0d0500;
      }
      .s4-topbar-left { display: flex; align-items: center; gap: 10px; }
      .s4-dot {
        width: 6px; height: 6px; border-radius: 50%; background: #e85a16;
        animation: s4-pulse 2s ease-in-out infinite;
      }
      @keyframes s4-pulse {
        0%,100% { opacity:1; box-shadow: 0 0 0 0 #e85a1640; }
        50% { opacity:0.5; box-shadow: 0 0 0 4px #e85a1600; }
      }
      .s4-sys { font-size: 12px; letter-spacing: 3px; color: #e85a16; opacity: 0.6; text-transform: uppercase; }
      .s4-classify {
        font-size: 12px; letter-spacing: 2px; color: #e85a16;
        border: 0.5px solid #e85a1680; padding: 2px 8px; text-transform: uppercase; opacity: 0.7;
      }
      .s4-main {
        position: relative; height: 260px; overflow: hidden;
        display: flex; align-items: stretch;
      }
      .s4-data-stream { position: absolute; inset: 0; pointer-events: none; overflow: hidden; }
      .s4-stream-col {
        position: absolute; top: 0; bottom: 0; display: flex;
        flex-direction: column; gap: 3px;
        animation: s4-stream-fall linear infinite; opacity: 0.07;
      }
      .s4-stream-char { font-size: 8px; color: #e85a16; line-height: 1.2; }
      @keyframes s4-stream-fall {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(100%); }
      }
      .s4-scanline {
        position: absolute; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, transparent 0%, #e85a1630 20%, #e85a1660 50%, #e85a1630 80%, transparent 100%);
        animation: s4-scan 3s linear infinite; pointer-events: none; z-index: 5;
      }
      @keyframes s4-scan {
        0% { top: -2px; }
        100% { top: 260px; }
      }
      .s4-left-bar {
        width: 3px; background: #e85a16; flex-shrink: 0; position: relative; z-index: 2;
      }
      .s4-left-bar::after {
        content: ''; position: absolute; inset: 0;
        background: linear-gradient(180deg, transparent, #e85a1690, transparent);
        animation: s4-bar-glow 2s ease-in-out infinite;
      }
      @keyframes s4-bar-glow {
        0%,100% { opacity: 0.3; }
        50% { opacity: 1; }
      }
      .s4-vert-label {
        writing-mode: vertical-rl; transform: rotate(180deg); font-size: 13px;
        letter-spacing: 3px; color: #e85a16; opacity: 0.5; text-transform: uppercase;
        padding: 12px 6px; flex-shrink: 0; position: relative; z-index: 2;
        border-right: 0.5px solid #2a0a0080;
      }
      .s4-center {
        flex: 1; display: flex; flex-direction: column; justify-content: center;
        padding: 0 20px; position: relative; z-index: 2;
      }
      .s4-chapter {
        font-size: 15px; letter-spacing: 4px; color: #e85a16; opacity: 0.55;
        text-transform: uppercase; margin-bottom: 5px;
        display: flex; align-items: center; gap: 8px;
      }
      .s4-chapter::before {
        content: ''; display: inline-block; width: 20px; height: 0.5px;
        background: #e85a16; opacity: 0.5;
      }
      .s4-title {
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 72px;
        line-height: 0.88; letter-spacing: -1.5px; color: #f8ece4;
        text-transform: uppercase; margin-bottom: 6px;
      }
      .s4-title .s4-accent { color: #e85a16; display: block; }
      .s4-meta {
        font-size: 12px; letter-spacing: 1.5px; color: #2a0a00;
        text-transform: uppercase; display: flex; align-items: center; gap: 8px;
      }
      .s4-meta-sep { color: #e85a1640; }
      .s4-right {
        display: flex; flex-direction: column; align-items: flex-end;
        justify-content: center; padding: 0 18px; gap: 6px;
        position: relative; z-index: 2; border-left: 0.5px solid #2a0a0060;
      }
      .s4-hex {
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 72px;
        line-height: 1; color: #e85a16; opacity: 0.06; letter-spacing: -3px;
      }
      .s4-badge {
        font-size: 12px; letter-spacing: 2px; padding: 3px 10px;
        border: 0.5px solid #e85a1660; color: #e85a16; opacity: 0.7;
        text-transform: uppercase; margin-top: -20px;
      }
      .s4-uptime { font-size: 12px; color: #3a1000; letter-spacing: 1px; opacity: 0.8; }
      .s4-corners span { position: absolute; width: 10px; height: 10px; }
      .s4-tl { top: 8px; left: 8px; border-top: 1px solid #e85a1640; border-left: 1px solid #e85a1640; }
      .s4-tr { top: 8px; right: 8px; border-top: 1px solid #e85a1640; border-right: 1px solid #e85a1640; }
      .s4-bl { bottom: 8px; left: 8px; border-bottom: 1px solid #e85a1640; border-left: 1px solid #e85a1640; }
      .s4-br { bottom: 8px; right: 8px; border-bottom: 1px solid #e85a1640; border-right: 1px solid #e85a1640; }
      .s4-glitch-bar {
        position: absolute; height: 1px; left: 0; right: 0; background: #e85a16;
        opacity: 0; animation: s4-glitch 7s ease-in-out infinite;
      }
      @keyframes s4-glitch {
        0%,100% { opacity: 0; }
        48% { opacity: 0; top: 60px; }
        50% { opacity: 0.15; top: 62px; }
        51% { opacity: 0; top: 58px; }
        52% { opacity: 0.08; top: 64px; }
        53% { opacity: 0; }
      }
      .s4-bottombar {
        display: flex; align-items: stretch;
        border-top: 0.5px solid #2a0a00; background: #0d0500;
      }
      .s4-ticker-wrap { flex: 1; overflow: hidden; position: relative; }
      .s4-ticker {
        display: flex; align-items: center; gap: 0;
        animation: s4-tick 18s linear infinite; white-space: nowrap; padding: 7px 0;
      }
      @keyframes s4-tick {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
      }
      .s4-tick-item {
        font-size: 12px; letter-spacing: 1.5px; color: #2a0a00; text-transform: uppercase;
        padding: 0 18px; border-right: 0.5px solid #2a0a00; flex-shrink: 0;
      }
      .s4-tick-item.hot { color: #e85a16; opacity: 0.8; }
      .s4-tick-item.warn { color: #c8a416; opacity: 0.7; }
      .s4-status-right {
        display: flex; align-items: center; gap: 12px;
        padding: 6px 14px; border-left: 0.5px solid #2a0a00; flex-shrink: 0;
      }
      .s4-led {
        width: 5px; height: 5px; border-radius: 50%; background: #e85a16;
        opacity: 0.8; animation: s4-led-blink 1.2s step-end infinite;
      }
      @keyframes s4-led-blink {
        0%,100% { opacity: 0.8; }
        50% { opacity: 0.2; }
      }
      .s4-ok { font-size: 12px; letter-spacing: 2px; color: #e85a16; opacity: 0.6; text-transform: uppercase; }
    </style>

    <div class="s4-root">
      <div class="s4-topbar">
        <div class="s4-topbar-left">
          <div class="s4-dot"></div>
          <span class="s4-sys">SYS::FINCORE · NODE_D · EXTRACTION IN PROGRESS</span>
        </div>
        <span class="s4-classify">RESTRICTED</span>
      </div>

      <div class="s4-main">
        <div class="s4-data-stream" id="s4-stream"></div>
        <div class="s4-scanline"></div>
        <div class="s4-glitch-bar"></div>
        <div class="s4-corners">
          <span class="s4-tl"></span><span class="s4-tr"></span>
          <span class="s4-bl"></span><span class="s4-br"></span>
        </div>
        <div class="s4-left-bar"></div>
        <div class="s4-vert-label">Stage 04 · Extraction</div>
        <div class="s4-center">
          <div class="s4-chapter">Chapter <strong style="color:#e85a16;opacity:1;font-size:10px;">04</strong></div>
          <div class="s4-title">
            Impostor
            <span class="s4-accent">Location</span>
          </div>
          <div class="s4-meta">
            <span>data digantikan</span>
            <span class="s4-meta-sep">·</span>
            <span>shadow ledger</span>
            <span class="s4-meta-sep">·</span>
            <span>jalur ditinggalkan sengaja</span>
          </div>
        </div>
        <div class="s4-right">
          <div class="s4-hex">04</div>
          <div class="s4-badge">Overwrite</div>
          <div class="s4-uptime" id="s4-uptime">00:00:00</div>
        </div>
      </div>

      <div class="s4-bottombar">
        <div class="s4-ticker-wrap">
          <div class="s4-ticker">
            <span class="s4-tick-item hot">OVERWRITE ████████</span>
            <span class="s4-tick-item">LEDGER_SHADOW: ACTIVE</span>
            <span class="s4-tick-item warn">DELTA: [CLASSIFIED]</span>
            <span class="s4-tick-item">ALARM: NONE</span>
            <span class="s4-tick-item hot">THEFT: UNDETECTED</span>
            <span class="s4-tick-item">DIFF: PRESENT</span>
            <span class="s4-tick-item warn">GATEWAY_EXT OPENED</span>
            <span class="s4-tick-item">PATH: TOO CLEAN</span>
            <span class="s4-tick-item hot">TRAIL: LEFT INTENTIONALLY</span>
            <span class="s4-tick-item">NODE_ID: —</span>
            <span class="s4-tick-item warn">SHADOW LEDGER</span>
            <span class="s4-tick-item">▓▓░░▓▓░░▓▓░░</span>
            <span class="s4-tick-item hot">OVERWRITE ████████</span>
            <span class="s4-tick-item">LEDGER_SHADOW: ACTIVE</span>
            <span class="s4-tick-item warn">DELTA: [CLASSIFIED]</span>
            <span class="s4-tick-item">ALARM: NONE</span>
            <span class="s4-tick-item hot">THEFT: UNDETECTED</span>
            <span class="s4-tick-item">DIFF: PRESENT</span>
            <span class="s4-tick-item warn">GATEWAY_EXT OPENED</span>
            <span class="s4-tick-item">PATH: TOO CLEAN</span>
            <span class="s4-tick-item hot">TRAIL: LEFT INTENTIONALLY</span>
            <span class="s4-tick-item">NODE_ID: —</span>
            <span class="s4-tick-item warn">SHADOW LEDGER</span>
            <span class="s4-tick-item">▓▓░░▓▓░░▓▓░░</span>
          </div>
        </div>
        <div class="s4-status-right">
          <div class="s4-led"></div>
          <span class="s4-ok">ONLINE</span>
        </div>
      </div>
    </div>

    <script>
      (function() {
        var chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノ';
        var stream = document.getElementById('s4-stream');
        if (stream) {
          var cols = 28;
          for (var i = 0; i < cols; i++) {
            var col = document.createElement('div');
            col.className = 's4-stream-col';
            col.style.left = (i / cols * 100) + '%';
            col.style.animationDuration = (6 + Math.random() * 8) + 's';
            col.style.animationDelay = (-Math.random() * 10) + 's';
            col.style.opacity = (0.03 + Math.random() * 0.06).toString();
            for (var j = 0; j < 20; j++) {
              var c = document.createElement('div');
              c.className = 's4-stream-char';
              c.textContent = chars[Math.floor(Math.random() * chars.length)];
              col.appendChild(c);
            }
            stream.appendChild(col);
          }
          setInterval(function() {
            var allCols = stream.querySelectorAll('.s4-stream-col');
            var idx = Math.floor(Math.random() * allCols.length);
            var chars2 = allCols[idx].querySelectorAll('.s4-stream-char');
            chars2.forEach(function(c) {
              c.textContent = '01アイウエオカキクケコ'[Math.floor(Math.random()*11)];
            });
          }, 200);
        }
        var uptime = document.getElementById('s4-uptime');
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
        max-width: 1250px;
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
        max-width: 820px;
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

    .terminal {
        background: #020617;
        border: 1px solid rgba(56,189,248,0.18);
        border-radius: 22px;
        padding: 2rem;
        max-width: 850px;
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

    .stSuccess, .stError, .stWarning { border-radius: 16px; }

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
        <div class="main-title">🧩 Stage 4</div>
        <div class="subtitle">Extraction</div>
        <div class="story-text">
Sistem tidak menunjukkan kegagalan.

Tidak ada transaksi yang hilang.

Namun ketika ledger lama dibandingkan dengan snapshot baru…

sesuatu tidak cocok.

<hr>

Bukan data yang hilang.

Tapi <b>struktur nilainya yang berubah.</b>

<hr>

Semua masih terlihat valid.

Semua masih berjalan normal.

Dan justru itu yang membuatnya berbahaya.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # DATA GENERATION
    # =========================
    np.random.seed(42)

    nodes = [f"NODE_{i}" for i in range(25)]
    nodes.append("EXTERNAL_GATEWAY")

    paths = []

    for _ in range(500):
        src = np.random.choice(nodes)
        dst = np.random.choice(nodes)
        if src != dst:
            paths.append([src, dst, np.random.randint(100, 900)])

    for _ in range(80):
        paths.append([
            np.random.choice(nodes[:-1]),
            "EXTERNAL_GATEWAY",
            np.random.randint(100, 900)
        ])

    decoy_1 = [
        ("NODE_3",  "NODE_6",           510),
        ("NODE_6",  "NODE_9",           505),
        ("NODE_9",  "NODE_12",          495),
        ("NODE_12", "EXTERNAL_GATEWAY", 500),
    ]

    decoy_2 = [
        ("NODE_10", "NODE_11",          480),
        ("NODE_11", "NODE_12",          485),
        ("NODE_12", "NODE_13",          490),
        ("NODE_13", "EXTERNAL_GATEWAY", 495),
    ]

    clean_path = [
        ("NODE_7",  "NODE_14",          331),
        ("NODE_14", "NODE_18",          332),
        ("NODE_18", "NODE_22",          333),
        ("NODE_22", "NODE_5",           334),
        ("NODE_5",  "EXTERNAL_GATEWAY", 335),
    ]

    paths += decoy_1 + decoy_2 + clean_path

    df = pd.DataFrame(paths, columns=["source", "destination", "amount"])

    # =========================
    # GRAPH BUILD
    # =========================
    G = nx.from_pandas_edgelist(
        df,
        "source",
        "destination",
        edge_attr="amount",
        create_using=nx.DiGraph()
    )

    pos = nx.spring_layout(G, seed=42, k=0.8, iterations=80)
    pos["EXTERNAL_GATEWAY"] = [1.0, -0.6]

    # =========================
    # EDGE CLASSIFICATION
    # =========================
    clean_values = {331, 332, 333, 334, 335}
    decoy_values = {510, 505, 495, 500, 480, 485, 490}

    edge_colors = []
    edge_widths = []
    edge_alpha  = []

    for u, v, d in G.edges(data=True):
        amt = d["amount"]
        if amt in clean_values:
            edge_colors.append("#4fc3f7")
            edge_widths.append(np.random.uniform(2.5, 3.5))
            edge_alpha.append(np.random.uniform(0.6, 0.95))
        elif amt in decoy_values:
            edge_colors.append("#ffd54f")
            edge_widths.append(np.random.uniform(1.8, 2.5))
            edge_alpha.append(np.random.uniform(0.4, 0.7))
        else:
            edge_colors.append("#9e9e9e")
            edge_widths.append(np.random.uniform(0.2, 0.8))
            edge_alpha.append(np.random.uniform(0.05, 0.2))

    # =========================
    # VISUALIZATION SECTION
    # =========================
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">🌐 Shadow Ledger Visualization</div>', unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(16, 10))
    fig.patch.set_facecolor("#0B1120")
    ax.set_facecolor("#0B1120")

    # Draw all edges (noise layer)
    for (u, v), c, w, a in zip(G.edges(), edge_colors, edge_widths, edge_alpha):
        nx.draw_networkx_edges(
            G, pos,
            edgelist=[(u, v)],
            edge_color=c,
            width=w,
            alpha=a,
            arrows=False,
            ax=ax,
        )

    # Draw clean signal edges with arrows on top
    clean_edges = [
        (u, v)
        for u, v, d in G.edges(data=True)
        if d["amount"] in clean_values
    ]

    nx.draw_networkx_edges(
        G, pos,
        edgelist=clean_edges,
        edge_color="#4fc3f7",
        width=3.0,
        alpha=0.9,
        arrows=True,
        arrowsize=10,
        ax=ax,
    )

    # Node styling
    clean_signal_nodes = {"NODE_7", "NODE_14", "NODE_18", "NODE_22", "NODE_5"}

    node_colors = []
    node_sizes  = []

    for n in G.nodes():
        if n == "EXTERNAL_GATEWAY":
            node_colors.append("#2c3e50")
            node_sizes.append(2500)
        elif n in clean_signal_nodes:
            node_colors.append("#ff6b6b")
            node_sizes.append(1300)
        else:
            node_colors.append("#3498db")
            node_sizes.append(int(np.random.randint(900, 1100)))

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=7, font_color="white", ax=ax)

    ax.set_title("Shadow Ledger — Extraction Layer", fontsize=14, color="white")
    ax.axis("off")

    st.pyplot(fig)

    st.markdown('</div>', unsafe_allow_html=True)

    # =========================
    # OBSERVATION SECTION
    # =========================
    st.markdown("""
    <div class="glass-card">
        <div class="section-title">🔍 System Observation</div>
        <div class="terminal">
Dalam chaos transaksi,
terdapat satu pola yang:

• tidak paling besar
• tidak paling sering
• tidak paling mencolok

Namun...

<b>paling konsisten secara struktur aliran.</b>

<hr>

Sistem ini tidak menyembunyikan jalurnya.

Ia hanya menguburnya
di bawah noise.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # EVALUATION FUNCTION
    # =========================
    def evaluate_start(node):

        current = node
        score   = 0

        signal_nodes = {"NODE_14", "NODE_18", "NODE_22", "NODE_5", "EXTERNAL_GATEWAY"}

        try:
            for _ in range(5):
                next_edges = df[df["source"] == current]
                if next_edges.empty:
                    break
                current = next_edges.sort_values("amount").iloc[0]["destination"]
                if current in signal_nodes:
                    score += 1
        except Exception:
            pass

        return score

    # =========================
    # FINAL CHALLENGE
    # =========================
    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">🎯 Identify Deterministic Origin</div>
    <div class="story-text">
Cari titik awal dari aliran
yang tidak mengikuti chaos sistem.

Bukan node terbesar.

Bukan node tersibuk.

Tapi node yang memulai pola paling stabil.
    </div>
    """, unsafe_allow_html=True)

    answer = st.text_input("Identify origin node of deterministic flow:")

    if st.button("Analyze"):

        node_input = answer.strip().upper()
        score = evaluate_start(node_input)

        if node_input == "NODE_7":

            st.success(
                "✔ Pattern Confidence High\n\n"
                "Deterministic chain detected:\n\n"
                "NODE_7 → NODE_14 → NODE_18 → NODE_22 → NODE_5 → EXTERNAL_GATEWAY\n\n"
                "Ini bukan transaksi.\n\n"
                "Ini sistem yang sedang mengarahkan dirinya sendiri."
            )

            st.session_state.current_stage = 6
            st.rerun()

        elif score >= 2:

            st.warning(
                "⚠ Partial Match\n\n"
                "Anda berada di dekat jalur yang benar.\n\n"
                "Tapi sistem ini tidak memiliki satu titik awal yang jelas."
            )

        else:

            st.error(
                "✖ No deterministic structure found.\n\n"
                "Sistem tetap terlihat acak.\n\n"
                "Tapi mungkin Anda belum melihat cukup dalam."
            )

    st.markdown('</div>', unsafe_allow_html=True)