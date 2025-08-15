#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增強版 INI 檔案解析器
專門處理 Centimani 專案中的非標準 INI 檔案格式

主要功能：
1. 解析包含 // 註解的 INI 檔案
2. 處理重複的設定項目
3. 提取關鍵設定資訊
4. 生成標準化的設定參考

作者：AI Assistant
版本：1.0.0
日期：2024-12-19
"""

import re
import json
from pathlib import Path
from collections import defaultdict

class EnhancedINIParser:
    """增強版 INI 檔案解析器"""
    
    def __init__(self):
        """初始化解析器"""
        self.settings = {}
        self.comments = {}
        self.sections = []
        
    def parse_file(self, file_path):
        """解析 INI 檔案"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            return self.parse_content(content, file_path)
            
        except Exception as e:
            print(f"解析檔案 {file_path} 時發生錯誤: {e}")
            return None
            
    def parse_content(self, content, file_path):
        """解析檔案內容"""
        lines = content.split('\n')
        current_section = None
        section_data = {}
        section_comments = {}
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # 跳過空行
            if not line:
                continue
                
            # 檢查是否為註解
            if line.startswith('//'):
                if current_section:
                    if current_section not in section_comments:
                        section_comments[current_section] = []
                    section_comments[current_section].append({
                        'line': line_num,
                        'comment': line[2:].strip()
                    })
                continue
                
            # 檢查是否為區段標題
            if line.startswith('[') and line.endswith(']'):
                # 儲存前一個區段
                if current_section and section_data:
                    self.settings[current_section] = section_data
                    self.comments[current_section] = section_comments.get(current_section, [])
                    
                # 開始新區段
                current_section = line[1:-1]
                section_data = {}
                section_comments = {}
                self.sections.append(current_section)
                continue
                
            # 解析設定項目
            if current_section and '=' in line:
                try:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # 處理重複的鍵值
                    if key in section_data:
                        if isinstance(section_data[key], list):
                            section_data[key].append(value)
                        else:
                            section_data[key] = [section_data[key], value]
                    else:
                        section_data[key] = value
                        
                except ValueError:
                    # 無法解析的行，記錄為註解
                    if current_section not in section_comments:
                        section_comments[current_section] = []
                    section_comments[current_section].append({
                        'line': line_num,
                        'comment': line
                    })
                    
        # 儲存最後一個區段
        if current_section and section_data:
            self.settings[current_section] = section_data
            self.comments[current_section] = section_comments.get(current_section, [])
            
        return {
            'file_path': str(file_path),
            'sections': self.sections,
            'settings': self.settings,
            'comments': self.comments
        }
        
    def extract_key_settings(self, parsed_data):
        """提取關鍵設定"""
        key_settings = []
        
        for section_name, section_data in parsed_data['settings'].items():
            for key, value in section_data.items():
                # 識別重要的設定類型
                setting_type = self.categorize_setting(key, value)
                
                key_settings.append({
                    'section': section_name,
                    'key': key,
                    'value': value,
                    'type': setting_type,
                    'comments': self.get_comments_for_setting(parsed_data['comments'], section_name, key)
                })
                
        return key_settings
        
    def categorize_setting(self, key, value):
        """分類設定類型"""
        key_lower = key.lower()
        value_lower = str(value).lower()
        
        if any(word in key_lower for word in ['ip', 'address', 'host']):
            return 'Network'
        elif any(word in key_lower for word in ['port', 'com', 'baud']):
            return 'Communication'
        elif any(word in key_lower for word in ['path', 'file', 'folder']):
            return 'File_Path'
        elif any(word in key_lower for word in ['time', 'delay', 'timeout']):
            return 'Timing'
        elif any(word in key_lower for word in ['enable', 'disable', 'on', 'off']):
            return 'Feature_Flag'
        elif any(word in key_lower for word in ['model', 'version', 'name']):
            return 'Device_Info'
        else:
            return 'Other'
            
    def get_comments_for_setting(self, comments, section, key):
        """獲取設定的相關註解"""
        section_comments = comments.get(section, [])
        relevant_comments = []
        
        for comment in section_comments:
            if comment['comment'].lower().find(key.lower()) != -1:
                relevant_comments.append(comment['comment'])
                
        return relevant_comments
        
    def generate_summary(self, parsed_data):
        """生成設定摘要"""
        summary = {
            'total_sections': len(parsed_data['sections']),
            'total_settings': sum(len(section) for section in parsed_data['settings'].values()),
            'section_summary': {},
            'setting_types': defaultdict(int),
            'key_settings': self.extract_key_settings(parsed_data)
        }
        
        # 統計每個區段的設定數量
        for section_name, section_data in parsed_data['settings'].items():
            summary['section_summary'][section_name] = {
                'setting_count': len(section_data),
                'comment_count': len(parsed_data['comments'].get(section_name, [])),
                'sample_settings': list(section_data.keys())[:5]  # 前5個設定作為範例
            }
            
        # 統計設定類型
        for setting in summary['key_settings']:
            summary['setting_types'][setting['type']] += 1
            
        return summary

def main():
    """主程式"""
    print("增強版 INI 檔案解析器")
    print("=" * 40)
    
    parser = EnhancedINIParser()
    
    # 解析 Centimani DOC 資料夾中的 INI 檔案
    ini_files = [
        "Centimani DOC/Global.ini",
        "Centimani DOC/System.ini"
    ]
    
    all_results = {}
    
    for ini_file in ini_files:
        if Path(ini_file).exists():
            print(f"\n解析檔案: {ini_file}")
            result = parser.parse_file(ini_file)
            
            if result:
                summary = parser.generate_summary(result)
                all_results[ini_file] = summary
                
                print(f"  - 區段數量: {summary['total_sections']}")
                print(f"  - 設定總數: {summary['total_settings']}")
                print(f"  - 設定類型: {dict(summary['setting_types'])}")
                
        else:
            print(f"檔案不存在: {ini_file}")
            
    # 儲存解析結果
    if all_results:
        output_dir = Path("organized_data/ini_settings_enhanced")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # 儲存為 JSON
        with open(output_dir / "enhanced_ini_analysis.json", 'w', encoding='utf-8') as f:
            json.dump(all_results, f, ensure_ascii=False, indent=2)
            
        # 儲存關鍵設定為 CSV
        all_key_settings = []
        for file_path, summary in all_results.items():
            for setting in summary['key_settings']:
                all_key_settings.append({
                    'File': Path(file_path).name,
                    'Section': setting['section'],
                    'Key': setting['key'],
                    'Value': setting['value'],
                    'Type': setting['type'],
                    'Comments': '; '.join(setting['comments'])
                })
                
        if all_key_settings:
            import pandas as pd
            df = pd.DataFrame(all_key_settings)
            df.to_csv(output_dir / "enhanced_ini_settings.csv", 
                     index=False, encoding='utf-8-sig')
            
        print(f"\n解析結果已儲存至: {output_dir}")
        
if __name__ == "__main__":
    main() 