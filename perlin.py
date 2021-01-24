import numpy as np

def step1(t, a, b):
    return a + t * (b - a)

def step3(t, a, b):
    return (b - a) * (3.0 - t * 2.0) * t * t + a

def sin_step(t, a, b):
    return a + np.sin(np.pi / 2.0 * t) * (b - a)

def logistic_step(t, a, b):
    return a + 1 / (1 + np.exp(-(t - 0.5) * 12.0)) * (b - a)

def gen_perlin(size_x, size_y, scale=1/16, seed=42, step=step3):
    rng = np.random.default_rng(seed)

    alpha = rng.uniform(0, 2 * np.pi, 
                        (int(size_x * scale) + 1, int(size_y * scale) + 1))

    vec_x, vec_y = np.sin(alpha), np.cos(alpha)
    vals = np.zeros((size_x, size_y))

    def get_dot(x, y, x0, y0):
        return (x - x0) * vec_x[x0][y0] + (y - y0) * vec_y[x0][y0]


    for x in range(size_x):
        for y in range(size_y):
            x_re, y_re = x * scale, y * scale
            x_lo, y_lo = int(x_re), int(y_re)
            x_hi, y_hi = x_lo + 1, y_lo + 1

            aa = get_dot(x_re, y_re, x_lo, y_lo)
            ba = get_dot(x_re, y_re, x_hi, y_lo)
            bb = get_dot(x_re, y_re, x_hi, y_hi)
            ab = get_dot(x_re, y_re, x_lo, y_hi)

            vals[x][y] = step(y_re - y_lo,
                              step(x_re - x_lo, aa, ba),
                              step(x_re - x_lo, ab, bb))
    
    return vals

if __name__ == "__main__":
    from PIL import Image
    import colorsys
    from scipy.signal import convolve2d

    SIZE = (1024, 512)
    SCALE = 1/32

    im = Image.new("RGB", SIZE, color=(0, 0, 0))
    pixels = im.load()

    vals = gen_perlin(SIZE[0], SIZE[1], SCALE, step=step3, seed=42)


    vals += np.sqrt(2) / 2
    vals /= np.sqrt(2)

    vals = 1.0 - np.exp(4 * np.log(vals))

    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1],])

    kernel = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]]) * 2

    vals = convolve2d(vals, kernel, "same")

    print(np.min(vals))
    print(np.max(vals))

    for x in range(SIZE[0]):
        for y in range(SIZE[1]):
            v = vals[x][y] % 1.0

            v = int(v * 8) / 8

            #v = int(v * 255)

            r, g, b = colorsys.hsv_to_rgb(v, 1.0, 1.0)
            pixels[x, y] = (int(r * 255), int(g * 255), int(b * 255))

            #v = int(v * 255)
            #pixels[x, y] = (v, v, v)
    




    #img.save("perlin.png")
    im.show()



