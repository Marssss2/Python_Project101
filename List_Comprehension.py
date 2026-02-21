domains = ['example.com', 'www.test.com', 'sample', 'Demo.com']

clean_domains = {
    d
    for d in domains
    if '.' in d
    
}

print(clean_domains) #it will print the set of cleaned domains which is {'example.com', 'test.com', 'demo.com'}