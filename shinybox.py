#mines needs portrait updates

import time
import tkinter as tk
import random
from pygame import mixer
from tkinter import messagebox
import tkinter.font as font

mixer.init()
ai_shinybox=mixer.Sound("shinybox.mp3")
ai_shinybox.play()
jingle=mixer.Sound("shinythings.mp3")
unlock_sound=mixer.Sound("portatom.mp3")
no_library_card=mixer.Sound("no_lib_card.mp3")
shinybox_win=mixer.Sound("shinyWIN.mp3")

class Player:
    def __init__(self):
        self.shiny_things = 0
        self.shiny_things_discarded = 0
        self.pigeons = 0

            #headlamp tree
        self.shinybox_unlock = False
        self.headlamp = False
        self.headlamp = 0
        self.headlamp_charge = 0
        self.headlamp_charged = False
        self.discard_unlock = False
        self.trader_unlock = False
        self.trader_button = None
        self.batteries = 0
        self.lemons = 0
        self.lemons_unlock = False
        self.vending_machine_unlock = False
        self.vending_machine_on = False
        self.cave_unlock = False
        self.dwarf_talk_flag = False
        self.rockcandy = 0
        self.rockcandy_check = 0
        self.rockcandy_flag = False

    #canary and library card tree
        self.lie_button_flag = False
        self.farmer_quest_on = False
        self.crow_bribed = False
        self.birdcage_number = 0
        self.birdcage = False
        self.birdcage_button_flag = False
        self.sticks = 0
        self.canary_number = 0
        self.canary = False
        self.ram_sticks = 0
        self.nerd_quest = False
        self.ram_sticks_check = 0
        self.library_card = False
        self.library_card_number = 0
        self.library_fee_paid = False

    #codex tree and pickaxe tree
        self.has_book = False
        self.has_codex = False
        self.codex_permflag = False
        self.codex = 0
        self.book_1_flag = False
        self.book_2_flag = False
        self.book_3_flag = False
        self.book_4_flag = False
        self.book_5_flag = False
        self.book_6_flag = False
        self.book_7_flag = False
        self.book_8_flag = False
        self.book_9_flag = False
        self.book_10_flag = False
        self.book_11_flag = False
        self.book_12_flag = False
        self.has_pickaxe = False
        self.pickaxe = 0

    #mines
        self.gold_bar = False
        self.gold_bar_count = 0
        self.shinybox = 0

    
        self.trader = str(r'''
  *******  
  *  ^  *  
  *  $  *  
  * --- *  
************* 
 /        \ 
 |  O O    | 
 \  ~~~~   /  
  \_______/   ''')

        self.lemontree = str(r'''
  vvvvvvvvvvv 
 vvvvvvvvvvvvv
vvvvvvvvvvvvvv
vvvvvvvvvvvvvv
 vvvvvvvvvvvvv
  vvvvvvvvvvv 
      vvv   | 
      vvv  (L)
  n   vvv     
  v   vvv     
 /O\  vvv     
  w   vvv     ''')

        self.vending_machine = str(r'''
______________
|____________|
|__VENDING|__|
|__|MACHINE__|
|-T-|--O-|-U-|
|---|----|---|
|-C-|--H-|-!-|
|------------|
|__|INSERT|__|
|__|SHINY*|__|''')
        
        self.cave = str(r'''
    ######    
  ##########  
 ############ 
##############
#####CAVE#####
##############
##############
##############
##############
##############
''')
        self.mines_entrance = str(r'''
y   ######   Y
o ########## o
|############|
##############
#####MINES####
######XXX#####
#####X...X####
####X.....X###
####X.....X###
###XX.....XX##
''')
        self.mines_1 = str(r'''
    ######    
  ##########  
 ############ 
##############
##############
######XX######
#####X**X#####
####X****X####
####X****X####
####X****X####
''')
        self.mines_deadend = str(r'''
    ######    
  ##########  
 ############ 
##############
##############
##############
##############
##############
##############
##############
''')
        self.mines_locked_door = str(r'''
|------------|
|  G.LD SM!-H|
|  INC.      |
|  AUTHORIZED|
|  PERSONELL |
|            |
|   [1][2][3]|
|   [4][5][6]|
|   [7][8][9]|
L____________|
''')
        self.mines_unlocked_door = str(r'''
|----------|#|
|G.LD SM!-H|#|
|INC.      |#|
|AUTHORIZED|#|
|PERSONELL |#|
|          |#|
| [1][2][3]|#|
| [4][5][6]|#|
| [7][8][9]|#|
L__________|#|
''')
        self.gold_mines = str(r'''
    ######    
  ##########  
 ############ 
##############
##############
#####GOLD#####
#####X**X#####
####X****X####
####X****X####
####X****X####
''')

        
        self.dwarf = str(r'''
    _______  
   /       \  
  /         \ 
  |___(Q)____|
  xxWWWxWWWxx 
 xxx(o)x(o)xxx
xxxxxx\ /xxxxx
xxxxxx\v/xxxxx
 xxxxxxxxxxxx 
   xxxxxxxxx  
''')

        self.farmer = str(r'''
       __     
      /  \    
     /    \   
(____________)
  WWWWWWWWWWW 
  ...O...O... 
 ......\/.... 
 ...wwwwwwwW. 
  ..WW....WW. 
    W......W  
''')

        self.pawnshop = str(r'''
|____________|
|------------|
|--PAWNSHOP--|
|------------|
|____________|
|-|_|_|_|_|_||
|------------|
|-|   |   |--|
|-|  .|.  |--|
|_|___|___|__|
''')
        self.library = str(r'''
|____________|
|------------|
|---LIBRARY--|
|------------|
|____________|
|-|x|-|x|-|x||
|------------|
|----|===|=--|
|----|  .|---|
|____|___|___|
''')
        self.librarian = str(r'''
       WWWW   
       W   W  
    WWWWWWW W 
   WWWWWWWWW W
  WWWWWWWWWWW 
  ~__Q-|-Q__~ 
  .....|....  
   ..,.U....  
    .\___/.   
     .....    
''')
        self.book_1_art = str(r'''
 ____________ 
||   HAIKU   |
||    by     |
||Rodanbobtha|
||niel       |
||Oldenbarkey|
||talyhoo    |
||Smithwicktu|
||rnupshire  |
||___________|
''')
        self.book_2_art = str(r'''
 ____________ 
||           |
||  Diary    |
||   of      |
||    a      |
||           |
||  PRO-     |
||crastinator|
||           |
||___________|
''')

        self.book_3_art = str(r'''
 ____________ 
||           |
|| DIOGENES  |
||           |
||           |
||~~~~~~~~~~~|
||           |
||    by     |
|| Diogenes  |
||___________|
''')
        self.book_4_art = str(r'''
 ____________ 
||           |
|| CALL of   |
|| the CHILD |
||           |
||___________|
||   by      |
||  Quack    |
||   London  |
||___________|
''')
        self.book_5_art = str(r'''
 ____________ 
|   FEAR &   |
|  LOATHING  |
|     in     |
|  Las SHINY |
|------------|
|    by      |
|   Hunter   |
| O Shinies |
|____________|
''')
        self.book_6_art = str(r'''
 ____________ 
|            |
| Programming|
| P Y T H O N|
|            |
|            |
|   by       |
| Guido von  |
|   Shinum   |
|____________|
''')
        self.book_7_art = str(r'''
 ____________ 
|            |
| SPELUNKING |
|     | |    |
|     | |    |
|_____\V/____|
|            |
|    by      |
|   Notch    |
|____________|
''')
        self.book_8_art = str(r'''
 ____________ 
|            |
|   DWARVES  |
|    xxxx    |
|            |
|____________|
|            |
|    by      |
|   Dwarves  |
|____________|
''')
        self.book_9_art = str(r'''
 ____________ 
|            |
|~~~~BOOK~~~~|
|~~~~~of~~~~~|
|~~~METALS~~~|
|~~~~~~~~~~~~|
|     by     |
| Gold Smith |
|     Fox    |
|____________|
''')
        self.book_10_art = str(r'''
 ____________ 
|            |
| ORNITHOLOGY|
|          o |
|          v |
|____________|
|     by     |
|    the     |
| Unbirdened |
|____________|
''')
        self.book_11_art = str(r'''
 ____________ 
|            |
|    How To  |
|  Not Suck  |
|   At VIDEO |
|    GAMES   |
|            |
|     by     |
|the internet|
|____________|
''')
        self.book_12_art = str(r'''
 _______~    
|         ~  
|    Shi-~ 
|       Magi~
|       Secre!
|____________|
|        Infi|
|         O~ !
|        ~    
|_______~     
''')
        self.book_codex_art = str(r'''
 ____________ 
|            |
|   ANCIENT  |
|   DWARVEN  |
|    CODEX   |
|     by     |
|   ANCIENT  |
|    CODEX   |
|   DWARVES  |
|____________|
''')

        self.nerd = str(r'''
              
              
    ~~~~~~~   
   ~~~~~~~~~  
  ~~^^^~~^^^~ 
  ~--O----O-~ 
  .,...\/..,. 
  ...,....... 
  ....(==).,. 
    ,.......  
''')


        self.spooky_woods = str(r'''
...^.....^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||spooky||..
...^woods^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_fork = str(r'''
...^.....^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_L1 = str(r'''
...^.....^....
.v^^^...^^^...
.^^^^^.^^^v^..
^^^v^^^^^^^^^^
..||......||..
...^.....^..v.
..^^^...^^^...
.^v^^^.^^^^^..
^^^^^^^^^^^^^^
..||.....||...
''')


        self.spooky_woods_L2_A = str(r'''
...^..v..^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^v^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^v^^^.^^^^^..
^^^^^^^^^^^v^^
..||.....||...
''')

        self.spooky_woods_L2_B = str(r'''
...^.....^....
..v^^...^^^...
.^^^^^.^^^^v..
^^^^^^^^^^^^^^
..||v.....||..
...^.....^....
v.^^^...^^^...
.^^^^^.^^v^^..
^^^^^^^^^^^^^^
..||.....||...
''')
        self.current_spooky_index_L2 = ["spooky_woods_L2_A 1", "spooky_woods_L2_B 2"]


        self.spooky_woods_L3_A = str(r'''
...^.....^....
..^^^...^^^v..
.^^^^^.^^^^^..
^^^^^v^^^^^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^^^^^.^^^^v..
^^v^^^^^^^^^^^
..||.....||...
''')

        self.spooky_woods_L3_B = str(r'''
...^.....^....
..^^^...^^v...
.^^^^v.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^^^^^.^^^^^..
v^^^^^^^^^^^^^
..||.....||...
''')

        self.spooky_woods_L3_C = str(r'''
              
      ....    
    ...S...   
 Y...........Y
  XXXXXXXXXXX 
  ...0...0... 
 .....|_|.... 
 .....\_/.... 
  ..W<><><>W. 
    V,,,,,V.  
''')

        self.spooky_woods_L3_D = str(r'''
...^.....^....
..^^^...v^^...
.^^^v^.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^v^^^.^^^^^..
^^^^^^^^^^^^^^
..||.....||...
''')
        self.current_spooky_index_L3 = ["spooky_woods_L3_A 1", "spooky_woods_L3_B 2", "spooky_woods_L3_C 3", "spooky_woods_L3_D 4"]


        self.spooky_woods_L4_A = str(r'''
...^.....^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^^v^^^
..||......||..
...^.....^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^v^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_L4_B = str(r'''
...^.....^....
..^^^...^^^...
.^^^^^.v^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..v^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^^v^^^
..||.....||...
''')
        self.spooky_woods_L4_C = str(r'''
....\\........
....(o>.......
\\_//)........
.\_/_)........
. _|_.........
''')
        self.spooky_woods_L4_D = str(r'''
...^.....^....
..^^^.v.^^^...
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..v^^...^^^..v
.^^^^^.^^^^^..
^^^^^^^^v^^^^^
..||.....||...
''')
        self.spooky_woods_L4_E = str(r'''
...^.....^....
..^^^..v^^^...
.^^^^^.^^^v^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^^^^^.^^^v^..
^^^^^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_L4_F = str(r'''
...^.....^....
..^v^...^^^v..
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^v....^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_L4_G = str(r'''
...^.....^....
..^^^...^^^...
.^^v^^.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..^^^...^^v...
.^^^^^.^^^^^..
v^^^^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_L4_H = str(r'''
...^.....^....
..^^^...^v^...
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^v^^^.^^^^^..
^^^^^^^^^^^^^^
..||.....||...
''')
        self.current_spooky_index_L4 = ["spooky_woods_L4_A 1", "spooky_woods_L4_B 2", "spooky_woods_L4_C 3", "spooky_woods_L4_D 4", "spooky_woods_L4_E 5", "spooky_woods_L4_F 6", "spooky_woods_L4_G 7", "spooky_woods_L4_H 8"]
        
        self.spooky_woods_R1 = str(r'''
...^.....^....
.v^^^...^^^...
.^^^^^.^^^v^..
^^^v^^^^^^^^^^
..||......||..
...^.....^..v.
..^^^...^^^...
.^v^^^.^^^^^..
^^^^^^^^^^^^^^
..||.....||...
''')

        self.spooky_woods_R2_A = str(r'''
...^.....^....
..v^^...^^^...
.^^^^^.^^^^v..
^^^^^^^^^^^^^^
..||v.....||..
...^.....^....
v.^^^...^^^...
.^^^^^.^^v^^..
^^^^^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_R2_B = str(r'''
...^..v..^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^v^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^v^^^.^^^^^..
^^^^^^^^^^^v^^
..||.....||...
''')
        self.spooky_woods_R3_A = str(r'''
...^.....^....
..^^^...^^v...
.^^^^v.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^^^^^.^^^^^..
v^^^^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_R3_B = str(r'''
...^.....^....
..^^^...^^^v..
.^^^^^.^^^^^..
^^^^^v^^^^^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^^^^^.^^^^v..
^^v^^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_R3_C = str(r'''
...o.....^.o..
..^^^...v^^...
o^^^v^o^^^^^oo
^^^^^^^^^^^^^^
oo||oo...o||oo
...^.....^....
..^^o...^^^...
.^v^^^.^^^^o..
o^^^^^^^^^^^^^
..||.....||...
''')

        self.spooky_woods_R3_D = str(r'''
...^.....^....
..^^^...^^^...
.^^^^^.^^v^^..
^^^^^^^^^^^^^^
..||.....v||..
...^.....^....
..^v^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^^^^v^
..||.....||...
''')
        self.spooky_woods_R4_A = str(r'''
...^.....^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^^v^^^
..||......||..
...^.....^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^v^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_R4_B = str(r'''
...^.....^....
..^v^...^^^v..
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^v....^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||.....||...
''')

        self.spooky_woods_R4_C = str(r'''
...^.....^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^^^^^^^^v^^^
..||......||..
...^.....^....
..^^^...^^^...
.^^^^^.^^^^^..
^^^v^^^^^^^^^^
..||.....||...
''')

        self.spooky_woods_R4_D = str(r'''
...^.....^....
..^^^...^v^...
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^v^^^.^^^^^..
^^^^^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_R4_E = str(r'''
...^.....^....
..^^^.v.^^^...
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..v^^...^^^..v
.^^^^^.^^^^^..
^^^^^^^^v^^^^^
..||.....||...
''')
        self.spooky_woods_R4_F = str(r'''
...^.....^....
..^^^..v^^^...
.^^^^^.^^^v^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..^^^...^^^...
.^^^^^.^^^v^..
^^^^^^^^^^^^^^
..||.....||...
''')

        self.spooky_woods_R4_G = str(r'''
...^.....^....
..^^^...^^^...
.^^v^^.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..^^^...^^v...
.^^^^^.^^^^^..
v^^^^^^^^^^^^^
..||.....||...
''')
        self.spooky_woods_R4_H = str(r'''
...^.....^....
..^^^.v.^^^...
.^^^^^.^^^^^..
^^^^^^^^^^^^^^
..||......||..
...^.....^....
..v^^...^^^..v
.^^^^^.^^^^^..
^^^^^^^^v^^^^^
..||.....||...
''')


    def debug_label_update(self):
        shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
        shiny_things_discarded_label.config(text=f"you threw {self.shiny_things_discarded} shiny things on the ground!")
        batteries_label.config(text=f"you have {self.batteries} batteries!")
        lemons_label.config(text=f"you have {self.lemons} lemons!")
        pigeons_label.config(text=f"you have {self.pigeons} pigeons!")
        rockcandy_label.config(text=f"you have {self.rockcandy} rockcandy!")
        headlamp_label.config(text=f"you have {self.headlamp} headlamp!")
        birdcage_label.config(text=f"you have {self.birdcage_number} birdcage!")
        canary_label.config(text=f"you have {self.canary_number} canary!")
        sticks_label.config(text=f"you have {self.sticks} sticks!")
        ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
        library_card_label.config(text=f"you have {self.library_card_number} library card!")
        codex_label.config(text=f"you have {self.codex} codex!")
        pickaxe_label.config(text=f"you have {self.pickaxe} pickaxe!")



    def increase_shiny_things(self):
        if self.pigeons == 1:
            self.shiny_things += 2
        elif self.pigeons == 2:
            self.shiny_things += 3
        elif self.pigeons == 3:
            self.shiny_things += 4
        elif self.pigeons == 4:
            self.shiny_things += 5
        elif self.pigeons == 5:
            self.shiny_things += 6
        elif self.pigeons == 6:
            self.shiny_things += 7
        elif self.pigeons == 7:
            self.shiny_things += 8
        elif self.pigeons == 8:
            self.shiny_things += 9
        elif self.pigeons == 9:
            self.shiny_things += 10
        elif self.pigeons >= 10:
            self.shiny_things += 11
        else:
            self.shiny_things += 1
        shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
        root.after(1000, self.increase_shiny_things)
            

        if pl_cl_instance.shiny_things >= 5 and self.discard_unlock == False:
            pl_cl_instance.unlock_discard()
        
        if pl_cl_instance.shiny_things >= 10 and self.trader_unlock == False:
            pl_cl_instance.unlock_trader()

        if pl_cl_instance.shiny_things >= 30 and self.lemons_unlock == False:
            pl_cl_instance.unlock_lemons()

        if pl_cl_instance.batteries >= 1 and self.vending_machine_unlock == False:
            pl_cl_instance.unlock_vending_machine()
            pl_cl_instance.unlock_cave()


    def unlock_discard(self):
        unlock_sound.play()
        discard_button = tk.Button(vendor_frame, text="throw some shiny things", command=self.discard, width=20)
        discard_button.grid()
        discard_button.configure(bg="#661daa", fg="white")
        self.discard_unlock = True
    def discard(self):
        if self.shiny_things >= 5:
            self.shiny_things -= (5)
            self.shiny_things_discarded += (5)
            shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
            shiny_things_discarded_label.config(text=f"you threw {self.shiny_things_discarded} shiny things on the ground!")
            jingle.play()
            vendor_portrait_label.config(text=f"you threw 5 shiny things on the ground! it made a jingle!")


    def unlock_trader(self):
        unlock_sound.play()
        trader_button = tk.Button(vendor_frame, text="trader", command=self.view_trader, width=20)
        trader_button.grid()
        trader_button.configure(bg="#cccccc", fg="blue")
        self.shinybox_unlock = True
        self.trader_unlock = True
    def view_trader(self):
        for widget in place_button_input_frame.winfo_children():
            widget.destroy()
        vendor_portrait_label.config(text=f"{self.trader}")
        vendor_dialog_label.config(text=f"trader: batteries for sale! get your batteries here! trading batteries!")
        batteries_button = tk.Button(place_button_input_frame, text="buy a battery", command=self.buy_batteries, bg="blue", fg="yellow")
        batteries_button.grid()
        pigeon_button = tk.Button(place_button_input_frame, text="buy a pigeon", command=self.buy_pigeons, bg="#f0ead6", fg="black")
        pigeon_button.grid()
        if self.shiny_things < 1000000:
            shinybox_button = tk.Button(place_button_input_frame, text="buy shinybox!\n(1,000,000\nshiny things)", command=self.buy_shinybox, width=10)
            shinybox_button.grid()
            shinybox_button.configure(bg="#bbbbbb", fg="#ffffff")
        elif self.shiny_things >= 1000000:
            shinybox_button = tk.Button(place_button_input_frame, text="buy shinybox!\n(1,000,000\nshiny things)", command=self.buy_shinybox, width=10)
            shinybox_button.grid()
            shinybox_button.configure(bg="gold", fg="white")
    def buy_batteries(self):
        if self.lemons >= 3:
            self.lemons -= 3
            self.batteries += 1
            vendor_dialog_label.config(text=f"trader: be careful with all that power now y'hear")
            batteries_label.config(text=f"you have {self.batteries} batteries!")
            lemons_label.config(text=f"you have {self.lemons} lemons!")
        else:
            vendor_dialog_label.config(text=f"trader: not enough lemons! go git more lemons!")
    def buy_pigeons(self):
        if self.shiny_things >= 50 and self.pigeons <= 9:
            self.shiny_things -= 50
            self.pigeons += 1
            vendor_dialog_label.config(text=f"trader: be careful with that bird now y'hear")
            shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
            pigeons_label.config(text=f"you have {self.pigeons} pigeons!")
        elif self.pigeons >= 10:
            vendor_dialog_label.config(text=f"trader: shinies be damned, i'm not giving you any more birds, what are you even doing with them?")
        else:
            vendor_dialog_label.config(text=f"trader: thats not enough shinies for this bird! you need more shinies!")
    def buy_shinybox(self):
        if self.shiny_things >= 1000000:
            self.shiny_things -= 1000000
            shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
            shinybox_win.play()
            self.shinybox += 1
            vendor_dialog_label.config(text=f"trader: be careful with all them shinies now y'hear")
            shinybox_label.config(text=f"you have the shinybox!")
            events_label.config(text=f"YOU WON SHINYBOX!")
            messagebox.showinfo("Yay!", "Congrats! You won shinybox! Thanks for playing!")
        else:
            vendor_dialog_label.config(text=f"trader: not enough shinies! go git more shinies!!")








    def unlock_lemons(self):
        unlock_sound.play()
        lemons_button = tk.Button(vendor_frame, text="lemontree", command=self.view_lemons, width=20)
        lemons_button.grid()
        lemons_button.configure(bg="#ead653", fg="#00720b")
        self.lemons_unlock = True
        
    def view_lemons(self):
        if self.farmer_quest_on == False:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.lemontree}")
            vendor_dialog_label.config(text=f"crow: shiny things for lemons caw caw! no shinies no lemon caw caw!")
            lemons_button = tk.Button(place_button_input_frame, text="buy a lemon", command=self.buy_lemons)
            lemons_button.grid()
            lemons_button.configure(bg="#ead653", fg="#00720b")
            if self.headlamp == True:
                talk_farmer_button = tk.Button(place_button_input_frame, text="speak to the farmer", command=self.firstspeak_farmer)
                talk_farmer_button.grid()
                talk_farmer_button.configure(bg="#ec9706", fg="#323a1f")
        elif self.farmer_quest_on == True and self.crow_bribed == False:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.lemontree}")
            vendor_dialog_label.config(text=f"crow: you shiny? caw caw, me lemon, give shiny! cawcaw give-shiny orrrr i-pluck-eye!!")
            talk_crow_button = tk.Button(place_button_input_frame, text="talk to the crow", command=self.talk_to_crow)
            talk_crow_button.grid()
            talk_crow_button.configure(bg="#ead653", fg="#00720b")
        elif self.farmer_quest_on == True and self.crow_bribed == True:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.lemontree}")
            vendor_dialog_label.config(text=f"crow: shh... crow not here...")
            talk_farmer_button = tk.Button(place_button_input_frame, text="speak to the farmer", command=self.firstspeak_farmer)
            talk_farmer_button.grid()
            talk_farmer_button.configure(bg="#ec9706", fg="#323a1f")

    def talk_to_crow(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.lemontree}")
        vendor_dialog_label.config(text=f"crow: crow want shiny!! pay shiny and crow leave!!")
        bribe_crow_button = tk.Button(place_button_input_frame, text="pay the crow (2,500 shinies)", command=self.bribe_crow)
        bribe_crow_button.grid()
        bribe_crow_button.configure(bg="#ead653", fg="#00720b")

    def bribe_crow(self):
        if self.shiny_things >= 2500 and self.crow_bribed == False:
            self.shiny_things -= 2500
            shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
            vendor_dialog_label.config(text=f"crow: crow always get shinies! easy lemons! ckRAW-ckRAW-ckRAW-ckRAW- *cackles*")
            self.crow_bribed = True
        elif self.crow_bribed == True:
            vendor_dialog_label.config(text=f"crow: [lie] crow leave crow leave! you leave! crow pack!")
        else:
            vendor_dialog_label.config(text=f"crow: crow make lemon out of face!! get more shinies!!")

            
    def buy_lemons(self):
        if self.shiny_things >= 60:
            self.shiny_things -= 60
            self.lemons += 1
            vendor_dialog_label.config(text=f"crow: lemon lemon for you you caw caw!")
            shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
            lemons_label.config(text=f"you have {self.lemons} lemons!")
        else:
            vendor_dialog_label.config(text=f"crow: you shine shine caw! me lemon caw caw caw! bring more shinies!")
            
    def firstspeak_farmer(self):
        if self.crow_bribed == False and self.farmer_quest_on == False:
            vendor_portrait_label.config(text=f"{self.farmer}")
            vendor_dialog_label.config(text=f"farmer: someone needs to get rid of that damn bird\ni haven't been able to pick any lemons in weeks\nhelp a poor old rawhide out\n")
            if self.lie_button_flag == False:
                lie_button = tk.Button(place_button_input_frame, text="(lie) i will help you", command=self.accept_farmer_quest)
                lie_button.grid()
                lie_button.configure(bg="black", fg="red")
                self.lie_button_flag = True
        elif self.crow_bribed == True and self.farmer_quest_on == True:
            vendor_portrait_label.config(text=f"{self.farmer}")
            vendor_dialog_label.config(text=f"farmer: what? he's gone?\nyou couldn't wrangle a longhorned goose in a concrete basement could you, 'll whippersnapper?\nkeep the cage, you come across that damn bird you bring him here\n")
            take_birdcage_button = tk.Button(place_button_input_frame, text="take BIRDCAGE", command=self.accept_farmer_quest)
            self.birdcage = True
            birdcage_label.config(text=f"you have {self.birdcage_number} birdcage!")

            unlock_sound.play()
            pawnshop_button = tk.Button(vendor_frame, text="pawnshop", command=self.view_pawnshop, width=20) #pawnshop*
            pawnshop_button.grid()                      #library*
            pawnshop_button.configure(bg="#bcbcbc", fg="gold")                                       #spooky_woods* woods* wood*
            library_button = tk.Button(vendor_frame, text="library", command=self.view_library, width=20)
            library_button.grid()
            library_button.configure(bg="navyblue", fg="white")
            spooky_woods_button = tk.Button(vendor_frame, text="spooky woods", command=self.view_spooky_woods, width=20)
            spooky_woods_button.grid()
            spooky_woods_button.configure(bg="#242624", fg="#126b25")
            self.farmer_quest_on = False
        elif self.crow_bribed == True and self.farmer_quest_on == False:
            vendor_dialog_label.config(text=f"farmer: uh, thanks for the 'help', kid, iyull get mah own dinner")
        else:
            vendor_dialog_label.config(text=f"farmer: go get that bird!!!")
    def accept_farmer_quest(self):
        vendor_portrait_label.config(text=f"{self.farmer}")
        vendor_dialog_label.config(text=f"farmer: good deal sonny, take this birdcage and bring him back to me,\ni want to eat him for dinner tonight... over lemons")
        self.farmer_quest_on = True
        if self.birdcage_button_flag == False:
            take_birdcage_button = tk.Button(place_button_input_frame, text="take BIRDCAGE", command=self.take_birdcage)
            take_birdcage_button.grid()
            take_birdcage_button.configure(bg="green", fg="white")
            self.birdcage_button_flag = True
    def take_birdcage(self):
        vendor_portrait_label.config(text=f"{self.farmer}")
        if self.birdcage == True:
            vendor_dialog_label.config(text=f"farmer: i ain't herdin' birds\ntake the dag'on cage")
        else:
            vendor_dialog_label.config(text=f"farmer: go get me mah dinner")
            self.birdcage_number += 1 #added cage here, but in firstpeak farmer it actually becomes true
            birdcage_label.config(text=f"you have {self.birdcage_number} birdcage!")






    def view_pawnshop(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.pawnshop}")
        vendor_dialog_label.config(text=f"pawnshop: y'hello *grumbles* what do you want?")
        convert_init_button = tk.Button(place_button_input_frame, text="flip sticks", command=self.convert_sticks)
        convert_init_button.grid()
        convert_init_button.configure(bg="#bcbcbc", fg="gold")
        if self.gold_bar == True:
            sell_gold_button = tk.Button(place_button_input_frame, text="sell some gold", command=self.sell_gold)
            sell_gold_button.grid()
            sell_gold_button.configure(bg="#bcbcbc", fg="gold")

    def sell_gold(self):
        vendor_portrait_label.config(text=f"{self.pawnshop}")
        if self.gold_bar_count >= 1:
            vendor_dialog_label.config(text=f"pawnshop: lay out ya gold on the scale\n")
            self.gold_bar_count -= 1
            gold_bar_label.config(text=f"you have {self.gold_bar_count} gold chunks!")
            self.shiny_things += 10000
            shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
        elif self.gold_bar_count <= 0:
            vendor_dialog_label.config(text=f"pawnshop: go get some gold kid, quit wasting my time\n")
            self.gold_bar_count -= 1
            gold_bar_label.config(text=f"you have {self.gold_bar_count} gold chunks!")
            self.shiny_things += 10000
            shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
    def convert_sticks(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.pawnshop}")
        vendor_dialog_label.config(text=f"pawnshop: lay 'em out on the counter but don't scratch it\n")
        convert_init_button = tk.Button(place_button_input_frame, text="flip sticks", command=self.convert_sticks)
        convert_init_button.grid()
        convert_init_button.configure(bg="#bcbcbc", fg="gold")
        if self.sticks >= 3:
            self.sticks -= 3
            sticks_label.config(text=f"you have {self.sticks} sticks!")
            self.ram_sticks += 1
            ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
            vendor_dialog_label.config(text=f"pawnshop: i sell plasma tv's for 50 shinies and dirty dish rags for 5 shinies,\nsticks for sticks is what you get kid\nnow i need your ID...")
        elif self.sticks < 3:
            vendor_dialog_label.config(text=f"pawnshop: not enough sticks! get out of here if you ain't got valuables!")







    def view_library(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.library}")
        vendor_dialog_label.config(text=f"it's an entrance to the library")
        enter_library_button = tk.Button(place_button_input_frame, text="enter library", command=self.enter_library)
        enter_library_button.grid()
        enter_library_button.configure(bg="navyblue", fg="white")
        speak_to_nerd_button = tk.Button(place_button_input_frame, text="speak to the nerd", command=self.firstspeak_nerd)
        speak_to_nerd_button.grid()
        speak_to_nerd_button.configure(bg="#ffba26", fg="#000000")

    def enter_library(self):
        vendor_portrait_label.config(text=f"{self.library}")
        if self.library_card == True and self.library_fee_paid == False:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.librarian}")
            vendor_dialog_label.config(text=f"hey, you! i don't remember you, but it says here you owe 10,000 shinies for the late fees!\nmy computer says you checked out a LOT of books and never returned them!")
            pay_library_fee_button = tk.Button(place_button_input_frame, text="pay 10,000 shinies", command=self.pay_library_fee)
            pay_library_fee_button.grid()
            pay_library_fee_button.configure(bg="navyblue", fg="white")
            convince_librarian_button = tk.Button(place_button_input_frame, text="try to tell her\nit's not your card", command=self.convince_librarian)
            convince_librarian_button.grid()
            convince_librarian_button.configure(bg="navyblue", fg="white")       
        elif self.library_card == True and self.library_fee_paid == True:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.librarian}")
            vendor_dialog_label.config(text=f"yes hello welcome to the library")
            checkout_book_button = tk.Button(place_button_input_frame, text="check out a book", command=self.checkout_book)
            checkout_book_button.grid(row=0, column=0)
            checkout_book_button.configure(bg="navyblue", fg="white", width=14)
            return_book_button = tk.Button(place_button_input_frame, text="return a book", command=self.return_book)
            return_book_button.grid(row=0, column=1)
            return_book_button.configure(bg="navyblue", fg="white", width=14)          
        elif self.library_card == False:
            vendor_dialog_label.config(text=f"library: ENGH! no access without library card!")
            no_library_card.play()
            
    def pay_library_fee(self):
        if self.shiny_things >= 10000 and self.library_fee_paid == False:
            self.shiny_things -= 10000
            shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
            vendor_dialog_label.config(text=f"librarian: it's about time someone paid up on a late fee, now HUSH UP and GET TO READING!! SHHHHH!!!!!!")
            self.library_fee_paid = True
        elif self.library_fee_paid == True:
            vendor_dialog_label.config(text=f"librarian: you're paid up you blabbermouth, i'm trying to read laura ingles wilder!! SHHHHHH!")
        else:
            vendor_dialog_label.config(text=f"librarian: ENGH! that's the POOR PEOPLE ALERT!\nthat's not enough shinies to cover this tab!\nNOW SHHH! PEOPLE ARE TRYING TO READ!!")
            no_library_card.play()

    def convince_librarian(self):
        vendor_portrait_label.config(text=f"{self.librarian}")
        vendor_dialog_label.config(text=f"that's not what the machine says, either pay up or get out, we don't let poor people read here\nyou'll probably just steal our books for firewood; \nis that what you did with all those books on quantum information science?\never heard of a STICK? TRY BURNING THOSE.")
        
            
    def checkout_book(self):
        vendor_dialog_label.config(text=f"librarian: SHHHHH!!!!!! KEEP YOUR VOICE DOWN!!!\n") #books* book*
        
        book_1_button = tk.Button(place_button_input_frame, text="book 1", command=self.book_1)
        book_1_button.grid(row=1, column=0)
        book_1_button.configure(bg="navyblue", fg="white", width=14)
        
        book_2_button = tk.Button(place_button_input_frame, text="book 2", command=self.book_2)
        book_2_button.grid(row=1, column=1)
        book_2_button.configure(bg="navyblue", fg="white", width=14)
        
        book_3_button = tk.Button(place_button_input_frame, text="book 3", command=self.book_3)
        book_3_button.grid(row=2, column=0)
        book_3_button.configure(bg="navyblue", fg="white", width=14)
        
        book_4_button = tk.Button(place_button_input_frame, text="book 4", command=self.book_4)
        book_4_button.grid(row=2, column=1)
        book_4_button.configure(bg="navyblue", fg="white", width=14)
        
        book_5_button = tk.Button(place_button_input_frame, text="book 5", command=self.book_5)
        book_5_button.grid(row=3, column=0)
        book_5_button.configure(bg="navyblue", fg="white", width=14)
        
        book_6_button = tk.Button(place_button_input_frame, text="book 6", command=self.book_6)
        book_6_button.grid(row=3, column=1)
        book_6_button.configure(bg="navyblue", fg="white", width=14)
        
        book_7_button = tk.Button(place_button_input_frame, text="book 7", command=self.book_7)
        book_7_button.grid(row=4, column=0)
        book_7_button.configure(bg="navyblue", fg="white", width=14)
        
        book_8_button = tk.Button(place_button_input_frame, text="book 8", command=self.book_8)
        book_8_button.grid(row=4, column=1)
        book_8_button.configure(bg="navyblue", fg="white", width=14)
        
        book_9_button = tk.Button(place_button_input_frame, text="book 9", command=self.book_9)
        book_9_button.grid(row=5, column=0)
        book_9_button.configure(bg="navyblue", fg="white", width=14)
        
        book_10_button = tk.Button(place_button_input_frame, text="book 10", command=self.book_10)
        book_10_button.grid(row=5, column=1)
        book_10_button.configure(bg="navyblue", fg="white", width=14)
        
        book_11_button = tk.Button(place_button_input_frame, text="book 11", command=self.book_11)
        book_11_button.grid(row=6, column=0)
        book_11_button.configure(bg="navyblue", fg="white", width=14)
        
        book_12_button = tk.Button(place_button_input_frame, text="book 12", command=self.book_12)
        book_12_button.grid(row=6, column=1)
        book_12_button.configure(bg="navyblue", fg="white", width=14)

        if all([self.book_1_flag, self.book_2_flag, self.book_3_flag, self.book_4_flag, self.book_5_flag, self.book_6_flag, self.book_7_flag, self.book_8_flag, self.book_9_flag, self.book_10_flag, self.book_11_flag, self.book_12_flag]) and self.codex_permflag == False:
            self.create_book_codex_button()

    def create_book_codex_button(self):
        book_codex_button = tk.Button(place_button_input_frame, text="codex", command=self.book_codex)
        book_codex_button.grid(columnspan=2)
        book_codex_button.configure(bg="navyblue", fg="white")

    def book_1(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_1_art}")
            vendor_dialog_label.config(text=f"glistening sunlight gleams,\nsparkling treasures in its hold,\nshiny dreams unfold\n\nmoonlit sparkles dance,\nnight's jewels on silent waves,\nshiny dreams aglow")
            self.book_1_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_2(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_2_art}")
            vendor_dialog_label.config(text=f"huh... it's empty...")
            self.book_2_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_3(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_3_art}")
            vendor_dialog_label.config(text=f"Diogenes: by Diogenes\nDiogenes is the greatest philosopher of all time, and every philosopher who is OBJECTIVELY a good philosopher\nwould agree with this OBJECTIVELY TRUE statement. Diogenes is the MOST HONEST MAN in ALL OF GREECE. That is a FACT.\nYou are not even REMOTELY close to being as honest as m̶e̶ Diogenes.\nAll of Greece recommends DIOGENES as the greatest thinker ever, except that fool Plato.\nHe doesn't know anything. DON'T LISTEN TO PLATO.\n")
            self.book_3_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_4(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_4_art}")
            vendor_dialog_label.config(text=f"Call of the Child, by Quack London:\nIt was an early morning when Huffer woke up his mother to take him to the donut shop.\nHuffer was a big boy, the biggest of them all. He was born at a whopping 35 pounds.\nAt 7 years old, he stood 8'3 and weighed 380 pounds. In his heart, however, he was of course still a child.\n'come on MOM!!!!! lets go get some DONUTS!!!!' Huffer called.")
            self.book_4_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_5(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_5_art}")
            vendor_dialog_label.config(text=f"Fear & Loathing in Las Shiny by Hunter O Shinies:\nWe were somewhere around shinybox, on the edge of the desert, when the lemons began to take hold...\n")
            self.book_5_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_6(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_6_art}")
            vendor_dialog_label.config(text=f"Programming Python: by Guido Von Shiny\n1. do not assign values to variables, leaving variables variable means you can do what you want!\n2. create while loops without break conditions for infinite computer stuff!! its like the MATRIX!!\n3. don't learn any keyboard shortcuts, they just slow you down")
            self.book_6_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_7(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_7_art}")
            vendor_dialog_label.config(text=f"Spelunking by Notch: they say 'you see that mountain? you can climb it', but i say 'you see that hole?',\nwell, guess what, you can DIG it. that's right, no matter where you are in the world, you can always go DOWN.\ncan't say the same for up, can we? ha, that's what you get when you go taking on gravity like that.\nnow when you descend, do NOT take on gravity like that")
            self.book_7_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_8(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_8_art}")
            vendor_dialog_label.config(text=f"DWARVES: Dwarves are as long-haired and big-bearded as they are frothy.\nDespite the Dwarven kind living underground, Dwarves are not pale.\nThis is because each Dwarf takes a pilgrimage once a lifetime to see the sun;\nwithin one second, they become a burnt crisp and require a year to recover from the sunburn.\nAnd they NEVER LIE. That's a PROMISE.")
            self.book_8_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_9(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_9_art}")
            vendor_dialog_label.config(text=f"Book of Metals:\n1) Glorium 2) Brillium 3) Incandescium 4) Shinium 5) Reflectium 6) Lightium\n7) Brightium 8) Notnightium 9) Metalium 10) Gleamium 11) Glowium 12) Woahium\nnote from the author:\n'this is a comprehensive list of every single metallic element ever known,\ni know because i found it on the internet, so it has to be true' - gold smith fox")
            self.book_9_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_10(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_10_art}")
            vendor_dialog_label.config(text=f"Ornithology: by the Unbirdened\nThere are many kinds of birds. That's why we decided it was a stupid idea to try to classify them.\nI mean, they all fly right? So what's the point?\nSquawk chirp tweet, that's all you need to know.\nPlain and simple: inconvenience with wings.")
            self.book_10_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_11(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_11_art}")
            vendor_dialog_label.config(text=f"HOW TO NOT SUCK AT VIDEO GAMES: THE TOP 10 ULTIMATE GO-TO SUPER ULTRA GUIDE\nBY ULTIMATE MAXIMUM MLGPRO GAMERS\n1) try clicking harder\n2) try thinking faster\n3) try being better\n4) try more RGB lights\n5) try a ping of -1\n6) try removing profanity filters\n7) try subscribing to my channel\n8) try playing games 24 hours a day\n9) try physical exercise to strengthen your wrist for ultragaming\n10) try reading this list again\n\nOKAY NOW CHECK US OUT ON TWITCH! DONATE NOW!")
            self.book_11_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_12(self):
        if self.has_book == False:
            self.has_book = True
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_12_art}")
            vendor_dialog_label.config(text=f"Shinies: The H.dden Bcok Of Ma.ic~l Secr*7s / ~~au..or unknc,n~~ /\nD.ep bel`w t~e gr..nd li-`d a m-.`ical u`~nown be.,ded ra`e. They dis.-er-d a chasm deep below .h` wcr1d, fi1led with bri.`iant and\ngle-`ing met4ls accomp.`~ed by a shadowed race of unknown origin. .,~><.,.` sh~d..ed race took advantage of the\nmystical race fo. their physical essence .` ul`.-.tely m!ne and ca~t the 'shining things' i?`to obj..`s of desire.. ..,.~er time, labor deve1~.ed ,.to slavery,\n.nd the m,tals m~~e their way to the surface .,...,iscovered by us, the top-dwellers. And so cur s~`iety was bo,.,\nand with it came trade and c~~merc. ,.. )>nly few know, in the gu.,ed circles,\n=.~+e shiny things are cursed with occult deviations, .~~.,`.abor will drive those who !s r.led bw it to destruction;\na.,~,ey keep not the treasures they fastened for themselves.")
            self.book_12_flag = True
        else:
            vendor_dialog_label.config(text=f"you already have a book!")
            
    def book_codex(self):
        if self.has_book == False:
            self.has_book = True
            self.has_codex = True
            self.codex_permflag = True
            self.codex += 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.book_codex_art}")
            vendor_dialog_label.config(text=f"what? i don't remember seeing this one... good thing i have my library card, i'll take this with me")
            codex_label.config(text=f"you have {self.codex} codex!")
        else:
            vendor_dialog_label.config(text=f"you already have a book!")



    def return_book(self):
        if self.has_book == True:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.librarian}")
            vendor_dialog_label.config(text=f"did you even read it?")
            self.has_book = False
            self.codex_permflag = False
            if self.codex > 1:
                self.codex = 1
        else:
            vendor_portrait_label.config(text=f"{self.librarian}")
            vendor_dialog_label.config(text=f"you don't have any books, you dogooder!")
            
    def firstspeak_nerd(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.nerd}")
        if self.library_card == False:
            if self.nerd_quest == False:
                vendor_dialog_label.config(text=f"nerd: ph'y'ello, echhow do you do?")
                inquire_nerd_button = tk.Button(place_button_input_frame, text="inquire about\nwhat the nerd is doing", command=self.inquire_nerd)
                inquire_nerd_button.grid()
                inquire_nerd_button.configure(bg="#ffba26", fg="#000000")
            elif self.nerd_quest == True:
                vendor_dialog_label.config(text=f"nerd: sch'y'ello, i still require ram")
                inquire_nerd_button = tk.Button(place_button_input_frame, text="give him a stick of ram", command=self.give_nerd_ram)
                inquire_nerd_button.grid()
                inquire_nerd_button.configure(bg="#ffba26", fg="#000000")
        elif self.library_card == True:
            vendor_dialog_label.config(text=f"nerd: salutations? i'm busy")
            

    def give_nerd_ram(self):
        if self.library_card == False:
            if self.ram_sticks >= 1 and self.ram_sticks_check == 0:
                self.ram_sticks -= 1
                ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
                self.ram_sticks_check += 1
                vendor_portrait_label.config(text=f"{self.nerd}")
                vendor_dialog_label.config(text=f"nerd: my gratitude! 9 more!")
            elif self.ram_sticks >= 1 and self.ram_sticks_check == 1:
                self.ram_sticks -= 1
                ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
                self.ram_sticks_check += 1
                vendor_portrait_label.config(text=f"{self.nerd}")
                vendor_dialog_label.config(text=f"nerd: my gratitude! 8 more!")
            elif self.ram_sticks >= 1 and self.ram_sticks_check == 2:
                self.ram_sticks -= 1
                ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
                self.ram_sticks_check += 1
                vendor_portrait_label.config(text=f"{self.nerd}")
                vendor_dialog_label.config(text=f"nerd: my gratitude! 7 more!")
            elif self.ram_sticks >= 1 and self.ram_sticks_check == 3:
                self.ram_sticks -= 1
                ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
                self.ram_sticks_check += 1
                vendor_portrait_label.config(text=f"{self.nerd}")
                vendor_dialog_label.config(text=f"nerd: my gratitude! 6 more!")
            elif self.ram_sticks >= 1 and self.ram_sticks_check == 4:
                self.ram_sticks -= 1
                ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
                self.ram_sticks_check += 1
                vendor_portrait_label.config(text=f"{self.nerd}")
                vendor_dialog_label.config(text=f"nerd: my gratitude! 5 more!")
            elif self.ram_sticks >= 1 and self.ram_sticks_check == 5:
                self.ram_sticks -= 1
                ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
                self.ram_sticks_check += 1
                vendor_portrait_label.config(text=f"{self.nerd}")
                vendor_dialog_label.config(text=f"nerd: my gratitude! 4 more!")
            elif self.ram_sticks >= 1 and self.ram_sticks_check == 6:
                self.ram_sticks -= 1
                ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
                self.ram_sticks_check += 1
                vendor_portrait_label.config(text=f"{self.nerd}")
                vendor_dialog_label.config(text=f"nerd: my gratitude! 3 more!")
            elif self.ram_sticks >= 1 and self.ram_sticks_check == 7:
                self.ram_sticks -= 1
                ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
                self.ram_sticks_check += 1
                vendor_portrait_label.config(text=f"{self.nerd}")
                vendor_dialog_label.config(text=f"nerd: my gratitude! 2 more!")
            elif self.ram_sticks >= 1 and self.ram_sticks_check == 8:
                self.ram_sticks -= 1
                ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
                self.ram_sticks_check += 1
                vendor_portrait_label.config(text=f"{self.nerd}")
                vendor_dialog_label.config(text=f"nerd: my gratitude! 1 more!")
            elif self.ram_sticks >= 1 and self.ram_sticks_check == 9:
                self.ram_sticks -= 1
                ram_sticks_label.config(text=f"you have {self.ram_sticks} sticks of ram!")
                self.ram_sticks_check += 1
                vendor_portrait_label.config(text=f"{self.nerd}")
                vendor_dialog_label.config(text=f"nerd: satisfactory. please take my library card for all your 'work' in foresting sticks of RAM;\ni simply did not have enough time for peasantry. i must resume my calculations now...")
                self.nerd_quest = False
                self.library_card_number += 1
                self.library_card = True
                library_card_label.config(text=f"you have {self.library_card_number} library card!")
            else:
                vendor_portrait_label.config(text=f"{self.nerd}")
                vendor_dialog_label.config(text=f"nerd: i still need more ram!")
        elif self.library_card == True:
            vendor_dialog_label.config(text=f"nerd: thank you, but you have provided a satisfactory amount of RAM.\n it is within acceptable margins.")
            
    def inquire_nerd(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.nerd}")
        vendor_dialog_label.config(text=f"nerd: oh, well, first you have to understand in the ineffably intricate tapestry of\nempirical inquiry and theoretical synthesis that constitutes contemporary scientific endeavors, a myriad \no̸f̴ ̸e̶r̴u̴d̶i̷t̶e̴ ̸d̶i̶s̷c̸i̸p̶l̵i̷n̶e̷s̷ ̸c̷o̵a̴l̴e̷s̷c̴e̸,̶ ̵e̵n̴d̸e̶a̷v̴o̸r̴i̵n̶g̸ ̴t̶o̵ ̸e̴x̸p̸l̵i̸c̶a̶t̸e̶ ̴t̸h̶e̸\n ̶a̶b̸s̶t̶r̴u̷s̴e̴ ̸p̶r̵o̷f̶u̸n̶d̷i̸t̶i̸e̸s̶ ̸i̵n̵h̷e̸r̷e̶n̶t̶\n ̸i̵n̵\n̴t̴h̴e̶ ̶f̶a̶b̴r̸i̸c̴ ̶o̵f̶ ̵r̸e̸a̷l̶i̴t̴y̶.̴̵̥̹̎f̵̜͆̈́ ̸̗͚͆s̸͔̑u̷̟̯̾͌b̸̬̣̒ą̵̉́t̴̮̀ȍ̶̢̄m̵̘̐î̷̢̿c̸̥̞̆̎ ̶̭̥̈́̀r̷̯̀e̸̠̊͊a̶̖̠͒l̴̲̲̇m̴̭̕s̸̙͛...")
        inquire_nerd_button = tk.Button(place_button_input_frame, text="okay...", command=self.view_nerd_quest)
        inquire_nerd_button.grid()
        inquire_nerd_button.configure(bg="#ffba26", fg="#000000")
    def view_nerd_quest(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.nerd}")
        vendor_dialog_label.config(text=f"nerd: ... the intricacies of the encephalic citadel,\nseeking to unravel the nebulous conundrums underpinning...\n...and that is why i need 10 sticks of ram.")
        inquire_nerd_button = tk.Button(place_button_input_frame, text="okay, i will do that", command=self.accept_nerd_quest)
        inquire_nerd_button.grid()
        inquire_nerd_button.configure(bg="#ffba26", fg="#000000")
    def accept_nerd_quest(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.nerd}")
        vendor_dialog_label.config(text=f"nerd: excellent! bring them post-haste!")
        self.nerd_quest = True








            
    def view_spooky_woods(self):
        for widget in place_button_input_frame.winfo_children(): #spooky woods* woods* wood*
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.spooky_woods}")
        vendor_dialog_label.config(text=f"it's an entrance to spooky woods...")
        enter_spooky_woods_button = tk.Button(place_button_input_frame, text="enter spooky woods", command=self.enter_spooky_woods)
        enter_spooky_woods_button.grid()
        enter_spooky_woods_button.configure(bg="#303331", fg="#139930")

    def enter_spooky_woods(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.spooky_woods_fork}")
        vendor_dialog_label.config(text=f"...you go deeper into the woods...")
        spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L)
        spooky_woods_L_button.grid()
        spooky_woods_L_button.configure(bg="#303331", fg="#139930")
        spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R)
        spooky_woods_R_button.grid()
        spooky_woods_R_button.configure(bg="#303331", fg="#139930")



    def spooky_woods_L(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.spooky_woods_L1}")
        vendor_dialog_label.config(text=f"... and deeper...")
        spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L2)
        spooky_woods_L_button.grid()
        spooky_woods_L_button.configure(bg="#303331", fg="#139930")
        spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R2)
        spooky_woods_R_button.grid()
        spooky_woods_R_button.configure(bg="#303331", fg="#139930")
    def spooky_woods_R(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.spooky_woods_R1}")
        vendor_dialog_label.config(text=f"... and deeeper...")
        spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L2)
        spooky_woods_L_button.grid()
        spooky_woods_L_button.configure(bg="#303331", fg="#139930")
        spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R2)
        spooky_woods_R_button.grid()
        spooky_woods_R_button.configure(bg="#303331", fg="#139930")

    def spooky_woods_L2(self):
        spooky_chance = random.randint(1, 2)
        if spooky_chance == 1:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L2_A}")
            vendor_dialog_label.config(text=f"...annnd deeper...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L3)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R3)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 2:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L2_B}")
            vendor_dialog_label.config(text=f"ouch! thorns hurt! better get a move on...\n[lost 50 shinies in the shambles]")
            self.shiny_things -= (50)
            shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L3)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R3)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")

    def spooky_woods_R2(self):
        spooky_chance = random.randint(1, 2)
        if spooky_chance == 1:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R2_A}")
            vendor_dialog_label.config(text=f"...annnd deeper...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L3)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R3)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 2:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R2_B}")
            vendor_dialog_label.config(text=f"\n[you found a stick! with your foot!\n[gained and lost 1 stick]")
            sticks_label.config(text=f"you have {self.sticks} sticks!")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L3)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R3)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")

    def spooky_woods_L3(self):
        spooky_chance = random.randint(1, 4)
        if spooky_chance == 1:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L3_A}")
            vendor_dialog_label.config(text=f"... and deeper...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L4)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R4)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 2:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L3_B}")
            vendor_dialog_label.config(text=f"you found a stick!\n[gained 1 stick]")
            self.sticks += (1)
            sticks_label.config(text=f"you have {self.sticks} sticks!")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L4)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R4)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 3:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L3_C}")
            vendor_dialog_label.config(text=f"OGRE: GET OUT OF MY SWAMP\nthe ogre will not let you pass")
            
        elif spooky_chance == 4:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L3_D}")
            vendor_dialog_label.config(text=f"... deeper...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L4)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R4)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
    def spooky_woods_R3(self):
        spooky_chance = random.randint(1, 4)
        if spooky_chance == 1:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R3_A}")
            vendor_dialog_label.config(text=f"... and deeper...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L4)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R4)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 2:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R3_B}")
            vendor_dialog_label.config(text=f"you found a stick!\n[gained 1 stick]")
            self.sticks += (1)
            sticks_label.config(text=f"you have {self.sticks} sticks!")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L4)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R4)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 3:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R3_C}")
            vendor_dialog_label.config(text=f"what are these things?")
            
        elif spooky_chance == 4:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R3_D}")
            vendor_dialog_label.config(text=f"... the depth of deepness...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L4)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R2)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")

    def catch_canary(self):
        canary_chance = random.randint(1, 5)
        if canary_chance == 1:
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_C}")
            vendor_dialog_label.config(text=f"you got a canary!")
            self.canary_number += 1
            canary_label.config(text=f"you have {self.canary_number} canary!")
            self.canary = True
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        elif canary_chance == 2:
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_C}")
            vendor_dialog_label.config(text=f"nope!")
        elif canary_chance == 3:
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_C}")
            vendor_dialog_label.config(text=f"missed!")
        elif canary_chance == 4:
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_C}")
            vendor_dialog_label.config(text=f"conflabit!")            
        elif canary_chance == 5:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_D}")
            vendor_dialog_label.config(text=f"no!!! he flew away!")
                
    def spooky_woods_L4(self):
        spooky_chance = random.randint(1, 8)
        if spooky_chance == 1:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_A}")
            vendor_dialog_label.config(text=f"... lost?")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L2)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R2)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 2:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_B}")
            vendor_dialog_label.config(text=f"... what in the name of zelda is this place?")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 3:
            if self.canary == False:
                for widget in place_button_input_frame.winfo_children():
                        widget.destroy()
                vendor_portrait_label.config(text=f"{self.spooky_woods_L4_C}")
                vendor_dialog_label.config(text=f"it's a canary! i think...") 
                catch_canary_button = tk.Button(place_button_input_frame, text="catch the canary", command=self.catch_canary)
                catch_canary_button.grid()
                catch_canary_button.configure(bg="#ffef00", fg="black")
            elif self.canary == True:
                for widget in place_button_input_frame.winfo_children():
                        widget.destroy()
                vendor_portrait_label.config(text=f"{self.spooky_woods_L4_B}")
                vendor_dialog_label.config(text=f"... where am i?")
            
        elif spooky_chance == 4:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_D}")
            vendor_dialog_label.config(text=f"... deeper...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L2)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R3)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 5:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_E}")
            vendor_dialog_label.config(text=f"... anddd deeepeer...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L2)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R3)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 6:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_F}")
            vendor_dialog_label.config(text=f"you found a stick!\n[gained 1 stick]")
            self.sticks += (1)
            sticks_label.config(text=f"you have {self.sticks} sticks!")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L4)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R3)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 7:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_G}")
            vendor_dialog_label.config(text=f"... how many left turns make a circle...?")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
            
        elif spooky_chance == 8:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_L4_H}")
            vendor_dialog_label.config(text=f"... deeeeper...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L2)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R2)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")

    def spooky_woods_R4(self):
        spooky_chance = random.randint(1, 8)
        if spooky_chance == 1:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R4_A}")
            vendor_dialog_label.config(text=f"... lost?")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L2)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R2)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 2:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R4_B}")
            vendor_dialog_label.config(text=f"... what in the name of zelda is this place?")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 3:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R4_B}")
            vendor_dialog_label.config(text=f"... it's dangerous to go alone...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
            
        elif spooky_chance == 4:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R4_D}")
            vendor_dialog_label.config(text=f"... deeper...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L2)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R3)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 5:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R4_E}")
            vendor_dialog_label.config(text=f"... anddd deeepeer...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L3)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R2)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 6:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R4_F}")
            vendor_dialog_label.config(text=f"... oh where am i...")
            sticks_label.config(text=f"you have {self.sticks} sticks!")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L2)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R3)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
        elif spooky_chance == 7:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R4_G}")
            vendor_dialog_label.config(text=f"... how many left turns make a circle...?")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")
            
        elif spooky_chance == 8:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.spooky_woods_R4_H}")
            vendor_dialog_label.config(text=f"... deeeeper...")
            spooky_woods_L_button = tk.Button(place_button_input_frame, text="go left", command=self.spooky_woods_L2)
            spooky_woods_L_button.grid()
            spooky_woods_L_button.configure(bg="#303331", fg="#139930")
            spooky_woods_R_button = tk.Button(place_button_input_frame, text="go right", command=self.spooky_woods_R2)
            spooky_woods_R_button.grid()
            spooky_woods_R_button.configure(bg="#303331", fg="#139930")




    def unlock_vending_machine(self):    #vending machine* vending*
        unlock_sound.play()
        vending_machine_button = tk.Button(vendor_frame, text="dirty vending machine", command=self.view_vending_machine, width=20)
        vending_machine_button.grid()
        vending_machine_button.configure(bg="#f40009", fg="white")
        self.vending_machine_unlock = True
    def view_vending_machine(self):
        for widget in place_button_input_frame.winfo_children():
            widget.destroy()
            
        if self.vending_machine_on is False:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.vending_machine}")
            vendor_dialog_label.config(text=f"vending machine: hey! you! yeah you! ...turn me on... come on...")
            turnon_vending_button = tk.Button(place_button_input_frame, text="power on vending machine\n(3 batteries)", command=self.turnon_vending_machine)
            turnon_vending_button.grid()
            turnon_vending_button.configure(bg="#f40009", fg="white")
        elif self.vending_machine_on is True:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.vending_machine}")
            vendor_dialog_label.config(text=f"vending machine: mmunyeah... put something shiny in me...")
            get_vending_button = tk.Button(place_button_input_frame, text="insert 10 shiny things", command=self.buy_vending_machine)
            get_vending_button.grid()

    def turnon_vending_machine(self):
        if self.batteries >= 3 and self.vending_machine_on == False:
            self.batteries -= 3
            batteries_label.config(text=f"you have {self.batteries} batteries!")
            vendor_portrait_label.config(text=f"{self.vending_machine}")
            vendor_dialog_label.config(text=f"vending machine: mmm yeah... that's the good good... now just walk around the corner and\n come back, yeh? i need to, uh... lubricate the old gears...")
            self.vending_machine_on = True
        elif self.batteries <= 3 and self.vending_machine_on == False:
            vendor_dialog_label.config(text=f"vending machine: that ain't enough power, iuh NEED more than that babydollop...")
        elif self.vending_machine_on == True:
            vendor_dialog_label.config(text=f"vending machine: damn baby you tryin to treat me on the good good...\njust hang on baby and come on back, i'll do you on the good good...")
        
    def buy_vending_machine(self):
        if self.shiny_things >= 10:
            self.shiny_things -= 10
            vending_chance = random.randint(1, 15)
            shiny_things_label.config(text=f"you have {self.shiny_things} shiny things!")
            if vending_chance == (1):
                self.shiny_things += 10
                vendor_dialog_label.config(text=f"vending machine: that's for you baaaby!\n[gained and lost nothing!]")
            elif vending_chance == (2):
                self.shiny_things += 30
                vendor_dialog_label.config(text=f"vending machine: mm yeah baby!\n[gained 20 shinies!]")

            elif vending_chance == (3):
                self.rockcandy += 1
                vendor_dialog_label.config(text=f"vending machine: AWH YEAHHHH BABY THAT'S THE BUTTON!\n[gained 1 rockcandy, finally!]")
                rockcandy_label.config(text=f"you have {self.rockcandy} rockcandy!")
            else:
                fail_chance = random.randint(1, 5)
                if fail_chance == (1):
                    vendor_dialog_label.config(text=f"vending machine: mm yeah baby put some more in me and i promise i'll give you something...\n[lost 10 shinies]")
                elif fail_chance == (2):
                    vendor_dialog_label.config(text=f"vending machine: aw yeah... make me a *bending* machine, babycakes... one more time...\n[lost 10 shinies]")
                elif fail_chance == (3):
                    vendor_dialog_label.config(text=f"vending machine: ... take it out on me baby, oh yeah...\n[lost 10 shinies]")
                elif fail_chance == (4):
                    vendor_dialog_label.config(text=f"vending machine: mm yeah baby put some more in me and i promise i'll give you something...\n[lost 10 shinies]")
                elif fail_chance == (5):
                    vendor_dialog_label.config(text=f"vending machine: i'm a *baaddd* vending machine...\n[lost 10 shinies]")
                     

            #lemons_label.config(text=f"you have {self.lemons} lemons!") configure updating label here
        else:
            vendor_dialog_label.config(text=f"vending machine: damn baby! if you broke, so am i!")




    def unlock_cave(self):    #cave*
        unlock_sound.play()
        cave_button = tk.Button(vendor_frame, text="cave", command=self.view_cave, width=20)
        cave_button.grid()
        cave_button.configure(bg="black", fg="#dd571c")
        self.cave_unlock = True
    def view_cave(self):
        for widget in place_button_input_frame.winfo_children():
            widget.destroy()
        vendor_portrait_label.config(text=f"{self.cave}")
        vendor_dialog_label.config(text=f"its a dark cave...")
        go_in_cave_button = tk.Button(place_button_input_frame, text="go in the cave", command=self.enter_cave)
        go_in_cave_button.grid()
        go_in_cave_button.configure(bg="black", fg="white")
    def enter_cave(self):
        if self.dwarf_talk_flag == False:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: hello, what are you doing here?")
            talk_dwarf_button = tk.Button(place_button_input_frame, text="speak to the dwarf", command=self.firstspeak_dwarf)
            talk_dwarf_button.grid()
            talk_dwarf_button.configure(bg="purple", fg="white")

        if self.dwarf_talk_flag == True and self.rockcandy_flag == False:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: hello again, have you any rock candy?\ni have been searching since we last spaketh and i have not found the codex...\ni sure am hungry...")
            give_rockcandy_button = tk.Button(place_button_input_frame, text="give him some rockcandy", command=self.give_rockcandy_dwarf)
            give_rockcandy_button.grid()
            give_rockcandy_button.configure(bg="purple", fg="white")
            
        elif self.dwarf_talk_flag == True and self.rockcandy_flag == True and self.has_codex == False and self.has_pickaxe == True:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: your contribution has been of great assistance, thank you for the codex")

        elif self.dwarf_talk_flag == True and self.rockcandy_flag == True and self.has_codex == False:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: hello, thanks for your assistance.\ni did not find the sacred codex down there.\nyou can have my HEADLAMP.\ni will continue my research...")
            take_headlamp_button = tk.Button(place_button_input_frame, text="take the HEADLAMP", command=self.take_headlamp)
            take_headlamp_button.grid()
            take_headlamp_button.configure(bg="green", fg="white")

        elif self.dwarf_talk_flag == True and self.rockcandy_flag == True and self.has_codex == True:
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: hello again, you are here in the caves again...?")
            show_codex_button = tk.Button(place_button_input_frame, text="show him the codex", command=self.show_codex)
            show_codex_button.grid()
            show_codex_button.configure(bg="purple", fg="white")

        
            

    def show_codex(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.dwarf}")
        vendor_dialog_label.config(text=f"dwarf: that is the codex! please! i must have it!")
        demand_shinies_button = tk.Button(place_button_input_frame, text="demand 1,000,000 shinies", command=self.demand_shinies)
        demand_shinies_button.grid()
        demand_shinies_button.configure(bg="blue", fg="yellow")

    def demand_shinies(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.dwarf}")
        vendor_dialog_label.config(text=f"dwarf: excuseth me? how rich do you think i am exactly? look\nall i have is my pickaxe, i am willing to trade it for the codex")
        reject_pickaxe_button = tk.Button(place_button_input_frame, text="reject trade", command=self.reject_pickaxe)
        reject_pickaxe_button.grid()
        reject_pickaxe_button.configure(bg="gray", fg="red")
        accept_pickaxe_button = tk.Button(place_button_input_frame, text="accept trade", command=self.accept_pickaxe)
        accept_pickaxe_button.grid()
        accept_pickaxe_button.configure(bg="gray", fg="green")
    def reject_pickaxe(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.dwarf}")
        vendor_dialog_label.config(text=f"dwarf: [?lie?] please, i must have it. you must give it to me.\nthere is probably nothing else you can do with it...")
    def accept_pickaxe(self):
        if self.has_pickaxe == False:
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            self.has_pickaxe = True
            self.pickaxe += 1
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: alas, my quest is complete. here, i do not need this anymore.\nthese are sacred to dwarves, treat it with respect.\nperhaps we value the labor itself.")
            pickaxe_label.config(text=f"you have {self.pickaxe} pickaxe!")
            self.codex = 0
            self.has_codex = False
            self.has_book = False
            codex_label.config(text=f"you have {self.codex} codex!")
            unlock_sound.play()
            mines_button = tk.Button(vendor_frame, text="mines", command=self.view_mines) #mines*
            mines_button.grid()                      
            mines_button.configure(bg="#323331", fg="#efe40e", width=20)
        elif self.has_pickaxe == True:
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: why would you think i mayest have two? i have given you the only one i had")
       
            
    def firstspeak_dwarf(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.dwarf}")
        vendor_dialog_label.config(text=f"dwarf: ah, i am also on a quest.\ni am seeking a long lost codex that was once important to my kind.\nperhaps you have seen it?\nno matter, i will continue my search once i find batteries for my headlamp...")
        give_battery_button = tk.Button(place_button_input_frame, text="give him a battery", command=self.give_batteries_dwarf)
        give_battery_button.grid()
        give_battery_button.configure(bg="blue", fg="yellow")

    def give_batteries_dwarf(self):
        if self.batteries >= 1 and self.dwarf_talk_flag == False:
            self.batteries -= 1
            batteries_label.config(text=f"you have {self.batteries} batteries!")
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: thank you, i must retreat below and resume my search... come back later...")
            self.dwarf_talk_flag = True
        elif self.batteries == 0 and self.dwarf_talk_flag == False:
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: um, you don't appear to have any batteries...")
        else:
            vendor_dialog_label.config(text=f"dwarf: thanks, but i must return to work now, come back later...")
    def give_rockcandy_dwarf(self):
        if self.rockcandy >= 1 and self.rockcandy_check == 0:
            self.rockcandy -= 1
            rockcandy_label.config(text=f"you have {self.rockcandy} rockcandy!")
            self.rockcandy_check += 1
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: oh, you mean it? that quest you mentioned must really be important to you")
        elif self.rockcandy >= 1 and self.rockcandy_check == 1:
            self.rockcandy -= 1
            rockcandy_label.config(text=f"you have {self.rockcandy} rockcandy!")
            self.rockcandy_check += 1
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: thank you, do you have any more?")
        elif self.rockcandy >= 1 and self.rockcandy_check == 2:
            self.rockcandy -= 1
            rockcandy_label.config(text=f"you have {self.rockcandy} rockcandy!")
            self.rockcandy_check += 1
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: i know it seems like a lot, but we are different than your kind... can you get some more?")
        elif self.rockcandy >= 1 and self.rockcandy_check == 3:
            self.rockcandy -= 1
            rockcandy_label.config(text=f"you have {self.rockcandy} rockcandy!")
            self.rockcandy_check += 1
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: ... just one more will do...")
        elif self.rockcandy >= 1 and self.rockcandy_check == 4:
            self.rockcandy -= 1
            rockcandy_label.config(text=f"you have {self.rockcandy} rockcandy!")
            self.rockcandy_check += 1
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: thank you, i will go down once more and return shortly now, come back later...")
            self.rockcandy_flag = True
        elif self.rockcandy < 1 and self.rockcandy_check < 5 :
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: uh, you don't seem to have any rockcandy... can you go get some... i should stay down here...")
        else:
            vendor_portrait_label.config(text=f"{self.dwarf}")
            vendor_dialog_label.config(text=f"dwarf: that's nice of you, but i'm stuffed")
    def take_headlamp(self):
        vendor_portrait_label.config(text=f"{self.dwarf}")
        if self.headlamp == True:
            vendor_dialog_label.config(text=f"dwarf: its the only one i had, i swear!")
        else:
            vendor_dialog_label.config(text=f"dwarf: don't you have a sun or something? whatever, it's yours... you'll need some more batteries for it though")
            self.headlamp += 1
            headlamp_label.config(text=f"you have {self.headlamp} headlamp!")
            headlamp_button = tk.Button(vendor_frame, text="charge the headlamp", command=self.charge_headlamp)
            headlamp_button.grid()
            headlamp_button.configure(bg="#2ba838", fg="#dae820", width=20)

        self.headlamp = True
        
    def charge_headlamp(self):
        if self.headlamp_charged == False:
            if self.batteries >= 10:
                self.headlamp_charge = 10
                self.batteries -= 10
                batteries_label.config(text=f"you have {self.batteries} batteries!")
                headlamp_charge_label.config(text=f"headlamp charged!")
                vendor_dialog_label.config(text=f"you charged the headlamp!")
                self.headlamp_charged = True
            elif self.batteries < 10:
                vendor_dialog_label.config(text=f"not enough batteries!")
        elif self.headlamp_charged == True:
            vendor_dialog_label.config(text=f"headlamp already charged!")
    def check_headlamp(self):
        if self.headlamp_charge <= 0:
            self.headlamp_charge = 0
            self.headlamp_charged = False
            for widget in place_button_input_frame.winfo_children():
                widget.destroy()
            vendor_dialog_label.config(text=f"dangit! the headlamp died!")
            headlamp_charge_label.config(text=f"headlamp not charged!")

    def view_mines(self):
        for widget in place_button_input_frame.winfo_children():
                widget.destroy()
        vendor_portrait_label.config(text=f"{self.mines_entrance}")
        vendor_dialog_label.config(text=f"it's an entrance to the mines\nit looks dark inside...")
        enter_mines_button = tk.Button(place_button_input_frame, text="enter the mines", command=self.enter_mines)
        enter_mines_button.grid()
        enter_mines_button.configure(bg="#323331", fg="#efe40e")
            
    def enter_mines(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_1}")
            vendor_dialog_label.config(text=f"looks like a series of passages...")
            mines_passage_1_L_button = tk.Button(place_button_input_frame, text="left passage", command=self.mines_passage_1_L)
            mines_passage_1_L_button.grid()
            mines_passage_1_L_button.configure(bg="#323331", fg="#efe40e")
            mines_passage_1_F_button = tk.Button(place_button_input_frame, text="forward passage", command=self.mines_passage_1_F)
            mines_passage_1_F_button.grid()
            mines_passage_1_F_button.configure(bg="#323331", fg="#efe40e")
            mines_passage_1_R_button = tk.Button(place_button_input_frame, text="right passage", command=self.mines_passage_1_R)
            mines_passage_1_R_button.grid()
            mines_passage_1_R_button.configure(bg="#323331", fg="#efe40e")
        elif self.headlamp_charged == False:
            vendor_dialog_label.config(text=f"it's too dark to enter...")

    def mines_passage_1_L(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_locked_door}")
            vendor_dialog_label.config(text=f"what's this? a locked door?")
            doorcode_1_button = tk.Button(place_button_input_frame, text="1", command=self.doorcode_1)
            doorcode_1_button.grid(row=0, column=0)
            doorcode_1_button.configure(bg="#323331", fg="#efe40e")
            doorcode_2_button = tk.Button(place_button_input_frame, text="2", command=self.doorcode_2)
            doorcode_2_button.grid(row=0, column=1)
            doorcode_2_button.configure(bg="#323331", fg="#efe40e")
            doorcode_3_button = tk.Button(place_button_input_frame, text="3", command=self.doorcode_3)
            doorcode_3_button.grid(row=0, column=2)
            doorcode_3_button.configure(bg="#323331", fg="#efe40e")
            doorcode_4_button = tk.Button(place_button_input_frame, text="4", command=self.doorcode_4)
            doorcode_4_button.grid(row=1, column=0)
            doorcode_4_button.configure(bg="#323331", fg="#efe40e")
            doorcode_5_button = tk.Button(place_button_input_frame, text="5", command=self.doorcode_5)
            doorcode_5_button.grid(row=1, column=1)
            doorcode_5_button.configure(bg="#323331", fg="#efe40e")
            doorcode_6_button = tk.Button(place_button_input_frame, text="6", command=self.doorcode_6)
            doorcode_6_button.grid(row=1, column=2)
            doorcode_6_button.configure(bg="#323331", fg="#efe40e")
            doorcode_7_button = tk.Button(place_button_input_frame, text="7", command=self.doorcode_7)
            doorcode_7_button.grid(row=2, column=0)
            doorcode_7_button.configure(bg="#323331", fg="#efe40e")
            doorcode_8_button = tk.Button(place_button_input_frame, text="8", command=self.doorcode_8)
            doorcode_8_button.grid(row=2, column=1)
            doorcode_8_button.configure(bg="#323331", fg="#efe40e")
            doorcode_9_button = tk.Button(place_button_input_frame, text="9", command=self.doorcode_9)
            doorcode_9_button.grid(row=2, column=2)
            doorcode_9_button.configure(bg="#323331", fg="#efe40e")
            self.doorcode_entry_field = tk.Entry(place_button_input_frame)
            self.doorcode_entry_field.grid(row=3, columnspan=3)
            doorcode_enter_button = tk.Button(place_button_input_frame, text="enter", command=self.doorcode_enter)
            doorcode_enter_button.grid(row=4, column=2)
            doorcode_enter_button.configure(bg="#323331", fg="#efe40e")
        elif self.headlamp_charged == False:
            vendor_dialog_label.config(text=f"it's too dark to enter...")
            
    def doorcode_enter(self):
        entered_code = self.doorcode_entry_field.get()
        if entered_code == "7482":
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_unlocked_door}")
            enter_locked_door_button = tk.Button(place_button_input_frame, text="go inside", command=self.enter_locked_door)
            enter_locked_door_button.grid(row=5, column=2)
            enter_locked_door_button.configure(bg="#323331", fg="#efe40e")
        else:
            self.doorcode_entry_field.delete(0, tk.END)
    
    def doorcode_1(self):
        entry_text = "1"
        self.doorcode_entry_field.insert(tk.END, entry_text)    
    def doorcode_2(self):
        entry_text = "2"
        self.doorcode_entry_field.insert(tk.END, entry_text)    
    def doorcode_3(self):
        entry_text = "3"
        self.doorcode_entry_field.insert(tk.END, entry_text)    
    def doorcode_4(self):
        entry_text = "4"
        self.doorcode_entry_field.insert(tk.END, entry_text)    
    def doorcode_5(self):
        entry_text = "5"
        self.doorcode_entry_field.insert(tk.END, entry_text)    
    def doorcode_6(self):
        entry_text = "6"
        self.doorcode_entry_field.insert(tk.END, entry_text)    
    def doorcode_7(self):
        entry_text = "7"
        self.doorcode_entry_field.insert(tk.END, entry_text)    
    def doorcode_8(self):
        entry_text = "8"
        self.doorcode_entry_field.insert(tk.END, entry_text)  
    def doorcode_9(self):
        entry_text = "9"
        self.doorcode_entry_field.insert(tk.END, entry_text)

    def enter_locked_door(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.gold_mines}")
            vendor_dialog_label.config(text=f"gold, gold everywhere! good thing i have a pickaxe!")
            mine_gold_button = tk.Button(place_button_input_frame, text="mine some gold!", command=self.mine_gold)
            mine_gold_button.grid()
            mine_gold_button.configure(bg="gold", fg="black", row=0, column=0)
    def mine_gold(self):
        self.gold_bar = True
        self.gold_bar_count += 1
        gold_bar_label.config(text=f"you have {self.gold_bar_count} gold chunks!")











        

    def mines_passage_1_F(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_1}")
            vendor_dialog_label.config(text=f"... you go deeper into the mines...")
            mines_passage_2_L_button = tk.Button(place_button_input_frame, text="left passage", command=self.mines_passage_2_L)
            mines_passage_2_L_button.grid()
            mines_passage_2_L_button.configure(bg="#323331", fg="#efe40e")
            mines_passage_2_F_button = tk.Button(place_button_input_frame, text="forward passage", command=self.mines_passage_2_F)
            mines_passage_2_F_button.grid()
            mines_passage_2_F_button.configure(bg="#323331", fg="#efe40e")
            mines_passage_2_R_button = tk.Button(place_button_input_frame, text="right passage", command=self.mines_passage_2_R)
            mines_passage_2_R_button.grid()
            mines_passage_2_R_button.configure(bg="#323331", fg="#efe40e")
        elif self.headlamp_charged == False:
            vendor_dialog_label.config(text=f"it's too dark to enter...")

    def mines_passage_2_L(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_deadend}")
            vendor_dialog_label.config(text=f"it's a dead end...")
            
    def mines_passage_2_F(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_1}")
            vendor_dialog_label.config(text=f"... you go deeper into the mines...")
            mines_passage_3_L_button = tk.Button(place_button_input_frame, text="left passage", command=self.mines_passage_3_L)
            mines_passage_3_L_button.grid()
            mines_passage_3_L_button.configure(bg="#323331", fg="#efe40e")
            mines_passage_3_R_button = tk.Button(place_button_input_frame, text="forward passage", command=self.mines_passage_3_R)
            mines_passage_3_R_button.grid()
            mines_passage_3_R_button.configure(bg="#323331", fg="#efe40e")
            
    def mines_passage_2_R(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_deadend}")
            vendor_dialog_label.config(text=f"it's a dead end...")

    def mines_passage_3_L(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_1}")
            vendor_dialog_label.config(text=f"... you go deeper into the mines...")
            mines_passage_4_L_button = tk.Button(place_button_input_frame, text="left passage", command=self.mines_passage_4_L)
            mines_passage_4_L_button.grid()
            mines_passage_4_L_button.configure(bg="#323331", fg="#efe40e")
            mines_passage_4_R_button = tk.Button(place_button_input_frame, text="forward passage", command=self.mines_passage_4_R)
            mines_passage_4_R_button.grid()
            mines_passage_4_R_button.configure(bg="#323331", fg="#efe40e")

    def mines_passage_3_R(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_deadend}")
            vendor_dialog_label.config(text=f"it's a dead end...")

    def mines_passage_4_L(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_1}")
            vendor_dialog_label.config(text=f"looks like someones identification... it's been here for a while...\ni can make out a '...1: 7...'")

    def mines_passage_4_R(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_1}")
            if self.canary == True:
                vendor_dialog_label.config(text=f"woah! my canary was knocked out!\nthat could have been a bad ending! better hold my breath...")
                mines_passage_5_F_button = tk.Button(place_button_input_frame, text="forward passage", command=self.mines_passage_5_F)
                mines_passage_5_F_button.grid()
                mines_passage_5_F_button.configure(bg="#323331", fg="#efe40e")
            elif self.canary == False:
                vendor_dialog_label.config(text=f"something smells... funny... smellssss... phunmy... lwrihe gassss.s..s.s....")

    def mines_passage_5_F(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_1}")
            vendor_dialog_label.config(text=f"looks like someones identification... it's been here for a while...\ni can make out a '...2: 4...'")










    def mines_passage_1_R(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_1}")
            vendor_dialog_label.config(text=f"... you go deeper into the mines...")
            mines_passage_6_L_button = tk.Button(place_button_input_frame, text="left passage", command=self.mines_passage_6_L)
            mines_passage_6_L_button.grid()
            mines_passage_6_L_button.configure(bg="#323331", fg="#efe40e")
            mines_passage_6_R_button = tk.Button(place_button_input_frame, text="forward passage", command=self.mines_passage_6_R)
            mines_passage_6_R_button.grid()
            mines_passage_6_R_button.configure(bg="#323331", fg="#efe40e")
        elif self.headlamp_charged == False:
            vendor_dialog_label.config(text=f"it's too dark to enter...")

    def mines_passage_6_L(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_1}")
            vendor_dialog_label.config(text=f"looks like someones identification... it's been here for a while...\ni can make out a '...3: 8...'")
    def mines_passage_6_R(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_1}")
            vendor_dialog_label.config(text=f"... you go deeper into the mines...")
            mines_passage_7_L_button = tk.Button(place_button_input_frame, text="left passage", command=self.mines_passage_7_L)
            mines_passage_7_L_button.grid()
            mines_passage_7_L_button.configure(bg="#323331", fg="#efe40e")
            mines_passage_7_R_button = tk.Button(place_button_input_frame, text="forward passage", command=self.mines_passage_7_R)
            mines_passage_7_R_button.grid()
            mines_passage_7_R_button.configure(bg="#323331", fg="#efe40e")
        elif self.headlamp_charged == False:
            vendor_dialog_label.config(text=f"it's too dark to enter...")

    def mines_passage_7_L(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_1}")
            vendor_dialog_label.config(text=f"looks like someones identification... it's been here for a while...\ni can make out a '...4: 2...'")
    def mines_passage_7_R(self):
        self.check_headlamp()
        if self.headlamp_charged == True:
            self.headlamp_charge -= 1
            for widget in place_button_input_frame.winfo_children():
                    widget.destroy()
            vendor_portrait_label.config(text=f"{self.mines_deadend}")
            vendor_dialog_label.config(text=f"it's a dead end...")

            

def information():
    title = "LSC shinybox"
    message = '''Inspired by aniwey's candybox:
https://candybox2.github.io/candybox/
I was one of the first 100 people to beat the first game!
This is a very small and skeletal recreation of the game.
Also inspired by the Jagex-created quest
for Runescape, "One Small Favor"'''
    messagebox.showinfo(title, message)

pl_cl_instance = Player()

root = tk.Tk()
root.title("LSC shinybox")
root.geometry("1000x1000+250+0")
root.configure(bg="#279fa5")

shiny_things_frame = tk.Frame(root, bg="#279fa5")  # currencies
shiny_things_frame.grid(row=0, column=0)
info_button = tk.Button(shiny_things_frame, text="info", command=information)
info_button.grid()
events_label = tk.Label(shiny_things_frame, text="welcome to shinybox", bg="#279fa5", fg="#f7f7f7")
events_label.grid()
shinybox_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
shinybox_label.grid()
shiny_things_label = tk.Label(shiny_things_frame, text=f"you have {pl_cl_instance.shiny_things} shiny things!", bg="#279fa5", fg="#f7f7f7")
shiny_things_label.grid()
shiny_things_discarded_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
shiny_things_discarded_label.grid()
lemons_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
lemons_label.grid()
pigeons_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
pigeons_label.grid()
batteries_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
batteries_label.grid()
rockcandy_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
rockcandy_label.grid()
headlamp_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
headlamp_label.grid()
headlamp_charge_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
headlamp_charge_label.grid()
birdcage_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
birdcage_label.grid()
canary_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
canary_label.grid()
sticks_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
sticks_label.grid()
ram_sticks_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
ram_sticks_label.grid()
library_card_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
library_card_label.grid()
codex_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
codex_label.grid()
pickaxe_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
pickaxe_label.grid()
gold_bar_label = tk.Label(shiny_things_frame, text=f"", bg="#279fa5", fg="#f7f7f7")
gold_bar_label.grid()

place_button_input_frame = tk.Frame(root, bg="#279fa5")#buy or interact buttons frame
place_button_input_frame.grid(row=2, column=1)

vendor_portrait_frame = tk.Frame(root, bg="#279fa5") #portraits
vendor_portrait_frame.grid(row=0, column=1)
vendor_portrait_font = ("Courier", 12)
vendor_portrait_label = tk.Label(vendor_portrait_frame, text="", bg="#279fa5", fg="#f7f7f7", font=vendor_portrait_font, justify=tk.LEFT)
vendor_portrait_label.grid()


vendor_dialog_frame = tk.Frame(root, bg="#279fa5") #vendor dialog
vendor_dialog_frame.grid(row=1, column=1)
vendor_dialog_label = tk.Label(vendor_dialog_frame, text="", bg="#279fa5", fg="#f7f7f7")
vendor_dialog_label.grid()

vendor_frame = tk.Frame(root, bg="#279fa5") #this is places LIKE MINES AND CAVE
vendor_frame.grid(row=1, column=0)



#pl_cl_instance.debug_label_update()

pl_cl_instance.increase_shiny_things()

# Game
root.mainloop()
