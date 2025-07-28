從 JSON 產生 .h 檔＋ .md API 文件

你會得到：

✅ my_api.h → 含有 Doxygen 註解的 C API header
✅ my_api.md → 清楚的 Markdown 格式 API 說明文件，可放 README 或文件頁

python generate_capi_with_doc.py api_definitions.json

include/
  └── my_api.h     ← 含 Doxygen 註解
docs/
  └── my_api.md    ← Markdown API 說明文件
