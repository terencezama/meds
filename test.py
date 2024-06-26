meds = [
    {
    'med_name': "cool",
    'name': 'cool_n',
},
{
    'med_name': "nice",
    'name': 'nice_n',
}
]

fields = list(meds[0].keys())
values = [tuple(med.values()) for med in meds]
print(fields)
print(values)


v2 = []
meds2 = ["med1", "med2", "med3"]
for med in meds2:
    v2.append((med,med))
print(v2)