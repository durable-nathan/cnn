import asyncio
import aiostream
import json
from openai import AsyncOpenAI
from utils.ss import take_screenshot
from .prompts import pro_designer, amateur_designer

client = AsyncOpenAI(api_key="")




async def run(i):
    print("Starting generation for:", i)
    completion = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": pro_designer,            },
            {
                "role": "user",
                "content": "generate me a hero sections, with text on one side and an image on the other"
            },
        ],
        #stream=True,
    )
    output = completion.choices[0].message.content
    output = output.replace("```html", "")
    output = output.replace("```", "")
    print("Got generation for:", i)

    take_screenshot(output, f"output_{i}.png", "screenshots")
    #output_json = json_repair.loads(output)
    return output 

async def main():
    def gen_items():
        for index, obj in enumerate(data):
            yield obj

    async def call_openai(i):
        try:
            output_json = await run(i)
            return output_json

        except Exception as e:
            print(f"Error: {e}")


    stream = aiostream.stream.iterate(range(100))
    openai_stream = aiostream.stream.map(stream, call_openai, task_limit=20)
    new_data = await aiostream.stream.list(openai_stream)

    print(new_data)

    # Write to json file
    with open("output.json", "w") as f:
        json.dump(new_data, f, indent=4)


asyncio.run(main())
