from matplotlib import font_manager

# Get a list of all system font paths
font_paths = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')

# # Print font paths and names
for font_path in font_paths:  # Limiting to the first 10 for readability
    print(font_path)

a =  {
        'cat01-item01': 'Idly',
        'cat01-item02': 'banana',
        'cat01-item03': 'cherry',
        'cat01-item04': 'date',
        'cat01-item05': 'elderberry',
        'cat01-item06': 'fig',
        'cat01-item07': 'grape',
        'cat01-item08': 'honeydew',
        'cat01-item09': 'kiwi',
        'cat01-item10': 'lemon',
        'c1-p1': '$6.99',
        'c1-p2': '$6.00',
        'c1-p3': '$7.00',
        'c1-p4': '$8.00',
        'c1-p5': '$5.00',
        'c1-p7': '$6.00',
        'c1-p6': '$6.00',
        'c1-p8': '$7.00',
        'c1-p9': '$8.00',
        'cat02-item01': 'mang11111111111o',
        'cat02-item02': 'nectarine',
        'cat02-item03': 'orange',
        'cat02-item04': 'papaya',
        'cat02-item05': 'quince',
        'cat03-item01': 'raspberry',
        'cat03-item02': 'strawberry',
        'cat03-item03': 'tangerine',
        'cat03-item04': 'ugli fruit',
        'cat03-item05': 'watermelon',
        'c3-p1': '$10.01',
        'c3-p2': '$10.02',
        'c3-p3': '$10.03',
        'c3-p4': '$10.04',
        'c3-p5': '$10.07',
        'c2-p1': '$5.00',
        'c2-p2': '$6.00',
        'c2-p3': '$7.00',
        'c2-p4': '$8.00',
        'c2-p5': '$5.00',
}
res = {}
for k in a:
    print(k, a[k])
    res[k] = [a[k], True]

print(res)