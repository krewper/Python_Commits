from pytrie import StringTrie

def prefixSearch(arr, prefix):
    trie = StringTrie()
    
    for key in arr:
        trie[key] = key
    return trie.values(prefix)

if __name__ =="__main__":
    arr = ['geeksforgeeks', 'forgeeks', 'geeks', 'eeksfor']
    prefix = 'geek'
    output = prefixSearch(arr, prefix)
    
    if __name__ == "__main__":
        arr = ['geeksforgeeks', 'forgeeks', 'geeks', 'eeksfor']
        prefix = 'geek'
        output = prefixSearch(arr, prefix)
        if len(output) > 0:
            print (output)
        else:
            print ('Pattern not found')
