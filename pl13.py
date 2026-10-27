import re                      # регулярные выражения - чтобы выделять слова из текста
import sys                     # sys.argv - аргументы командной строки, sys.exit - аварийный выход

TABLE_SIZE = 257               
BASE = 31                      
WORD_RE = re.compile(r"[A-Za-zА-Яа-яЁё]+")  
in_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"         
out_path = sys.argv[2] if len(sys.argv) > 2 else "output_lab13.txt"    
table = [None] * TABLE_SIZE    
total = 0                      

with open(in_path, "r", encoding="utf-8") as f:
    
    for line in f:
        
        for w in WORD_RE.findall(line):            
            word = w.lower()                       
            total += 1                             
            start = 0
            
            for ch in word:                        
                start = (start * BASE + ord(ch)) % TABLE_SIZE  
            idx = start                            
            placed = False
            
            for _ in range(TABLE_SIZE):            
                cell = table[idx]                  
                
                if cell is None:                   
                    table[idx] = [word, 1, start]  
                    placed = True                  
                    break
                
                if cell[0] == word:                
                    cell[1] += 1                   
                    placed = True                  
                    break                          
                idx = (idx + 1) % TABLE_SIZE
                
            if not placed:                         
                print("Ошибка: таблица заполнена, увеличьте TABLE_SIZE")
                sys.exit(1)                        

used = 0                       
shifted = 0                    
for i in range(TABLE_SIZE):    
    if table[i] is not None:   
        used += 1              
        if table[i][2] != i:   
            shifted += 1       

with open(out_path, "w", encoding="utf-8") as out:   
    out.write("хеш таблица с наложением \n")
    out.write(f"размер таблицы {TABLE_SIZE}, слов в тексте: {total}, уникальных: {used}\n")
    out.write(f"коэффициент заполнения: {used / TABLE_SIZE:.2f}, слов со сдвигом из-за коллизий: {shifted}\n")
    out.write("-" * 70 + "\n")                       
    for i in range(TABLE_SIZE):                      
        cell = table[i]                              
        if cell is None:                             
            out.write(f"{i:3d} | <пусто>\n")
        else:                                        
            note = "" if cell[2] == i else f"  (коллизия, хеш={cell[2]})"  
            out.write(f"{i:3d} | {cell[0]:<14} x{cell[1]}{note}\n")

print(f"Готово: {out_path}")   