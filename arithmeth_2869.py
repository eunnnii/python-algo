
day_up, night_down, distance = map(int, intpu().split())
# day_up : 낮동안에 올라가는 길이
# night_down : 밤동안에 내려오는 길이
# distance : 총 도달해야하는 길이

# 총 몇일이 걸릴까?
# 밤까지 간다 --> 그날안에 못올라간다.
# 올라갈 수 있으면 낮동안에 올라갈 수 있음
# (day_up - night_down)*n + day_up = distance

## ???
