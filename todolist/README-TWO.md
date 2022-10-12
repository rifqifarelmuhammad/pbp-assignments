# Tugas 6 PBP (Javascript dan AJAX)

## Jawaban dari Pertanyaan Tugas 6

### 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Asynchronous programming adalah model programing yang bersifat multithreaded (bisa digunakan oleh lebih dari satu user tanpa membutuhkan duplikasi program yang sedang dijalankan). Asynchronous programming bersifat non-blocking (tidak memblokir eksekusi proses lain saat mengeksekusi suatu proses) sehingga program dapat dijalankan secara concurrent yang membuat program tidak perlu menunggu menyelesaikan suatu tugas terlebih dahulu untuk mengerjakan tugas lain.
- Synchronous programming adalah model programming yang bersifat single-thread (hanya dapat menjalankan satu eksekusi setiap waktu). Synchronous programming bersifat blocking (memblokir eksekusi proses lain saat mengeksekusi suatu proses) sehingga program berjalan secara sequential yang membuat program perlu menunggu menyelesaikan suatu tugas terlebih dahulu untuk mengerjakan tugas lain.

## 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah suatu paradigma yang memungkinkan setiap objek dan lain sebagainya berkomunikasi satu sama lain secara tidak langsung (melalui perantara berupa event) sehingga suatu program akan dieksekusi berdasarkan event yang terjadi. Salah satu contoh penerapannya pada tugas kali ini adalah ketika user telah mengisi title dan descripton Task pada modal Add Task, kemudian user menekan tombol 'Add task' maka fungsi akan langsung dijalankan (eventnya berupa click button Add task).

## 3. Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX terjadi ketika program tidak perlu mereload halaman html ketika terjadi request dari user (contohnya perubahan data). Di dalam tugas 6 ini, kita dapat melihat penerapan asynchronous programming pada AJAX ketika kita menambahkan serta mendelete task. Ketika menambahkan task, program akan langsung menambahkan card task tanpa perlu mereload halaman, begitu juga dengan mendelete task.

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat fungsi 'return_data_JSON' di views.py yang akan mengembalikan seluruh data task dari user yang login dalam bentuk JSON. Kemudian saya Menambhahkan path '/json' yang mengarah ke function 'return_data_JSON'. Selanjutnya, saya menerapkan AJAX GET dengan menggunakan konsep for loop sehingga saya dapat mengakses seluruh data dalam data json tersebut dan menambahkan cardnya menggunakan format HTML dan menampilkannya ke halaman todolist.
- Membuat button 'Add Task' yang menampilkan modal berisi form create task. Selanjutnya saya membuat function 'add_task' yang akan membuat task baru dan menyimpannya ke database dan mengembalikan json yang berisi data dari task baru tersebut. Kemudian saya menambahkan card baru secara otomatis menggunakan data yang dikirimkan oleh function 'add_task' agar user tidak perlu mereload halaman terlebih dahulu untuk menambahkan card task.