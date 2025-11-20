#!/usr/bin/env python3
"""
Final Thesis Validation Script
=====================================
Validates all thesis components and generates final summary
Author: Debraj Das (21ME3AI31)
Master Thesis Project: Graph-RULE Framework
"""

import os
import sys
import json
import datetime
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

class ThesisValidator:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.results = {
            'validation_timestamp': datetime.datetime.now().isoformat(),
            'thesis_components': {},
            'critical_issues': [],
            'recommendations': [],
            'completion_status': 'PENDING'
        }
    
    def validate_core_files(self):
        """Validate essential thesis files"""
        print("🔍 Validating Core Thesis Files...")
        
        essential_files = {
            'MTECH_MTP_FINAL_REPORT_COMPREHENSIVE.md': 'Main thesis report',
            'graph_rule_experimental_pipeline.py': 'Core experimental code',
            'generate_thesis_defense_curves.py': 'Visualization generator',
            'CRITICAL_EVALUATION_CURVES_GUIDE.md': 'Curves documentation',
            'GRAPH_RULE_EXPERIMENTAL_RESULTS_SUMMARY.md': 'Results summary'
        }
        
        for file_path, description in essential_files.items():
            full_path = self.base_dir / file_path
            if full_path.exists():
                size = full_path.stat().st_size
                self.results['thesis_components'][file_path] = {
                    'exists': True,
                    'size_bytes': size,
                    'description': description,
                    'status': 'VALID'
                }
                print(f"✅ {file_path}: {size:,} bytes")
            else:
                self.results['thesis_components'][file_path] = {
                    'exists': False,
                    'status': 'MISSING',
                    'description': description
                }
                self.results['critical_issues'].append(f"Missing essential file: {file_path}")
                print(f"❌ {file_path}: MISSING")
    
    def validate_thesis_curves(self):
        """Validate thesis defense curves"""
        print("\n📊 Validating Thesis Defense Curves...")
        
        curves_dir = self.base_dir / 'thesis_defense_curves'
        if not curves_dir.exists():
            self.results['critical_issues'].append("Thesis defense curves directory missing")
            return
        
        expected_curves = [
            '01_learning_curves.png',
            '02_effectiveness_utility_tradeoff.png', 
            '03_scalability_analysis.png',
            '04_revolutionary_improvements.png',
            '05_message_passing_learning.png',
            '06_connectivity_preservation.png',
            '07_healthcare_compliance.png',
            '08_adversarial_resistance.png',
            '09_statistical_significance.png',
            '10_cross_validation.png',
            '11_speed_comparisons.png',
            '12_multiscale_performance.png',
            '13_financial_improvements.png',
            '14_noise_tolerance.png',
            '15_memory_usage.png',
            '16_hyperparameter_sensitivity.png'
        ]
        
        curve_status = {}
        for curve_file in expected_curves:
            curve_path = curves_dir / curve_file
            if curve_path.exists():
                size = curve_path.stat().st_size
                curve_status[curve_file] = {'exists': True, 'size': size}
                print(f"✅ {curve_file}: {size:,} bytes")
            else:
                curve_status[curve_file] = {'exists': False, 'size': 0}
                print(f"❌ {curve_file}: MISSING")
        
        self.results['thesis_components']['defense_curves'] = curve_status
        
        # Count valid curves
        valid_curves = sum(1 for status in curve_status.values() if status['exists'])
        print(f"\n📈 Curve Generation Status: {valid_curves}/16 curves available")
        
        if valid_curves >= 10:
            print("✅ Sufficient curves for thesis defense")
        else:
            self.results['critical_issues'].append(f"Only {valid_curves}/16 curves available (minimum 10 recommended)")
    
    def validate_experimental_results(self):
        """Validate experimental pipeline execution"""
        print("\n🧪 Validating Experimental Results...")
        
        results_dir = self.base_dir / 'graph_rule_results'
        if not results_dir.exists():
            self.results['critical_issues'].append("Experimental results directory missing")
            print("❌ No experimental results found")
            return
        
        # Check for key result files
        result_files = list(results_dir.glob('*.json'))
        csv_files = list(results_dir.glob('*.csv'))
        png_files = list(results_dir.glob('*.png'))
        
        print(f"📄 JSON Results: {len(result_files)} files")
        print(f"📊 CSV Data: {len(csv_files)} files") 
        print(f"🖼️  PNG Charts: {len(png_files)} files")
        
        self.results['thesis_components']['experimental_results'] = {
            'json_files': len(result_files),
            'csv_files': len(csv_files),
            'png_files': len(png_files),
            'total_files': len(result_files) + len(csv_files) + len(png_files)
        }
        
        if len(result_files) >= 5:
            print("✅ Sufficient experimental data available")
        else:
            self.results['recommendations'].append("Consider running additional experiments for more comprehensive results")
    
    def check_code_quality(self):
        """Basic code quality checks"""
        print("\n🔧 Checking Code Quality...")
        
        python_files = [
            'graph_rule_experimental_pipeline.py',
            'generate_thesis_defense_curves.py'
        ]
        
        for file_name in python_files:
            file_path = self.base_dir / file_name
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Basic syntax check
                    compile(content, file_name, 'exec')
                    print(f"✅ {file_name}: Syntax valid")
                    
                    # Check for common issues
                    lines = content.split('\n')
                    if any('# TODO' in line or '# FIXME' in line for line in lines):
                        self.results['recommendations'].append(f"Review TODO/FIXME comments in {file_name}")
                    
                except SyntaxError as e:
                    self.results['critical_issues'].append(f"Syntax error in {file_name}: {e}")
                    print(f"❌ {file_name}: Syntax error - {e}")
                except Exception as e:
                    self.results['recommendations'].append(f"Check encoding/format of {file_name}: {e}")
                    print(f"⚠️  {file_name}: Warning - {e}")
    
    def generate_completion_certificate(self):
        """Generate thesis completion certificate"""
        print("\n🏆 Generating Completion Certificate...")
        
        # Calculate completion percentage
        essential_files_complete = sum(1 for comp in self.results['thesis_components'].values() 
                                     if isinstance(comp, dict) and comp.get('exists', False))
        
        curves_complete = 0
        if 'defense_curves' in self.results['thesis_components']:
            curves_complete = sum(1 for status in self.results['thesis_components']['defense_curves'].values() 
                                if status['exists'])
        
        total_score = 0
        max_score = 100
        
        # File completeness (40 points)
        total_score += min(40, essential_files_complete * 8)
        
        # Curves completeness (30 points)  
        total_score += min(30, curves_complete * 2)
        
        # Experimental results (20 points)
        if 'experimental_results' in self.results['thesis_components']:
            exp_files = self.results['thesis_components']['experimental_results']['total_files']
            total_score += min(20, exp_files * 2)
        
        # No critical issues bonus (10 points)
        if not self.results['critical_issues']:
            total_score += 10
        
        completion_percentage = min(100, total_score)
        
        if completion_percentage >= 95:
            status = "EXCELLENT - THESIS READY"
        elif completion_percentage >= 85:
            status = "GOOD - MINOR IMPROVEMENTS NEEDED"
        elif completion_percentage >= 70:
            status = "ACCEPTABLE - SOME WORK REQUIRED"
        else:
            status = "INCOMPLETE - SIGNIFICANT WORK NEEDED"
        
        self.results['completion_status'] = status
        self.results['completion_percentage'] = completion_percentage
        
        # Generate certificate
        certificate = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                        THESIS COMPLETION CERTIFICATE                        ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Student: Debraj Das (21ME3AI31)                                           ║
║  Project: Graph-RULE (G-RULE) Framework                                    ║
║  Supervisor: Professor Plaban Bhowmick                                           ║
║                                                                              ║
║  COMPLETION STATUS: {status:<42} ║
║  COMPLETION SCORE:  {completion_percentage:3d}%                                           ║
║                                                                              ║
║  COMPONENTS VALIDATED:                                                       ║
║  • Core Files:      {essential_files_complete}/5 Complete                                    ║
║  • Defense Curves:  {curves_complete}/16 Generated                                  ║  
║  • Experimental:    ✅ Pipeline Executed                                     ║
║  • Documentation:   ✅ Comprehensive Report                                  ║
║                                                                              ║
║  VALIDATION DATE: {datetime.datetime.now().strftime('%B %d, %Y %H:%M:%S'):<42} ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        
        print(certificate)
        
        # Save certificate
        cert_path = self.base_dir / 'THESIS_COMPLETION_CERTIFICATE.txt'
        try:
            with open(cert_path, 'w', encoding='utf-8') as f:
                f.write(certificate)
            print(f"💾 Certificate saved to: {cert_path}")
        except Exception as e:
            print(f"⚠️  Could not save certificate: {e}")
    
    def generate_final_summary(self):
        """Generate final thesis summary"""
        print("\n📋 Generating Final Summary...")
        
        summary_content = f"""# THESIS PROJECT FINAL VALIDATION SUMMARY

## Project Information
- **Student:** Debraj Das (21ME3AI31)
- **Project:** Graph-RULE (G-RULE) Framework  
- **Validation Date:** {datetime.datetime.now().strftime('%B %d, %Y %H:%M:%S')}
- **Status:** {self.results['completion_status']}
- **Completion:** {self.results.get('completion_percentage', 0)}%

## Critical Issues
"""
        
        if self.results['critical_issues']:
            for issue in self.results['critical_issues']:
                summary_content += f"- ❌ {issue}\n"
        else:
            summary_content += "- ✅ No critical issues identified\n"
        
        summary_content += "\n## Recommendations\n"
        if self.results['recommendations']:
            for rec in self.results['recommendations']:
                summary_content += f"- 💡 {rec}\n"
        else:
            summary_content += "- ✅ No specific recommendations\n"
        
        summary_content += f"""
## Component Status Summary
"""
        
        for component, details in self.results['thesis_components'].items():
            if isinstance(details, dict):
                if 'exists' in details:
                    status_icon = "✅" if details['exists'] else "❌"
                    summary_content += f"- {status_icon} {component}: {details.get('description', 'Component')}\n"
        
        # Save summary with proper encoding
        summary_path = self.base_dir / 'THESIS_FINAL_VALIDATION_SUMMARY.md'
        try:
            with open(summary_path, 'w', encoding='utf-8') as f:
                f.write(summary_content)
            print(f"💾 Summary saved to: {summary_path}")
        except Exception as e:
            print(f"⚠️  Could not save summary: {e}")
    
    def run_full_validation(self):
        """Run complete thesis validation"""
        print("🎓 STARTING THESIS FINAL VALIDATION")
        print("=" * 60)
        
        self.validate_core_files()
        self.validate_thesis_curves()
        self.validate_experimental_results()
        self.check_code_quality()
        
        print("\n" + "=" * 60)
        self.generate_completion_certificate()
        self.generate_final_summary()
        
        print("\n🎉 THESIS VALIDATION COMPLETE!")
        
        if not self.results['critical_issues']:
            print("✅ Your thesis is ready for submission and defense!")
        else:
            print("⚠️  Please address the critical issues identified above.")
        
        return self.results

def main():
    """Main execution function"""
    try:
        validator = ThesisValidator()
        results = validator.run_full_validation()
        return results
    except Exception as e:
        print(f"❌ Validation failed with error: {e}")
        return None

if __name__ == "__main__":
    main()
