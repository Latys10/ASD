import re                      # регулярные выражения для выделения слов
import sys                     # аргументы командной строки

TABLE_SIZE = 53                
BASE = 31                      
WORD_RE = re.compile(r"[A-Za-zА-Яа-яЁё]+")  
in_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"          
out_path = sys.argv[2] if len(sys.argv) > 2 else "output_lab14.txt"    
table = [None] * TABLE_SIZE   
total = 0                    

with open(in_path, "r", encoding="utf-8") as f:
    
    for line in f:
        
        for w in WORD_RE.findall(line):           
            word = w.lower()                      
            total += 1                             
            h = 0
            
            for ch in word:                        
                h = (h * BASE + ord(ch)) % TABLE_SIZE  
            node = table[h]                       
            found = False
            
            while node is not None:
                
                if node[0] == word:                
                    node[1] += 1                  
                    found = True                  
                    break                          
                node = node[2]
                
            if not found:                          
                table[h] = [word, 1, table[h]]    
unique = 0                     
longest = 0                  
collisions = 0                
lines = []                    

for i in range(TABLE_SIZE):    
    parts = []                 
    node = table[i]
    
    while node is not None:    
        parts.append(f"{node[0]}(x{node[1]})")   
        node = node[2]        
    n = len(parts)            
    unique += n
    
    if n > longest:          
        longest = n          
    if n > 1:                 
        collisions += n - 1
    if n == 0:                 
        lines.append(f"{i:3d} | <пусто>")
    else:                      
        lines.append(f"{i:3d} | " + " -> ".join(parts) + " -> None")

with open(out_path, "w", encoding="utf-8") as out:   
    out.write("хеш таблица со списками \n")
    out.write(f"размер таблицыт {TABLE_SIZE}, слов в тексте: {total}, уникальных: {unique}\n")
    out.write(f"коэффициент заполнения: {unique / TABLE_SIZE:.2f}, коллизий: {collisions}, самая длинная цепочка: {longest}\n")
    out.write("-" * 70 + "\n")
    out.write("\n".join(lines) + "\n")          

print(f"Готово: {out_path}") 