import discord
client = discord.Client()


@client.event
async def on_ready():
    print('=' * 40)
    print('Logado como:')
    print(client.user.name)
    print(client.user.id)
    print('Bem vindo ao programa de mandar mensagem!\nFeito por AlexTheHedgehog/Daniel Chaves.')
    print('=' * 40)
    while True:
        c = ''
        print('COLOQUE AS INFORMAÇÕES')
        msg = str(input('Mensagem: '))
        canal = int(input('Canal: '))
        channel = client.get_channel(canal)
        await channel.send(msg)

client.run('seu token')
