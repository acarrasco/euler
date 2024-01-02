import itertools

def make_hist(sides, dices):
        counts = [0 for _ in range((sides+1)*dices+1)]
        for roll in itertools.product(*[range(1, sides+1)]*dices):
                counts[sum(roll)] += 1
        return [float(i)/(sides**dices) for i in counts]

def make_cdf(hist):
        return [sum(hist[:i+1]) for i in range(len(hist))]

hist_peter = make_hist(4, 9)
cdf_colin = make_cdf(make_hist(6, 6))
p = sum(hist_peter[i]*cdf_colin[i-1] for i in range(1,37))

print(format(p, ".7f"))

