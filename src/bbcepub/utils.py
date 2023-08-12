def read_user_input(input_path):
    with open(input_path, "r") as f:
        lines = f.readlines()
    return lines


def get_user_config(input_path):
    lines = read_user_input(input_path)
    if len(lines) < 1:
        raise ValueError(rf"No title or article urls specified in '{input_path}'")
    if len(lines) < 2:
        raise ValueError(rf"No article urls specified in '{input_path}'")
    if len(lines) > 101:
        raise ValueError(rf"Too many urls specified in '{input_path}' (max 100)")
    title = lines[0].strip()
    urls = [url.strip() for url in lines[1:]]
    return title, urls
