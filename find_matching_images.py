import os, hashlib

def get_hash(p):
    with open(p, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

h11 = get_hash('extracted_p315_media_image11.png')
h12 = get_hash('extracted_p318_media_image12.png')
print('Hash image11 (Lớp thực thể thiết kế):', h11)
print('Hash image12 (CSDL ERD):', h12)

bdir = r'C:\Users\admin\Documents\flashcard\GaraMan-De26'
for root, dirs, files in os.walk(bdir):
    for f in files:
        if f.endswith(('.png', '.jpg', '.jpeg')):
            p = os.path.join(root, f)
            try:
                h = get_hash(p)
                if h == h11:
                    print(f'Match image11: {p}')
                if h == h12:
                    print(f'Match image12: {p}')
            except:
                pass
print("Done scan.")
