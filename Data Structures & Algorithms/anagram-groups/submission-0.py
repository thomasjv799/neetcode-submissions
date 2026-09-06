class Solution:
    def groupAnagrams(self, strs):
        grp = {}

        # Step 1: create sorted keys and store indices
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))

            if key not in grp:
                grp[key] = [i]
            else:
                grp[key].append(i)

        # Step 2: build the final answer
        final = []

        for indices in grp.values():
            group = []

            for i in indices:
                group.append(strs[i])

            final.append(group)

        return final