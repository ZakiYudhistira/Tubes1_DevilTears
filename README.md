# Tugas Besar IF2211
## Implementasi Algoritma Greedy dalam Permainan Etimo Diamonds
Kelompok--Devil_Tears
| NIM | Nama |
| ------ | ------ |
| 10023608 | Tazkirah Amaliah |
| 13522031 | Zaki Yudhistira Candra |
| 13522059 | Dzaky Satrio Nugroho |

## Algortima Greedy

Algoritma greedy merupakan algortima pemecahan masalah yang bersifat rakus. Algoritma ini memprioritaskan penyelesaian elemen-elemen tertentu.

## Implementasi

Urutan Prioritas (By distance / Jarak)  :
1. Diamonds
2. Reset Button 
3. Bila diamonds == 5 return to base

## Requirements
- Python 3.9.X
- Node js / yarn
- Docker

## Installation

1. Ikuti instruksi pada docs berikut:
[Get Started with Diamonds](https://docs.google.com/document/d/1L92Axb89yIkom0b24D350Z1QAr8rujvHof7-kXRAp7c/edit)
2. Navigasi pada folder bot, dan masukkan command berikut pada terminal
```sh
py main.py --logic MyBot --email=random@email.com --name=nama1 --password=123456 --team etimo
```
3. Amati pergerakan bot

## Susunan file
```
├───README.md
│
├───doc  
│   ├─── Devil Tears.pdf
│                      
├───src                                             
    ├── tubes1-IF2211-bot-starter-pack-1.0.1        
        ├─── game
             ├─── logic 
                  ├─── MyBot.py
                  ├─── random.py
             ├─── __init__.py 
             ├─── api.py 
             ├─── board_handler.py 
             ├─── bot_handler.py 
             ├─── models.py 
             ├─── util.py 
        ├─── decode.py
        ├─── main.py
        ├─── README.md
        ├─── requirements.txt
        ├─── run-bots.bat
        ├─── run-bots.sh
```