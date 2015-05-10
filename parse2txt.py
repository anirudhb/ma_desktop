import sys
s = sys.stdin.read()
while "<" in s or ">" in s:
    s = s.replace(s[s.index("<"):s.index(">")+1], "")
print s
