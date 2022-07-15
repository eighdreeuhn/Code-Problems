def heavy_metal_umlauts(boring_text):
    boring_text = boring_text.replace('A', u'\u00c4')
    boring_text = boring_text.replace('E', u'\u00cb')
    boring_text = boring_text.replace('I', u'\u00cf')
    boring_text = boring_text.replace('O', u'\u00d6')
    boring_text = boring_text.replace('U', u'\u00dc')
    boring_text = boring_text.replace('Y', u'\u0178')
    boring_text = boring_text.replace('a', u'\u00e4')
    boring_text = boring_text.replace('e', u'\u00eb')
    boring_text = boring_text.replace('i', u'\u00ef')
    boring_text = boring_text.replace('o', u'\u00f6')
    boring_text = boring_text.replace('u', u'\u00fc')
    boring_text = boring_text.replace('y', u'\u00ff')
    return boring_text


print(heavy_metal_umlauts("Announcing the Macbook Air Guitar"))


# A = Ä = \u00c4     E = Ë = \u00cb     I = Ï = \u00cf
# O = Ö = \u00d6     U = Ü = \u00dc     Y = Ÿ = \u0178
# a = ä = \u00e4     e = ë = \u00eb     i = ï = \u00ef
# o = ö = \u00f6     u = ü = \u00fc     y = ÿ = \u00ff
