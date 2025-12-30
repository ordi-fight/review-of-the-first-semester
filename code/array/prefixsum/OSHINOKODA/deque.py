import sys
from collections import deque



# 第一次掃描：處理前面的資料，同時保留最後兩行
all_lines = []   # 如果你真的需要「再次處理」可以存，但會爆記憶體
for line in sys.stdin:
    all_lines.append(line.strip())
buffer = deque(all_lines,maxlen=2)

# 現在 buffer 只剩最後 2 行
queries = [list(map(int, line.split())) for line in buffer]

print( queries)