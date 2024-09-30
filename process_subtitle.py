def subtitle_cleaning(file_sub):
    with open(file_sub) as f:
        content = f.read().split("\n")

    new_content = []
    for line in content:
        if line.strip() == "":
            continue
        if line.strip().isnumeric():
            continue
        if "-->" in line:
            start, end = line.split("-->")
            start = start.rsplit(',', 1)[0]
            end = end.rsplit(',', 1)[0]
            new_content.append(f"{start} -> {end}: ")
        else:
            text = line.strip()
            new_content[-1] += text

    with open(file_sub.rsplit('.', 1)[0] + "_handled.txt", "w") as f:
        f.write("\n".join(new_content))
    return file_sub.rsplit('.', 1)[0] + "_handled.txt"

# sub_file = "captions.txt"
# subtitle_cleaning(sub_file)