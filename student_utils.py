def parse_student(line):
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError("字段数量错误")
    name = parts[0].strip()
    score = int(parts[1].strip())
    if name == "":
        raise ValueError("姓名为空")
    if score < 0 or score > 100:
        raise ValueError("成绩超出范围")
    return {"name": name, "score": score}
