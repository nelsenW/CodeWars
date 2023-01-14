class List:
    def remove_(self, integer_list, values_list):
        ans = []
        for num in integer_list:
            if num not in values_list:
                ans.append(num)
        return ans