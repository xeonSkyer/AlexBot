import discord
from random import randint
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hoi'):
        msg = 'H0i!!!! {0.author.mention}'
        await message.channel.send(msg.format(message))
    elif message.content.startswith('$dado') or message.content.startswith('$dice'):
        if ' ' in message.content:
            inp = int(message.content[5:])
        else:
            inp = 6
        num = str(randint(1, inp))
        msg = '{0.author.mention} um dado de '+str(inp)+' lados rolou! Caiu em '+num+'.'
        await message.channel.send(msg.format(message))
    elif message.content.startswith('$info'):
        msg = '''{0.author.mention} Sou um bot bem básico, criado com o objetivo de testar o módulo discord.py.
Feito por AlexTheHedgehog 
(aka Daniel Chaves).'''
        await message.channel.send(msg.format(message))
    elif message.content.startswith('$help') or message.content.startswith('$ajuda'):
        msg = '''```Prefixo: $
hoi - Faz o bot falar "H0i!!!" pra você.
dice/dado [número] - rola um dado, com o limite sendo o número que você escolher. (ex: $dado 6)
help/ajuda - Mostra a lista de comandos do bot.
info - Mostra as informações do bot.
say/falar [mensagem] - Deixe o bot falar por você!
shipp [nome 1] [nome 2] - Veja a probabilidade do seu shipp preferido!
terminal [mensagem] - Mande uma mensagem para o terminal do bot!```'''
        await message.channel.send(msg.format(message))
    elif message.content.startswith('$falar') or message.content.startswith('$say'):
        msg = '{0.author.mention}'+message.content[message.content.find(' '):]
        await message.channel.send(msg.format(message))
    elif message.content.startswith('$shipp'):
        p1 = message.content[message.content.find(' '): message.content.rfind(' ')+1]
        p2 = message.content[message.content.rfind(' '):]
        prob = randint(0, 100)
        msg = '{0.author.mention} :heart: O shipp entre'+p1+'e'+p2+' tem '+str(prob)+'% de chance de dar certo. :heart:'
        if 0 < prob <= 20:
            msg2 = 'Que pena... Parece que esse shipp não vai funcionar muito bem... :broken_heart:'
        elif 20 < prob <= 40:
            msg2 = 'Hmmm... esse shipp tem um pouco de potencial... :blue_heart:'
        elif 40 < prob <= 70:
            msg2 = 'Eles parecem bem apegados. será que conseguem fazer esse amor crescer? :heart:'
        elif 70 < prob <= 99:
            msg2 = 'Oooh... se eles dessem mais alguns passos... :gift_heart:'
        elif prob == 0:
            msg2 = 'Esse casal não tem a mínima chance... :sob:'
        else:
            msg2 = ':revolving_hearts: CASAL PERFEITO!!! :revolving_hearts:'
        await message.channel.send(msg.format(message))
        await message.channel.send(msg2.format(message))
    elif message.content.startswith('$terminal'):
        print('Mensagem:', message.content[10:])
        print('Servidor:', message.guild)
        print('Canal:', message.channel)
        print('Usuário:', message.author)


@client.event
async def on_ready():
    print('='*40)
    print('Logado como:')
    print(client.user.name)
    print(client.user.id)
    print('Bem vindo ao programa de bots do Discord!\nFeito por AlexTheHedgehog/Daniel Chaves.')
    print('='*40)


client.run('seu token')
