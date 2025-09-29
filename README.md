# Job Recommendation System

Proyek ini dibuat untuk memenuhi tugas pada mata kuliah Proyek Sains Data.

## 📌 Overview
Perkembangan teknologi memudahkan akses informasi, termasuk dalam pencarian kerja. Namun, banyak platform hanya menampilkan daftar lowongan tanpa memperhatikan kesesuaian antara skill pengguna dengan persyaratan pekerjaan. Hal ini sering menimbulkan kebingungan pencari kerja dalam menentukan skill yang perlu ditingkatkan. Sistem rekomendasi ini hadir untuk memberikan solusi dengan mencocokkan skill pencari kerja dengan kebutuhan industri, sekaligus memberikan informasi skill tambahan yang perlu dikuasai.

## 🎯 Problem Statement
Pencari kerja memerlukan sistem yang membantu menemukan pekerjaan sesuai skill yang dimiliki, serta memberikan rekomendasi keterampilan tambahan agar memenuhi persyaratan pekerjaan.

## 🚀 Objectives & Benefits
- Mempermudah pencari kerja menemukan pekerjaan yang sesuai dengan kemampuan.  
- Memberikan rekomendasi keterampilan tambahan yang perlu ditingkatkan.  
- Membantu pencari kerja merencanakan pengembangan diri agar lebih siap menghadapi kebutuhan pasar kerja.  

## 📂 Scope
- Sistem berbasis **web** menggunakan Flask.
- Fokus pada rekomendasi skill dan kesesuaian dengan deskripsi pekerjaan.  

## 🛠 Methodology
Metode yang digunakan adalah **CRISP-DM**, dengan tahapan:  
1. **Business Understanding** – identifikasi kebutuhan pencari kerja dan tujuan sistem.  
2. **Data Understanding** – data lowongan IT dikumpulkan via web scraping LinkedIn.  
3. **Data Preparation** – pembersihan dan transformasi data.  
4. **Modeling** – sistem mencocokkan job skills pengguna dengan deskripsi pekerjaan.  
5. **Evaluation** – menilai akurasi rekomendasi terhadap kebutuhan industri.  
6. **Deployment** – sistem diimplementasikan sebagai aplikasi web dengan Flask + HTML.  
