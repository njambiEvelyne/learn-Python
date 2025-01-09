rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}

for river, country in rivers.items():
    print(f"{river} runs through {country}")
print("")

for river in rivers.keys():
    print(river)
print("")

for country in rivers.values():
    print(country)