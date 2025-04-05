import pickle

with open("app/embeddings.pkl", "rb") as f:
    data = pickle.load(f)

print("\n📦 Type of loaded object:", type(data))

if isinstance(data, dict):
    print("📑 Keys:", data.keys())
elif isinstance(data, tuple):
    print("🧩 Tuple length:", len(data))
    for i, part in enumerate(data):
        print(f"\n🔍 Part {i} type: {type(part)}")
        if hasattr(part, "head"):
            print(part.head())
else:
    print("⚠️ Unexpected format")
