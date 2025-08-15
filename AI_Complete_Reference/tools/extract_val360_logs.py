# -*- coding: utf-8 -*-
"""
extract_val360_logs.py

用途:
    掃描 `Centimani DOC/LOG` 目錄下的若干 LOG，取樣命令與回覆片段，
    匯整成 JSON 供 AI 參考比對腳本命令使用。
輸出:
    AI_Complete_Reference/tools/VAL360_LOG_Samples.json
"""
from pathlib import Path
import json
import re

# 粗略規則: 以 '>' 開頭視為執行命令, 以 '<' 或不含 '>' 視為回覆行（依實際LOG格式調整）
CMD_RE = re.compile(r"^\s*[>].*")


def sample_log(file_path: Path, max_lines: int = 500) -> dict:
    result = {"file": str(file_path), "commands": [], "replies": []}
    try:
        with file_path.open('r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()[:max_lines]
        for line in lines:
            s = line.strip()
            if not s:
                continue
            if CMD_RE.match(s):
                result["commands"].append(s)
            else:
                result["replies"].append(s)
        # 取樣前20條
        result["commands"] = result["commands"][:20]
        result["replies"] = result["replies"][:20]
    except Exception as e:
        result["error"] = str(e)
    return result


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    log_dir = root / "Centimani DOC" / "LOG"
    if not log_dir.exists():
        raise SystemExit(f"找不到 LOG 目錄: {log_dir}")

    logs = sorted([p for p in log_dir.iterdir() if p.is_file() and p.suffix.lower() == '.log'])[:6]
    samples = [sample_log(p) for p in logs]

    out_json = Path(__file__).resolve().parent / "VAL360_LOG_Samples.json"
    out_json.write_text(json.dumps({"dir": str(log_dir), "samples": samples}, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"已輸出: {out_json}")


if __name__ == '__main__':
    main() 