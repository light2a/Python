# Python → AI Engineer

Nhật ký học Python của một dev C# trên đường trở thành AI engineer.
Mỗi bài là một thư mục riêng, gồm code thực hành và bài tập.

## Lộ trình

| Bài | Chủ đề | Trạng thái |
|-----|--------|------------|
| [0.1](0_1_python_basics/) | Python cho dev C#: list/dict/set, comprehension, dataclass, module, venv | ✅ Xong |
| [0.2](0_2_numpy/) | NumPy và tư duy vector hoá: ndarray, shape, mask, broadcasting, view/copy, z-score, khoảng cách | ✅ Xong |

## Cấu trúc

```
Python/
├── 0_1_python_basics/   # Bài 0.1
│   ├── check.py         # Bài kiểm tra tự động
│   └── requirements.txt
└── 0_2_numpy/           # Bài 0.2
```

## Chạy code

Mỗi bài có môi trường ảo (`.venv`) riêng, không đẩy lên git.

```bash
# Tạo môi trường và cài thư viện (ví dụ bài 0.1)
python3 -m venv 0_1_python_basics/.venv
0_1_python_basics/.venv/bin/pip install -r 0_1_python_basics/requirements.txt

# Chạy bài kiểm tra
0_1_python_basics/.venv/bin/python 0_1_python_basics/check.py
```

## Môi trường

- macOS, Python 3.14 (Homebrew)
- Quản lý gói: `pip` + `venv`, hoặc `uv`
