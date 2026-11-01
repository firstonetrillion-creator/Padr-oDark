from PIL import Image
import json, subprocess, os, glob

tempos = json.load(open('tempos_cenas.json'))
for f in glob.glob('qa-frames/*.png'):
    os.remove(f)
for t in tempos:
    ts = round(t['inicio'] + t['duration'] * 0.62, 2)
    out = 'qa-frames/f%02d-%.2fs.png' % (t['cena'], ts)
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
                    '-ss', str(ts), '-i', 'final.mp4', '-frames:v', '1', out], check=True)

fs = sorted(glob.glob('qa-frames/f*.png'))

def sheet(files, out):
    W, H = 360, 640
    sh = Image.new('RGB', (W * 3, H * ((len(files) + 2) // 3)), (10, 10, 11))
    for i, f in enumerate(files):
        sh.paste(Image.open(f).convert('RGB').resize((W, H), Image.LANCZOS),
                 ((i % 3) * W, (i // 3) * H))
    sh.save(out)
    print(out, sh.size)

sheet(fs[:9], 'contact-1.png')
sheet(fs[9:], 'contact-2.png')

for f in fs:
    im = Image.open(f).convert('L')
    w, h = im.size
    px = im.load()
    rows = []
    for y in range(h):
        xs = [x for x in range(0, w, 2) if px[x, y] > 120]
        if len(xs) >= 4:
            rows.append((y, min(xs), max(xs)))
    x0 = min(r[1] for r in rows)
    x1 = max(r[2] for r in rows)
    linhas = 1
    for a, b in zip(rows, rows[1:]):
        if b[0] - a[0] > 6:
            linhas += 1
    flag = 'ESTOURA' if (x1 - x0) > 840 or x1 > 960 or x0 < 116 else ('apertado' if (x1 - x0) > 810 else 'ok')
    print('%-26s largura=%4d x0=%4d x1=%4d linhas=%2d %s' % (os.path.basename(f), x1 - x0, x0, x1, linhas, flag))
