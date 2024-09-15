
register_set = ["rax", "rcx", "rdx", "rbx", "rsi", "rdi", "rsp", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
for register in register_set:
    string = input()
    string=string.replace(".","1")
    print(register +"\t" + hex(int(string, 2)))



