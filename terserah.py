
import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm
import os
import base64

bg_path = os.path.join(os.path.dirname(__file__), "background.jpeg")

def load_background(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_base64 = load_background(bg_path)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Titan+One&family=Baloo+2:wght@400;600;700&display=swap');

{
    font-family: 'Baloo 2', sans-serif !important;
}

h1, h2 {
    font-family: 'Titan One', cursive !important;
    letter-spacing: 1px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
}}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700&display=swap');

{
    font-family: 'Baloo 2', sans-serif !important;
}

[data-testid="stSidebar"] {
    background: #4a90e2;
    border-right: 3px solid #ffd54f;
}

[data-testid="stSidebar"] * {
    color: #fffef9 !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2 {
    color: #ffeb3b !important;
    text-shadow: 1px 1px 0px #1565c0;
}

h1 {
    color: #ffeb3b !important;
    text-shadow: 2px 2px 0 #e53935;
}

h2 { color: #1565c0 !important; }
h3 { color: #1976d2 !important; }

p, li, label, span, div {
    color: #243447 !important;
}

.stTabs [data-baseweb="tab"] {
    background-color: #ffe082;
    color: #37474f;
    border-radius: 10px;
    padding: 6px 12px;
    margin-right: 6px;
    border: 2px solid #ffca28;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background-color: #ff5252 !important;
    color: white !important;
}

div.stButton > button {
    background-color: #ff5252;
    color: white;
    padding: 10px 20px;
    border-radius: 999px;
    border: none;
    font-weight: 700;
    box-shadow: 0 3px 0 #c62828;
    transition: 0.15s;
}

div.stButton > button:hover {
    transform: translateY(1px);
    box-shadow: 0 1px 0 #c62828;
}

div[role="radiogroup"] > label {
    border-radius: 999px;
    padding: 4px 10px;
    margin-bottom: 4px;
}

div[role="radiogroup"] > label:hover {
    background-color: rgba(255, 255, 255, 0.25) !important;
}

div[role="radiogroup"] > label > div:first-child {
    height: 14px;
    width: 14px;
    border-radius: 50%;
    border: 2px solid #ffeb3b !important;
    margin-right: 8px;
}

div[role="radiogroup"] > label[data-selected="true"] {
    background-color: rgba(255, 235, 59, 0.25) !important;
}

div[role="radiogroup"] > label[data-selected="true"] > div:first-child {
    background-color: #ffeb3b !important;
}

[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 12px;
    padding: 10px;
    border: 2px solid #ffd54f;
}

.stMetric {
    background-color: #fffde7;
    border-radius: 10px;
    border: 2px solid #ffe082;
    padding: 6px;
}

.stTextInput input,
.stNumberInput input {
    color: #ffffff !important;
}

.stTextArea textarea {
    color: #ffffff !important;
}

.stSelectbox div[data-baseweb="select"] * {
    color: #ffffff !important;
}

ul[role="listbox"] li {
    color: #000 !important; 
}

.stTextInput input::placeholder,
.stNumberInput input::placeholder,
.stTextArea textarea::placeholder {
    color: rgba(255, 255, 255, 0.7) !important;
}

.stNumberInput button svg {
    fill: #ffffff !important;
}

.stSelectbox [data-testid="stMarkdownContainer"] p {
    color: #ffffff !important;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.title("📊 Menu Utama")

main_menu = st.sidebar.radio(
    "Navigasi:",
    [
        "🏠 Home",
        "📄 Flowchart",
        "📚 Pilih Uji Statistik"
    ]
)

if main_menu == "📚 Pilih Uji Statistik":
    menu = st.sidebar.radio(
        "Pilih Jenis Uji Statistik:",
        [
            "Uji Proporsi 1 Sampel",
            "Uji Proporsi 2 Sampel",
            "Uji Rata-rata 1 Sampel (Z)",
            "Uji Rata-rata 1 Sampel (t)",
            "Uji Rata-rata 2 Sampel Independen (Z-test)",
            "Uji Kesamaan Varians (F-test)",
            "Uji Rata-rata 2 Sampel Independen (Pooled t-test)",
            "Uji Rata-rata 2 Sampel Independen (Welch t-test)",
            "Uji Rata-rata 2 Sampel Dependen (Paired t-test)"
        ]
    )
else:
    menu = None

st.title("Dashboard Pengujian Hipotesis")
st.write("Aplikasi Proyek Akhir Pemrograman Komputer — Dashboard Uji Statistik")

if main_menu == "🏠 Home":
    st.header("Selamat Datang 👋")
    st.write("""
        Dashboard ini dibuat untuk memenuhi proyek akhir mata kuliah **Pemrograman Komputer**.

        Anggota Kelompok:
        1. Mohamad Iqbal (140610250088)
        2. Meira Libna Rofilah (140610250056)
        3. Rebecca Manurung (140610250125)
        4. Anindi Syahlia (140610250101)
        5. Fitriyanti  Dwi Rahmadani (140610250026)
        6. Abdi Permata Buana (140610250113)
        7. Ardunt Kamil Upangga (140610250035)
        
        Di dalam aplikasi ini, Anda dapat melakukan berbagai macam **uji statistika parametrik**, lengkap dengan:
        - Penjelasan konsep
        - Rumus matematis
        - Contoh perhitungan
        - Perhitungan otomatis (coming soon)
        
        Silakan pilih menu di sebelah kiri untuk mulai.
    """)

elif main_menu == "📄 Flowchart":
    st.header("📄 Flowchart Pengujian Hipotesis");
    st.write("Berikut flowchart uji statistik yang dapat digunakan:")
    
    st.image("flowchart.jpg", caption="Flowchart Pengujian Hipotesis", use_container_width=True)
    

# ======================== 1) a. UJI PROPORSI 1 SAMPEL ========================

def load_uji_proporsi_1_sampel(title):
    st.header(title)
    
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📘 Penjelasan", "📐 Rumus", "📊 Contoh", "🧮 Perhitungan"]
    )

    with tab1:
        st.subheader("📘 Penjelasan Uji Proporsi 1 Sampel")
        st.info("Uji proporsi 1 sampel digunakan untuk menguji apakah proporsi pupulasi sama dengan proporsi tertentu.")

        st.subheader("📌 Hipotesis")
        st.markdown(r"""
        **Hipotesis:**

        - **H₀:** p = p₀  
        - **H₁:** p ≠ p₀ (uji dua arah)  
        - **H₁:** p > p₀ (uji kanan)  
        - **H₁:** p < p₀ (uji kiri)  
        """)

    with tab2:
        st.subheader("📐 Rumus Statistik Uji")
        st.latex(r"""
        Z_{hitung} = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}
        """)
        st.write("Keterangan:")
        st.markdown(r"""
        - $\bar{X}$ : Rata-rata sampel
        - $\mu_0$ : Rata-rata hipotesis (nilai acuan)
        - $\sigma$ : Simpangan baku populasi (diketahui)
        - $n$ : Jumlah sampel
        """)

        st.subheader("📌 Penentuan Nilai Kritis")
        st.markdown(r"""
        - Untuk **uji dua arah**: Tolak H₀ jika  
          \(|Z_{hitung}| > Z_{\alpha/2}\)
        
        - Untuk **uji satu arah kanan**: Tolak H₀ jika  
          \(Z_{hitung} > Z_{\alpha}\)
        
        - Untuk **uji satu arah kiri**: Tolak H₀ jika  
          \(Z_{hitung} < -Z_{\alpha}\)
        """)

    with tab3:
        st.subheader("🧮 Contoh Perhitungan")
        st.write("Misal: dari 100 mahasiswa, 40 lulus tepat waktu. Uji apakah proporsi = 0.5.")
        st.latex(r"Z = \frac{0.4 - 0.5}{\sqrt{0.5(1-0.5)/100}} = -2")

    with tab4:
        st.subheader("Perhitungan Uji Proporsi 1 Sampel")
        x = st.number_input("Jumlah sukses (x)", min_value=0, value=40)
        n = st.number_input("Jumlah sampel (n)", min_value=1, value=100)
        p0 = st.number_input("Proporsi hipotesis p0", min_value=0.0, max_value=1.0, value=0.5)
        alpha = st.number_input("Taraf signifikansi (α)", min_value=0.001, max_value=0.2, value=0.05)

        phat = x / n
        Z = (phat - p0) / np.sqrt(p0 * (1 - p0) / n)
        pvalue = 2 * (1 - norm.cdf(abs(Z)))

        st.write("### Hasil Perhitungan")
        st.write(f"- Proporsi sampel (p̂) = {phat:.4f}")
        st.write(f"- Statistik Z = {Z:.4f}")
        st.write(f"- p-value = {pvalue:.6f}")

        st.subheader("Kesimpulan")
        if pvalue < alpha:
            st.success(f"Tolak H0 karena p-value < α ({pvalue:.4f} < {alpha}).")
        else:
            st.info(f"Gagal menolak H0 karena p-value ≥ α ({pvalue:.4f} ≥ {alpha}).")


# ======================== 1) b. UJI PROPORSI 2 SAMPEL ========================

def load_uji_proporsi_2_sampel(title):
    st.header(title)
    
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📘 Penjelasan", "📐 Rumus", "📊 Contoh", "🧮 Perhitungan"]
    )

    with tab1:
        st.subheader("📘 Penjelasan Uji Proporsi 2 Sampel")
        st.info("Uji proporsi 2 sampel digunakan untuk membandingkan apakah dua proporsi populasi memiliki perbedaan signifikan.")

        st.subheader("📌 Hipotesis")
        st.markdown(r"""
        - **H₀:** p₁ = p₂  
        - **H₁:** p₁ ≠ p₂ (dua arah)
        - **H₁:** p₁ > p₂  
        - **H₁:** p₁ < p₂  
        """)

    with tab2:
        st.subheader("📐 Rumus Statistik Uji")
        st.latex(r"""
        Z = \frac{(\hat{p}_1 - \hat{p}_2)}
        {\sqrt{\hat{p}(1-\hat{p})(1/n_1 + 1/n_2)}}
        """)
        st.write("Keterangan:")
        st.markdown(r"""
        - $\hat{p}_1 = x_1 / n_1$  
        - $\hat{p}_2 = x_2 / n_2$  
        - $\hat{p}$ : Proporsi gabungan  
        """)

        st.subheader("📌 Nilai Kritis")
        st.markdown(r"""
        Kriteria keputusan sama seperti uji Z:
        
        - Dua arah: Tolak H₀ jika \(|Z| > Z_{\alpha/2}\)  
        - Arah kanan: Tolak H₀ jika \(Z > Z_{\alpha}\)  
        - Arah kiri: Tolak H₀ jika \(Z < -Z_{\alpha}\)
        """)

    with tab3:
        st.subheader("🧮 Contoh Perhitungan")
        st.write("Suatu penelitian dilakukan di daerah A terhadap 250 pemilih. Ternyata 150 pemilih menyatakan akan memilih calon C. Di daerah B, penelitian dilakukan terhadap 300 pemilih dan terdapat 162 yang akan memilih C. Adakah perbedaan yang nyata mengenai pemilihan calon C di antara kedua daerah itu? Gunakan taraf nyata 5% ")
        st.latex(r"""
        \hat{p} = \frac{x_1 + x_2}{n_1 + n_2}
        = \frac{150 + 162}{250 + 300}
        = 0.57
        """)

        st.latex(r"""
        Z = \frac{\hat{p}_1 - \hat{p}_2}
        {\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}
        """)

        st.latex(r"""
        Z = \frac{0.6 - 0.54}
        {\sqrt{0.57(1-0.57)\left(\frac{1}{250} + \frac{1}{300}\right)}}
        = 1.414
        """)

        st.success("Z = 1.414 → Karena |Z| < 1.96, maka **H₀ diterima**. Tidak terdapat perbedaan proporsi antara dua daerah.")

    with tab4:
        st.subheader("Perhitungan Uji Proporsi 2 Sampel")
        
        x1 = st.number_input("Jumlah sukses sampel 1 (x1)", min_value=0, value=150)
        n1 = st.number_input("Jumlah sampel 1 (n1)", min_value=1, value=200)
        x2 = st.number_input("Jumlah sukses sampel 2 (x2)", min_value=0, value=162)
        n2 = st.number_input("Jumlah sampel 2 (n2)", min_value=1, value=300)
        alpha = st.number_input("Taraf signifikansi (α)", min_value=0.001, max_value=0.2, value=0.05)
        
        p1 = x1 / n1
        p2 = x2 / n2
        
        p_pool = (x1 + x2) / (n1 + n2)
        
        Z = (p1 - p2) / np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
        
        pvalue = 2 * (1 - stats.norm.cdf(abs(Z)))

        st.write("### Hasil Perhitungan")
        st.write(f"- Proporsi 1 (p̂₁) = {p1:.4f}")
        st.write(f"- Proporsi 2 (p̂₂) = {p2:.4f}")
        st.write(f"- Proporsi gabungan (p̂) = {p_pool:.4f}")
        st.write(f"- Statistik Z = {Z:.4f}")
        st.write(f"- p-value = {pvalue:.6f}")
        
        st.subheader("Kesimpulan")
        
        if pvalue < alpha:
            st.success(
                f"Tolak H₀ karena p-value < α ({pvalue:.4f} < {alpha}). "
                "Artinya, kedua proporsi **berbeda secara signifikan**."
            )
        else:
            st.info(
                f"Gagal menolak H₀ karena p-value ≥ α ({pvalue:.4f} ≥ {alpha}). "
                "Artinya, **tidak ada perbedaan signifikan** antara kedua proporsi."
            )

# ======================== 2) a. UJI Z-TEST ======================== 

def load_z_test_1(title):
    st.header(title)

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📘 Penjelasan", "📐 Rumus", "📊 Contoh", "🧮 Perhitungan"]
    )

    with tab1:
        st.subheader("📘 Penjelasan")
        st.write(r"""
        **Uji Z satu sampel** digunakan untuk menguji apakah rata-rata populasi ($\mu$) 
        sama dengan nilai tertentu ($\mu_0$) ketika **varians populasi ($\sigma^2$) diketahui**.
        """)
        st.info(r"""
        **Syarat Penggunaan:**
        1. Data berdistribusi normal (atau $n > 30$).
        2. Varians populasi ($\sigma^2$) atau simpangan baku ($\sigma$) **diketahui**.
        3. Sampel diambil secara acak.
        """)

    with tab2:
        st.subheader("📐 Rumus Statistik Uji Z-Test")
        st.latex(r"""
        Z_{hitung} = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}
        """)
        st.write("Keterangan:")
        st.markdown(r"""
        - $\bar{X}$ : Rata-rata sampel
        - $\mu_0$ : Rata-rata hipotesis (nilai acuan)
        - $\sigma$ : Simpangan baku populasi (diketahui)
        - $n$ : Jumlah sampel
        """)

        st.subheader("Kriteria Pengujian (P-value)")
        st.write(r"""
        - **Tolak $H_0$** jika $P\text{-value} < \alpha$
        - **Gagal Tolak $H_0$** jika $P\text{-value} \ge \alpha$
        """)

    with tab3:
        st.subheader("🧮 Contoh Perhitungan")
        st.write(r"""
        Sebuah pabrik lampu mengklaim umur lampunya rata-rata **800 jam** ($\mu_0$). 
        Diketahui simpangan baku populasi adalah **40 jam** ($\sigma$). 
        Diambil sampel 9 lampu, rata-ratanya **780 jam** ($\bar{X}$). 
        Uji apakah rata-rata umur lampu tersebut berbeda dari klaim pabrik ($\alpha = 5\%$).
        """)
        
        st.markdown("**Perhitungan Manual:**")
        st.latex(r"Z = \frac{780 - 800}{40 / \sqrt{9}} = \frac{-20}{13.33} = -1.5")
        st.write("Karena ini uji dua arah, P-value = $2 \\times P(Z < -1.5) \\approx 0.1336$")
        st.write("Karena $0.1336 > 0.05$, maka **Gagal Tolak H0** (Klaim pabrik diterima).")

    with tab4:
        st.subheader("Kalkulator Uji Z 1 Sampel")
        
        st.write("### 1. Tentukan Parameter & Hipotesis")
        
        col1, col2 = st.columns(2)
        with col1:
            mu0 = st.number_input("Rata-rata Hipotesis ($\mu_0$)", value=0.0)
            sigma = st.number_input("Simpangan Baku Populasi ($\sigma$)", value=1.0, min_value=0.0001)
        
        with col2:
            alpha = st.selectbox(r"Taraf Signifikansi ($\alpha$)", [0.05, 0.01, 0.10], index=0)
            jenis_uji = st.selectbox("Jenis Hipotesis Alternatif ($H_1$)", 
                                     ["Dua Arah (≠)", "Satu Arah Kanan (>)", "Satu Arah Kiri (<)"])

        st.markdown("---")
        
        st.write("### 2. Input Data Sampel")
        input_metode = st.radio("Pilih metode input:", ["Ketik Manual"], horizontal=True)
        
        data_sampel = []
        
        if input_metode == "Ketik Manual":
            input_text = st.text_area("Masukkan data (pisahkan dengan koma)", "10, 12, 11, 14, 13")
            if input_text:
                try:
                    data_sampel = np.array([float(x.strip()) for x in input_text.split(",") if x.strip()])
                except ValueError:
                    st.error("Format salah! Pastikan hanya memasukkan angka dipisahkan koma.")

        if st.button("Jalankan Uji Hipotesis 🚀"):
            if len(data_sampel) == 0:
                st.error("Data kosong! Masukkan data terlebih dahulu.")
            else:
                n = len(data_sampel)
                x_bar = np.mean(data_sampel)
                
                se = sigma / np.sqrt(n)
                z_score = (x_bar - mu0) / se
                
                if jenis_uji == "Dua Arah (≠)":
                    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
                    tanda_h1 = "≠"
                    ket_hipotesis = f"H0: μ = {mu0} vs H1: μ ≠ {mu0}"
                elif jenis_uji == "Satu Arah Kanan (>)":
                    p_value = 1 - stats.norm.cdf(z_score)
                    tanda_h1 = ">"
                    ket_hipotesis = f"H0: μ ≤ {mu0} vs H1: μ > {mu0}"
                else:
                    p_value = stats.norm.cdf(z_score)
                    tanda_h1 = "<"
                    ket_hipotesis = f"H0: μ ≥ {mu0} vs H1: μ < {mu0}"

                st.success("✅ Perhitungan Selesai")
                
                st.write("#### Hasil Analisis")
                st.markdown(f"**Hipotesis:** {ket_hipotesis}")
                
                col_res1, col_res2, col_res3 = st.columns(3)
                col_res1.metric("Rata-rata Sampel (x̄)", f"{x_bar:.4f}")
                col_res2.metric("Z-Hitung", f"{z_score:.4f}")
                col_res3.metric("P-Value", f"{p_value:.5f}")
                
                st.write("#### Kesimpulan")
                if p_value < alpha:
                    st.error(f"**Keputusan: Tolak H0**")
                    st.write(f"Karena P-value ({p_value:.5f}) < Alpha ({alpha}), maka ada cukup bukti untuk menyatakan bahwa rata-rata populasi **{tanda_h1} {mu0}**.")
                else:
                    st.warning(f"**Keputusan: Gagal Tolak H0**")
                    st.write(f"Karena P-value ({p_value:.5f}) ≥ Alpha ({alpha}), maka **tidak ada cukup bukti** untuk menyatakan rata-rata populasi berbeda dari {mu0}.")


# ======================== 2) b. UJI T-TEST ======================== 

def load_t_test_1_sample(title):
    st.header(title)
    
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📘 Penjelasan", "📐 Rumus", "📊 Contoh", "🧮 Perhitungan"]
    )

    with tab1:
        st.subheader("Konsep Uji t 1 Sampel")
        st.write(r"""
        **Uji t satu sampel** digunakan ketika kita ingin menguji rata-rata populasi ($\mu$) 
        tetapi **varians populasi ($\sigma^2$) tidak diketahui**. 
        Sebagai gantinya, kita menggunakan varians sampel ($s^2$).
        """)
        st.info("""
        **Syarat:**
        1. Varians populasi tidak diketahui.
        2. Sampel diambil secara acak.
        3. Data berdistribusi normal.
        """)

        st.subheader("📌 Hipotesis")
        st.markdown(r"""
        - **H₀:** μ = μ₀  
        - **H₁:** μ ≠ μ₀  
        - **H₁:** μ > μ₀  
        - **H₁:** μ < μ₀  
        """)

    with tab2:
        st.subheader("Rumus Statistik Uji t")
        st.latex(r"t_{hitung} = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}")
        st.write("Derajat Bebas ($df$):")
        st.latex(r"df = n - 1")
        st.write("Keterangan:")
        st.markdown(r"""
        - $\bar{X}$: Rata-rata sampel
        - $\mu_0$: Rata-rata hipotesis
        - $s$: Standar deviasi sampel
        - $n$: Jumlah sampel
        """)

        st.subheader("📌 Nilai Kritis")
        st.markdown(r"""
        Gunakan distribusi t dengan \(df = n-1\):
        
        - Dua arah: Tolak H₀ jika \(|t| > t_{\alpha/2, df}\)
        - Arah kanan: Tolak H₀ jika \(t > t_{\alpha, df}\)
        - Arah kiri: Tolak H₀ jika \(t < -t_{\alpha, df}\)
        """)

    with tab3:
        st.subheader("Contoh Kasus")
        st.write(r"""
        Seorang peneliti menduga rata-rata berat badan mahasiswa adalah **60 kg**. 
        Diambil sampel 5 orang: **62, 65, 58, 61, 64**. 
        Uji apakah rata-rata berat badan berbeda dari 60 kg ($\alpha=0.05$).
        """)
        st.markdown("**Langkah:**")
        st.write("1. Rata-rata ($X$) = 62")
        st.write("2. Standar Deviasi ($s$) = 2.738")
        st.write("3. $t_{hitung} = (62 - 60) / (2.738 / \sqrt{5}) = 1.633$")

    with tab4:
        st.subheader("Kalkulator Uji t")
        
        st.write("#### 1. Tentukan Hipotesis")
        col1, col2 = st.columns(2)
        with col1:
            mu0 = st.number_input(r"Nilai Acuan ($\mu_0$)", value=0.0)
        with col2:
            alpha = st.selectbox(r"Taraf Signifikansi ($\alpha$)", [0.05, 0.01, 0.10])
            jenis_uji = st.selectbox("Jenis Uji ($H_1$)", ["Dua Arah (≠)", "Satu Arah Kanan (>)", "Satu Arah Kiri (<)"])

        st.write("#### 2. Input Data Sampel")
        input_metode = st.radio("Pilih metode input:", ["Ketik Manual"], horizontal=True)
        
        data_sampel = []
        input_text = "" 

        if input_metode == "Ketik Manual":
            input_text = st.text_area("Masukkan data (pisahkan dengan koma)", "62, 65, 58, 61, 64")
            if input_text:
                try:
                    data_sampel = np.array([float(x.strip()) for x in input_text.split(",") if x.strip()])
                except ValueError:
                    st.error("Format salah! Pastikan hanya memasukkan angka dipisahkan koma.")

        if st.button("Mulai Perhitungan 🚀"):
            try:
                if input_metode == "Ketik Manual" and len(data_sampel) == 0 and input_text:
                     try:
                        data_sampel = np.array([float(x.strip()) for x in input_text.split(",") if x.strip()])
                     except:
                        pass 

                if len(data_sampel) == 0:
                     st.error("Data kosong atau belum diinput dengan benar.")
                else:
                    n = len(data_sampel)
                    x_bar = np.mean(data_sampel)
                    s = np.std(data_sampel, ddof=1)
                    df = n - 1
                    se = s / np.sqrt(n)
                    t_hitung = (x_bar - mu0) / se
                    
                    if jenis_uji == "Dua Arah (≠)":
                        p_value = 2 * (1 - stats.t.cdf(abs(t_hitung), df))
                        tanda = "≠"
                    elif jenis_uji == "Satu Arah Kanan (>)":
                        p_value = 1 - stats.t.cdf(t_hitung, df)
                        tanda = ">"
                    else:
                        p_value = stats.t.cdf(t_hitung, df)
                        tanda = "<"
                    
                    st.markdown("---")
                    st.success("✅ Hasil Perhitungan")
                    col_A, col_B, col_C = st.columns(3)
                    col_A.metric(r"Rata-rata ($\bar{X}$)", f"{x_bar:.4f}")
                    col_B.metric(r"Std. Deviasi ($s$)", f"{s:.4f}")
                    col_C.metric(r"Derajat Bebas ($df$)", f"{df}")
                    st.metric(r"t-hitung ($t$)", f"{t_hitung:.4f}")
                    st.metric("P-value", f"{p_value:.5f}")
                    
                    st.write("#### Kesimpulan Hipotesis")
                    if p_value < alpha:
                        st.error(f"**Tolak H0**")
                        st.write(f"Karena P-value ({p_value:.5f}) < Alpha ({alpha}), maka rata-rata populasi **{tanda} {mu0}**.")
                    else:
                        st.warning(f"**Gagal Tolak H0**")
                        st.write(f"Karena P-value ({p_value:.5f}) ≥ Alpha ({alpha}), maka tidak cukup bukti rata-rata berbeda.")
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
                

# ======================== 3) UJI Z-TEST ======================== 

def load_z_test_2_sample_simple(title):
    st.header(title)
    
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📘 Penjelasan", "📐 Rumus", "📊 Contoh", "🧮 Perhitungan"]
    )

    with tab1:
        st.subheader("📘 Penjelasan")
        st.write("""
        Uji Z Dua Sampel Independen adalah uji hipotesis statistik yang digunakan untuk menentukan apakah terdapat **perbedaan signifikan** antara rata-rata ($\mu$) dari **dua populasi yang berbeda**, berdasarkan data dari dua sampel independen.
        """)
        st.info("""
        **Asumsi Z-test 2 Sampel Independen:**
        * **Sampel Independen:** Pengamatan di satu sampel tidak memengaruhi pengamatan di sampel lain.
        * **Varians Populasi Diketahui:** Nilai varians populasi ($\sigma_1^2$ dan $\sigma_2^2$) harus sudah diketahui.
        * **Distribusi Normal:** Populasi didistribusikan secara normal **atau** ukuran sampel cukup besar ($n_1, n_2 \ge 30$).
        """)
        
        st.subheader("Rumusan Hipotesis")
        
        st.markdown("**1. Dua Arah (Two-Tailed Test):**")
        st.latex(r"H_0: \mu_1 = \mu_2")
        st.latex(r"H_1: \mu_1 \neq \mu_2")

        st.markdown("**2. Satu Arah (One-Tailed Test):**")
        col_left, col_right = st.columns(2)
        with col_left:
            st.markdown("Ekor Kiri ($\mu_1$ lebih kecil dari $\mu_2$)")
            st.latex(r"H_0: \mu_1 \ge \mu_2")
            st.latex(r"H_1: \mu_1 < \mu_2")
        with col_right:
            st.markdown("Ekor Kanan ($\mu_1$ lebih besar dari $\mu_2$)")
            st.latex(r"H_0: \mu_1 \le \mu_2")
            st.latex(r"H_1: \mu_1 > \mu_2")

    with tab2:
        st.subheader ("📐 Rumus Statistik Uji Z-Test")
        st.latex(r"""
        Z = \frac{(\bar{X}_1 - \bar{X}_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}
        """)
        st.subheader("Keterangan")
        st.markdown(r"""
        * $Z$ : Nilai Statistik Uji Z
        
        * $\bar{X}_1, \bar{X}_2$ : Rata-rata Sampel
        
        * $\sigma_1^2, \sigma_2^2$ : Varians Populasi (Diketahui)
        
        * $n_1, n_2$ : Ukuran Sampel
        """)
        
        st.subheader("Kriteria Pengambilan Keputusan")
        st.write("Keputusan untuk menolak atau gagal menolak $H_0$ dapat diambil menggunakan dua metode:")
        
        st.markdown("#### 1. Kriteria Nilai Kritis ($Z$-Kritis)")
        st.markdown("""
        * **TOLAK $H_0$** jika nilai $|Z_{\\text{hitung}}|$ berada di luar area penerimaan (yaitu, $|Z_{\\text{hitung}}| > Z_{\\text{tabel}}|$).
        * **GAGAL TOLAK $H_0$** jika nilai $|Z_{\\text{hitung}}|$ berada di dalam area penerimaan (yaitu, $|Z_{\\text{hitung}}| \le Z_{\\text{tabel}}|$).
        """)
        
        st.markdown("#### 2. Kriteria $P$-Value")
        st.markdown(r"""
        * **TOLAK $H_0$** jika **$P$-value $< \alpha$** (Tingkat signifikansi).
        * **GAGAL TOLAK $H_0$** jika **$P$-value $\ge \alpha$**.
        """)

    with tab3:
        st.subheader("🧮 Contoh Perhitungan Uji Z Dua Sampel")
        
        x_bar_1 = 125
        x_bar_2 = 120
        sigma_1_sq = 64
        sigma_2_sq = 60
        n_1 = 50
        n_2 = 55
        alpha = 0.05
        se_sq_contoh = (64 / 50) + (60 / 55)
        se_contoh = np.sqrt(se_sq_contoh)
        z_contoh = (125 - 120) / se_contoh
        p_value_contoh = 2 * (1 - stats.norm.cdf(abs(z_contoh)))
        
        st.write(r"""
        Sebuah perusahaan ingin membandingkan efektivitas dua metode pelatihan karyawan. 
        **Uji Hipotesis:** Apakah ada **perbedaan** skor rata-rata yang signifikan ($\mathbf{\alpha = 0.05}$)?
        
        * $H_0: \mu_1 = \mu_2$
        * $H_1: \mu_1 \neq \mu_2$
        """)
        
        st.markdown("##### 📝 Data Sampel")
        col_data1, col_data2 = st.columns(2)
        
        with col_data1:
            st.write("**Metode A (Sampel 1):**")
            st.write(f"Ukuran Sampel ($n_1$): **{n_1}**")
            st.write(r"Rata-rata Sampel ($\bar{X}_1$): **125**")
            st.write(r"Varians Populasi ($\sigma_1^2$): **64**")
            
        with col_data2:
            st.write("**Metode B (Sampel 2):**")
            st.write(f"Ukuran Sampel ($n_2$): **{n_2}**")
            st.write(r"Rata-rata Sampel ($\bar{X}_2$): **120**")
            st.write(r"Varians Populasi ($\sigma_2^2$): **60**")
        
        st.markdown("---")
        
        st.markdown("##### 📊 Hasil Uji (Dua Arah)")
        
        col_res_z, col_res_p, col_res_zkrit = st.columns(3)
        col_res_z.metric("Z-Hitung", f"{z_contoh:.3f}")
        col_res_p.metric("P-Value", f"{p_value_contoh:.6f}")
        col_res_zkrit.metric("Z-Kritis", f"±{stats.norm.ppf(1 - alpha/2):.4f}")
        
        st.write("#### Keputusan dan Kesimpulan")
        
        if p_value_contoh < alpha:
            st.error(f"**Keputusan: Tolak H0**")
            st.write(f"**Metode P-Value:** Karena P-value ({p_value_contoh:.5f}) < Alpha ({alpha}), maka ada cukup bukti untuk menyatakan bahwa rata-rata populasi **berbeda** signifikan.")
            st.write(f"**Metode Nilai Kritis:** Z-Hitung **{z_contoh:.4f}** berada di area penolakan, menguatkan keputusan Tolak H0.")
        else:
            st.warning(f"**Keputusan: Gagal Tolak H0**")
            st.write(f"**Metode P-Value:** Karena P-value ({p_value_contoh:.5f}) $\\ge$ Alpha ({alpha}), maka **tidak ada cukup bukti** untuk menyatakan perbedaan signifikan antara rata-rata populasi.")
            st.write(f"**Metode Nilai Kritis:** Z-Hitung **{z_contoh:.4f}** berada di area penerimaan, menguatkan keputusan Gagal Tolak H0.")

    with tab4:
        st.subheader("Kalkulator Uji Z 2 Sampel")
        
        st.markdown("### 1.  Input Parameter Uji")
        
        col1, col2 = st.columns(2)
        with col1:
            variance1 = st.number_input(r"Varians Populasi 1 ($\sigma_1^2$)", value=100.0, min_value=0.0001, format="%.4f", key='var1_calc')
            alpha_input = st.selectbox(r"Taraf Signifikansi ($\alpha$)", [0.05, 0.01, 0.10], index=0, key='alpha_calc')
        
        with col2:
            variance2 = st.number_input(r"Varians Populasi 2 ($\sigma_2^2$)", value=81.0, min_value=0.0001, format="%.4f", key='var2_calc')
            jenis_uji = st.selectbox("Jenis Hipotesis Alternatif ($H_1$)", 
                                     ["Dua Arah (≠)", "Satu Arah Kanan (>)", "Satu Arah Kiri (<)"], key='jenis_uji_calc')

        st.markdown("---")
        
        st.markdown("### 2. Input Data Sampel")
        input_metode = st.radio("Pilih metode input:", ["Ketik Manual"], horizontal=True, key='input_method')
        
        data1 = np.array([])
        data2 = np.array([])
        
        if input_metode == "Ketik Manual":
            col_man1, col_man2 = st.columns(2)
            with col_man1:
                input_text1 = st.text_area("Data Sampel 1 (pisahkan dengan koma)", "88, 79, 90, 83, 85, 86, 92, 75, 78, 84", key='text1_calc')
                if input_text1:
                    try:
                        data1 = np.array([float(x.strip()) for x in input_text1.replace(';', ',').split(",") if x.strip()])
                    except ValueError:
                        st.error("Format Sampel 1 salah! Masukkan hanya angka dipisahkan koma atau titik koma.")
            
            with col_man2:
                input_text2 = st.text_area("Data Sampel 2 (pisahkan dengan koma)", "75, 82, 78, 85, 81, 79, 83, 76, 74, 80", key='text2_calc')
                if input_text2:
                    try:
                        data2 = np.array([float(x.strip()) for x in input_text2.replace(';', ',').split(",") if x.strip()])
                    except ValueError:
                        st.error("Format Sampel 2 salah! Masukkan hanya angka dipisahkan koma atau titik koma.")

        st.markdown("---")
        if st.button("Jalankan Uji Hipotesis 🚀", key='btn_z_test_calc'):
            
            if len(data1) == 0 or len(data2) == 0:
                st.error("Data sampel 1 atau 2 kosong atau tidak valid! Masukkan data terlebih dahulu.")
            else:
                D0 = 0.0

                n1 = len(data1)
                x_bar1 = np.mean(data1)
                n2 = len(data2)
                x_bar2 = np.mean(data2)
                
                # Cek ukuran sampel
                if n1 < 30 or n2 < 30:
                    st.warning(f"**Peringatan:** Ukuran sampel kecil (n1={n1}, n2={n2}). Pastikan populasi berdistribusi Normal, jika tidak, Z-test mungkin kurang tepat. T-test lebih disarankan jika varians populasi **tidak** diketahui.")
                
                # Hitung Statistik Uji Z
                se_squared = (variance1 / n1) + (variance2 / n2)
                se = np.sqrt(se_squared)
                
                z_score = (x_bar1 - x_bar2 - D0) / se
                
                if jenis_uji == "Dua Arah (≠)":
                    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
                    tanda_h1 = "≠"
                    ket_hipotesis = r"H0: \mu_1 = \mu_2 \quad vs \quad H1: \mu_1 \neq \mu_2"
                    
                elif jenis_uji == "Satu Arah Kanan (>)":
                    p_value = 1 - stats.norm.cdf(z_score)
                    tanda_h1 = ">"
                    ket_hipotesis = r"H0: \mu_1 \le \mu_2 \quad vs \quad H1: \mu_1 > \mu_2"
                    
                else: # Satu Arah Kiri (<)
                    p_value = stats.norm.cdf(z_score)
                    tanda_h1 = "<"
                    ket_hipotesis = r"H0: \mu_1 \ge \mu_2 \quad vs \quad H1: \mu_1 < \mu_2"
                
                # 2. Hitung Z-Kritis
                if jenis_uji == "Dua Arah (≠)":
                    z_kritis_pos = stats.norm.ppf(1 - (alpha_input / 2))
                    z_kritis_tampil = f"±{z_kritis_pos:.4f}"
                    
                elif jenis_uji == "Satu Arah Kanan (>)":
                    z_kritis_pos = stats.norm.ppf(1 - alpha_input)
                    z_kritis_tampil = f"+{z_kritis_pos:.4f}"
                    
                else:
                    z_kritis_neg = stats.norm.ppf(alpha_input)
                    z_kritis_tampil = f"{z_kritis_neg:.4f}"
                

                st.markdown("### 📊 Hasil Perhitungan")
                st.success("✅ Perhitungan Selesai")
                
                st.markdown("#### 1. Hipotesis")
                st.latex(ket_hipotesis)
                
                st.markdown("#### 2. Statistik Deskriptif Sampel")
                
                col_res_n, col_res_xbar = st.columns(2)
                col_res_n.metric("Jml. Sampel 1 ($n_1$)", f"{n1}")
                col_res_xbar.metric(r"Rata-rata Sampel 1 ($\bar{{x}}_1$)", f"{x_bar1:.4f}")

                col_res_n2, col_res_xbar2 = st.columns(2)
                col_res_n2.metric("Jml. Sampel 2 ($n_2$)", f"{n2}")
                col_res_xbar2.metric(r"Rata-rata Sampel 2 ($\bar{{x}}_2$)", f"{x_bar2:.4f}")
                
                st.markdown("#### 3. Hasil Uji Statistik")
                
                col_res_z_hit, col_res_p, col_res_z_krit = st.columns(3)
                col_res_z_hit.metric("Z-Hitung", f"{z_score:.4f}")
                col_res_p.metric("P-Value", f"{p_value:.5f}")
                col_res_z_krit.metric("Z-Kritis", z_kritis_tampil)
                
                st.markdown("###### Formula Uji Z")
                st.latex(r"Z = \frac{(\bar{X}_1 - \bar{X}_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}")
                
                
                st.markdown("#### 4. Keputusan dan Kesimpulan")
                
                if p_value < alpha_input:
                    st.error(f"**Keputusan: Tolak H0**")
                    st.write(f"**Metode P-Value:** Karena P-value ({p_value:.5f}) < Alpha ({alpha_input}), maka ada cukup bukti untuk menyatakan bahwa rata-rata populasi **berbeda** (atau $\mu_1$ {tanda_h1} $\mu_2$).")
                    st.write(f"**Metode Nilai Kritis:** Z-Hitung **{z_score:.4f}** berada di area penolakan, menguatkan keputusan Tolak H0.")
                else:
                    st.warning(f"**Keputusan: Gagal Tolak H0**")
                    st.write(f"**Metode P-Value:** Karena P-value ({p_value:.5f}) $\\ge$ Alpha ({alpha_input}), maka **tidak ada cukup bukti** untuk menyatakan perbedaan signifikan antara rata-rata populasi.")
                    st.write(f"**Metode Nilai Kritis:** Z-Hitung **{z_score:.4f}** berada di area penerimaan, menguatkan keputusan Gagal Tolak H0.")


# ======================== 4) UJI KESAMAAN VARIANS (F-TEST) ======================== 

def load_f_test(title):
    st.header(title)

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📘 Penjelasan", "📐 Rumus", "📊 Contoh", "🧮 Perhitungan"]
    )

    with tab1:
        st.subheader("📘 Penjelasan")
        st.write("""
        **Uji F (F-test)** digunakan untuk menguji apakah **dua varians populasi sama atau berbeda**.
        
        Biasanya dilakukan sebelum uji t dua sampel,
        untuk menentukan apakah memakai **Pooled t-test** atau **Welch t-test**.
        """)

        st.info("""
        **Asumsi F-test:**
        1. Data dari dua sampel berdistribusi normal.
        2. Dua sampel independen.
        """)

        st.subheader("📌 Hipotesis")
        st.markdown(r"""
        - **H₀:** σ₁² = σ₂²  
        - **H₁:** σ₁² ≠ σ₂²
        """)

    with tab2:
        st.subheader("📐 Rumus Statistik Uji")
        
        st.latex(r"""
        F = \frac{S_1^2}{S_2^2}
        """)

        st.write("Keterangan:")
        st.markdown("""
        - $S_1^2$ : Varians sampel 1  
        - $S_2^2$ : Varians sampel 2  
        - df1 = $n_1 - 1$  
        - df2 = $n_2 - 1$  
        """)

        st.subheader("📌 Nilai Kritis F")
        st.markdown(r"""
        Nilai kritis diperoleh dari distribusi **F(df1, df2)**:
        
        - Tolak H₀ jika:  
          \(F_{hitung} > F_{\alpha/2}(df1, df2)\)  
          atau  
          \(F_{hitung} < F_{1-\alpha/2}(df1, df2)\)
        """)

        st.warning("Catatan: varians yang lebih besar biasanya ditempatkan sebagai pembilang, agar F ≥ 1.")

    with tab3:
        st.subheader("🧮 Contoh Perhitungan")

        st.write("""
        Misalkan data panjang baja dari dua pabrik sebagai berikut:
        """)

        data1 = [7, 9, 12, 10, 11]
        data2 = [8, 8, 9, 7, 6]

        df = pd.DataFrame({
            "Pabrik A": data1,
            "Pabrik B": data2
        })

        st.dataframe(df)

        var1 = np.var(data1, ddof=1)
        var2 = np.var(data2, ddof=1)

        st.write(f"Varians Pabrik A = {var1:.3f}")
        st.write(f"Varians Pabrik B = {var2:.3f}")
        st.write(f"Rasio F = {var1/var2:.3f}")

    with tab4:
        st.subheader("Kalkulator F-Test")

        col1, col2 = st.columns(2)

        with col1:
            input1 = st.text_area("Data Sampel 1")

        with col2:
            input2 = st.text_area("Data Sampel 2")

        alpha = st.selectbox("Alpha", [0.05, 0.01, 0.10])

        if st.button("Hitung F-test"):
            try:
                x1 = np.array([float(x) for x in input1.split(",")])
                x2 = np.array([float(x) for x in input2.split(",")])

                var1 = np.var(x1, ddof=1)
                var2 = np.var(x2, ddof=1)

                F = var1 / var2 if var1 >= var2 else var2 / var1

                df1 = len(x1) - 1
                df2 = len(x2) - 1

                p_value = 1 - stats.f.cdf(F, df1, df2)

                colA, colB, colC = st.columns(3)
                colA.metric("F-hitung", f"{F:.4f}")
                colB.metric("df1, df2", f"{df1}, {df2}")
                colC.metric("p-value", f"{p_value:.5f}")

                if p_value < alpha:
                    st.success("Tolak H0 — Varians berbeda.")
                else:
                    st.warning("Gagal Tolak H0 — Varians sama.")

            except:
                st.error("Format input tidak valid.")

                
# ======================== 5) UJI RATA-RATA 2 SAMPEL INDEPENDENT (POOLED T-TEST) ======================== 

def load_pooled_t_test(title):
    st.header(title)

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📘 Penjelasan", "📐 Rumus", "📊 Contoh", "🧮 Perhitungan"]
    )

    with tab1:
        st.subheader("📘 Penjelasan")
        st.write(r"""
        Uji t dua sampel pooled digunakan untuk menguji apakah rata-rata dua populasi berbeda
        ketika **diasumsikan varians populasi sama**.
        """)
        st.info(r"""
        **Syarat:**
        1. Dua sampel independen.
        2. Varians populasi diasumsikan sama → gunakan pooled variance.
        3. Data berdistribusi normal.
        """)

        st.subheader("📌 Hipotesis")
        st.markdown(r"""
        - **H₀:** μ₁ = μ₂  
        - **H₁:** μ₁ ≠ μ₂  
        - **H₁:** μ₁ > μ₂  
        - **H₁:** μ₁ < μ₂  
        """)
   
    with tab2:
        st.subheader("📐 Rumus Statistik Uji")
        st.latex(r"""
        S_p^2 = \frac{(n_1 - 1) S_1^2 + (n_2 - 1) S_2^2}{n_1 + n_2 - 2}
        """)
        st.latex(r"""
        t = \frac{\bar{X}_1 - \bar{X}_2}{S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
        """)
        st.markdown(r"""
        - $\bar{X}_1, \bar{X}_2$ : rata-rata sampel  
        - $S_1^2, S_2^2$ : varians sampel  
        - $n_1, n_2$ : ukuran sampel  
        - $S_p^2$ : pooled variance  
        - df = $n_1 + n_2 - 2$
        """)

        st.subheader("📌 Nilai Kritis t")
        st.markdown(r"""
        Gunakan \(df = n₁ + n₂ - 2\):
        
        - Dua arah: \(|t| > t_{\alpha/2, df}\)  
        - Kanan: \(t > t_{\alpha, df}\)  
        - Kiri: \(t < -t_{\alpha, df}\)
        """)
   
    with tab3:
        st.subheader("🧮 Contoh Perhitungan")
        st.write(r"""
        Misalkan:
        - Sampel 1: n1 = 10, x̄1 = 50, s1 = 8  
        - Sampel 2: n2 = 12, x̄2 = 45, s2 = 7  

        Uji apakah rata-rata kedua populasi berbeda (α = 0.05).
        """)

        st.markdown("**Perhitungan Manual:**")
        st.latex(r"""
        S_p^2 
        = \frac{(10-1)8^2 + (12-1)7^2}{10 + 12 - 2}
        = 56.27
        """)
        st.latex(r"""
        t = \frac{50 - 45}{\sqrt{56.27}\sqrt{\frac{1}{10} + \frac{1}{12}}}
        = 1.57
        """)
        st.write("df = 20")

    
    with tab4:
        st.subheader("Kalkulator Uji t Dua Sampel (Pooled)")

        st.write("### 1. Input Data")
        metode = st.radio("Pilih metode input:", ["Manual"], horizontal=True)

        data1, data2 = [], []

        if metode == "Manual":
            colA, colB = st.columns(2)
            with colA:
                input1 = st.text_area("Data Sampel 1 (pisahkan dengan koma)")
            with colB:
                input2 = st.text_area("Data Sampel 2 (pisahkan dengan koma)")

            if input1 and input2:
                try:
                    data1 = np.array([float(x.strip()) for x in input1.split(",")])
                    data2 = np.array([float(x.strip()) for x in input2.split(",")])
                except:
                    st.error("Format data salah!")

        st.markdown("---")
        st.write("### 2. Pilih Jenis Hipotesis Alternatif")
        jenis = st.selectbox(
            "H1:",
            ["Dua Arah (≠)", "Satu Arah Kanan (μ1 > μ2)", "Satu Arah Kiri (μ1 < μ2)"]
        )
        alpha = st.selectbox("Alpha:", [0.05, 0.01, 0.10])

        if st.button("Jalankan Uji t 🚀"):
            if len(data1) == 0 or len(data2) == 0:
                st.error("Data tidak boleh kosong!")
                return

            n1, n2 = len(data1), len(data2)
            x1, x2 = np.mean(data1), np.mean(data2)
            s1, s2 = np.var(data1, ddof=1), np.var(data2, ddof=1)

            Sp2 = (((n1-1)*s1) + ((n2-1)*s2)) / (n1 + n2 - 2)
            Sp = np.sqrt(Sp2)

            t_hit = (x1 - x2) / (Sp * np.sqrt(1/n1 + 1/n2))
            df = n1 + n2 - 2

            if jenis == "Dua Arah (≠)":
                p = 2 * (1 - stats.t.cdf(abs(t_hit), df))
            elif jenis == "Satu Arah Kanan (μ1 > μ2)":
                p = 1 - stats.t.cdf(t_hit, df)
            else:
                p = stats.t.cdf(t_hit, df)

            st.success("Perhitungan selesai!")

            col1, col2, col3 = st.columns(3)
            col1.metric("t Hitung", f"{t_hit:.4f}")
            col2.metric("df", df)
            col3.metric("P-Value", f"{p:.5f}")

            st.write("### Kesimpulan")
            if p < alpha:
                st.error("Tolak H0")
            else:
                st.warning("Gagal Tolak H0")


# ======================== 6) UJI RATA-RATA 2 SAMPEL INDEPENDENT (WHELCH T-TEST) ======================== 

def load_welch_t_test(title):
    st.header(title)

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📘 Penjelasan", "📐 Rumus", "📊 Contoh", "🧮 Perhitungan"]
    )
    
    with tab1:
        st.subheader("📘 Penjelasan (Welch's T-Test)")
        st.info("""
        digunakan untuk membandingkan rata-rata dari dua kelompok independen ketika varians populasi kedua kelompok diasumsikan tidak sama
        
        **Kapan Menggunakan Welch's T-Test (Syarat Kunci):**
        1.  **Dua Kelompok Independen:** Data berasal dari dua kelompok yang tidak berpasangan.
        3.  **Distribusi Normal:** Data terdistribusi normal (atau ukuran sampel cukup besar).
        4.  **Varians Tidak Sama** Ini adalah kondisi pembeda
        """)

        st.subheader("📌 Hipotesis")
        st.markdown(r"""
        - **H₀:** μ₁ = μ₂  
        - **H₁:** μ₁ ≠ μ₂  
        """)

    with tab2:
        st.subheader("📐 Rumus Statistik Uji")
        
        st.markdown("**1. Statistik t (t-statistic):**")
        st.latex(r"""
            t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
        """)
        
        st.markdown(r"""
        * $\bar{X}_1, \bar{X}_2$: Rata-rata sampel kelompok 1 dan 2.
        * $s_1^2, s_2^2$: Varians sampel kelompok 1 dan 2.
        * $n_1, n_2$: Ukuran sampel kelompok 1 dan 2.
        """)
        
        st.markdown("**2. Derajat Kebebasan (df) :**")
        st.latex(r"""
            \nu = \text{df} = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{\left(s_1^2/n_1\right)^2}{n_1 - 1} + \frac{\left(s_2^2/n_2\right)^2}{n_2 - 1}}
        """)

        st.subheader("📌 Nilai Kritis")
        st.markdown(r"""
        Gunakan distribusi t dengan df Welch:
        
        - Dua arah: \(|t| > t_{\alpha/2, df}\)
        """)

    with tab3:
        st.subheader("🧮 Contoh Perhitungan")
        st.markdown("""
        **Contoh Kasus – Uji Welch t-test**
    
        Seorang peneliti ingin mengetahui apakah terdapat perbedaan 
        rata-rata nilai ujian Matematika antara **Kelas A** dan **Kelas B**.
    
        - **Kelas A:** 78, 85, 80, 90, 88, 76, 82, 84  
        - **Kelas B:** 70, 72, 68, 75, 73, 77  
        """)

        kelas_A = np.array([78, 85, 80, 90, 88, 76, 82, 84])
        kelas_B = np.array([70, 72, 68, 75, 73, 77])
        st.write("Data Kelas A:", kelas_A)
        st.write("Data Kelas B:", kelas_B)

        t_stat, p_value = stats.ttest_ind(kelas_A, kelas_B, equal_var=False)
        n1, n2 = len(kelas_A), len(kelas_B)
        s1, s2 = np.var(kelas_A, ddof=1), np.var(kelas_B, ddof=1)
        df = (s1/n1 + s2/n2)**2 / ((s1**2)/((n1**2)*(n1-1)) + (s2**2)/((n2**2)*(n2-1)))

        st.write("t-statistic:", round(t_stat, 4))
        st.write("p-value:", round(p_value, 6))
        st.write("Derajat kebebasan (Welch df):", round(df, 4))

        if p_value < 0.05:
            st.success("H₀ ditolak — ada perbedaan signifikan (α=0.05).")
        else:
            st.info("Gagal menolak H₀ — tidak ada bukti perbedaan signifikan.")

    with tab4:
        st.subheader("Perhitungan Otomatis (Menggunakan Data Input)")
        st.write("Silakan masukkan data Anda untuk menghitung Welch's T-Test secara otomatis.")

        st.markdown("#### Taraf Signifikansi dan Data Sampel")
        
        alpha = st.number_input(
            "Taraf Signifikansi (α):", 
            min_value=0.001, 
            max_value=0.5, 
            value=0.05, 
            step=0.005,
            format="%.3f",
            help="Taraf maksimum risiko kesalahan Tipe I yang diterima (biasanya 0.05)."
        )

        data_a_str = st.text_input("Data Program A (Kelompok 1):", "84, 85, 86, 83, 85, 87, 84, 85, 86, 85, 84, 85, 86, 83, 85, 87, 84, 85, 86, 85") 
        data_b_str = st.text_input("Data Program B (Kelompok 2):", "70, 95, 65, 80, 90, 75, 50, 99, 81, 78, 60, 100, 72, 88, 77") 

        try:
            data_A = np.array([float(x.strip()) for x in data_a_str.split(',') if x.strip()])
            data_B = np.array([float(x.strip()) for x in data_b_str.split(',') if x.strip()])

            if len(data_A) > 1 and len(data_B) > 1:
                t_stat_auto, p_value_auto = stats.ttest_ind(
                    a=data_A, 
                    b=data_B, 
                    equal_var=False 
                )
                
                df_deskriptif = pd.DataFrame({
                    'Kelompok': ['A', 'B'],
                    'Rata-rata (X̄)': [np.mean(data_A), np.mean(data_B)],
                    'Varians (s²)': [np.var(data_A, ddof=1), np.var(data_B, ddof=1)],
                    'Ukuran Sampel (n)': [len(data_A), len(data_B)]
                })
                st.dataframe(df_deskriptif, hide_index=True)

                st.markdown("#### Hasil Welch's T-Test")
                st.code(f"""
                Statistik t Welch: {t_stat_auto:.4f}
                Nilai p (Dua Arah): {p_value_auto:.4f}
                Derajat Kebebasan (df): Diperkirakan oleh SciPy
                """, language='text')

                if p_value_auto < alpha:
                    st.error(f"P-value ({p_value_auto:.4f}) < Taraf Signifikansi ($\\alpha$ = {alpha:.3f}). Tolak H0.")
                    st.markdown("##### **Kesimpulan:** Ada perbedaan rata-rata yang signifikan secara statistik antara Kelompok A dan Kelompok B.")
                else:
                    st.success(f"P-value ({p_value_auto:.4f}) ≥ Taraf Signifikansi ($\\alpha$ = {alpha:.3f}). Gagal Tolak H0.")
                    st.markdown("##### **Kesimpulan:** Tidak ada bukti yang cukup untuk menyatakan perbedaan rata-rata yang signifikan antara Kelompok A dan Kelompok B.")

            else:
                st.warning("Masukkan minimal dua nilai di setiap kelompok untuk melakukan perhitungan.")
        
        except ValueError:
            st.error("Pastikan data yang dimasukkan hanya berupa angka dan dipisahkan oleh koma.")


# ======================== 7) UJI RATA-RATA 2 SAMPEL DEPENDENT (PAIRED T-TEST) ======================== 

def load_paired_t_test(title):
    st.header(title)

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📘 Penjelasan", "📐 Rumus", "📊 Contoh", "🧮 Perhitungan"]
    )

    with tab1:
        st.subheader("📘 Penjelasan")
        st.write("""
        **Uji t Berpasangan (Paired t-test)** digunakan untuk menguji apakah terdapat perbedaan rata-rata antara dua kelompok sampel yang **saling berhubungan (dependen)**.
        
        Kasus yang sering ditemui:
        - **Pre-test & Post-test:** Mengukur kinerja siswa sebelum dan sesudah pelatihan.
        - **Eksperimen Berulang:** Mengukur tekanan darah pasien sebelum dan sesudah minum obat.
        - **Pasangan Matched:** Mengukur dua objek yang dipasangkan secara khusus (misal: suami-istri).
        """)

        st.info("""
        **Asumsi:**
        1. Data berupa selisih ($d$) berdistribusi normal.
        2. Skala data interval atau rasio.
        """)

        st.subheader("📌 Hipotesis")
        st.markdown(r"""
        - **H₀:** μ_d = 0  (tidak ada perbedaan)  
        - **H₁:** μ_d ≠ 0  (ada perbedaan)  
        """)

    with tab2:
        st.subheader("📐 Rumus Statistik Uji")
        st.write("Uji ini berbasis pada **selisih ($d$)** dari setiap pasangan data.")
        
        st.latex(r"""
        t = \frac{\bar{d}}{\frac{s_d}{\sqrt{n}}}
        """)

        st.markdown("""
        **Keterangan:**
        - $\bar{d}$ : Rata-rata dari selisih ($d_i = x_{1i} - x_{2i}$)
        - $s_d$ : Standar deviasi dari selisih
        - $n$ : Jumlah pasangan data
        - **Derajat bebas (df)** = $n - 1$
        """)

        st.subheader("📌 Nilai Kritis")
        st.markdown(r"""
        Gunakan \(df = n - 1\):
        
        - Dua arah: Tolak H₀ jika \(|t| > t_{\alpha/2, df}\)
        """)

    with tab3:
        st.subheader("🧮 Contoh Perhitungan")
        st.write("Seorang guru ingin menguji efektivitas metode belajar baru.")
        
        data_pre = [50, 60, 70, 80, 65]
        data_post = [60, 65, 75, 85, 70]
        
        df_contoh = pd.DataFrame({
            "Nilai Pre-test": data_pre,
            "Nilai Post-test": data_post,
            "Selisih (d)": np.array(data_pre) - np.array(data_post)
        })
        
        st.table(df_contoh)
        
        d_bar = df_contoh["Selisih (d)"].mean()
        sd = df_contoh["Selisih (d)"].std(ddof=1)
        n = len(df_contoh)
        t_hit = d_bar / (sd / np.sqrt(n))
        
        st.write(f"Rata-rata selisih ($\\bar{{d}}$) = {d_bar}")
        st.write(f"Standar deviasi selisih ($s_d$) = {sd:.3f}")
        st.write(f"t-hitung = {t_hit:.3f}")

    with tab4:
        st.subheader("Kalkulator Paired t-test")
        
        col1, col2 = st.columns(2)
        with col1:
            input1 = st.text_area("Data Sampel 1 (misal: Sebelum)", "80, 85, 90, 75, 70")
        with col2:
            input2 = st.text_area("Data Sampel 2 (misal: Sesudah)", "85, 88, 92, 80, 75")
            
        alpha = st.selectbox("Taraf Signifikansi (Alpha)", [0.05, 0.01, 0.10], key='alpha_paired')
        
        if st.button("Hitung Paired t-test"):
            try:
                data1 = np.array([float(x) for x in input1.split(",")])
                data2 = np.array([float(x) for x in input2.split(",")])
                
                if len(data1) != len(data2):
                    st.error("⚠️ Jumlah data sampel 1 dan 2 harus sama!")
                else:
                    d = data1 - data2
                    d_bar = np.mean(d)
                    s_d = np.std(d, ddof=1)
                    n = len(d)
                    df = n - 1
                    
                    se = s_d / np.sqrt(n)
                    t_stat = d_bar / se
                    
                    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

                    t_tabel = stats.t.ppf(1 - (alpha/2), df)
                    
                    st.divider()
                    col_res1, col_res2, col_res3, col_res4 = st.columns(4)
                    
                    col_res1.metric("t-hitung", f"{t_stat:.4f}")
                    col_res2.metric("t-tabel", f"{t_tabel:.4f}")
                    col_res3.metric("p-value", f"{p_value:.5f}")
                    col_res4.metric("Rata-rata Selisih", f"{d_bar:.3f}")
                    
                    st.write(f"**Derajat Bebas (df):** {df}")
                    
                    # Kesimpulan
                    if p_value < alpha:
                        st.success(f"**Kesimpulan:** Tolak H0 (p-value < {alpha}). Ada perbedaan signifikan.")
                    else:
                        st.warning(f"**Kesimpulan:** Gagal Tolak H0 (p-value > {alpha}). Tidak cukup bukti perbedaan.")
                        
                    with st.expander("Lihat Detail Statistik Selisih"):
                        sum_d = np.sum(d)
                        
                        df_summary = pd.DataFrame({
                            "Total Selisih": [f"{sum_d:.2f}"],
                            "Ukuran Sampel (n)": [n],
                            "Rata-rata Selisih": [f"{d_bar:.4f}"],
                            "Simpangan Baku (s)": [f"{s_d:.4f}"]
                        })
                        
                        st.dataframe(df_summary, use_container_width=True, hide_index=True)
                        
            except ValueError:
                st.error("Pastikan input hanya berupa angka dipisahkan koma.")

if main_menu == "📚 Pilih Uji Statistik":
    if menu == "Uji Proporsi 1 Sampel":
        load_uji_proporsi_1_sampel("Uji Proporsi 1 Sampel")#Meira

    elif menu == "Uji Proporsi 2 Sampel":
        load_uji_proporsi_2_sampel("Uji Proporsi 2 Sampel")#Meira

    elif menu == "Uji Rata-rata 1 Sampel (Z)":
        load_z_test_1("Uji Rata-rata 1 Sampel – Z Test")#Rebeca

    elif menu == "Uji Rata-rata 1 Sampel (t)":
        load_t_test_1("Uji Rata-rata 1 Sampel – t Test")#Rebeca

    elif menu == "Uji Rata-rata 2 Sampel Independen (Z-test)":
        load_z_test_2_sample_simple("Uji Rata-rata Dua Sampel Independen – Z Test")#Fitri
    
    elif menu == "Uji Kesamaan Varians (F-test)":
        load_f_test("Uji Kesamaan Varians (F-test)")#Ardunt

    elif menu == "Uji Rata-rata 2 Sampel Independen (Pooled t-test)":
        load_pooled_t_test("Uji Rata-rata 2 Sampel Independen – Pooled t-Test (Varians Sama)")#Disya

    elif menu == "Uji Rata-rata 2 Sampel Independen (Welch t-test)":
        load_welch_t_test("Uji Rata-rata Dua Sampel Independen – Welch t-test")#Abdi

    elif menu == "Uji Rata-rata 2 Sampel Dependen (Paired t-test)":
        load_paired_t_test("Uji Rata-rata 2 Sampel Dependen (Paired t-test)")#Iqbal
