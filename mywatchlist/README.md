# Tugas 3 PBP (Pengimplementasian Data Delivery Menggunakan Django)

## Link Heroku

[Heroku](https://katalog-project-django.herokuapp.com/mywatchlist/)

[Heroku_HTML](https://katalog-project-django.herokuapp.com/mywatchlist/html/)

[Heroku_XML](https://katalog-project-django.herokuapp.com/mywatchlist/xml/)

[Heroku_JSON](https://katalog-project-django.herokuapp.com/mywatchlist/json/)

## Jawaban dari Pertanyaan

### 1. Jelaskan perbedaan antara JSON, XML, dan HTML!

#### JSON (JavaScript Object Notation)
- Merupakan format data untuk melakukan perturakan data ringan yang lebih mudah untuk diuraikan oleh komputer.
- Berasal dari JavaScript Language.
- Memiliki ukuran file yang lebih kecil karna tidak menggunakan end tag serta lebih mudah dibaca karena formatnya lebih menggambarkan dan menjelaskan data (format berupa map -> key: value).
- Mendukung array sebagai masukkan atau input dalam pertukaran data.
- Tidak mendukung adanya comment, namespaces, dan metadata.
- Tidak mendukung untuk melakukan pemrosesan atau perhitungan apapun.
- Hanya mendukung type data strings, numbers, arrays, booleans, dan objects. Objects pun hanya boleh mengandung primitive data types.
- Encoding menggunakan UTF & ASCII.
- Memiliki keamanan yang kurang baik jika dibandingkan dengan XML.
- Pertama kali dibuat pada tahun 2001.
- File diakhiri dengan ekstensi '.json'

#### XML (eXtensible Markup Language)
- Merupakan bahasa markup (memiliki tag untuk mendefinisikan elemen) yang memiliki fungsi untuk melakukan pertukaran data tetapi lebih sulit untuk diuraikan oleh komputer.
- Berasal dari SGML.
- Memiliki ukurann file yang lebih besar karena memiliki lebih banyak tag dan memiliki struktur data yang jelas sehingga membantu dalam konfigurasi dinamis dan pemuatan variable ketika melakukan pertukaran data (format berupa tree structure, sehingga akan banyak tag yang muncul)
- Tidak mendukung array sebagai masukkan atau input dalam pertukaran data.
- Mendukung adanya comment, namespaces, dan metadata.
- Mendukung untuk melakukan pemrosesan serta pemformatan dokumen dan objek.
- Mendukung banyak complex data types, seperti charts, images, dan nom-primitive data types lainnya.
- Encoding menggunakan UTF-8 dan UTF-16.
- Memiliki keamanan yang lebih baik jika dibandingkan dengan JSON.
- Pertama kali dibuat pada tahun 1998.
- File diakhiri dengan ekstensi '.xml'

#### HTML (Hyper Text Markup Language)
- Merupakan bahasa markup (memiliki tag untuk mendefinisikan elemen) untuk membuat halaman web, dimana HTML membuatnya dengan cara mendeskripsikan struktur dari halaman web tersebut.
- Tidak digunakan sebagai alat untuk melakukan pertukaran data.
- Elemen dari HTML akan memberitahu browser konten apa yang harus ditampilkan dan bagaimana konten tersebut ditampilkan.
- Mendukung adanya comment.
- Default encodingnya adalah UTF-8.
- Pertama kali dibuat pada tahun 1990.
- File diakhiri dengan ekstensi '.html'

### 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Dalam mengembangkan sebuah platform untuk aplikasi yang dinamis, tentu saja akan terjadi pertukaran data antara user dan server. Oleh karena itu, dibutuhkan suatu format file yang digunakan sebagai tempat atau wadah untuk pengiriman data (data delivery), agar pertukaran data yang terjadi dapat berjalan dengan baik dan cepat. Terdapat banyak sekali format file yang dapat digunakan untuk data delivery, diantaranya adalah XML dan JSON. XML dan JSON sendiri memiliki kelebihan dan kekurangannya masing-masing, sehingga dalam pengembangan platform perlu diperhatikan format file mana yang cocok dijadikan sebagai format file data delivery untuk platform yang akan dibuat.

Selain itu, dalam pengimplementasian sebuah platform terdapat kemungkinan untuk menerapkan prinsip cross-platform atau multi-platform. Oleh karena itu, dibutuhkan suatu format file data delivery agar memungkinkan terjadinya pertukaran data antar platform. Salah satu contohnya adalah ketika kita baru saja selesai membangun sebuah web platform dan kemudian ingin lanjut untuk membuat sebuah mobile platform untuk aplikasi yang sama, maka tentu saja data-data yang terdapat di web platform serta mobile platform tersebut haruslah sama. Oleh karena itu, harus dilakukan pertukaran data antar platform tersebut agar memiliki data yang sama. Pertukaran data dilakukan dengan bantuan format file data delivary agar pertukaran data dapat berjalan dengan baik serta cepat.

### 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Poin 1. Membuka CMD dan mengubah directory ke folder pbp-assignments, lalu menulis 'python manage.py startapp mywatchlist' untuk membuat aplikasi django baru bernama 'mywatchlist'. Setelah itu, saya menambahkan 'mywatchlist' di variable INSTALLED_APPS yang ada di settings.py project_django.

- Poin 2. Menambahkan path baru di urls.py folder project_django, yaitu path('mywatchlist/', include('mywatchlist.urls')), dan juga menambahkan path baru di urls.py folder mywatchlist, yaitu path('', show_mywatchlist, name='show_mywatchlist'), agar user dapat mengakses http://localhost:8000/mywatchlist. Hal ini dapat terjadi karena ketika user memasukkan URL http://localhost:8000/mywatchlist, maka program akan mengarahkan ke urls.py mywatchlist dan mengambil fungsi dari path dengan nama berupa string kosong (''). Selain itu, saya juga menambahkan fungsi baru di views.py mywatchlist bernama 'show_mywatchlist' yang akan diakses ketika user mengakses http://localhost:8000/mywatchlist, dimana fungsi 'show_mywatchlist' akan mengembalikan sebuah template HTML bernama 'mywatchlist.html', sehingga saya juga membuat sebuah file html sebagai template yang bernama 'mywatchlist.html'.

- Poin 3. Membuat sebuah class baru di models.py mywatchlist bernama 'MyWatchList' yang berisi variable 'watched' (boolean field), 'title' (text field), 'rating' (integer field), 'release_date' (text field), dan 'review' (text field).

- Poin 4. Membuat folder baru bernama 'fixtures' serta menambahkan file baru bernama 'initial_mywatchlist_data.json' yang berisi 10 data untuk object MyWatchList

- Poin 5. Membuat beberapa function baru di views.py mywatchlist ('show_mywatchlist_HTML', 'show_mywatchlist_XML', dan 'show_mywatchlist_JSON') yang masing-masing akan bertugas untuk menyajikan data dalam format HTML, XML, dan JSON. Selanjutnya, saya membuat sebuah file HTML baru untuk dijadikan sebagai template ketika user ingin menyajikan data menggunakan HTML (hanya data saja yang ditampilkan), file html tersebut bernama 'html_mywatchlist.html'. Terakhir, saya menambahkan path baru di urls.py mywatchlist ('path('html/', show_mywatchlist_HTML, name='show_mywatchlist_HTML')', 'path('xml/', show_mywatchlist_XML, name='show_mywatchlist_XML')', 'path('json/', show_mywatchlist_JSON, name='show_mywatchlist_JSON')') agar user dapat mengakses http://localhost:8000/mywatchlist/html untuk mengakses mywatchlist dalam format HTML, http://localhost:8000/mywatchlist/xml untuk mengakses mywatchlist dalam format XML, dan http://localhost:8000/mywatchlist/json untuk mengakses mywatchlist dalam format JSON.

- Poin 6. Menambahkan '&& python manage.py loaddata initial_mywatchlist_data.json' di variable release di file Procfile agar heroku melakukan load data object MyWatchList yang sudah dibuat sebelumnya. Selanjutnya, saya melakukan push ke github dan aplikasi mywatchlist berhasil dideploy di Heroku.

## Screenshot Postman
### 1. http://localhost:8000/mywatchlist/html
![html](https://user-images.githubusercontent.com/87516736/191299185-c6d184ac-1186-465b-a97d-ab026509afa0.png)

### 2. http://localhost:8000/mywatchlist/xml
![xml](https://user-images.githubusercontent.com/87516736/191299427-da1775db-f465-49ea-92b1-f99e24e0d4b9.png)

### 3. http://localhost:8000/mywatchlist/json
![json](https://user-images.githubusercontent.com/87516736/191299517-afb409c8-9125-42a7-9c17-05d65ab024c3.png)

## Referensi
- Krishnan, Abhimanyu. (2022). JSON vs XML in 2022: Comparing Features and Examples. https://hackr.io/blog/json-vs-xml