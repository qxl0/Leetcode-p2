class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        MOD = 10**9 + 7
        P = 31
        n = len(s)
        cnt_ch = [[0] * 26 for _ in range(n + 2)]

        def FastPower(a, b):  # a^b
            a %= MOD
            b %= MOD
            ans = 1
            while b:
                if b & 1:
                    ans = (ans * a) % MOD
                b //= 2
                a = (a * a) % MOD
            return ans

        powerp = [0] * (n + 2)
        powerp[0] = 1
        for j in range(1, n + 2):
            powerp[j] = (powerp[j - 1] * P) % MOD
        invp = [0] * (n + 1)
        invp[n] = FastPower(P, MOD - n - 1)
        for j in range(n - 1, -1, -1):
            invp[j] = (invp[j + 1] * P) % MOD

        def swap(a, b):
            tmp = a
            a = b
            b = tmp

        def ForwardHash(l, r):
            return (fwd_pref[r] - fwd_pref[l - 1] + MOD) * invp[l - 1] % MOD

        def ReverseHash(l, r):
            return (rev_pref[l] - rev_pref[r + 1] + MOD) * invp[n - r] % MOD

        def CharCount(l, r):
            res = []
            for ch in range(26):
                if l <= r:
                    res.append(cnt_ch[r][ch] - cnt_ch[l - 1][ch])
                else:
                    res.append(0)
            return res

        def EqualChars(l, r):
            l1, r1 = l, r
            l2, r2 = n - r + 1, n - l + 1
            return CharCount(l1, r1) == CharCount(l2, r2)

        # l-r
        def CharDiff(l, r):
            res = []
            lft = CharCount(l[0], l[1])
            rgt = CharCount(r[0], r[1])
            for ch in range(26):
                res.append(lft[ch] - rgt[ch])
            return res

        fwd_pref = [0] * (n + 2)
        rev_pref = [0] * (n + 2)
        for j in range(1, n + 1):
            fwd_pref[j] = (
                fwd_pref[j - 1] + (powerp[j] * (ord(s[j - 1]) - ord("a") + 1)) % MOD
            ) % MOD
        for j in range(n, -1, -1):
            rev_pref[j] = (
                rev_pref[j + 1]
                + (powerp[n + 1 - j] * (ord(s[j - 1]) - ord("a") + 1)) % MOD
            ) % MOD
        for j in range(1, n + 1):
            cnt_ch[j] = cnt_ch[j - 1].copy()
            cnt_ch[j][ord(s[j - 1]) - ord("a")] += 1
        res = []
        for a, b, c, d in queries:
            a, b, c, d = a + 1, b + 1, c + 1, d + 1  # make it 1-based
            l1, r1 = a, b
            l2, r2 = n - d + 1, n - c + 1
            is_intersecting = (l1 <= l2 and l2 <= r1) or (l2 <= l1 and l1 <= r2)
            if is_intersecting:
                l = min(l1, l2)
                r = max(r1, r2)
                if l != 1 and ForwardHash(1, l - 1) != ReverseHash(n - l + 2, n):
                    res.append(False)
                    continue
                if r != n // 2 and ForwardHash(r + 1, n // 2) != ReverseHash(
                    n // 2 + 1, n - r
                ):
                    res.append(False)
                    continue
                is_full_intersection = (l1 <= l2 and r2 <= r1) or (
                    l2 <= l1 and r1 <= r2
                )
                if is_full_intersection:
                    res.append(EqualChars(min(l1, l2), max(r1, r2)))
                    continue
                ans = True  # partial intersecting
                if l1 <= l2:
                    full_lft = (l1, r1)
                    must_rgt = (n - l2 + 2, n - l1 + 1)
                    must_lft = (r1 + 1, r2)
                    full_rgt = (n - r2 + 1, n - l2 + 1)
                    extra_lft = CharDiff(full_lft, must_rgt)
                    extra_rgt = CharDiff(full_rgt, must_lft)
                    for j in range(26):
                        if (
                            extra_lft[j] < 0
                            or extra_rgt[j] < 0
                            or extra_lft[j] != extra_rgt[j]
                        ):
                            ans = False
                else:
                    full_lft = (l1, r1)
                    must_rgt = (n - r1 + 1, n - r2)
                    must_lft = (l2, l1 - 1)
                    full_rgt = (n - r2 + 1, n - l2 + 1)
                    extra_lft = CharDiff(full_lft, must_rgt)
                    extra_rgt = CharDiff(full_rgt, must_lft)
                    for j in range(26):
                        if (
                            extra_lft[j] < 0
                            or extra_rgt[j] < 0
                            or extra_lft[j] != extra_rgt[j]
                        ):
                            ans = False
                res.append(ans)
            else:  # not overlapping
                if l1 > l2:
                    l1,l2 = l2,l1
                    r1,r2 = r2,r1
                if l1 != 1 and ForwardHash(1, l1 - 1) != ReverseHash(n - l1 + 2, n):
                    res.append(False)
                    continue
                if r2 != n // 2 and ForwardHash(r2 + 1, n // 2) != ReverseHash(
                    n // 2 + 1, n - r2
                ):
                    res.append(False)
                    continue
                if ForwardHash(r1 + 1, l2 - 1) != ReverseHash(n - l2 + 2, n - r1):
                    res.append(False)
                    continue
                ans = EqualChars(l1, r1) and EqualChars(l2, r2)
                res.append(ans)
        return res
                
                    
        