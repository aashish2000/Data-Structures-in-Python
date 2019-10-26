class TrieNode:
	def __init__(self):
		self.children=[None]*26
		self.endOfWord=False

class Trie:
	def __init__(self):
		self.root=TrieNode()

def insert(trie,word):
	root=trie.root
	word=word.lower()
	for i in range(len(word)):
		if(root.children[ord(word[i])-ord("a")] is None):
			root.children[ord(word[i])-ord("a")]=TrieNode()
		root=root.children[ord(word[i])-ord("a")]
		if(i==len(word)-1):
			root.endOfWord=True

def search(trie,word):
	root=trie.root
	word=word.lower()
	for i in range(len(word)):
		if(root.children[ord(word[i])-ord("a")] is None):
			return(word+": Not Found")
		root=root.children[ord(word[i])-ord("a")]
		if(i==len(word)-1 and root.endOfWord!=True):
			return(word+": Not Found")
		elif(i==len(word)-1):
			return(word+": Found")


trie=Trie()

array=["there","they","the","carnatic","cat"]

for i in array:
	insert(trie,i)

print(search(trie,"carnatic"))
print(search(trie,"they"))
print(search(trie,"th"))






