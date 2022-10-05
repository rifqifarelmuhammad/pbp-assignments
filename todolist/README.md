# Tugas 4 PBP (Pengimplementasian Form dan Autentikasi Menggunakan Django)

## Link Heroku

[Heroku](https://katalog-project-django.herokuapp.com/todolist/)

## Jawaban dari Pertanyaan Tugas 4

### 1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

CSRF Token atau Cross-Site Request Forgery Token merupakan token acak yang dibuat secara otomatis oleh server ketika terdapat request dari user/client untuk login ke webiste server. Setiap terdapat permintaan login ke website, server akan membuat CRSF Token yang baru. Sehingga dengan adanya CRSF Token, website dapat menghilangkan kemungkinan terjadinya serangan CSRF atau pemalsuan permintaan lintas situs, karena jika terdapat request yang masuk ke server tetapi request tersebut tidak memiliki CSRF Token atau CSRF Tokennya tidak dikenali oleh server, maka request tersebut akan ditolak oleh server. {% csrf_token %} sendiri digunakan ketika terdapat template html yang menggunakan post method. Tugas lain dari CSRF Token adalah melindungi informasi yang dikirimkan oleh user/client.

Berdasarkan penjelasan di atas, dapat disimpulkan bahwa kegunaan {% csrf_token %} pada elemen <form> adalah untuk memastikan bahwa lintas situs server aman karna tidak adanya pemalsuan sehingga informasi yang ada pada form yang dikirimkan oleh user/client akan terlindungi dan aman. Hal ini dikarenakan server akan memeriksa crsf token user/client, jika user/client tidak memiliki crsf token atau crsf tokennya tidak terdaftar pada server, server akan menolak request dari user/client tersebut.

Jika {% csrf_token %} pada elemen <form> dihapus, ketika user/client melakukan POST (submit form), maka akan muncul error 403 (Forbidden) dikarenakan tidak adanya verifikasi CSRF Token, sehingga program akan menolak request karena hal ini adalah salah satu cara yang diterapkan oleh Django untuk menjaga keamanan server program sehingga harus diterapkan pada setiap program yang menggunakan Django sebagai frameworknya.

### 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Bisa. Pada tugas kali ini, di file html saya menggunakan generator {{ form.as_table }} karena tampilan form telah dibuat di views.py, sehingga hanya tinggal ditampilkan saja ke template HTML. Hal ini dapat dibuktikan dengan data yang dikirimkan ke template HTML form hanya berupa form/tampilan form saja. Jika kita ingin membuat <form> secara manual (tampilan dibuat secara manual), maka kita harus membuat tampilan formnya terlebih dahulu di file html. Dengan cara ini, maka form dapat dibuat dengan lebih fleksibel (tidak perlu mengikuti template django), tentu akan lebih baik jika menggunakan bantuan css agar tampilan form lebih menarik. Setelah tampilan <form> selesai dibuat, maka selanjutnya kita perlu membuat fungsi di views.py untuk mengambil serta mengolah data-data dari form tersebut.

### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Jika terdapat request dari user/client untuk menampilkan halaman HTML form menggunakan path yang ada di urls.py, maka program akan men-trigger fungsi views.py yang bersangkutan untuk melakukan tugasnya, yaitu membuat form/tampilan form dan mengirimkan tampilannya ke file html untuk ditampilkan ke user. Ketika user selesai menginput data dan melakukan submisi pada HTML form, program akan melakukan validasi pada form serta CRSF Token terlebih dahulu, jika valid maka data akan diambil oleh fungsi views.py (yang bersangkutan) dan melakukan proses penyimpanan data ke database dengan bantuan Query yang ada di models.py, pada tugas kali ini adalah query Task. Selanjutnya, ketika terdapat request untuk menampilkan data, program akan memverifikasi terlebih dahulu apakah user/client yang mengirimkan request sudah login dan melakukan validasi pada CRSF Tokennya. Jika lolos tahap verifikasi dan validasi, maka program akan mengambil data user/client tersebut dari database dengan bantuan Query di models.py (Task), dan mengirimkan datanya ke template html untuk ditampilkan.

### 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Poin 1. Membuka CMD dan mengubah directory ke folder pbp-assignments, lalu menulis 'python manage.py startapp todolist' untuk membuat aplikasi django baru bernama 'todolist'. Setelah itu, saya menambahkan 'todolist' di variable INSTALLED_APPS yang ada di settings.py project_django.

2. Poin 2. Menambahkan path baru di urls.py folder project_django, yaitu path('todolist/', include('todolist.urls')), dan juga menambahkan path baru di urls.py folder todolist, yaitu path('', show_todolist, name='show_todolist'), agar user dapat mengakses http://localhost:8000/todolist. Hal ini dapat terjadi karena ketika user memasukkan URL http://localhost:8000/todolist, maka program akan mengarahkan ke urls.py todolist dan mengambil fungsi dari path dengan nama berupa string kosong ('').

3. Poin 3. Membuat sebuah class baru di models.py todolist bernama 'Task' yang memiliki atribute 'user', 'date', 'title', dan 'description'.

4. Poin 4. Membuat fungsi 'register' di views.py yang akan membuat form dan menampilkannya ke user dalam bentuk file html (register.html). Ketika user melakukan submit, maka program akan membuat akun menggunakan data dari form tersebut dan membuat message yang akan ditampilkan di halaman login (login.html). Karena fungsi ini membutuhkan method POST, maka pada register.html ditambahkan {% csrf_token %}. Selanjutnya, saya membuat fungsi 'login_user' di views.py yang akan menampilkan sebuah form untuk mengisi username & password akun melalui login.html. Ketika user melakukan submit, maka program akan mengambil data username & password yang dimasukkan untuk dilakukan authenticate. Jika berhasil, maka program akan mengarahkan ke fungsi 'show_todolist'. Karena fungsi ini membutuhkan method POST, maka pada login.html ditambahkan {% csrf_token %}. Terakhir, saya menambahkan fungsi 'logout_user' yang akan melakukan proses logout dan mengembalikan halaman yang ada pada fungsi 'login' (login.html).

5. Poin 5. Membuat fungsi 'show_todolist' di views.py yang akan mengambil data user dari database untuk ditampilkan di todolist. Selain itu, fungsi 'show_todolist' juga akan mengambil username dari user yang melakukan request sebagai data yang akan ditampilkan pada file html. Pada todolist.html, saya memunculkan username user yang melakukan request, menambahkan tombol "Tambah Task Baru" yang akan mengarahkan user ke fungsi 'create_task', menambahkan tombol "logout" yang akan mengarahkan user ke fungsi "logout_user", serta tabel yang berisi tanggal pembuatan task, judul task, dan deskripsi task.

6. Poin 6. Membuat fungsi 'create_task' di views.py yang akan membuat form berisi title dan description dari task yang ingin dibuat, dan memunculkannya ke user dalam bentuk file html (create_task.html). Ketika user melakukan submit, maka program akan menambahkan task baru ke database menggunakan data yang disubmit tersebut. Karena fungsi ini menggunakan method post, maka pada crate_task.html ditambahkan {% csrf_token %}.

7. Poin 7. Menambahkan path('register/', register, name='register'), path('login/', login_user, name='login'), path('create-task/', create_task, name='create_task'), dan path('logout/', logout_user, name='logout') agar fungsi-fungsi yang bersangkutan dapat diakses.

8. Poin 8. Melakukan deployment ke Heroku dengan cara melakukan push repository ke github.

9. Poin 9. Membuat 2 akun baru, sebagai dummy, dan membuat tiga dummy data pada 2 akun tersebut (total ada 6 data).

## Jawaban dari Pertanyaan Tugas 5

### 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

1. Inline CSS adalah style penggunaan CSS dengan cara properti CSS dimasukkan ke dalam tag elemen HTML tertentu. Penerapan inline CSS bersifat unik pada satu elemen HTML saja. Jenis css ini di-define dalam tag HTML menggunakan atribute "style".
- Kelebihan: Memiliki prioritas paling tinggi dalam urutan penerapan CSS pada HTML. Lebih mudah dan cepat untuk membuat properti CSS ke dalam HTML, karena tidak perlu membuat file CSS terpisah (seperti di external style) atau membuat ruang tersendiri (seperti di internal style).
- Kekurangan: Menambahkan properti CSS ke setiap tag HTML dapat membuat strukturnya berantakan, tidak terlihat rapih, dan memakan waktu yang cukup lama. Styling pada beberapa elemen HTML dapat mempengaruhi ukuran halaman HTML secara tidak sengaja. Terakhir, styling pada beberapa elemen HTML dapat mempengaruhi waktu loadingnya.

2. Internal CSS adalah style penggunaan CSS dengan cara kumpulan properti CSS berada di dalam head HTML, dengan kata lain CSS diletakkan di dalam file HTML. Penerapan internal css bersifat unik pada satu halaman HTML, sehingga style ini baik digunakan ketika satu halaman HTML harus ditata dengan unik.
- Kelebihan: Memiliki struktur yang terlihat lebih rapih jika dibandingkan dengan Inline CSS, khususnya jika ingin membuat properti CSS yang cukup banyak ke dalam suatu halaman HTML. Dapat menggunakan class dan id selector, sehingga penggunaanya lebih fleksibel. Berbeda dengan external CSS, internal CSS tidak perlu mengungah atau membuat file CSS (file dengan ekstensi '.css').
- Kekurangan: Memiliki prioritas yang lebih rendah daripada inline CSS, sehingga ada kemungkinan properti CSS pada suatu atribut HTML yang menggunakan Internal CSS akan di-override oleh properti CSS yang menggunakan inline CSS. Kode atau properti yang terlalu banyak pada dokumen HTML dapat meningkatkann ukuran file HTML dan waktu loading, sehingga penggunaan internal CSS harus efisien.

3. External CSS adalah style penggunaan CSS dengan cara membuat file CSS terpisah (ekstensi '.css') yang hanya berisi properti CSS dan atribute tag pada HTML. Jika menggunakan cara ini, kita harus memasukkan link dokumen CSS tersebut ke dalam dokumen HTML menggunakan tag 'link'. Untuk setiap tag, style CSS hanya dapat diatur sekali dan dapat diterapkan pada seluruh halaman HTML. Penerapan External CSS bersifat unik untuk setiap tag pada seluruh dokumen HTML.
- Kelebihan: File HTML akan terlihat lebih bersih dan rapih karena properti CSS berada pada file yang berbeda. Dapat menggunakan properti CSS yang sama pada banyak dokumen HTML dengan cara yang sangat mudah, yaitu menggunakan file dengan ekstensi .css yang sama pada setiap dokumen HTML tersebut, sehingga akan lebih efisien dalam pembuatan properti CSS pada banyak dokumen HTML.
- Kekurangan: Memiliki prioritas yang lebih rendah daripada inline CSSdan internal CSS, sehingga ada kemungkinan properti CSS pada suatu atribut HTML yang menggunakan external CSS akan di-override oleh properti CSS yang menggunakan inline atau internal CSS. Dapat meningkatkan waktu loading web karena akan bergantung dengan berapa lama CSS eksternal dimuat.

### 2. Jelaskan tag HTML5 yang kamu ketahui.

- <html>: Mendefine root file HTML
- <body>: Mendefine bagian body file HTML
- <head>: Mendefine bagian head file HTML
- <header>: Mendefine bagian header file HTML
- <footer>: Mendefine footer pada sebuah dokumen HTML
- <div>: Mendefine sebuah divisi pada dokumen HTML
- <nav>: Mendefine link navigasi
- <style>: Mendefine style HTML di Head dokumen HTML
- <title> Mendefine judul dokumen HTML
- <h1> sampai <h6>: Menampilkan header HTML (memiliki ukuran huruf yang berbeda, <h1> memiliki huruf terbesar)
- <a>: Mendefine Hyperlink
- <b>: Menampilkan teks bold
- <p>: Menampilkan paragraf
- <hr>: Membuat garis mendatar atau horizontal
- <textare>: Mendefine multi-line input text
- <iframe>: Menampilkan url dalam inline frame
- <img>: Menampilkan gambar pada file HTML
- <label>: Mendefine label untuk kontrol input
- <table>: Mendefine table
- <td>: Mendefine cell dalam table
- <th>: Mendefine cell teratas pada table
- <button>: Membuat tombol pada file HTML
- <ul>: Mendefine daftar yang tidak berurutan
- <object>: Mendefine sebuah object pada file HTML
- <caption>: Mendefine caption atau judul suatu tabel
- <form>: Mendefine form HTML pada dokumen HTML
- <embed>: Memasukkan aplikasi eksternal ke dalam dokumen HTML
- <audio>: Memasukkan audio ke dalam file HTML
- <video>: Memasukkan video ke dalam dokumen HTML
- <code>: Mendefine teks sebagai code pemrograman
- <script>: Tempat menaruh script pada dokumen HTML

### 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.

1. Simple selector adalah selector yang memilih elemen berdasarkan nama, id, atau class pada dokumen HTML. Dibagi menjadi 3, yaitu Element Selector, ID Selector, dan Class selector.
- Element selector adalah selector yang menggunakan tag HTML
- ID selector adalah selector yang menggunakan ID pada tag HTML (harus didefine sebelumnya pada HTML dan harus bersifat unik)
- Class selector adalah selector yang menggunakan class pada tag HTML (harus didefine sebelumnya pada HTML dan harus bersifat unik)
2. Combinator selector adalah selector yang memilih elemen berdasarkan hubungan spesifik antar elemen. DIbagi menjadi 4, yaitu:
- Descendant selector: Memilih semua elemen yang merupakan turunan dari elemen tertentu
- Child selector: Memilih semua elemen yang merupakan child dari elemen tertentu
- Adjacent sibling selector: Memilih semua elemen yang berada pada posisi tepat setelah elemen tertentu dan memilik elemen parent yang sama
- General sibling selector: Memilih semua elemen yang merupakan sibling berikutnya dari elemen tertentu
3. Pseudo-class selector adalah selector yang memilih elemen berdasarkan keadaan tertentu. Dibagi menjadi 7, yaitu:
- :active -> Memilih semua elemen yang aktif
- :checked -> Memilih semua elemen yang telah dicentang
- :disabled -> Memilih semua elemen yang dinonaktifkan
- :enabled -> Memilih semua elemen yang diaktifkan
- :link -> Memilih semua tautan yang belum pernah dikunjungi
- :hover -> Memilih semua elemen yang terdapat kursor di atasnya
- :visited -> Memilih link yang sudah pernah dikuncungi
4. Atribute selector adalah selector yang memilih elemen berdasarkaan nama atribute atau nilai atributenya

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Memperindah tampilan HTML (login, register, todolist, dan create-task) dengan cara mengkustomisasi template HTML menggunakan CSS dengan bantuan framework Tailwind.
- Melakukan modifikasi pada tampilan list task yang dimana sebelumnya ditampilkan dalam bentuk table, diubah menjadi Card (satu card mengandung satu task). Dimodifikasi dengan bantuan framework Tailwind.
- Membuat halaman login, register, todolist, dan create-task menjadi responsive (menggunakan bantuan framework Tailwind) sehingga tampilan web tidak rusak ketika digunakan pada device yang berbeda.