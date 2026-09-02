domains = [
    'WWW.google.com',
    'openai.com',
    'localhost',
    'www.facebook.com',
    'mydoamins',
    'www.pythonwithjoy.com'
]

new_domains = [
    d.lower().replace('www','').replace('.','')
    for d in domains
    if '.' in d
]

print(new_domains)