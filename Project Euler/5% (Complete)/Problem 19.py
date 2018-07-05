jan=31; feb=28; mar=31; apr=30; may=31; jun=30; jul=31; aug=31; sep=30; octo=31; nov=30; dec=31
months = [jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec]

day_count = 1; score = 0
for year in xrange(1, 101):
    if year%4==0:
        months[1] = 29
    else:
        months[1] = 28
    for mt in months:
        day_count += mt
        if (day_count+1)%7==0:
            score += 1

print score        
        
