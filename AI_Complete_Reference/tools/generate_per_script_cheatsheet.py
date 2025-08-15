# -*- coding: utf-8 -*-
"""
generate_per_script_cheatsheet.py

用途:
    讀取 `AI_Complete_Reference/tools/All_Scripts_Logic_Analysis.json`，
    為每個腳本建立一個子章節（Markdown），包含結構摘要、統計、與「為什麼這樣寫」理由，
    並匯總成 `AI_Complete_Reference/tools/Per_Script_CheatSheet.md`。
"""
from pathlib import Path
import json


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    tools_dir = root / "AI_Complete_Reference" / "tools"
    src = tools_dir / "All_Scripts_Logic_Analysis.json"
    if not src.exists():
        raise SystemExit(f"找不到分析來源: {src}")
    data = json.loads(src.read_text(encoding="utf-8"))

    out = []
    out.append("# 每檔腳本邏輯速查表\n")
    for i, item in enumerate(data, start=1):
        out.append(f"## {i}. {item.get('file')}")
        if item.get('error'):
            out.append(f"- 讀取錯誤: {item['error']}")
            out.append("")
            continue
        out.append(f"- 工作表: {', '.join(item.get('sheets', []))}")
        out.append(f"- 儀器函數: {', '.join(item.get('instrument_functions', [])) or '-'}")
        dc = item.get('duts_connections', {})
        if dc:
            out.append(f"- DUT 連線: {', '.join(f'{k}:{v}' for k,v in dc.items())}")
        agg = item.get('aggregate', {})
        out.append(f"- 步驟數: {agg.get('total_steps', 0)} | CLI: {agg.get('send_cli', 0)} | Dev: {agg.get('send_device', 0)} | Validation: {agg.get('validations', 0)}")
        phases = ', '.join(f"{k}:{v}" for k,v in (agg.get('phases', {}) or {}).items()) or '-'
        out.append(f"- Phase 分佈: {phases}")
        execm = ', '.join(f"{k}:{v}" for k,v in (agg.get('exec_modes', {}) or {}).items()) or '-'
        out.append(f"- ExecMode: {execm}")
        out.append(f"- 為什麼這樣寫: {'；'.join(item.get('why', []))}")
        out.append("")

    dest = tools_dir / "Per_Script_CheatSheet.md"
    dest.write_text("\n".join(out), encoding="utf-8")
    print(f"已輸出: {dest}")


if __name__ == "__main__":
    main() 