# Dict
# time: O(2n)
# space: O(n)

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hashmap = {}
        bulls = cows = 0

        for index, num in enumerate(secret):
            # 數字、位置皆正確
            if guess[index] == num:
                bulls += 1
            else:
                # 記錄各個數字的數量
                hashmap[num] = hashmap.get(num, 0) + 1

                # if num in hashmap:
                #   map[num] += 1
                # else:
                #   map[num] = 1
            
        for index, num in enumerate(secret):
            # 位置不正確 & 數字正確
            if (guess[index] != num) and (hashmap.get(guess[index],0) != 0):
                cows += 1
                hashmap[guess[index]] -= 1

        return f"{bulls}A{cows}B"
    

# Counter
# time: O(N)
# space: O(N)

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        count_secret = Counter(secret)  # Counter({'1': 2, '2': 1, '3': 1})
        count_guess = Counter(guess)    # Counter({'1': 3, '0': 1})

        # 交集
        secret_and_guess = count_secret & count_guess  # Counter({'1': 2})

        # 所有數字相同的個數(位置可能不同)
        total = sum(secret_and_guess.values())  # dict_values([1, 1, 1, 1]) => 4
        
        for s_num, g_num in zip(secret, guess):
            # 位置、數字相同
            if s_num == g_num:
                bulls += 1

        # 扣掉重複的
        cows = total - bulls        

        return f"{bulls}A{cows}B"