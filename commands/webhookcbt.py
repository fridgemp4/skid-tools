import asyncio
import aiohttp

async def send_message(session, webhook_url, message_content, username, successful_messages, num_messages):
    payload = {'content': f'{message_content}', 'tts': False, 'username': username}

    async with session.post(webhook_url, json=payload) as response:
        if response.status == 204:
            successful_messages += 1
            print(f"Message sent successfully. ({successful_messages}/{num_messages})")
            return True
        elif response.status == 429:
            print("Rate limited, retrying after 2 seconds...")
            await asyncio.sleep(2)
            return False
        else:
            print("Failed to send message. Retrying...")
            return False

async def webhook_spammer():
    webhook_url = input("Webhook URL: ")
    message_content = ("@everyone @here https://discord.gg/TaAFW8UDa2 Cock and ball torture from Wikipedia, the free encyclopedia at en.wikipedia.org. Cock and ball torture, CBT, is a sexual activity involving torture of the male genitals. This may involve directly painful activities such as wax play, genital spanking, squeezing, ball busting, genital flogging, urethera play, tickle torture, erotic electro stimulation, or even kicking. The recipient of such activities may receive direct physical pleasure via masochism through knowledge that the play is pleasing to a sadistic dominant. Image: electro stimulation applied on a penis. Contents Section 1: In pornography Section 2: Ball stretcher Section 3: Parachute Section 4: Humbler Section 5: Testicle Cuff Section 1: In pornography. In addition to it's occational role in BDSM pornography, temakeria, literally ball kicking, is a separate genre in Japan. One notable actress in temakeria is Erika Negai, who typically uses her martial art skills to knee or kick men in the testicles. Section 2: Ball stretcher. A ball stretcher is a sex toy that is fastened around a man in order to elongate the scrotum, and provide a feeling of weight, pulling the testicles away from the body. While leather stretchers are most common, other models are made of steel rings that are fastened with screws causing additional, mildly uncomfortable weight to the wearer. The length of the stretchers may very from 1-4 inches, and the steel models can weigh up to 5 pounds. Section 3: Parachute. A parachute is a small collar usually made from leather which fastens around the scrotum, and from which weights can be hung. Conical is shape, with 3 or 4 short chains having beneath to which weight can be applied. Used as part of cock and ball torture within a BDSM relationship, the parachute provides a constant drag and squeezing affect on man's testicles. Moderate weights of 3 to 5 kilograms can be suspended especially during bondage.")
    username = ("F X")
    num_messages = int(input("Number of messages to send: "))

    successful_messages = 0

    async with aiohttp.ClientSession() as session:
        while successful_messages < num_messages:
            try:
                success = await send_message(session, webhook_url, message_content, username, successful_messages, num_messages)
                if success:
                    successful_messages += 1
            except:
                print("An error occurred while sending the message. Retrying...")

    print("Total messages sent:", successful_messages)

asyncio.run(webhook_spammer())
