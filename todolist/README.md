# Tugas 4 PBP (Pengimplementasian Form dan Autentikasi Menggunakan Django)

## Link Heroku

[Heroku](https://katalog-project-django.herokuapp.com/todolist/)

## Jawaban dari Pertanyaan

### 1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

CSRF Token atau Cross-Site Request Forgery Token merupakan token acak yang dibuat secara otomatis oleh server ketika terdapat request dari user/client untuk login ke webiste server. Setiap terdapat permintaan login ke website, server akan membuat CRSF Token yang baru. Sehingga dengan adanya CRSF Token, website dapat menghilangkan kemungkinan terjadinya serangan CSRF atau pemalsuan permintaan lintas situs, karena jika terdapat request yang masuk ke server tetapi request tersebut tidak memiliki CSRF Token atau CSRF Tokennya tidak dikenali oleh server, maka request tersebut akan ditolak oleh server. {% csrf_token %} sendiri digunakan ketika terdapat template html yang menggunakan post method. Tugas lain dari CSRF Token adalah melindungi informasi yang dikirimkan oleh user/client.

Berdasarkan penjelasan di atas, dapat disimpulkan bahwa kegunaan {% csrf_token %} pada elemen <form> adalah untuk memastikan bahwa lintas situs server aman karna tidak adanya pemalsuan sehingga informasi yang ada pada form yang dikirimkan oleh user/client akan terlindungi dan aman. Hal ini dikarenakan server akan memeriksa crsf token user/client, jika user/client tidak memiliki crsf token atau crsf tokennya tidak terdaftar pada server, server akan menolak request dari user/client tersebut.

Jika {% csrf_token %} pada elemen <form> dihapus, ketika user/client melakukan POST (submit form), maka akan muncul error 403 (Forbidden) dikarenakan tidak adanya verifikasi CSRF Token, sehingga program akan menolak request karena hal ini adalah salah satu cara yang diterapkan oleh Django untuk menjaga keamanan server program sehingga harus diterapkan pada setiap program yang menggunakan Django sebagai frameworknya.

### 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Bisa. 

### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

- Ketika user melakukan submisi pada HTML form, program akan melakukan validasi CRSF Token terlebih dahulu, jika valid maka data akan diambil oleh fungsi views.py (yang bersangkutan) dan akan melakukan proses penyimpanan data ke database.

- Ketika terdapat request untuk menampilkan data, program akan memverifikasi terlebih dahulu apakah user/client yang mengirimkan request sudah login dan melakukan validasi pada CRSF Tokennya. Jika lolos tahap verifikasi dan validasi, maka program akan mengambil data user/client tersebut dari database, dan menampilkannya di html.

### 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Poin 1. Membuka CMD dan mengubah directory ke folder pbp-assignments, lalu menulis 'python manage.py startapp todolist' untuk membuat aplikasi django baru bernama 'todolist'. Setelah itu, saya menambahkan 'todolist' di variable INSTALLED_APPS yang ada di settings.py project_django.

2. Poin 2. Menambahkan path baru di urls.py folder project_django, yaitu path('todolist/', include('todolist.urls')), dan juga menambahkan path baru di urls.py folder todolist, yaitu path('', show_todolist, name='show_todolist'), agar user dapat mengakses http://localhost:8000/todolist. Hal ini dapat terjadi karena ketika user memasukkan URL http://localhost:8000/todolist, maka program akan mengarahkan ke urls.py todolist dan mengambil fungsi dari path dengan nama berupa string kosong ('').

3. Poin 3. Membuat sebuah class baru di models.py todolist bernama 'Task' yang memiliki atribute 'user', 'date', 'title', dan 'description'.

4. Poin 4. Membuat fungsi 'register' di views.py yang akan membuat form dan menampilkannya ke user dalam bentuk file html (register.html). Ketika user melakukan submit, maka program akan membuat akun menggunakan data dari form tersebut dan membuat message yang akan ditampilkan di halaman login (login.html). Karena fungsi ini membutuhkan method POST, maka pada register.html ditambahkan {% csrf_token %}. Selanjutnya, saya membuat fungsi 'login_user' di views.py yang akan menampilkan sebuah form untuk mengisi username & password akun melalui login.html. Ketika user melakukan submit, maka program akan mengambil data username & password yang dimasukkan untuk dilakukan authenticate. Jika berhasil, maka program akan mengarahkan ke fungsi 'show_todolist' dan menyimpan waktu terakhir kali user login sebagai cookie. Karena fungsi ini membutuhkan method POST, maka pada login.html ditambahkan {% csrf_token %}. Terakhir, saya menambahkan fungsi 'logout_user' yang akan melakukan proses logout dan mengembalikan halaman yang ada pada fungsi 'login' (login.html), serta menghapus waktu terakhir kali user login dari cookie.

5. Poin 5. Membuat fungsi 'show_todolist' di views.py yang akan mengambil data user dari database untuk ditampilkan di todolist. Selain itu, fungsi 'show_todolist' juga akan mengambil username dari user yang melakukan request, serta waktu terakhir kali user login sebagai data yang akan ditampilkan pada file html. Pada todolist.html, saya memunculkan username user yang melakukan request, menambahkan tombol "Tambah Task Baru" yang akan mengarahkan user ke fungsi 'create_task', menambahkan tombol "logout" yang akan mengarahkan user ke fungsi "logout_user", serta tabel yang berisi tanggal pembuatan task, judul task, dan deskripsi task.

6. Poin 6. Membuat fungsi 'create_task' di views.py yang akan membuat form berisi title dan description dari task yang ingin dibuat, dan memunculkannya ke user dalam bentuk file html (create_task.html). Ketika user melakukan submit, maka program akan menambahkan task baru ke database menggunakan data yang disubmit tersebut. Karena fungsi ini menggunakan method post, maka pada crate_task.html ditambahkan {% csrf_token %}.

7. Poin 7. Menambahkan path('register/', register, name='register'), path('login/', login_user, name='login'), path('create-task/', create_task, name='create_task'), dan path('logout/', logout_user, name='logout') agar fungsi-fungsi yang bersangkutan dapat diakses.

8. Poin 8. Melakukan deployment ke Heroku dengan cara melakukan push repository ke github.

9. Poin 9. Membuat 2 akun baru, sebagai dummy, dan membuat tiga dummy data pada 2 akun tersebut (total ada 6 data).