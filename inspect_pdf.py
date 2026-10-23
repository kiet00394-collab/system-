import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

reader = pypdf.PdfReader(r'C:\Users\LENOVO\Downloads\Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf')
print(f"Total Pages: {len(reader.pages)}")
for i, p in enumerate(reader.pages):
    txt = p.extract_text() or ''
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    first_line = lines[0] if lines else 'EMPTY'
    print(f"Page {i+1} (chars: {len(txt)}): {first_line[:80]}")
