# Submission Dicoding Course titled "Belajar Data Analytics dengan Python"

## Deskripsi

Proyek ini adalah ujian akhir untuk kursus yang disediakan oleh Dicoding.

## Struktur Direktori

- **/dataset**: Direktori ini berisi data yang digunakan dalam proyek, dalam format .csv .
    - **/raw_data**: Sub direktori ini adalah tempat dimana data yang original masih disimpan
    - **/combined_data** Sub direktori ini adalah tempat dimana data dari seluruh csv yang terpisah digabungkan menjadi satu file .csv
- **/dashboard**: Direktori ini berisi main.py yang digunakan untuk membuat dashboard hasil analisis data.
- **Project Notebook.ipynb**: File ini yang digunakan untuk melakukan analisis data.

## Instalasi
1. Pertama lakukanlah installasi library python yang relevan untuk projek ini

    ```shell
    pip install streamlit
    pip install -r requirements.txt
    ```

## Menjalankan Streamlit
1. Masuk ke direktori yang terdapat file streamlit.

    ```shell
    cd Analisis-Data-Dicoding/dashboard/
    streamlit run dashboard.py
    ```
