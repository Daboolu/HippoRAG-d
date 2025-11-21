import json

def explore_json(obj, indent=0, max_depth=10):
    """递归打印 JSON 结构（层级预览）"""
    prefix = "  " * indent
    if isinstance(obj, dict):
        for k, v in obj.items():
            print(f"{prefix}- {k}: {type(v).__name__}")
            if indent < max_depth:
                explore_json(v, indent + 1, max_depth)
    elif isinstance(obj, list):
        print(f"{prefix}- [list] 长度: {len(obj)}")
        if obj and indent < max_depth:
            explore_json(obj[0], indent + 1, max_depth)
    else:
        print(f"{prefix}- 值类型: {type(obj).__name__}, 示例值: {str(obj)[:80]}")

# === 用法 ===
import pathlib
path = pathlib.Path("/home/daisj/sijundai/HippoRAG-d/reproduce/dataset/hotpotqa_corpus.json")
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)
print(f"Exploring JSON structure of file: {path}\n\n")
explore_json(data, max_depth=3)
