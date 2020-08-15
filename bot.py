from random import randint, choice

import discord
import os
from discord import member

client = discord.Client()
diret = os.getcwd()


@client.event
async def on_message(message):
    #    os.chdir('diretório pro arquivo dos prefixos')
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
    if message.content.startswith(p + 'hoi'):
        msg = 'H0i!!!! {0.author.mention}'
        await message.channel.send(msg.format(message))
        await message.channel.send('''
https://tenor.com/view/h-oi-undertale-temmie-funny-toby-fox-gif-18014661'''.format(message))
    elif message.content.startswith(p + 'dado') or message.content.startswith(p + 'dice'):
        if ' ' in message.content:
            inp = int(message.content[5:])
        else:
            inp = 6
        num = str(randint(1, inp))
        msg = '{0.author.mention} um dado de ' + str(inp) + ' lados rolou! Caiu em ' + num + '.'
        await message.channel.send(msg.format(message))
    elif message.content.startswith(p + 'info'):
        msg = '''{0.author.mention} Sou um bot bem básico, criado com o objetivo de testar o módulo discord.py.
Feito por AlexTheHedgehog 
(aka Daniel Chaves).'''
        await message.channel.send(msg.format(message))
    elif message.content.startswith(p + 'help') or message.content.startswith(p + 'ajuda'):
        os.chdir('diretório das imagens')
        msg = '```Prefixo: ' + p + '''\n$hoi - Faz o bot falar "H0i!!!" pra você.
dice/dado [número] - rola um dado, com o limite sendo o número que você escolher. (ex: $dado 6)
help/ajuda - Mostra a lista de comandos do bot.
info - Mostra as informações do bot.
say/falar [mensagem] - Deixe o bot falar por você!
shipp [nome 1] [nome 2] - Veja a probabilidade do seu shipp preferido!
terminal [mensagem] (admin) - Mande uma mensagem para o terminal do bot!
coin/moeda - Gire uma moeda para ver se cai cara ou coroa.
prefixo [prefixo] (fase de teste) (admin) - Muda o prefixo do bot no seu servidor!```'''
        await message.author.send(msg.format(message))
        await message.add_reaction('👌')
        await message.author.send(file=discord.File('wonderful.png'))
    elif message.content.startswith(p + 'falar') or message.content.startswith(p + 'say'):
        msg = '{0.author.mention}' + message.content[message.content.find(' '):]
        await message.channel.send(msg.format(message))
    elif message.content.startswith(p + 'shipp'):
        p1 = message.content[message.content.find(' '): message.content.rfind(' ') + 1]
        p2 = message.content[message.content.rfind(' '):]
        prob = randint(0, 100)
        msg = '{0.author.mention} :heart: O shipp entre' + p1 + 'e' + p2 + ' tem ' + str(
            prob) + '% de chance de dar certo. :heart:'
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
    elif message.content.startswith(p + 'terminal') and member.Permissions.administrator:
        print('Mensagem:', message.content[10:])
        print('Servidor:', message.guild)
        print('Canal:', message.channel)
        print('Usuário:', message.author)
    elif message.content.startswith('$moeda') or message.content.startswith('$coin'):
        moeda = 'cara', 'coroa'
        msg = '{0.author.mention} Jogou a moeda, caiu em ' + choice(moeda) + '.'
        await message.channel.send(msg.format(message))
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
    await client.change_presence(activity=discord.Game(name='jooj'))

client.run('seu token')
