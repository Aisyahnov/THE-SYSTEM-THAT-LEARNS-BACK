def stage1_page():

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from PIL import Image

    # =========================
    # BANNER HTML (pengganti image1)
    # =========================
    st.markdown("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Barlow+Condensed:wght@700;900&display=swap');

      .s1-root {
        font-family: 'Space Mono', monospace;
        background: #030a06;
        border: 1px solid #0d2a14;
        border-radius: 4px;
        overflow: hidden;
        position: relative;
        width: 100%;
        user-select: none;
        margin-bottom: 1.5rem;
      }
      .s1-topbar {
        display: flex; align-items: center; justify-content: space-between;
        padding: 6px 14px; border-bottom: 0.5px solid #0d2a14; background: #020806;
      }
      .s1-topbar-left { display: flex; align-items: center; gap: 10px; }
      .s1-dot {
        width: 6px; height: 6px; border-radius: 50%; background: #16c846;
        animation: s1-pulse 2s ease-in-out infinite;
      }
      @keyframes s1-pulse {
        0%,100% { opacity:1; box-shadow: 0 0 0 0 #16c84640; }
        50% { opacity:0.5; box-shadow: 0 0 0 4px #16c84600; }
      }
      .s1-sys { font-size: 12px; letter-spacing: 3px; color: #16c846; opacity: 0.6; text-transform: uppercase; }
      .s1-classify {
        font-size: 12px; letter-spacing: 2px; color: #e85a16;
        border: 0.5px solid #e85a1680; padding: 2px 8px; text-transform: uppercase; opacity: 0.7;
      }
      .s1-main {
        position: relative; height: 260px; overflow: hidden;
        display: flex; align-items: stretch;
      }
      .s1-data-stream { position: absolute; inset: 0; pointer-events: none; overflow: hidden; }
      .s1-stream-col {
        position: absolute; top: 0; bottom: 0; display: flex;
        flex-direction: column; gap: 3px;
        animation: s1-stream-fall linear infinite; opacity: 0.07;
      }
      .s1-stream-char { font-size: 8px; color: #16c846; line-height: 1.2; }
      @keyframes s1-stream-fall {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(100%); }
      }
      .s1-scanline {
        position: absolute; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, transparent 0%, #16c84630 20%, #16c84660 50%, #16c84630 80%, transparent 100%);
        animation: s1-scan 3s linear infinite; pointer-events: none; z-index: 5;
      }
      @keyframes s1-scan {
        0% { top: -2px; }
        100% { top: 260px; }
      }
      .s1-left-bar {
        width: 3px; background: #16c846; flex-shrink: 0; position: relative; z-index: 2;
      }
      .s1-left-bar::after {
        content: ''; position: absolute; inset: 0;
        background: linear-gradient(180deg, transparent, #16c84690, transparent);
        animation: s1-bar-glow 2s ease-in-out infinite;
      }
      @keyframes s1-bar-glow {
        0%,100% { opacity: 0.3; }
        50% { opacity: 1; }
      }
      .s1-vert-label {
        writing-mode: vertical-rl; transform: rotate(180deg); font-size: 13px;
        letter-spacing: 3px; color: #16c846; opacity: 0.5; text-transform: uppercase;
        padding: 12px 6px; flex-shrink: 0; position: relative; z-index: 2;
        border-right: 0.5px solid #0d2a1480;
      }
      .s1-center {
        flex: 1; display: flex; flex-direction: column; justify-content: center;
        padding: 0 20px; position: relative; z-index: 2;
      }
      .s1-chapter {
        font-size: 15px; letter-spacing: 4px; color: #16c846; opacity: 0.55;
        text-transform: uppercase; margin-bottom: 5px;
        display: flex; align-items: center; gap: 8px;
      }
      .s1-chapter::before {
        content: ''; display: inline-block; width: 20px; height: 0.5px;
        background: #16c846; opacity: 0.5;
      }
      .s1-title {
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 72px;
        line-height: 0.88; letter-spacing: -1.5px; color: #eef5ef;
        text-transform: uppercase; margin-bottom: 6px;
      }
      .s1-title .s1-accent { color: #16c846; display: block; }
      .s1-meta {
        font-size: 12px; letter-spacing: 1.5px; color: #1a4a20;
        text-transform: uppercase; display: flex; align-items: center; gap: 8px;
      }
      .s1-meta-sep { color: #16c84440; }
      .s1-right {
        display: flex; flex-direction: column; align-items: flex-end;
        justify-content: center; padding: 0 18px; gap: 6px;
        position: relative; z-index: 2; border-left: 0.5px solid #0d2a1460;
      }
      .s1-hex {
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 72px;
        line-height: 1; color: #16c846; opacity: 0.06; letter-spacing: -3px;
      }
      .s1-badge {
        font-size: 12px; letter-spacing: 2px; padding: 3px 10px;
        border: 0.5px solid #16c84660; color: #16c846; opacity: 0.7;
        text-transform: uppercase; margin-top: -20px;
      }
      .s1-uptime { font-size: 12px; color: #0d3a14; letter-spacing: 1px; opacity: 0.8; }
      .s1-corners span { position: absolute; width: 10px; height: 10px; }
      .s1-tl { top: 8px; left: 8px; border-top: 1px solid #16c84440; border-left: 1px solid #16c84440; }
      .s1-tr { top: 8px; right: 8px; border-top: 1px solid #16c84440; border-right: 1px solid #16c84440; }
      .s1-bl { bottom: 8px; left: 8px; border-bottom: 1px solid #16c84440; border-left: 1px solid #16c84440; }
      .s1-br { bottom: 8px; right: 8px; border-bottom: 1px solid #16c84440; border-right: 1px solid #16c84440; }
      .s1-glitch-bar {
        position: absolute; height: 1px; left: 0; right: 0; background: #16c846;
        opacity: 0; animation: s1-glitch 7s ease-in-out infinite;
      }
      @keyframes s1-glitch {
        0%,100% { opacity: 0; }
        48% { opacity: 0; top: 60px; }
        50% { opacity: 0.15; top: 62px; }
        51% { opacity: 0; top: 58px; }
        52% { opacity: 0.08; top: 64px; }
        53% { opacity: 0; }
      }
      .s1-bottombar {
        display: flex; align-items: stretch;
        border-top: 0.5px solid #0d2a14; background: #020806;
      }
      .s1-ticker-wrap { flex: 1; overflow: hidden; position: relative; }
      .s1-ticker {
        display: flex; align-items: center; gap: 0;
        animation: s1-tick 18s linear infinite; white-space: nowrap; padding: 7px 0;
      }
      @keyframes s1-tick {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
      }
      .s1-tick-item {
        font-size: 12px; letter-spacing: 1.5px; color: #1a4a20; text-transform: uppercase;
        padding: 0 18px; border-right: 0.5px solid #0d2a14; flex-shrink: 0;
      }
      .s1-tick-item.hot { color: #16c846; opacity: 0.8; }
      .s1-tick-item.warn { color: #e85a16; opacity: 0.7; }
      .s1-status-right {
        display: flex; align-items: center; gap: 12px;
        padding: 6px 14px; border-left: 0.5px solid #0d2a14; flex-shrink: 0;
      }
      .s1-led {
        width: 5px; height: 5px; border-radius: 50%; background: #16c846;
        opacity: 0.8; animation: s1-led-blink 1.2s step-end infinite;
      }
      @keyframes s1-led-blink {
        0%,100% { opacity: 0.8; }
        50% { opacity: 0.2; }
      }
      .s1-ok { font-size: 8px; letter-spacing: 2px; color: #16c846; opacity: 0.6; text-transform: uppercase; }
    </style>

    <div class="s1-root">
      <div class="s1-topbar">
        <div class="s1-topbar-left">
          <div class="s1-dot"></div>
          <span class="s1-sys">SYS::FINCORE · NODE_A · MONITORING ACTIVE</span>
        </div>
        <span class="s1-classify">RESTRICTED</span>
      </div>

      <div class="s1-main">
        <div class="s1-data-stream" id="s1-stream"></div>
        <div class="s1-scanline"></div>
        <div class="s1-glitch-bar"></div>
        <div class="s1-corners">
          <span class="s1-tl"></span><span class="s1-tr"></span>
          <span class="s1-bl"></span><span class="s1-br"></span>
        </div>
        <div class="s1-left-bar"></div>
        <div class="s1-vert-label">Stage 01 · Noise</div>
        <div class="s1-center">
          <div class="s1-chapter">Chapter <strong style="color:#16c846;opacity:1;font-size:10px;">01</strong></div>
          <div class="s1-title">
            Gemuruh
            <span class="s1-accent">Dalam Diam</span>
          </div>
          <div class="s1-meta">
            <span>anomali terdeteksi</span>
            <span class="s1-meta-sep">·</span>
            <span>audit: [null]</span>
            <span class="s1-meta-sep">·</span>
            <span>signal: terlalu stabil</span>
          </div>
        </div>
        <div class="s1-right">
          <div class="s1-hex">01</div>
          <div class="s1-badge">Pattern-B</div>
          <div class="s1-uptime" id="s1-uptime">00:00:00</div>
        </div>
      </div>

      <div class="s1-bottombar">
        <div class="s1-ticker-wrap">
          <div class="s1-ticker">
            <span class="s1-tick-item hot">TXN 0x4F2A</span>
            <span class="s1-tick-item">ERR:NULL</span>
            <span class="s1-tick-item warn">MASK_ON</span>
            <span class="s1-tick-item">0.00042 BTC · SRC:??</span>
            <span class="s1-tick-item hot">PATTERN_B ████████████</span>
            <span class="s1-tick-item">STABLE</span>
            <span class="s1-tick-item warn">ANOMALY_FLAGGED</span>
            <span class="s1-tick-item">AUDIT_LOG: [EMPTY]</span>
            <span class="s1-tick-item hot">TXN 0x9C1D</span>
            <span class="s1-tick-item">NODE_ID: —</span>
            <span class="s1-tick-item warn">SIGNAL DETECTED</span>
            <span class="s1-tick-item">▓▓░░▓▓░░▓▓░░</span>
            <span class="s1-tick-item hot">TXN 0x4F2A</span>
            <span class="s1-tick-item">ERR:NULL</span>
            <span class="s1-tick-item warn">MASK_ON</span>
            <span class="s1-tick-item">0.00042 BTC · SRC:??</span>
            <span class="s1-tick-item hot">PATTERN_B ████████████</span>
            <span class="s1-tick-item">STABLE</span>
            <span class="s1-tick-item warn">ANOMALY_FLAGGED</span>
            <span class="s1-tick-item">AUDIT_LOG: [EMPTY]</span>
            <span class="s1-tick-item hot">TXN 0x9C1D</span>
            <span class="s1-tick-item">NODE_ID: —</span>
            <span class="s1-tick-item warn">SIGNAL DETECTED</span>
            <span class="s1-tick-item">▓▓░░▓▓░░▓▓░░</span>
          </div>
        </div>
        <div class="s1-status-right">
          <div class="s1-led"></div>
          <span class="s1-ok">ONLINE</span>
        </div>
      </div>
    </div>

    <script>
      (function() {
        var chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノ';
        var stream = document.getElementById('s1-stream');
        if (stream) {
          var cols = 28;
          for (var i = 0; i < cols; i++) {
            var col = document.createElement('div');
            col.className = 's1-stream-col';
            col.style.left = (i / cols * 100) + '%';
            col.style.animationDuration = (6 + Math.random() * 8) + 's';
            col.style.animationDelay = (-Math.random() * 10) + 's';
            col.style.opacity = (0.03 + Math.random() * 0.06).toString();
            for (var j = 0; j < 20; j++) {
              var c = document.createElement('div');
              c.className = 's1-stream-char';
              c.textContent = chars[Math.floor(Math.random() * chars.length)];
              col.appendChild(c);
            }
            stream.appendChild(col);
          }

          setInterval(function() {
            var allCols = stream.querySelectorAll('.s1-stream-col');
            var idx = Math.floor(Math.random() * allCols.length);
            var chars2 = allCols[idx].querySelectorAll('.s1-stream-char');
            chars2.forEach(function(c) {
              c.textContent = '01アイウエオカキクケコ'[Math.floor(Math.random()*11)];
            });
          }, 200);
        }

        var uptime = document.getElementById('s1-uptime');
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

    .hero {
        text-align: center;
    }

    .main-title {
        font-size: 4.5rem;
        font-weight: 900;
        line-height: 0.95;
        letter-spacing: -3px;
        margin-bottom: 1rem;

        background: linear-gradient(to bottom, #FFFFFF, #94A3B8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
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
    }

    .section-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 2rem;
        color: white;
    }

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

    /* =========================
    BEAUTIFUL DIVIDER
    ========================= */

    hr {
        border: none;
        height: 1px;
        width: 72%;
        margin: 3rem auto;

        background: linear-gradient(
            90deg,
            transparent 0%,
            rgba(255,255,255,0.08) 15%,
            rgba(148,163,184,0.45) 50%,
            rgba(255,255,255,0.08) 85%,
            transparent 100%
        );

        box-shadow:
            0 0 10px rgba(148,163,184,0.18),
            0 0 25px rgba(59,130,246,0.10);

        opacity: 1;
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================
    # LOAD DATA
    # =========================
    df = pd.read_csv("./data/stage1.csv")

    # =========================
    # HERO SECTION
    # =========================
    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">🧩 Stage 1</div>
        <div class="subtitle">Noise</div>
        <div class="story-text">
Malam itu, sistem keuangan nasional berjalan seperti biasa.

Tidak ada gangguan.
Tidak ada alarm.
Tidak ada alasan untuk khawatir.

Setidaknya… di permukaan.

<hr>
Transaksi mengalir seperti setiap hari.

Angka naik dan turun sesuai pola yang bisa diprediksi.

Semuanya terlihat stabil.

Terlalu stabil.

<hr>
Seorang analis membuka dashboard utama.

Ia berhenti.

Bukan karena ada error.

Tapi karena…

sesuatu terlihat terlalu "rapi".

<hr>
Dalam lautan data yang bergerak acak,
ada satu bagian yang tidak ikut bergerak.

Tidak mencolok.
Tidak mencurigakan.

Hanya… berbeda.

<hr>
Dan di sistem yang seharusnya tidak punya ingatan,

bagian itu terasa seperti sesuatu yang sedang menunggu untuk dikenali.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # GRAPH SECTION
    # =========================
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">📊 Grafik Transaksi</div>', unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(12, 6))

    for col in df.columns[1:]:
        ax.plot(df["time"], df[col], alpha=0.65, linewidth=1.5)

    ax.set_facecolor("#0B1120")
    fig.patch.set_facecolor("#0B1120")
    ax.tick_params(colors="white")

    for spine in ax.spines.values():
        spine.set_color("#334155")

    ax.grid(alpha=0.15)
    st.pyplot(fig)

    st.markdown('</div>', unsafe_allow_html=True)

    # =========================
    # ANALYSIS SECTION
    # =========================
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">🔍 Analisis Data</div>', unsafe_allow_html=True)

    option = st.radio(
        "Pilih alat analisis:",
        ["Heatmap Korelasi", "Lihat Data Penuh"],
        horizontal=True
    )

    if option == "Heatmap Korelasi":

        st.markdown("""
        <div class="story-text">
Tidak semua yang berbeda itu mencolok.

Kadang…
justru yang paling "tenang".
        </div>
        """, unsafe_allow_html=True)

        corr = df.drop(columns="time").corr()

        fig2, ax2 = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
        fig2.patch.set_facecolor("#0B1120")
        st.pyplot(fig2)

    else:

        st.markdown("""
        <div class="story-text">
Kadang jawabannya tidak muncul dari perbandingan…

tapi dari melihat semuanya sekaligus.
        </div>
        """, unsafe_allow_html=True)

        st.dataframe(df, use_container_width=True)

        st.info("💡 Tidak semua anomali terlihat seperti error.\n\nBeberapa justru terlihat seperti keteraturan.")

    st.markdown('</div>', unsafe_allow_html=True)

    # =========================
    # FINAL SECTION
    # =========================
    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)

    image3 = Image.open("assets/ascii.png")
    st.image(image3, use_column_width=True)

    st.markdown('<div class="section-title">🎯 Temukan Pesan Tersembunyi</div>', unsafe_allow_html=True)

    answer = st.text_input("Masukkan kata yang kamu temukan:")

    if st.button("Kirim Jawaban"):

        if answer.strip().upper() == "YOU ARE LATE":

            st.success("✅ Access Granted.")

            st.markdown("""
            <div class="terminal">
Layar berkedip.

Satu baris teks muncul.

YOU ARE LATE.

Tidak ada konteks.
Tidak ada sumber.

Dan untuk pertama kalinya—
sistem tidak mencoba menjelaskan apa pun.
            </div>
            """, unsafe_allow_html=True)

            st.session_state.current_stage = 2
            st.rerun()

        else:

            st.error("❌ Tidak tepat...")
            st.warning("Sistem mengulang analisis...")

    st.markdown('</div>', unsafe_allow_html=True)