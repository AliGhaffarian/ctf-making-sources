import os
for i in range (2,18):
    os.system(f"cat register_content_table | cut -f{i} -d '\t' | tail -n+2 | tr -d $'\n'")
    os.system("echo")

