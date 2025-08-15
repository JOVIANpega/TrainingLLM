#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VALO360 腳本分析工具
====================

本工具用於分析 VALO360_TestFlow_20250318_MB_ER2.xlsx 文件，
理解每個有寫字的欄位的作用和功能。

作者: AI 開發團隊
版本: 1.0
創建日期: 2025-01-XX
"""

import pandas as pd
import json
from pathlib import Path
from typing import Dict, List, Any

def analyze_valo360_script():
    """分析 VALO360 腳本文件"""
    
    # 文件路徑
    file_path = "VALO360_TestFlow_20250318_MB_ER2.xlsx"
    
    print("=" * 80)
    print("VALO360 腳本分析報告")
    print("=" * 80)
    print(f"分析文件: {file_path}")
    print()
    
    try:
        # 讀取 Excel 文件
        print("正在讀取 Excel 文件...")
        excel_data = pd.read_excel(file_path, sheet_name=None)
        
        print(f"✅ 成功讀取文件，共 {len(excel_data)} 個工作表")
        print()
        
        # 分析每個工作表
        analysis_results = {}
        
        for sheet_name, sheet_data in excel_data.items():
            print(f"📊 分析工作表: {sheet_name}")
            print(f"   行數: {len(sheet_data)}")
            print(f"   列數: {len(sheet_data.columns)}")
            print(f"   列名: {list(sheet_data.columns)}")
            print()
            
            # 分析工作表內容
            sheet_analysis = analyze_sheet_content(sheet_name, sheet_data)
            analysis_results[sheet_name] = sheet_analysis
        
        # 生成分析報告
        generate_analysis_report(analysis_results, file_path)
        
        return analysis_results
        
    except Exception as e:
        print(f"❌ 分析文件時發生錯誤: {e}")
        return None

def analyze_sheet_content(sheet_name: str, sheet_data: pd.DataFrame) -> Dict[str, Any]:
    """分析工作表內容"""
    
    analysis = {
        "sheet_name": sheet_name,
        "dimensions": {
            "rows": len(sheet_data),
            "columns": len(sheet_data.columns)
        },
        "column_info": {},
        "data_samples": {},
        "non_empty_cells": 0,
        "content_analysis": {}
    }
    
    # 分析每一列
    for col_idx, col_name in enumerate(sheet_data.columns):
        col_data = sheet_data[col_name]
        
        # 統計非空單元格
        non_empty_count = col_data.notna().sum()
        non_empty_percentage = (non_empty_count / len(col_data)) * 100
        
        # 獲取非空值的樣本
        non_empty_values = col_data.dropna().head(5).tolist()
        
        # 分析列內容
        col_analysis = {
            "column_index": col_idx,
            "non_empty_count": non_empty_count,
            "non_empty_percentage": round(non_empty_percentage, 2),
            "data_types": col_data.dtype,
            "sample_values": non_empty_values,
            "unique_values": col_data.nunique(),
            "content_description": analyze_column_content(col_name, non_empty_values)
        }
        
        analysis["column_info"][col_name] = col_analysis
        analysis["non_empty_cells"] += non_empty_count
        
        # 記錄有內容的列
        if non_empty_count > 0:
            analysis["data_samples"][col_name] = non_empty_values
    
    # 分析工作表整體內容
    analysis["content_analysis"] = analyze_overall_content(sheet_name, analysis["data_samples"])
    
    return analysis

def analyze_column_content(col_name: str, sample_values: List[Any]) -> str:
    """分析列內容的含義"""
    
    col_name_lower = str(col_name).lower()
    
    # 根據列名和內容推測列的用途
    if any(keyword in col_name_lower for keyword in ['test', '測試', 'item', '項目']):
        return "測試項目或測試項目編號"
    elif any(keyword in col_name_lower for keyword in ['step', '步驟', 'step_no', '步驟號']):
        return "測試步驟編號或順序"
    elif any(keyword in col_name_lower for keyword in ['description', '描述', 'desc', '說明']):
        return "測試項目描述或說明"
    elif any(keyword in col_name_lower for keyword in ['parameter', '參數', 'param', '設定']):
        return "測試參數或設定值"
    elif any(keyword in col_name_lower for keyword in ['result', '結果', 'status', '狀態']):
        return "測試結果或狀態"
    elif any(keyword in col_name_lower for keyword in ['limit', '限制', '標準', 'criteria']):
        return "測試限制或標準"
    elif any(keyword in col_name_lower for keyword in ['instrument', '儀器', 'equipment', '設備']):
        return "使用的測試儀器或設備"
    elif any(keyword in col_name_lower for keyword in ['time', '時間', 'duration', '持續時間']):
        return "測試時間或持續時間"
    elif any(keyword in col_name_lower for keyword in ['note', '註解', 'remark', '備註']):
        return "註解或備註信息"
    elif any(keyword in col_name_lower for keyword in ['pass', 'fail', 'pass/fail', '通過/失敗']):
        return "測試通過/失敗狀態"
    else:
        # 根據樣本值推測
        if sample_values:
            first_value = str(sample_values[0]).lower()
            if any(keyword in first_value for keyword in ['pass', 'fail', 'ok', 'ng']):
                return "測試結果狀態"
            elif any(keyword in first_value for keyword in ['test', '測試']):
                return "測試相關信息"
            elif first_value.isdigit() or first_value.replace('.', '').isdigit():
                return "數值參數或測量結果"
            else:
                return "文本信息或描述"
        else:
            return "未知用途"
    
    return "需要進一步分析"

def analyze_overall_content(sheet_name: str, data_samples: Dict[str, List[Any]]) -> Dict[str, Any]:
    """分析工作表整體內容"""
    
    analysis = {
        "sheet_type": "未知",
        "main_purpose": "需要進一步分析",
        "key_components": [],
        "test_flow_structure": "未識別",
        "special_features": []
    }
    
    # 根據工作表名稱推測類型
    sheet_name_lower = sheet_name.lower()
    
    if 'testflow' in sheet_name_lower or 'test_flow' in sheet_name_lower:
        analysis["sheet_type"] = "測試流程表"
        analysis["main_purpose"] = "定義測試流程和步驟"
        analysis["test_flow_structure"] = "測試項目 → 步驟 → 參數 → 結果"
        
        # 識別關鍵組件
        if 'mb' in sheet_name_lower:
            analysis["key_components"].append("主機板測試 (Mainboard)")
        if 'er2' in sheet_name_lower:
            analysis["key_components"].append("ER2 版本測試")
    
    elif 'function' in sheet_name_lower:
        analysis["sheet_type"] = "功能測試表"
        analysis["main_purpose"] = "功能驗證和測試"
    
    elif 'oqc' in sheet_name_lower:
        analysis["sheet_type"] = "出貨品質控制表"
        analysis["main_purpose"] = "最終品質檢查"
    
    # 根據數據樣本分析特殊特徵
    for col_name, samples in data_samples.items():
        if samples:
            first_sample = str(samples[0]).lower()
            if any(keyword in first_sample for keyword in ['pass', 'fail', 'ok', 'ng']):
                analysis["special_features"].append("包含測試結果判斷")
            if any(keyword in first_sample for keyword in ['test', '測試']):
                analysis["special_features"].append("包含測試項目定義")
    
    return analysis

def generate_analysis_report(analysis_results: Dict[str, Any], file_path: str):
    """生成分析報告"""
    
    print("=" * 80)
    print("📋 詳細分析報告")
    print("=" * 80)
    
    for sheet_name, sheet_analysis in analysis_results.items():
        print(f"\n📊 工作表: {sheet_name}")
        print(f"   尺寸: {sheet_analysis['dimensions']['rows']} 行 x {sheet_analysis['dimensions']['columns']} 列")
        print(f"   非空單元格: {sheet_analysis['non_empty_cells']}")
        
        # 工作表類型分析
        content_analysis = sheet_analysis['content_analysis']
        print(f"   類型: {content_analysis['sheet_type']}")
        print(f"   主要用途: {content_analysis['main_purpose']}")
        print(f"   測試流程結構: {content_analysis['test_flow_structure']}")
        
        if content_analysis['key_components']:
            print(f"   關鍵組件: {', '.join(content_analysis['key_components'])}")
        
        if content_analysis['special_features']:
            print(f"   特殊特徵: {', '.join(content_analysis['special_features'])}")
        
        # 列詳細分析
        print(f"\n   列詳細分析:")
        for col_name, col_info in sheet_analysis['column_info'].items():
            if col_info['non_empty_count'] > 0:  # 只顯示有內容的列
                print(f"     📝 {col_name}:")
                print(f"        用途: {col_info['content_description']}")
                print(f"        非空值: {col_info['non_empty_count']} ({col_info['non_empty_percentage']}%)")
                print(f"        樣本值: {col_info['sample_values'][:3]}")  # 只顯示前3個樣本
                print(f"        唯一值數量: {col_info['unique_values']}")
    
    # 生成 JSON 報告文件
    report_file = f"VALO360_analysis_report_{Path(file_path).stem}.json"
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(analysis_results, f, ensure_ascii=False, indent=2, default=str)
        print(f"\n✅ 詳細報告已保存到: {report_file}")
    except Exception as e:
        print(f"\n❌ 保存報告時發生錯誤: {e}")

if __name__ == "__main__":
    # 執行分析
    results = analyze_valo360_script()
    
    if results:
        print("\n🎉 分析完成！")
        print("=" * 80)
    else:
        print("\n❌ 分析失敗！") 