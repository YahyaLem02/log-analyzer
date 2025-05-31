#!/usr/bin/env python3
import sys
import re
import os

def analyze_log_file(file_path):
    if not os.path.exists(file_path):
        print(f"Erreur: Le fichier {file_path} n'existe pas.")
        sys.exit(1)
        
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            
            # Statistiques de base
            total_lines = len(lines)
            total_words = len(re.findall(r'\b\w+\b', content))
            total_chars = len(content)
            
            # Comptage des types de logs
            error_count = len(re.findall(r'ERROR', content))
            warning_count = len(re.findall(r'WARNING', content))
            info_count = len(re.findall(r'INFO', content))
            
            # Création du rapport
            with open('rapport.txt', 'w', encoding='utf-8') as report:
                report.write("RAPPORT D'ANALYSE DE LOGS\n")
                report.write("=======================\n\n")
                report.write(f"Fichier analysé: {file_path}\n\n")
                report.write("STATISTIQUES GÉNÉRALES:\n")
                report.write(f"- Nombre total de lignes: {total_lines}\n")
                report.write(f"- Nombre total de mots: {total_words}\n")
                report.write(f"- Nombre total de caractères: {total_chars}\n\n")
                report.write("ANALYSE DES LOGS:\n")
                report.write(f"- Occurrences de ERROR: {error_count}\n")
                report.write(f"- Occurrences de WARNING: {warning_count}\n")
                report.write(f"- Occurrences de INFO: {info_count}\n")
                
            print(f"Analyse terminée. Rapport bien généré dans 'rapport.txt'")
            
    except Exception as e:
        print(f"Une erreur est survenue lors de l'analyse: {e}")
        
        
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <chemin_vers_fichier_log>")
        sys.exit(1)
        
    analyze_log_file(sys.argv[1])