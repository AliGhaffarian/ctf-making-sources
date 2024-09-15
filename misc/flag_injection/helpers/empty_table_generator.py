register_set = ["rax", "rcx", "rdx", "rbx", "rsi", "rdi", "rsp", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]

print("\t", end="")
for register in register_set:
    print(register + "\t", end="")
print()

for i in range (64):
    print(f"{i}\t", end="")
    for j in range(len(register_set)):
        print(f"0\t",end="")
    print()

