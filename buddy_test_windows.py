import os

if os.name == 'nt':
    print("Windows OS found")
    
    folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    print(folder)