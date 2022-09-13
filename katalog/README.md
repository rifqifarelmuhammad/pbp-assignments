# Tugas 2 PBP (Katalog Proyek Django)

## Link Heroku

[Heroku](https://katalog-project-django.herokuapp.com/katalog/)

## Jawaban dari Pertanyaan

### 1. Bagan request client ke web aplikasi berbasis Django beserta responnya dan penjelasan tentang kaitannya dengan urls.py, views.py, models.py, dan berkas html

![Bagan](https://user-images.githubusercontent.com/87516736/189913656-69bac547-14ca-4f8f-ada6-c0a81c80360c.png)

Kaitan :
- Pada Web aplikasi berbasis Django, urls.py bertugas sebagai URLconf (pada bagan), dimana pada file ini akan dipetakan seluruh path dengan function yang tersedia pada file views.py. Sehingga jika terdapat request dari User/Client berbentuk URL, maka urls.py akan meneruskan request ke fungsi view yang dipicu berdasarkan path yang telah ditentukan.

- views.py bertugas sebagai Views (pada bagan), dimana pada file ini terdapat berbagai macam fungsi yang akan digunakan berdasarkan URL yang direquest oleh User/Client. Terdapat beberapa fungsi pada views.py yang membutuhkan data, sehingga views.py akan bekerja sama dengan models.py dalam pertukaran data dengan database. Selain itu, setelah suatu fungsi pada views.py dipanggil, maka fungsi tersebut akan memilih template HTML yang telah ditentukan sebelumnya untuk ditampilkan sebagai response ke User/Client.

- models.py bertugas sebagai Model (pada bagan), dimana pada file ini terdapat beberapa query yang merupakan informasi apa yang diterima ataupun apa yang diambil dari database. Jika terdapat query yang dibutuhkan oleh suatu fungsi pada views.py, maka models.py akan melakukan transaksi data dengan database berdasarkan query tersebut dan memberikannya kepada fungsi views.py tersebut. Dengan kata lain, models.py merupakan suatu bagian yang memiliki fokus untuk melakukan transaksi data dengan database.

- Berkas html bertugs sebagai Template (pada bagan), dimana pada berkas ini terdiri dari berbagai macam template file HTML yang beberapa diantaranya membutuhkan data (karena kita ingin membuat website yang dynamic, itulah fungsi keberadaan dari template file HTML ini dimana data tersebut yang membuat tampilan HTML bisa berubah-ubah). Fungsi-fungsi pada views.py akan memilih file HTML mana yang akan digunakan untuk ditampilkan sebagai response kepada User/Client.

### 2. Mengapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment merupakan sebuah alat yang berfungsi untuk menjaga ruang antar proyek di komputer dengan cara mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada di komputer. Kita dapat mengasumsikan tugas dari virtual environment seperti membuat sekat atau wadah antar proyek sehingga menghilangkan kemungkinan terjadinya tabrakan antar requirement setiap proyek. Virtual environment memiliki sifat spesifik pada proyek tertentu dan tidak berinterfer dengan dependensi proyek lainnya.

Contoh kasus dari penggunaan virtual environment ini adalah ketika kita memiliki beberapa proyek yang memiliki spesifikasi requirement yang berbeda-beda. Seperti kita memiliki 2 proyek yang bernama proyek A dan B, dimana kedua proyek tersebut membutuhkan Python, Django, serta requirement lainnya dengan versi yang berbeda-beda, baik berbeda antar proyek maupun dengan versi yang ada di komputer kita. Pada kasus ini, Virtual environment akan menampung seluruh teknologi dan requirement pada proyek kita sehingga memungkinkan kita untuk melakukan instalasi seluruh teknologi dan requirement tersebut tanpa tercampur ataupun bertabrakan dengan global environment komputer kita.

Oleh karena itu, kita menggunakan virtual environment pada pembuatan aplikasi web berbasis Django agar memungkinkan kita untuk menggunakan teknologi ataupun requirement yang dibutuhkan sesuai dengan kebutuhan aplikasi web yang ingin kita buat tanpa perlu memikirkan adanya kemungkinan tercampur atau bertabrakannya teknologi atau requirement tersebut dengan proyek lainnya ataupun dengan global environment komputer kita sehingga aplikasi web dapat berjalan dengan lancar di berbagai device.

Walaupun begitu, kita masih bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, karena pada dasarnya virtual environment hanyalah sebatas alat bantu saja, bukan sebuah alat wajib pada pembuatan aplikasi web berbasis Django. Akan tetapi, cara ini sangat tidak direkomendasikan karena bisa mengakibatkan conflict dependancy antara satu proyek dengan proyek lainnya ataupun dengan global environment suatu device, terutama jika aplikasi web akan digunakan atau dijalankan di device lain. 

### 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas!

- Poin 1. Pada file views.py, saya membuat suatu fungsi bernama 'show_katalog' dimana ia akan mengambil query beserta data dari models.py menggunakan syntax 'CatalogItem.objects.all()', dimana 'CatalogItem' merupakan nama query yang terdapat di models.py. Setelah itu, fungsi 'show_katalog' akan mengembalikan sebuah file HTML bernama 'katalog.html' beserta dengan data-data yang dibutuhkan oleh file HTML tersebut.

- Poin 2. Pada file urls.py di folder katalog, saya membuat suatu path baru, yaitu path('', show_katalog, name='show_katalog'), untuk memetakan jika User/Client mengirimkan request dengan akhiran URL 'katalog/' maka request akan diteruskan kepada fungsi 'show_katalog' yang ada di views.py. Hal ini dapat terjadi karena pada urls.py di folder 'project_django' saya juga menambahkan path baru, yaitu path('katalog/', include('katalog.urls')), sehingga jika terdapat request dengan URL akhiran 'katalog/', program akan masuk ke dalam urls.py di folder katalog.

- Poin 3. Karena pada dasarnya 'katalog.html' merupakan template HTML, maka saya melakukan penyesuaian pada file ini agar tampilan HTML dapat berubah-ubah (dynamis) tergantung dengan data-data yang diberikan oleh fungsi 'show_katalog', seperti nama, student id, dan data yang telah diambil dari database menggunakan bantuan models.py. Beberapa penyesuaian yang saya lakukan diantaranya adalah menambahkan syntax '{{nama}}' dan '{{id}}' agar nama dan id yang muncul nanti akan bergantung dengan data yang dimasukkan dalam fungsi 'show_katalog' di views.py.

- Poin 4. Setelah aplikasi katalog saya dapat berjalan di localhost dengan baik serta dengan tampilan yang sesuai dengan harapan, maka selanjutnya saya melakukan persiapan untuk melakukan deployment aplikasi ke Heroku. Hal pertama yang saya lakukan adalah menambahkan beberapa konfigurasi pada kode saya seperti yang saya lakukan sebelumnya pada Lab 0. Setelah itu, saya melakukan add, commit, serta push perubahan file project ke Github milik saya. Setelah berhasil melakukan push ke Github, saya membuat sebuah aplikasi baru di heroku. Selanjutnya, saya membuat repository secret baru yang berisi nama aplikasi beserta API Key heroku di repository github aplikasi katalog. Terakhir, saya menjalankan kembali workflow yang sebelumnya sempat gagal karena belum adanya konfigurasi pada repository secret. Akhirnya, aplikasi katalog berhasil untuk dideploy di Heroku.

## Referensi
- Agasthyan, Roy. (2017). Memahami Virutal Environments di Python. https://code.tutsplus.com/id/tutorials/understanding-virtual-environments-in-python--cms-28272
- Sukedy, Nanra. (2018). Mengenal Python Virtual Environment. https://nanrasukedy.medium.com/mengenal-python-virtual-environment-fc61e5d299d3