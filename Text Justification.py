# Text Justification
# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified and no extra space is inserted between words.


from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Explain below code
        res = []
        cur = []
        cur_len = 0
        for word in words:
            # if the current line is too long, we need to start a new line
            if cur_len + len(word) + len(cur) > maxWidth:
                # if the current line is empty, we need to add the word to it
                for i in range(maxWidth - cur_len):
                    # if the current line is not empty, we need to add a space to it
                    cur[i % (len(cur) - 1 or 1)] += " "

                # add the current line to the result
                res.append("".join(cur))

                # start a new line
                cur = [word]
                cur_len = len(word)
            else:
                # if the current line is not too long, we need to add the word to it
                cur_len += len(word)
                cur.append(word)
        # if the last line is not empty, we need to add spaces to it
        return res + [" ".join(cur).ljust(maxWidth)]


if __name__ == "__main__":
    s = Solution()
    print(
        s.fullJustify(
            ["This", "is", "an", "example", "of", "text", "justification."], 16
        )
    )
    print(s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
