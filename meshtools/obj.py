import io
import struct


def parse_obj(obj: str, mode: str = "vntc") -> bytes:
    s = struct.Struct("11f")
    buf = io.StringIO(obj)
    out = io.BytesIO()

    vv = [(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)]
    vt = [(0.0, 0.0)]
    vn = [(0.0, 0.0, 0.0)]

    def face(word):
        w = word.split("/")

        match len(w):
            case 3:
                v, t, n = w
            case 2:
                v, t = w
                n = None
            case 1:
                v = w[0]
                t = None
                n = None

        vx, vy, vz, r, g, b = vv[int(v or "0")]
        nx, ny, nz = vn[int(n or "0")]
        tx, ty = vt[int(t or "0")]

        return s.pack(vx, vy, vz, nx, ny, nz, tx, ty, r, g, b)

    while line := buf.readline():
        line = line.split()

        if not line:
            continue

        match line[0]:

            case "v":
                _, vx, vy, vz, *vc = line
                if vc:
                    r, g, b, *_ = vc
                    vv.append((float(vx), float(vy), float(vz), float(r), float(g), float(b)))
                else:
                    vv.append((float(vx), float(vy), float(vz), 0.0, 0.0, 0.0))

            case "vn":
                _, nx, ny, nz, *_ = line
                vn.append((float(nx), float(ny), float(nz)))

            case "vt":
                _, tx, ty, *_ = line
                vt.append((float(tx), float(ty)))

            case "f":
                a = face(line[1])
                b = face(line[2])
                for i in range(3, len(line)):
                    c = face(line[i])
                    out.write(a)
                    out.write(b)
                    out.write(c)
                    b = c

    if mode == "vntc":
        return out.getvalue()

    out.seek(0)
    temp = io.BytesIO()

    vertex, normal, uv, color = "v" in mode, "n" in mode, "t" in mode, "c" in mode

    while v := out.read(44):
        if vertex:
            temp.write(v[0:12])
        if normal:
            temp.write(v[12:24])
        if uv:
            temp.write(v[24:32])
        if color:
            temp.write(v[32:44])

    return temp.getvalue()
