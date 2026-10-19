import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"

battery = [100,92,60,22,98]

fig,ax = plt.subplots(figsize=(7,4))
ax.plot(battery)

for i,p in enumerate(battery):
    ax.annotate(f"{p:,}",(i,p),textcoords="offset points",xytext=(0,8),ha="center")

ax.set_title("내 스마트폰 배터리")
fig.savefig("my_phone_battery.png")