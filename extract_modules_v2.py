import json
import os

files = [
    'mathematics_curriculum.json',
    'aiml_curriculum.json',
    'programming_c_curriculum.json'
]

all_modules = {}

for fname in files:
    path = os.path.join(r'c:\Users\Rohan\Desktop\dtl', fname)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            subject = data.get('subject', 'unknown')
            all_modules[subject] = []
            if 'levels' in data:
                for level in data['levels']:
                    for mod in data['levels'][level]['modules']:
                        all_modules[subject].append({
                            'id': mod.get('module_id'),
                            'name': mod.get('module_name'),
                            'level': mod.get('level')
                        })

print(json.dumps(all_modules, indent=2))
