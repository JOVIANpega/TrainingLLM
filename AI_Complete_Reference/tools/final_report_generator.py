#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最終整合報告生成器
整合所有 Centimani 資料分析結果，生成完整的速查表和範例

主要功能：
1. 整合 Excel 檔案分析結果
2. 整合 INI 設定分析結果
3. 生成完整的速查表
4. 創建使用範例和最佳實踐指南
5. 輸出多種格式的報告

作者：AI Assistant
版本：1.0.0
日期：2024-12-19
"""

import json
import pandas as pd
from pathlib import Path
from datetime import datetime
import os

class FinalReportGenerator:
    """最終整合報告生成器"""
    
    def __init__(self):
        """初始化報告生成器"""
        self.base_dir = Path("organized_data")
        self.output_dir = Path("final_reports")
        self.output_dir.mkdir(exist_ok=True)
        
        # 載入所有分析結果
        self.excel_data = None
        self.ini_data = None
        self.quick_ref = None
        
    def load_all_data(self):
        """載入所有分析資料"""
        print("載入分析資料...")
        
        # 載入 Excel 檔案總覽
        excel_file = self.base_dir / "quick_reference" / "excel_files_overview.csv"
        if excel_file.exists():
            self.excel_data = pd.read_csv(excel_file)
            print(f"載入 Excel 資料: {len(self.excel_data)} 筆記錄")
            
        # 載入測試流程分類
        test_flow_file = self.base_dir / "quick_reference" / "test_flow_categories.csv"
        if test_flow_file.exists():
            self.test_flow_data = pd.read_csv(test_flow_file)
            print(f"載入測試流程資料: {len(self.test_flow_data)} 筆記錄")
            
        # 載入 INI 設定
        ini_file = self.base_dir / "ini_settings_enhanced" / "enhanced_ini_settings.csv"
        if ini_file.exists():
            self.ini_data = pd.read_csv(ini_file)
            print(f"載入 INI 設定資料: {len(self.ini_data)} 筆記錄")
            
        # 載入速查表
        quick_ref_file = self.base_dir / "quick_reference" / "quick_reference.json"
        if quick_ref_file.exists():
            with open(quick_ref_file, 'r', encoding='utf-8') as f:
                self.quick_ref = json.load(f)
            print("載入速查表資料")
            
    def generate_comprehensive_quick_reference(self):
        """生成綜合速查表"""
        print("生成綜合速查表...")
        
        # 1. 檔案分類統計
        file_stats = {}
        if self.excel_data is not None:
            category_counts = self.excel_data['Category'].value_counts()
            file_stats = {
                'total_files': len(self.excel_data),
                'category_breakdown': category_counts.to_dict(),
                'platform_summary': self.generate_platform_summary()
            }
            
        # 2. 測試流程總覽
        test_flow_summary = {}
        if hasattr(self, 'test_flow_data') and self.test_flow_data is not None:
            test_flow_summary = self.generate_test_flow_summary()
            
        # 3. INI 設定總覽
        ini_summary = {}
        if self.ini_data is not None:
            ini_summary = self.generate_ini_summary()
            
        # 4. 整合速查表
        comprehensive_ref = {
            'generated_date': datetime.now().isoformat(),
            'file_statistics': file_stats,
            'test_flow_overview': test_flow_summary,
            'ini_settings_overview': ini_summary,
            'usage_examples': self.generate_usage_examples(),
            'best_practices': self.generate_best_practices()
        }
        
        # 儲存綜合速查表
        with open(self.output_dir / "comprehensive_quick_reference.json", 'w', encoding='utf-8') as f:
            json.dump(comprehensive_ref, f, ensure_ascii=False, indent=2)
            
        print("綜合速查表生成完成")
        return comprehensive_ref
        
    def generate_platform_summary(self):
        """生成平台摘要"""
        if self.excel_data is None:
            return {}
            
        platform_summary = {}
        
        # KANGAROO 平台
        kangaroo_files = self.excel_data[self.excel_data['Category'] == 'KANGAROO']
        if not kangaroo_files.empty:
            platform_summary['KANGAROO'] = {
                'total_files': len(kangaroo_files),
                'file_types': kangaroo_files['File_Name'].tolist(),
                'main_categories': ['Mainboard', 'OQC', 'Cellular', 'WIFI_BT', 'OTA', 'MultiDUT']
            }
            
        # VALO360 平台
        valo360_files = self.excel_data[self.excel_data['Category'] == 'VALO360']
        if not valo360_files.empty:
            platform_summary['VALO360'] = {
                'total_files': len(valo360_files),
                'file_types': valo360_files['File_Name'].tolist(),
                'main_categories': ['ER2', 'POE', 'IMU', 'Function', 'DMIC']
            }
            
        # Centimani 工具
        centimani_files = self.excel_data[self.excel_data['Category'] == 'Centimani']
        if not centimani_files.empty:
            platform_summary['Centimani'] = {
                'total_files': len(centimani_files),
                'file_types': centimani_files['File_Name'].tolist(),
                'main_categories': ['INI_Settings', 'Parameters', 'Script_Guide']
            }
            
        return platform_summary
        
    def generate_test_flow_summary(self):
        """生成測試流程摘要"""
        if not hasattr(self, 'test_flow_data') or self.test_flow_data is None:
            return {}
            
        summary = {}
        
        # 按平台分組
        for platform in self.test_flow_data['Platform'].unique():
            platform_data = self.test_flow_data[self.test_flow_data['Platform'] == platform]
            categories = platform_data['Category'].unique()
            
            summary[platform] = {
                'total_flows': len(platform_data),
                'categories': list(categories),
                'category_details': {}
            }
            
            # 每個分類的詳細資訊
            for category in categories:
                category_data = platform_data[platform_data['Category'] == category]
                summary[platform]['category_details'][category] = {
                    'count': len(category_data),
                    'files': category_data['File_Name'].tolist()
                }
                
        return summary
        
    def generate_ini_summary(self):
        """生成 INI 設定摘要"""
        if self.ini_data is None:
            return {}
            
        summary = {
            'total_settings': len(self.ini_data),
            'files': self.ini_data['File'].unique().tolist(),
            'sections': self.ini_data['Section'].unique().tolist(),
            'setting_types': self.ini_data['Type'].value_counts().to_dict(),
            'key_network_settings': self.extract_key_network_settings(),
            'key_device_settings': self.extract_key_device_settings()
        }
        
        return summary
        
    def extract_key_network_settings(self):
        """提取關鍵網路設定"""
        if self.ini_data is None:
            return []
            
        network_settings = self.ini_data[self.ini_data['Type'] == 'Network']
        key_settings = []
        
        for _, row in network_settings.iterrows():
            key_settings.append({
                'file': row['File'],
                'section': row['Section'],
                'key': row['Key'],
                'value': row['Value'],
                'description': self.get_setting_description(row['Key'])
            })
            
        return key_settings
        
    def extract_key_device_settings(self):
        """提取關鍵設備設定"""
        if self.ini_data is None:
            return []
            
        device_settings = self.ini_data[self.ini_data['Type'] == 'Device_Info']
        key_settings = []
        
        for _, row in device_settings.iterrows():
            key_settings.append({
                'file': row['File'],
                'section': row['Section'],
                'key': row['Key'],
                'value': row['Value'],
                'description': self.get_setting_description(row['Key'])
            })
            
        return key_settings
        
    def get_setting_description(self, key):
        """獲取設定的描述"""
        descriptions = {
            'PCIP_1': 'PC 端 IP 位址',
            'DUTIP_1': '被測設備 IP 位址',
            'DUT_UR1': '被測設備 UART 埠',
            'PCUART_fixture': 'PC 端夾具 UART 埠',
            'VALO360_ALL_MODEL': 'VALO360 所有支援的型號',
            'FW_VERSION': '韌體版本',
            'Product_SKU': '產品 SKU',
            'sfisSKU': 'SFIS 系統 SKU'
        }
        
        return descriptions.get(key, '一般設定')
        
    def generate_usage_examples(self):
        """生成使用範例"""
        examples = {
            'finding_test_flows': {
                'description': '如何找到特定的測試流程檔案',
                'examples': [
                    '要找 KANGAROO 主機板測試流程，查看 Category=KANGAROO 且包含 "Mainboard" 的檔案',
                    '要找 VALO360 ER2 測試流程，查看 Platform=VALO360 且 Category=ER2 的檔案',
                    '要找蜂窩網路驗證流程，查看包含 "Cellular" 關鍵字的檔案'
                ]
            },
            'ini_configuration': {
                'description': '如何配置 INI 檔案',
                'examples': [
                    '網路設定：修改 [Settings] 區段中的 PCIP_1 和 DUTIP_1',
                    '設備設定：修改 [Scripts] 區段中的 VALO360_ALL_MODEL',
                    '功能開關：修改 [System] 區段中的 Feature_Flag 類型設定'
                ]
            },
            'file_organization': {
                'description': '檔案組織結構說明',
                'examples': [
                    'KANGAROO 平台：主機板、OQC、蜂窩網路、WiFi/BT、OTA、多設備測試',
                    'VALO360 平台：ER2、POE、IMU、功能驗證、DMIC 測試',
                    'Centimani 工具：INI 設定、參數、腳本指南'
                ]
            }
        }
        
        return examples
        
    def generate_best_practices(self):
        """生成最佳實踐指南"""
        best_practices = {
            'file_management': [
                '使用統一的命名規範：Platform_TestType_Date_Version.xlsx',
                '定期更新測試項目代碼檔案',
                '保持檔案版本的一致性'
            ],
            'configuration_management': [
                '備份原始的 INI 設定檔案',
                '使用註解說明重要設定的用途',
                '測試環境和生產環境使用不同的設定檔案'
            ],
            'testing_workflow': [
                '根據設備型號選擇對應的測試流程',
                '確認測試環境的網路和設備設定',
                '記錄測試過程中的重要參數和結果'
            ],
            'troubleshooting': [
                '檢查網路連線和 IP 設定',
                '確認設備埠號和通訊設定',
                '查看日誌檔案中的錯誤資訊'
            ]
        }
        
        return best_practices
        
    def generate_csv_reports(self):
        """生成 CSV 格式的報告"""
        print("生成 CSV 報告...")
        
        # 1. 檔案總覽報告
        if self.excel_data is not None:
            self.excel_data.to_csv(self.output_dir / "file_overview_report.csv", 
                                 index=False, encoding='utf-8-sig')
            
        # 2. 測試流程詳細報告
        if hasattr(self, 'test_flow_data') and self.test_flow_data is not None:
            self.test_flow_data.to_csv(self.output_dir / "test_flow_detailed_report.csv", 
                                     index=False, encoding='utf-8-sig')
            
        # 3. INI 設定詳細報告
        if self.ini_data is not None:
            self.ini_data.to_csv(self.output_dir / "ini_settings_detailed_report.csv", 
                               index=False, encoding='utf-8-sig')
            
        # 4. 關鍵設定快速查詢表
        if self.ini_data is not None:
            key_settings = self.ini_data[self.ini_data['Type'].isin(['Network', 'Device_Info', 'Feature_Flag'])]
            key_settings.to_csv(self.output_dir / "key_settings_quick_lookup.csv", 
                              index=False, encoding='utf-8-sig')
            
        print("CSV 報告生成完成")
        
    def generate_markdown_report(self):
        """生成 Markdown 格式的報告"""
        print("生成 Markdown 報告...")
        
        report = f"""# Centimani 資料整合報告

## 生成時間
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 資料概覽

### 檔案統計
- **總檔案數**: {len(self.excel_data) if self.excel_data is not None else 0}
- **主要平台**: KANGAROO, VALO360, Centimani
- **檔案類型**: Excel 測試流程、INI 設定、測試項目代碼

### 平台分類

#### KANGAROO 平台
- 主機板測試流程
- OQC 出貨品質檢查
- 蜂窩網路驗證
- WiFi & Bluetooth 校準驗證
- OTA 韌體升級測試
- 多設備測試

#### VALO360 平台
- ER2 功能檢查
- POE 測試流程
- IMU 測試流程
- 功能驗證測試
- DMIC 測試流程

#### Centimani 工具
- INI 設定檔案
- 儀器參數設定
- 腳本使用指南

## 快速查詢指南

### 1. 找到特定測試流程
- 使用 `file_overview_report.csv` 按類別篩選
- 使用 `test_flow_detailed_report.csv` 按平台和功能篩選

### 2. 配置系統設定
- 使用 `ini_settings_detailed_report.csv` 查看所有設定
- 使用 `key_settings_quick_lookup.csv` 快速找到重要設定

### 3. 檔案組織結構
- 按平台分類：KANGAROO、VALO360
- 按功能分類：Mainboard、OQC、Cellular、WiFi_BT、OTA、ER2、POE、IMU

## 使用範例

### 測試流程選擇
1. 確認設備平台 (KANGAROO 或 VALO360)
2. 選擇測試類型 (主機板、OQC、蜂窩網路等)
3. 根據日期選擇最新版本

### 設定配置
1. 修改網路設定 (IP 位址、埠號)
2. 配置設備參數 (型號、版本)
3. 啟用/停用功能開關

## 最佳實踐

### 檔案管理
- 使用統一的命名規範
- 定期更新測試項目代碼
- 保持版本一致性

### 配置管理
- 備份原始設定檔案
- 使用註解說明設定用途
- 區分測試和生產環境

### 測試流程
- 根據設備型號選擇對應流程
- 確認環境設定正確性
- 記錄重要參數和結果

## 輸出檔案說明

- **comprehensive_quick_reference.json**: 完整的速查表 (JSON 格式)
- **file_overview_report.csv**: 檔案總覽報告
- **test_flow_detailed_report.csv**: 測試流程詳細報告
- **ini_settings_detailed_report.csv**: INI 設定詳細報告
- **key_settings_quick_lookup.csv**: 關鍵設定快速查詢表

## 聯絡資訊

如有問題或建議，請參考原始資料或聯絡系統管理員。
"""
        
        with open(self.output_dir / "comprehensive_report.md", 'w', encoding='utf-8') as f:
            f.write(report)
            
        print("Markdown 報告生成完成")
        
    def run_generation(self):
        """執行完整的報告生成"""
        print("開始生成最終整合報告...")
        
        # 1. 載入所有資料
        self.load_all_data()
        
        # 2. 生成綜合速查表
        comprehensive_ref = self.generate_comprehensive_quick_reference()
        
        # 3. 生成 CSV 報告
        self.generate_csv_reports()
        
        # 4. 生成 Markdown 報告
        self.generate_markdown_report()
        
        print(f"\n報告生成完成！")
        print(f"輸出目錄: {self.output_dir}")
        print("\n主要輸出檔案:")
        print("- comprehensive_quick_reference.json - 綜合速查表")
        print("- comprehensive_report.md - 完整報告")
        print("- *_report.csv - 各種 CSV 報告")
        
        return comprehensive_ref

def main():
    """主程式"""
    print("Centimani 最終整合報告生成器")
    print("=" * 50)
    
    generator = FinalReportGenerator()
    result = generator.run_generation()
    
    print("\n生成完成！")

if __name__ == "__main__":
    main() 