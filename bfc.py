

# 定义 Brainfuck 解释器函数 bfc，接受代码和可选参数 inl（初始化时的内存长度，默认为 128）
def bfc(code, inl=128):
    try:
        # 初始化 Brainfuck 内存数组 bf，指针位置 p，计数器 i，和括号跟踪栈 stack
        bf = list(code)
        l = inl
        if type(inl) == int:
            l = [0] * inl
        l = list(l)
        p = 0
        i = 0
        pr = ""
        stack = []  # 用于跟踪括号的栈

        # 遍历 Brainfuck 代码
        while i < len(code):
            # 处理 ">" 指令，移动指针到右边
            if bf[i] == ">":
                if p < len(l):
                    p += 1

            # 处理 "<" 指令，移动指针到左边
            elif bf[i] == "<":
                if p > 0:
                    p -= 1

            # 处理 "+" 指令，增加当前内存位置的值
            elif bf[i] == "+":
                l[p] += 1

            # 处理 "-" 指令，减少当前内存位置的值
            elif bf[i] == "-":
                l[p] -= 1

            # 处理 "." 指令，输出当前内存位置的 ASCII 字符
            elif bf[i] == "." and l[p] < 128 and l[p]>=0:
                pr += chr(l[p])

            # 处理 "," 指令，从用户输入获取字符并存入当前内存位置
            elif bf[i] == ",":
                pass
                # l[p] = ord(input())

            # 处理 "[" 指令，如果当前内存位置为零，跳转到对应的 "]"
            elif bf[i] == "[" and l[p] == 0:
                qz = 1
                while qz > 0:
                    i += 1
                    if bf[i] == "[":
                        qz += 1
                    elif bf[i] == "]":
                        qz -= 1
            
            # 处理 "[" 指令，如果当前内存位置不为零，将当前位置压入栈
            elif bf[i] == "[" and l[p] != 0:
                stack.append(i)

            # 处理 "]" 指令，如果当前内存位置不为零，跳转到对应的 "["
            elif bf[i] == "]":
                if l[p] != 0:
                    i = stack[-1]
                else:
                    stack.pop()

            # 处理 "~" 指令，返回当前内存数组
            elif bf[i] == "~":
                return pr

            i += 1
            
        return pr
    
    except:
        return

