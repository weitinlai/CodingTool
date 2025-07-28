import json
import os

def generate_doxygen_comment(func):
    lines = ["/**"]
    lines.append(f" * @brief {func['description']}")
    lines.append(" *")
    for param in func["params"]:
        lines.append(f" * @param {param['name']} {param['description']}")
    lines.append(f" * @return {func['return_type']}")
    lines.append(" */")
    return "\n".join(lines)

def generate_markdown_doc(funcs, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        f.write(f"# 📘 API Documentation\n\n")
        for func in funcs:
            f.write(f"## `{func['name']}`\n")
            f.write(f"**Description:** {func['description']}\n\n")
            f.write(f"**Declaration:**\n```c\n{func['return_type']} {func['name']}(")
            f.write(", ".join([f"{p['type']} {p['name']}" for p in func['params']]))
            f.write(");\n```\n\n")

            if func['params']:
                f.write("**Parameters:**\n")
                for p in func['params']:
                    f.write(f"- `{p['name']}` ({p['type']}): {p['description']}\n")
                f.write("\n")

            f.write(f"**Returns:** `{func['return_type']}`\n\n---\n")

    print(f"📄 Markdown doc '{output_path}' generated.")

def generate_header(data):
    output_file = data["header"]
    guard = os.path.basename(output_file).replace(".", "_").upper()
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        f.write("/* Auto-generated C API Header File */\n")
        f.write(f"#ifndef {guard}\n#define {guard}\n\n")

        for func in data["functions"]:
            f.write(generate_doxygen_comment(func) + "\n")
            params = ", ".join([f"{p['type']} {p['name']}" for p in func['params']])
            f.write(f"{func['return_type']} {func['name']}({params});\n\n")

        f.write(f"#endif // {guard}\n")

    print(f"✅ Header file '{output_file}' generated.")

def main(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)

    generate_header(data)

    if "doc_output" in data:
        generate_markdown_doc(data["functions"], data["doc_output"])

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python generate_capi_with_doc.py api_definitions.json")
        sys.exit(1)

    main(sys.argv[1])
