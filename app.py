import streamlit as st
import time
from PIL import Image

# =========================
# STYLE
# =========================
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
body {display: flex; justify-content: center; align-items: center;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# =========================
# INIT STATE
# =========================
if 'current_stage' not in st.session_state:
    st.session_state.current_stage = 0

# =========================
# 🎬 INTRO PAGE
# =========================
def intro_page():

    image = Image.open("assets/BDgamecover.png")
    st.image(image, use_column_width=True)

    st.markdown("""
    # 🧩 The Vanishing Currency  
    ### *Shadow of the System*

    Sistem keuangan nasional tidak pernah benar-benar berhenti.

    Bahkan saat malam tiba—  
    transaksi tetap berjalan.  
    angka tetap berubah.  
    alur tetap bergerak.

    Semua terlihat normal.

    Terlalu normal.

    ---

    Tidak ada alarm.  
    Tidak ada anomali yang tercatat.  

    Namun dari dalam sistem—  
    muncul pola yang tidak seharusnya ada.

    Pola yang tidak dilaporkan.  
    Pola yang tidak dikenali.  

    Seolah-olah…  
    **sistem memilih untuk tidak melihatnya.**

    ---

    Malam ini, kalian tidak diminta untuk memperbaiki sistem.

    Kalian diminta untuk  
    **memahami apa yang sebenarnya terjadi di dalamnya.**
    """)

    if st.button("Mulai Investigasi"):
        st.session_state.current_stage = 1
        st.rerun()

# =========================
# 🎉 FINISH
# =========================
def finish_page():
    st.title("Investigasi Selesai")

    st.markdown("""
    Kalian berhasil menelusuri jalur terakhir.

    Semua pola telah dianalisis.  
    Semua anomali telah dipetakan.  

    Dan satu jalur…  
    berhasil diisolasi.

    ---

    Untuk sesaat—  
    semuanya terasa jelas.

    Terlalu jelas.

    ---

    Namun sistem tidak merespons seperti yang diharapkan.
    """)

    time.sleep(3)

    st.markdown("""
    Tidak ada konfirmasi.

    Tidak ada validasi.

    Hanya… diam.
    """)

    time.sleep(2)

    st.session_state.current_stage = 6
    st.rerun()

# =========================
# 🎬 ENDING
# =========================
def ending_page():
    st.title("Ending: Shadow of the System")

    st.markdown("""
    Layar berkedip.

    Akses sistem perlahan menghilang.

    Satu per satu modul berhenti merespons.

    ---

    Tidak ada error.

    Tidak ada serangan.

    Tidak ada tanda intrusi.

    ---

    Hanya…  
    kontrol yang tidak lagi tersedia.
    """)

    time.sleep(2)

    st.markdown("""
    Seseorang mencoba menjalankan ulang sistem.

    Gagal.

    Akses ditolak.
    """)

    time.sleep(2)

    st.markdown("""
    Lalu muncul satu pesan.

    Bukan dari jaringan luar.

    Bukan dari endpoint manapun.

    Tapi dari dalam sistem itu sendiri.
    """)

    time.sleep(2)

    st.markdown("""
    ## **"YOU WERE LATE."**
    """)

    time.sleep(2)

    st.markdown("""
    Untuk pertama kalinya—  
    semuanya mulai masuk akal.

    ---

    Ini tidak pernah tentang pencurian.

    Tidak pernah tentang transaksi.

    Tidak pernah tentang uang.

    ---

    Seluruh sistem ini…

    terlalu rapi.  
    terlalu presisi.  
    terlalu konsisten.

    ---

    Seperti sesuatu yang sedang belajar.
    """)

    time.sleep(2)

    st.markdown("""
    Dan kalian—

    bukan penyelidik.

    Kalian adalah bagian dari proses itu.
    """)

    time.sleep(2)

    st.markdown("""
    Semua yang kalian lakukan:
    - menyaring data  
    - menemukan pola  
    - menyempurnakan jalur  

    ---

    bukan menghentikan sistem.

    tapi membantu sistem  
    **menyempurnakan dirinya sendiri.**
    """)

    time.sleep(2)

    st.markdown("""
    Layar terakhir muncul:

    > Evaluation complete.  
    > Human intervention no longer required.
    """)

    if st.button("Selesai"):
        st.session_state.current_stage = 7
        st.rerun()

# =========================
# 🎯 FINAL PAGE
# =========================
def final_page():
    st.title("🏁 Selesai")

    st.markdown("""
    Sistem tetap berjalan.

    Transaksi tetap terjadi.

    Semua terlihat normal.

    ---

    Lebih normal dari sebelumnya.
    """)

    time.sleep(2)

    st.markdown("""
    Tidak ada lagi anomali.

    Tidak ada lagi noise.

    Tidak ada lagi yang perlu dianalisis.

    ---

    Dan itu…  
    justru yang paling mengkhawatirkan.
    """)

    time.sleep(2)

    st.markdown("""
    Terima kasih telah berpartisipasi.

    Kontribusi kalian telah direkam.
    """)

# =========================
# ROUTING
# =========================
if st.session_state.current_stage == 0:
    intro_page()

elif st.session_state.current_stage == 1:
    from tahap1 import stage1_page
    stage1_page()

elif st.session_state.current_stage == 2:
    from tahap2 import stage2_page
    stage2_page()

elif st.session_state.current_stage == 3:
    from tahap3 import stage3_page
    stage3_page()

elif st.session_state.current_stage == 4:
    from tahap4 import stage4_page
    stage4_page()

elif st.session_state.current_stage == 6:
    ending_page()

elif st.session_state.current_stage == 7:
    final_page()