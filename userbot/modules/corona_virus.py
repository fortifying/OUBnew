from .john_hopkins import Covid as JohnHopkinsCovid
from userbot import CMD_HELP
from userbot.events import register

@register(pattern="^.covid(?: |$)(.*)")
async def corona(event):
    covid = Covid()
    data = covid.get_data()
    input_str	 = event.pattern_match.group(1)
    country = input_str.capitalize()
    country_data = get_country_data(country, data)
    output_text = "" 
    for name, value in country_data.items():
        output_text += "`{}`: `{}`\n".format(str(name), str(value))
    await event.edit("**CoronaVirus Info in {}**:\n\n{}".format(country.capitalize(), output_text))

def get_country_data(country, world):
    for country_data in world:
        if country_data["country"] == country:
            return country_data
    return {"Status": "No information yet about this country!"}

CMD_HELP.update({
        "covid": ".covid <country>\
        \nUsage: Get info about COVID-19 in countries.\n"
    })
