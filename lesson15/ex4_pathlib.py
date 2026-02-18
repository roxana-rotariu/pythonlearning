from pathlib import Path

# Creează folderul reports/
reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)

# Creează fișierul report.txt
report_file = reports_dir / "report.txt"
report_file.write_text("Python rules!", encoding="utf-8")

# Citește conținutul
content = report_file.read_text(encoding="utf-8")
print(content)

# Listează toate fișierele din reports/
for file in reports_dir.iterdir():
    print(file.name)
