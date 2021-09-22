import sys
args = sys.argv

number = args[1]
a = int(number)

#60未満の時「Cランク」
if a < 60:
    print("Cランク")
# 60以上80未満の時「Bランク」
elif 60 <= a < 80:
    print("Bランク")
else: #elseには条件がつかない
    print("Aランク")
