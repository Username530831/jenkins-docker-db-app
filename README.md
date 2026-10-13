[Persiapan lingkungan]
Java 21 + Git + Jenkins (localhost:8080) + plugin Git/GitHub/Pipeline
        + Ngrok (link publik + localhost:8080)
        + WSL2 + Docker Desktop (hello-world)

[Akses & keamanan]
Buat user (akun asprak) + login Incognito via link Ngrok
Docker Hub: token + Credentials Jenkins (dockerhub-credentials)

[Integrasi Git]
Repo GitHub (kode + Dockerfile + compose + Jenkinsfile)
    Webhook (push event) + Ngrok + Jenkins

[Pipeline otomatis]
Developer push ke GitHub
GitHub memanggil /github-webhook/ lewat Ngrok
Jenkins mengambil Jenkinsfile dari repo
Stage 1 Checkout     : clone kode terbaru
Stage 2 Build App    : langkah build (di sini placeholder)
Stage 3 Build Image  : docker build, tag nomor build + latest
Stage 4 Push Image   : login dengan credentials, push ke Docker Hub
Stage 5 Deploy       : docker compose + app Flask + PostgreSQL
Hasil: http://localhost:5000/db terhubung ke database

Testing Terakhir! 