from random import randint, choice

import discord
import os
from discord import member

client = discord.Client()
diret = os.getcwd()


@client.event
async def on_message(message):
    #    os.chdir(os.chdir(diret.replace(' \ '.replace(' ', ''), '/')+'/prefixes'))
    #    file = open('prefixos.txt')
    #    if str(message.guild) in file.read():
    #        linhacom = int(file.read().find(str(message.guild)))
    #        linha = str(file.read()[linhacom:])
    #        p = linha[int(linha.rfind('\n'))-1]
    #    else:
    #        p = '$'
    p = '$'
    if message.author == client.user:
        return
    if message.content.startswith(f'{p}hoi'):
        msg = 'H0i!!!! {0.author.mention}'
        await message.channel.send(msg.format(message))
        await message.channel.send('''
https://tenor.com/view/h-oi-undertale-temmie-funny-toby-fox-gif-18014661'''.format(message))
    elif message.content.startswith(f'{p}dado') or message.content.startswith(f'{p}dice'):
        if ' ' in message.content:
            inp = int(message.content[5:])
        else:
            inp = 6
        num = str(randint(1, inp))
        msg = f'um dado de {inp} lados rolou! Caiu em {num}.'
        await message.channel.send(('{0.author.mention} '+msg).format(message))
    elif message.content.startswith(f'{p}info'):
        msg = '''{0.author.mention} Sou um bot bem básico, criado com o objetivo de testar o módulo discord.py.
Feito por AlexTheHedgehog 
(aka Daniel Chaves).'''
        await message.channel.send(msg.format(message))
    elif message.content.startswith(f'{p}help') or message.content.startswith(f'{p}ajuda'):
        os.chdir(diret.replace(' \ '.replace(' ', ''), '/')+'/images')
        msg = f'''```Prefixo: {p}\n$hoi - Faz o bot falar "H0i!!!" pra você.
dice/dado [número] - rola um dado, com o limite sendo o número que você escolher. (ex: $dado 6)
help/ajuda - Mostra a lista de comandos do bot.
info - Mostra as informações do bot.
say/falar [mensagem] - Deixe o bot falar por você!
shipp [nome 1] [nome 2] - Veja a probabilidade do seu shipp preferido!
terminal [mensagem] (admin) - Mande uma mensagem para o terminal do bot!
coin/moeda - Gire uma moeda para ver se cai cara ou coroa.
prefixo [prefixo] (fase de teste) (admin) - Muda o prefixo do bot no seu servidor!
tabuada/mt [número] - escolha um número para ver a tabuada!```'''
        await message.author.send(msg.format(message))
        await message.add_reaction('🥞')
        await message.author.send(file=discord.File('wonderful.png'))
    elif message.content.startswith(f'{p}falar') or message.content.startswith(f'{p}say'):
        msg = message.content[message.content.find(' '):]
        await message.channel.send(('{0.author.mention}'+msg).format(message))
    elif message.content.startswith(f'{p}shipp'):
        p1 = message.content[message.content.find(' '): message.content.rfind(' ') + 1]
        p2 = message.content[message.content.rfind(' '):]
        prob = randint(0, 100)
        msg = f':heart: O shipp entre {p1} e {p2} tem {prob}% de chance de dar certo. :heart:'
        if 0 < prob <= 20:
            msg2 = 'Que pena... Parece que esse shipp não vai funcionar muito bem... 💔'
        elif 20 < prob <= 40:
            msg2 = 'Hmmm... esse shipp tem um pouco de potencial... 💙'
        elif 40 < prob <= 70:
            msg2 = 'Eles parecem bem apegados. será que conseguem fazer esse amor crescer? :heart:'
        elif 70 < prob <= 99:
            msg2 = 'Oooh... se eles dessem mais alguns passos... 💝'
        elif prob == 0:
            msg2 = 'Esse casal não tem a mínima chance... 😭'
        else:
            msg2 = '💞 CASAL PERFEITO!!! 💞'
        await message.channel.send(('{0.author.mention} '+msg).format(message))
        await message.channel.send(msg2.format(message))
    elif message.content.startswith(f'{p}terminal') and member.Permissions.administrator:
        print('Mensagem:', message.content[10:])
        print('Servidor:', message.guild)
        print('Canal:', message.channel)
        print('Usuário:', message.author)
    elif message.content.startswith(f'{p}moeda') or message.content.startswith(f'{p}coin'):
        moeda = 'cara', 'coroa'
        msg = f'jogou a moeda, caiu em {choice(moeda)}.'
        await message.channel.send(('{0.author.mention} '+msg).format(message))
    elif message.content.startswith(f'{p}tabuada') or message.content.startswith(f'{p}mt'):
        if ' ' not in message.content:
            await message.add_reaction('😔')
            await message.channel.send('{0.author.mention} Digite um número, por favor!'.format(message))
            return
        num = int(message.content[message.content.find(' '):])
        t = f'Tabuada do número {num}:\n```'
        for c in range(1, 11):
            t += f'{num} x {c} = {num*c}\n'
        t += '```'
        await message.channel.send(('{0.author.mention} '+t).format(message))
    #    elif message.content.startswith(p+'prefixo') and member.Permissions.administrator:
    #        with open('prefixos.txt', 'a') as file:
    #            file.write(str(message.guild)+' '+str(message.content)[9]+'\n')
    #        await message.channel.send('{0.author.mention} prefixo modificado!'.format(message))
    os.chdir(diret)


#    file.close()

@client.event
async def on_ready():
    print('=' * 40)
    print('Logado como:')
    print(client.user.name)
    print(client.user.id)
    print('Bem vindo ao programa de bots do Discord!\nFeito por AlexTheHedgehog/Daniel Chaves.')
    print('=' * 40)
    await client.change_presence(activity=discord.Game(name='🥞 Fazendo panquecas 🥞'))

client.run('seu token')
