<?php
$host = "localhost";
$username = "root";
$password = "15haziran";
$database = "newproje";

// Bağlantıyı oluştur
$connection = mysqli_connect($host, $username, $password, $database);

// Karakter setini ayarla
mysqli_set_charset($connection, "utf8");

// Bağlantıyı kontrol et
if (!$connection) {
    die("Connection failed: " . mysqli_connect_error());
}
// echo "Connected successfully"; // Bağlantı mesajını kaldırdık, prodüksiyon ortamında gereksiz olabilir.
?>
