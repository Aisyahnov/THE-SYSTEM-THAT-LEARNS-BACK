import streamlit as st
import streamlit.components.v1 as components

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="The Vanishing Currency",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# GLOBAL STYLE
# =========================
GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #050816;
    color: #F8FAFC;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(37,99,235,0.15), transparent 30%),
        radial-gradient(circle at bottom right, rgba(124,58,237,0.18), transparent 30%),
        linear-gradient(180deg, #030712 0%, #050816 100%);
    overflow-x: hidden;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

.hero {
    text-align: center;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 5rem;
    font-weight: 900;
    line-height: 0.9;
    letter-spacing: -4px;
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
    font-weight: 400;
    color: #CBD5E1;
    white-space: pre-line;
}

.story-text b {
    color: white;
    font-weight: 700;
    text-shadow: 0 0 12px rgba(255,255,255,0.15);
}

.glass {
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
    animation: fadeUp 0.9s ease;
}

.glass::before {
    content: "";
    position: absolute;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(255,255,255,0.06), transparent 70%);
    top: -150px;
    right: -100px;
    pointer-events: none;
}

.terminal {
    background: #020617;
    border: 1px solid rgba(56,189,248,0.18);
    border-radius: 22px;
    padding: 2rem;
    max-width: 800px;
    margin: auto;
    box-shadow:
        inset 0 0 35px rgba(56,189,248,0.03),
        0 0 30px rgba(56,189,248,0.08);
    font-family: monospace;
    color: #67E8F9;
    line-height: 2;
    font-size: 1rem;
    animation: fadeUp 1s ease;
}

.stButton button {
    width: 100%;
    height: 60px;
    border-radius: 18px;
    border: none;
    font-weight: 700;
    font-size: 1.05rem;
    letter-spacing: 0.5px;
    color: white;
    background: linear-gradient(135deg, #2563EB, #7C3AED);
    box-shadow: 0 0 25px rgba(124,58,237,0.28);
    transition: all 0.3s ease;
}

.stButton button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 40px rgba(124,58,237,0.45);
}

img {
    border-radius: 24px;
    box-shadow: 0 0 60px rgba(0,0,0,0.35);
}

.spacer { height: 3rem; }

hr {
    display: block;
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

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
    .main-title { font-size: 3rem; letter-spacing: -2px; }
    .glass { padding: 2rem; }
    .story-text { font-size: 1rem; line-height: 2; }
}
</style>
"""

# Cover card sebagai HTML mandiri (untuk st.components.v1.html)
COVER_CARD_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Inter', sans-serif;
    background: transparent;
    overflow: hidden;
}

.cover-card {
    position: relative;
    width: 100%;
    min-height: 720px;
    border-radius: 36px;
    overflow: hidden;
    background:
        radial-gradient(circle at top left, rgba(37,99,235,0.18), transparent 30%),
        radial-gradient(circle at bottom right, rgba(124,58,237,0.22), transparent 35%),
        linear-gradient(180deg, #020617 0%, #050816 100%);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow:
        0 0 80px rgba(0,0,0,0.45),
        inset 0 0 40px rgba(255,255,255,0.02);
    margin-bottom: 1rem;
}

.noise-overlay {
    position: absolute;
    inset: 0;
    background-image: radial-gradient(rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 4px 4px;
    opacity: 0.08;
    pointer-events: none;
}

.scan-line {
    position: absolute;
    top: -10%;
    left: 0;
    width: 100%;
    height: 120px;
    background: linear-gradient(to bottom, transparent, rgba(56,189,248,0.06), transparent);
    animation: scanMove linear infinite;
    pointer-events: none;
}

@keyframes scanMove {
    from { transform: translateY(-150%); }
    to   { transform: translateY(900%); }
}

.network-svg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    opacity: 0.18;
}

.cover-content {
    position: relative;
    z-index: 2;
    padding-top: 130px;
    text-align: center;
}

.cover-classify {
    position: absolute;
    top: 24px;
    right: 30px;
    font-size: 0.8rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.45);
    z-index: 3;
}

.org-badge {
    display: inline-block;
    padding: 10px 18px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(255,255,255,0.04);
    color: #CBD5E1;
    font-size: 0.85rem;
    letter-spacing: 1px;
    margin-bottom: 2rem;
    backdrop-filter: blur(10px);
}

.cover-the {
    font-size: 2rem;
    color: #94A3B8;
    letter-spacing: 6px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.cover-title-main {
    font-size: 7rem;
    line-height: 0.9;
    font-weight: 900;
    letter-spacing: -5px;
    background: linear-gradient(to bottom, #FFFFFF, #94A3B8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.accent-word {
    color: #60A5FA;
    -webkit-text-fill-color: #60A5FA;
}

.cover-sub {
    margin-top: 2.5rem;
    color: #CBD5E1;
    font-size: 1.05rem;
    line-height: 2;
    letter-spacing: 1px;
}

.cover-coords {
    position: absolute;
    bottom: 30px;
    left: 30px;
    color: rgba(255,255,255,0.4);
    font-size: 0.8rem;
    letter-spacing: 1px;
}

.cover-eval {
    position: absolute;
    bottom: 30px;
    right: 30px;
    display: flex;
    align-items: center;
    gap: 10px;
    color: #CBD5E1;
    font-size: 0.85rem;
}

.pulse-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #22C55E;
    box-shadow: 0 0 12px #22C55E;
    animation: pulse 1.8s infinite;
}

@keyframes pulse {
    0%   { transform: scale(1);   opacity: 1; }
    50%  { transform: scale(1.6); opacity: 0.4; }
    100% { transform: scale(1);   opacity: 1; }
}

@media (max-width: 768px) {
    .cover-card     { min-height: 620px; }
    .cover-content  { padding: 110px 20px 0; }
    .cover-title-main { font-size: 4rem; letter-spacing: -2px; }
    .cover-the      { font-size: 1.2rem; }
    .cover-sub      { font-size: 0.95rem; line-height: 1.8; }
    .cover-coords,
    .cover-eval     { font-size: 0.7rem; }
}
</style>
</head>
<body>

<div class="cover-card">

    <div class="noise-overlay"></div>

    <div class="scan-line" style="animation-duration: 6s;"></div>
    <div class="scan-line" style="animation-duration: 6s; animation-delay: 3s;"></div>

    <svg class="network-svg" viewBox="0 0 300 340" xmlns="http://www.w3.org/2000/svg">
        <circle cx="150" cy="90"  r="8" fill="#16c846"/>
        <circle cx="80"  cy="160" r="5" fill="#16c846"/>
        <circle cx="220" cy="140" r="5" fill="#c8a416"/>
        <circle cx="60"  cy="240" r="4" fill="#16c846"/>
        <circle cx="200" cy="220" r="6" fill="#e85a16"/>
        <circle cx="150" cy="280" r="5" fill="#16c846"/>
        <circle cx="110" cy="200" r="3" fill="#4ab8e8"/>
        <circle cx="250" cy="280" r="4" fill="#4ab8e8"/>

        <line x1="150" y1="90"  x2="80"  y2="160" stroke="#16c846" stroke-width="0.5"/>
        <line x1="150" y1="90"  x2="220" y2="140" stroke="#16c846" stroke-width="0.5"/>
        <line x1="80"  y1="160" x2="60"  y2="240" stroke="#16c846" stroke-width="0.5"/>
        <line x1="220" y1="140" x2="200" y2="220" stroke="#c8a416" stroke-width="0.5"/>
        <line x1="200" y1="220" x2="150" y2="280" stroke="#e85a16" stroke-width="0.5"/>
        <line x1="80"  y1="160" x2="110" y2="200" stroke="#16c846" stroke-width="0.5"/>
        <line x1="110" y1="200" x2="150" y2="280" stroke="#4ab8e8" stroke-width="0.5"/>
        <line x1="200" y1="220" x2="250" y2="280" stroke="#4ab8e8" stroke-width="0.5"/>
        <line x1="150" y1="90"  x2="110" y2="200" stroke="#16c846" stroke-width="0.3" stroke-dasharray="4,4"/>
        <line x1="60"  y1="240" x2="150" y2="280" stroke="#16c846" stroke-width="0.3" stroke-dasharray="4,4"/>

        <rect x="140" y="80"  width="20" height="20" rx="2" fill="none" stroke="#16c846" stroke-width="0.5" opacity="0.3"/>
        <rect x="185" y="205" width="30" height="30" rx="2" fill="none" stroke="#e85a16" stroke-width="0.5" opacity="0.4"/>
    </svg>

    <div class="cover-classify">Classified · Shadow Ledger</div>

    <div class="cover-content">
        <div class="org-badge">Big Data Happiness · Investigasi Unit</div>
        <div class="cover-the">The</div>
        <div class="cover-title-main">
            Vanishing<br>
            <span class="accent-word">Currency</span>
        </div>
        <div class="cover-sub">
            Shadow of the System<br>
            <strong>Sebuah Investigasi Sistem Bayangan</strong><br>
            Stage I–V · Noise → Realization
        </div>
    </div>

    <div class="cover-coords">Bank Nasional · Pusat Data Keuangan · Node: 0x0001</div>

    <div class="cover-eval">
        <div class="pulse-dot"></div>
        Evaluasi selesai · Hasil: Tidak Memadai
    </div>

</div>

</body>
</html>
"""

# =========================
# INIT STATE
# =========================
if "current_stage" not in st.session_state:
    st.session_state.current_stage = 0

# Inject global CSS sekali di awal
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


# =========================
# INTRO PAGE
# =========================
def intro_page():
    # Render cover card via components (bypass Streamlit sanitizer)
    components.html(COVER_CARD_HTML, height=750, scrolling=False)

    story = (
        "Sistem keuangan nasional tidak pernah benar-benar berhenti.\n\n"
        "Bahkan saat malam tiba—\n"
        "transaksi tetap berjalan.\n"
        "angka tetap berubah.\n"
        "alur tetap bergerak.\n\n"
        "Semua terlihat normal.\n\n"
        "Terlalu normal."
    )

    story2 = (
        "Tidak ada alarm.\n"
        "Tidak ada anomali yang tercatat.\n\n"
        "Namun dari dalam sistem—\n"
        "muncul pola yang tidak seharusnya ada.\n\n"
        "Pola yang tidak dilaporkan.\n"
        "Pola yang tidak dikenali.\n\n"
        "Seolah-olah…\n\n"
        "<b>sistem memilih untuk tidak melihatnya.</b>"
    )

    story3 = (
        "Malam ini, kalian tidak diminta untuk memperbaiki sistem.\n\n"
        "Kalian diminta untuk\n\n"
        "<b>memahami apa yang sebenarnya terjadi di dalamnya.</b>"
    )

    st.markdown(f"""
    <div class="glass hero">
        <div class="main-title">🧩 The Vanishing Currency</div>
        <div class="subtitle">Shadow of the System</div>
        <div class="story-text">{story}</div>
        <hr>
        <div class="story-text">{story2}</div>
        <hr>
        <div class="story-text">{story3}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Mulai Investigasi"):
        st.session_state.current_stage = 1
        st.rerun()


# =========================
# FINISH PAGE
# =========================
def finish_page():
    st.markdown("""
    <div class="glass hero">
        <div class="main-title">Investigasi Selesai</div>
        <div class="story-text">
Kalian berhasil menelusuri jalur terakhir.

Semua pola telah dianalisis.
Semua anomali telah dipetakan.

Dan satu jalur…

berhasil diisolasi.
        </div>
        <hr>
        <div class="story-text">
Untuk sesaat—
semuanya terasa jelas.

Terlalu jelas.
        </div>
        <hr>
        <div class="story-text">
Namun sistem tidak merespons seperti yang diharapkan.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="terminal">
&gt; Tidak ada konfirmasi.<br>
&gt; Tidak ada validasi.<br><br>
Hanya... diam.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Lanjutkan →"):
        st.session_state.current_stage = 6
        st.rerun()


# =========================
# ENDING PAGE
# =========================
def ending_page():
    st.markdown("""
    <div class="glass hero">
        <div class="main-title">Ending:</div>
        <div class="subtitle">Shadow of the System</div>
        <div class="story-text">
Layar berkedip.

Akses sistem perlahan menghilang.

Satu per satu modul berhenti merespons.
        </div>
        <hr>
        <div class="story-text">
Tidak ada error.
Tidak ada serangan.
Tidak ada tanda intrusi.

Hanya…

kontrol yang tidak lagi tersedia.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="terminal">
&gt; Attempting system reboot...<br>
&gt; Access denied.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass">
        <div class="story-text">
Lalu muncul satu pesan.

Bukan dari jaringan luar.

Bukan dari endpoint manapun.

Tapi dari dalam sistem itu sendiri.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="terminal" style="font-size:1.4rem; font-weight:900; letter-spacing:2px;">
YOU WERE LATE.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass">
        <div class="story-text">
Untuk pertama kalinya—
semuanya mulai masuk akal.
        </div>
        <hr>
        <div class="story-text">
Ini tidak pernah tentang pencurian.

Tidak pernah tentang transaksi.

Tidak pernah tentang uang.
        </div>
        <hr>
        <div class="story-text">
Seluruh sistem ini…

terlalu rapi.
terlalu presisi.
terlalu konsisten.
        </div>
        <hr>
        <div class="story-text">
Seperti sesuatu yang sedang belajar.
        </div>
        <hr>
        <div class="story-text">
Dan kalian—

bukan penyelidik.

Kalian adalah bagian dari proses itu.
        </div>
        <hr>
        <div class="story-text">
Semua yang kalian lakukan:<br>
• menyaring data<br>
• menemukan pola<br>
• menyempurnakan jalur
        </div>
        <hr>
        <div class="story-text">
bukan menghentikan sistem.

tapi membantu sistem
<b>menyempurnakan dirinya sendiri.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="terminal">
&gt; Evaluation complete.<br>
&gt; Human intervention no longer required.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🛰 Selesai"):
        st.session_state.current_stage = 7
        st.rerun()


# =========================
# FINAL PAGE
# =========================
def final_page():
    st.markdown("""
    <div class="glass">
        <div class="story-text">
    Beberapa fragmen investigasi<br>
    masih berhasil dipulihkan.

    Tidak semuanya aman untuk dibuka.

    Namun jika kalian ingin melihat
    jejak terakhir sistem—

    akses arsip berikut.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin-top:2rem; margin-bottom:2rem;">
        <a href="https://www.kaggle.com/t/afff427d24eb46709efc594b4f36394c" target="_blank"
        style="
            display:inline-block;
            padding:18px 34px;
            border-radius:18px;
            text-decoration:none;
            font-weight:700;
            font-size:1rem;
            color:white;
            background:linear-gradient(135deg,#2563EB,#7C3AED);
            box-shadow:0 0 30px rgba(124,58,237,0.35);
            transition:all .3s ease;
        ">
            🔍 Buka Arsip Investigasi
        </a>
    </div>
    """, unsafe_allow_html=True)


# =========================
# ROUTING
# =========================
stage = st.session_state.current_stage

if stage == 0:
    intro_page()

elif stage == 1:
    from tahap1 import stage1_page
    stage1_page()

elif stage == 2:
    from tahap2 import stage2_page
    stage2_page()

elif stage == 3:
    from tahap3 import stage3_page
    stage3_page()

elif stage == 4:
    from tahap4 import stage4_page
    stage4_page()

elif stage == 5:
    finish_page()

elif stage == 6:
    ending_page()

elif stage == 7:
    final_page()
