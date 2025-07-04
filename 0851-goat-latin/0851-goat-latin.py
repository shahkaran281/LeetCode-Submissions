class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = []
        extra = 'a'
        words = sentence.split()
        
        for i, word in enumerate(words, 1):
            if word[0].lower() in vowels:
                goat_word = word + 'ma'
            else:
                goat_word = word[1:] + word[0] + 'ma'
            goat_word += 'a' * i
            ans.append(goat_word)
        
        return ' '.join(ans)
