from pathlib import Path
p=next(Path('weave').rglob('build_survey_dashboard.py'))
s=p.read_text(encoding='utf-8-sig')
a=s.index('q8groups = {')
b=s.index('\nq11 = values(11)',a)
new='''q8groups = {
    '\ucc3e\uc544\ubd04\u00b7\uacb0\uad6d \ucc3e\uc74c': q8.str.contains('\\ucc3e\uc558\ub2e4', regex=False) & ~q8.str.contains('\\ubabb', regex=False),
    '\ucc3e\uc544\ubd24\uc9c0\ub9cc \ubabb \ucc3e\uc74c': q8.str.contains('\\ubabb \\ucc3e', regex=False),
    '\ub2e4\ub978 \uae30\ub85d\uc744 \ucc3e\uc544\ubcf8 \uc801 \uc5c6\uc74c': q8.str.startswith('\\uc5c6')
}'''
s=s[:a]+new+s[b:]
a=s.index('q13short = {')
b=s.index('\nq8rows = [',a)
new='''q13rows = answer_rows(13)
for row, label in zip(q13rows, ['온디바이스에서만 처리되면 사용', '서버 전송도 허용하면 사용', '사용하지 않음']):
    row['label'] = label'''
s=s[:a]+new+s[b:]
p.write_text(s,encoding='utf-8')
