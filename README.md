# Tugas Post Test 2
## Jump Search

#### Cara Kerja Program
Jump Search bekerja dengan membagi array menjadi bagian-bagian yang sama ukurannya, yang disebut blok. Selanjutnya, algoritma akan melompat dari blok ke blok secara linear, dengan interval atau step yang tetap dan optimal, hingga elemen yang dicari ditemukan atau batas akhir array dicapai. Jika elemen yang dicari terdapat pada blok tertentu, Jump Search kemudian melakukan pencarian linear pada blok tersebut. Jika elemen tidak ditemukan dalam blok manapun, maka program akan mengeluarkan hasil "element not found"

#### Fungsionalitas Algoritma
Fungsionalitas utama dari jump search adalah untuk mencari elemen tertentu dalam array yang diurutkan secara efisien dan dengan kompleksitas waktu yang rendah. Pencarian linier (liniear search) melakukan pencarian elemen dalam array satu persatu. Dengan algoritma ini menghindari pencarian linier pada seluruh array dan melompati blok-blok tertentu untuk mempercepat proses pencarian, sehingga akan lebih menghemat waktu

#### Elemen - Elemen dalam Program

###### Line 1 - 2
Menggunakan library os untuk merapihkan tampilan output.

###### Line 4
Deklarasi array "arr" dengan value ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]].

###### Line 6
Deklarasi fungsi jump search dengan parameter "arr" dan "x".

###### Line 8 
Deklarasi variabel "n" sebagai panjang dari "arr".

###### Line 10
Deklarasi variabel "step" sebagai interval atau langkah tetap untuk melompat dari blok satu ke blok lain.

###### Line 13
Deklarasi variabel "start" yang fungsinya akan menjadi pembentuk blok di dalam array. Di sini di isi dengan nilai 0 karena pencarian dimulai dari array index paling kiri (index ke 0).

###### Line 16 - 26
Di sini dilakukan pencarian elemen, dengan cara membandingkan nilai step. Selama nilai step lebih kecil dari x (nilai yang dicari), maka disitu kita tahu kalau x tidak ada di blok tersebut. Maka dari itu step akan bertambah. Jika step lebih dari x, maka perulangan akan terhenti dan masuk ke baris kode selanjutnya.

###### Line 30 - 35
Setelah diketahui elemen x di dalam suatu blok, maka kita melakukan linear search di dalam blok tersebut. Jadi selama arr[start] kurang dari x, maka start akan terus ditambah. Tapi jika start sudah menyentuh n, berarti elemen x tidak ditemukan dan akan mengembalikan nilai -1.

###### Line 36 - 42
Jika nilai arr[start] bertipe data list, maka kita lakukan perulangan di situ untuk menemukan elemen di dalam list yang terdapat dalam list (nested list/list bersarang). Lalu kita kembalikan nilai index dan kolom-nya.

###### Line 45 - 46
Mengecek apakah elemen yang dicari adalah elemen yang sesuai.

###### Line 48
Return -1 jika (element not found) jika dari kesemuanya tidak berhasil ditemukan.

###### Line 50
Deklarasi variabel "x" sebagai nilai elemen yang ingin dicari.

###### Line 51
Menampilkan (output) array "arr".

###### Line 52
Deklarasi variabel "result" untuk menampung hasil dari fungsi jump search.

###### Line 54 - 59
Jika "result" bernilai -1, berarti elemen tidak ada/tidak ditemukan. Jika "result" bertipe data tuple, maka tampilkan posisi elemen yang di dalam nested list. Jika "result" bertipe data integer dan selain -1, maka tampilkan posisinya di dalam list tersebut.
