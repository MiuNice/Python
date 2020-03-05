def distributeCandies(candies, num_people):
    re_list = [0] * num_people
    p = 0
    get_candies = 0
    while candies:
        get_candies += 1
        if candies > get_candies:
            re_list[p] += get_candies
            candies -= get_candies
        else:
            re_list[p] += candies
            return re_list
        p = (p + 1) % num_people


a = distributeCandies(60, 4)
print(a)
