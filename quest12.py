f = open('notes12-1.txt').read().split('\n')

def getTargets(lines):
    tgts = []
    srcs = []
    mxR = len(lines) - 2







def get_targets(lines):
    tgts = []
    srcs = []
    max_y = len(lines) - 2
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c in 'T':
                tgts += [(x, max_y - y)]
            if c in 'ABC':
                srcs += [(x, max_y - y)]
    return tgts, srcs

def get_power(src, tgt):
    dx = tgt[0] - src[0]
    dy = tgt[1] - src[1]

    # Only on ascending phase if dx=dy
    if dx == dy:
        return int(dx) * (1 + src[1])

    # On horizontal phase, have to have gone up by dy
    # and have less remaining x than the dy
    if dx - dy <= dy:
        return int(dy) * (1 + src[1])

    # For descending phase, again a dx=dy check, but after some travel
    # After p, we're at x = xs + 2*p and y = ys + p
    # so only on descending if (xt - xs - 2*p) = (ys + p - yt)
    # and if that's the case then solve for p = (dx + dy) / 3
    if (dx + dy) % 3 == 0:
        return (dx + dy) // 3 * (1 + src[1])

    return float('inf')

lines = open('notes12-1.txt').read().split('\n')
tgts, srcs = get_targets(lines)
t = sum(min(get_power(s, t) for s in srcs) for t in tgts)
print(t)