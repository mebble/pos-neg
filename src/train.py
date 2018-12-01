from sklearn.datasets import load_files

data = load_files('../dataset/txt_sentoken', encoding="utf-8", decode_error="replace")

print(type(data))
