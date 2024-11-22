f1, f2, f3 = 4098123, 912, 948543

def createPyramid(n):
    cur = 1
    t = 1
    while t < n:
        new = cur + 2
        t += new
        cur = new   
    return (t-n) * cur

def betterPyramid(n):
    layer = 1
    t = 1
    thick = 1
    while t < 20240000:
        thick = (thick*n) % 1111
        new = (layer+2) * thick
        t += new
        layer += 2
        
    return (t-20240000) * layer

def bestPyramid(n):
    

print(createPyramid(f1))
print(betterPyramid(f2))
