#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import chatbot
import sys
import re
import codecs
import time
from datetime import datetime
import wikibot
from command import command
import threading
import json
import random
import math

try:
    config_file = json.loads(open('config.json').read())
except:
    print "Error while reading the config file. Exiting..."
    sys.exit(1)

wiki_name = 'http://' + config_file['wiki'] + '.wikia.com/'
wikibot.site(wiki_name)

initial_time = time.time()
userdict = {}
try:
    tell = json.loads(codecs.open('tell.json', 'r').read())
except:
    tell = {}

ignored = []


class EthBot(chatbot.ChatBot):
    def __init__(self):
        chatbot.ChatBot.__init__(self, config_file['user'], config_file['password'], wiki_name)
        self.command = command(self, config_file['user'], config_file['password'])
        self.last_updated = time.time()
        self.logger_on = True
        self.hello_status = True
        self.youtubeinfo = True
        self.twitterinfo = True
        self.seen = True
        self.tell = True
        self.new_day = False
        self.updated = False
        self.log_thread()


    def on_join(self, c, e):
        if (self.logger_on):
            self.format_message(user=e.user.encode('ascii', 'ignore'), event='join')
        print '%s ~ %s ha entrado al chat. ~' % (time.strftime('%H:%M', time.gmtime()), e.user)
        if e.user not in userdict or e.user in userdict:
            userdict[e.user] = time.time()

#Saludos a usuarios cuando entran al chat
        if e.user == "Connie Maheswaran":
            c.send("¡Nigga Queen! (elmo2)")
            
        if e.user == "Fire Garnet":
            c.send("Granatencia \ :v /")

        if e.user == "Water Pearl":
            c.send("WaterO Perola :u /")

        if e.user == "Ethereal Rose":
            c.send("Hola Eth c:")

        if e.user == "Wheatley and GLaDOS":
            c.send("La Whea (.-.) /")

        if e.user == "MarcelinePeridorito002":
            c.send("MP2 .v. /")

        if e.user == "Una papa aburrida":
            c.send("Papita Kwaii \ (bebe) /")

        if e.user == "The Fireflies":
            c.send("ARCHIVOS INFERNALES :u /")

        if e.user == "Señor Panda":
            c.send("El Panda cósmico y mágico ha vuelto.")

        if e.user == "David a esmeralda sayan":
            c.send("¡¡HO!! ¡El super sayan legendario! (david:V) /")

        if e.user == "Sora Shiro Azuma":
            c.send("Shizuka Shiro (.-.) /")

        if e.user == "Meowstic :3":
            c.send("Hola Gato Azul Psíquico, Digo Meow  (doge) /")

        if e.user == "StevonnieLaLoca":
            c.send("JuanaLaCubana \ :v /")

        if e.user == "Perlita Everdeen":
            c.send("Perli ust  (perlita:u)")

        if e.user == "Connie's Autumn":
            c.send("Melissa. \ (connie:v) /")
            
        if e.user == "BengiDog":
            c.send("Hola Dorito, digo Illuminati, es decir Bengi :v")
            
        if e.user == "Sapphire U":
            c.send("Wii U de la esquina (rikka:v) /")

        if e.user == "Granate La Gema de Cristal":
            c.send("Laura d4")

        if e.user == "Mamoncho":
            c.send("Momancho. d2 /")

        if e.user == "Enzuka T Θ":
            c.send("Azukarado (frasko)")

        if e.user == "Juan Universe :D":
            c.send("Juanito Iuniverse (:v:) /")
            
        if e.user == "Peridot Universe c:":
            c.send("PeriU :D /")
            
        if e.user == "Rubi Universe":
            c.send("Rubi (holi)")
            
        if e.user == "Shippingx":
            c.send("Ship :v /")
            
        if e.user == "Elhatter":
            c.send("¡Miren es el odiador! Emm... Quiero decir... Señor sombrero :3")
            
        if e.user == "Un Usuario Raro":
            c.send("hOnK :0)")
            
        if e.user == "RedDiamond1373":
            c.send("El Millonario y poderoso Red! (elmo2)")
            
        if e.user == "Aguamarina Kawaii :3":
            c.send("¡Hola kabrita kawaii! Digo. ¡Hola Agua (holi:3) !")
            
        if e.user == "Fayemelin Kasane Rosanha":
            c.send("Aloh reina desquiciada Yukimenoko (elmo2)")
            
        if e.user == "Snow Amy :3":
            c.send("Reina de la nieve (elmo2)")
            
        if e.user == "Wendigo Salvaje":
            c.send("Guendigo SalvaG :V /")
            
        if e.user == "Perfect Cherry Blossom":
            c.send("Nyanpasu, Perfect")
            
        if e.user == "Dangerdark24":
            c.send("Danger (riko) ola k ase :v")
            
        if e.user == "Carol The Swagger":
            c.send("Crayola La Swaggera. \ :v /")
        
        if e.user == "Mangle la mas kawaii :3":
            c.send("Mangle animatronica (bebe)")
            
        if e.user == "Thunder Khight":
            c.send("Caballero Neón ¡Bienvenido! (Hunter:v) /")
            
        if e.user == "ELMOR1230":
            c.send("Oh, llego Elmoroso, dame 10 empanadas \ (woody1) /")
            
        if e.user == "Marshallow":
            c.send("Arrodíllense ante Marshallow.")
            
        if e.user == "Daemon Cat":
            c.send("¡PCC Daemon! :v")
            
        if e.user == "Ludius Quassas":
            c.send("Bonjour, monsieur Quassas.")

        if e.user == "GTU v:":
            c.send("Doña GTU :v / Digo Don :v /")
            
        if e.user == "Luxine":
            c.send("Hola, Lux. (holi)")
            
        if e.user == "Yukimenoko marionette":
            c.send("Corran todos, la marioneta siniestra a aparecido de las sombras (nuu) d4 :o")
            
        if e.user == "ElTitoDan72":
            c.send("(doge) Such Tito. So Dan. Much Wow. (doge)")
            
#Saludos a usuarios cuando salen del chat (herpderp)            
    def on_leave(self, c, e):

        if e.user == "Señor Panda":
            c.send("Las estrellas caen...")
            
        if e.user == "David a esmeralda sayan":
            c.send("Adios David (hola)")
            
        if e.user == "Una papa aburrida":
            c.send("Se fue Papa, voy a comprar Pringles (sf)")
        
        if e.user == "Ethereal Rose":
            c.send("Adeu Ethiliana Rosada :c")

        if e.user == "Mamoncho":
            c.send("Bay Monsho.")
            
        if e.user == "Perlita Everdeen":
            c.send("Y Perlita ust se fué de fiesta a tomorrowland d4 (?)")
            
        if e.user == "Marshallow":
            c.send("Marshallow, tráeme algo cuando regreses.")
            
        if e.user == "MarcelinePeridorito002":
            c.send("La versión hippie de Vilma Russet se ha ido. (cryluigi)")
            
        if (self.logger_on):
            self.format_message(user=e.user.encode('ascii', 'ignore'), event='leave')
        print '%s ~ %s ha salido del chat. ~' % (time.strftime('%H:%M', time.gmtime()), e.user)
    
    
    def on_kick(self, c, e):
        if (self.logger_on):
            self.format_message(user=e.user[0].encode('ascii', 'ignore'),
                                mod=e.user[1].encode('ascii', 'ignore'),
                                event='kick')

        print '%s ~ %s ha sido expulsado por %s . ~' % (time.strftime('%H:%M', time.gmtime()), e.user[0], e.user[1])  


    def on_ban(self, c, e):
        if (self.logger_on):
            if e.time is not None:
                self.format_message(user=e.user[0].encode('ascii', 'ignore'),
                                    mod=e.user[1].encode('ascii', 'ignore'),
                                    time=e.time,
                                    event='ban')
            else:
                self.format_message(user=e.user[0].encode('ascii', 'ignore'),
                                    mod=e.user[1].encode('ascii', 'ignore'),
                                    event='unban')
        if e.time is not None:
            print '%s ~ %s ha sido baneado del chat durante %s segundos por %s' % (time.strftime('%H:%M', time.gmtime()),
                                                                                   e.user[0], e.time, e.user[1])
        else:
            print '%s ~ %s ha sido desbaneado del chat por %s. ~' % (time.strftime('%H:%M', time.gmtime()), e.user[0], e.user[1])


    def on_message(self, c, e):
        msg = e.text.lower()
        if (self.logger_on):
            self.format_message(user=e.user, text=e.text, event='message')

        if e.user in tell.keys() and self.tell:
            for message in tell[e.user]:
                c.send(self.command.tell_say(e.user, message))
            del tell[e.user]
            open('tell.json', 'w').write(json.dumps(tell))

        print u'%s <%s>: %s' % (time.strftime('%H:%M', time.gmtime()), e.user, e.text)

        if e.user not in ignored:
            #Activar/desactivar comando !hello
            if msg.startswith('!hon') and not self.hello_status and (wikibot.userrights(e.user)):
                self.hello_status = True
                c.send('Comando !hello activado')
            elif msg.startswith('!hoff') and self.hello_status and (wikibot.userrights(e.user)):
                self.hello_status = False
                c.send('Comando !hello desactivado')

            #Activar/desactivar registros de chat
            if msg.startswith('!log_on') and not self.logger_on and (wikibot.userrights(e.user)):
                self.logger_on = True
                c.send('Registros de chat activados.')
            elif msg.startswith('!log_off') and self.logger_on and (wikibot.userrights(e.user)):
                self.logger_on = False
                self.command.update_command(None)
                self.updated = True
                c.send('Registros de chat desactivados.')

            #Activar/desactivar información de YouTube
            if msg.startswith('!yton') and not self.youtubeinfo and (wikibot.userrights(e.user)):
                self.youtubeinfo = True
                c.send('Informacion de YouTube activada')
            elif msg.startswith('!ytoff') and self.youtubeinfo and (wikibot.userrights(e.user)):
                self.youtubeinfo = False
                c.send('Informacion de YouTube desactivada')

            #Activar/desactivar comando !seen
            if msg.startswith('!seenon') and not self.seen and (wikibot.userrights(e.user)):
                self.seen = True
                c.send('Comando !seen activado')
            elif msg.startswith('!seenoff') and self.seen and (wikibot.userrights(e.user)):
                self.seen = False
                c.send('Comando !seen desactivado')

            #Activar/descactivar información de Twitter
            if msg.startswith('!twon') and not self.twitterinfo and (wikibot.userrights(e.user)):
                self.twitterinfo = True
                c.send('Informacion de Twitter activada')
            elif msg.startswith('!twoff') and self.twitterinfo and (wikibot.userrights(e.user)):
                self.twitterinfo = False
                c.send('Informacion de Twitter desactivada')

            #Activar/desactivar comando !tell
            if msg.startswith('!tellon') and not self.tell and (wikibot.userrights(e.user)):
                self.tell = True
                c.send('Comando !tell activado')
            elif msg.startswith('!telloff') and self.tell and (wikibot.userrights(e.user)):
                self.tell = False
                c.send('Comando !tell desactivado')

            #Comando !hello
            if msg.startswith('!hello') and self.hello_status:
                c.send("Saludos, {} :u".format(e.user))

            if msg.startswith('!welcome') and (wikibot.userrights(e.user)):
                c.send(self.command.welcome_command(e.text))

            if msg.startswith('!invo'):
                c.send(self.command.invoke_command(e.text))

            #Comando !bye
            if msg.startswith('!bye'):
                c.send('Adéu')

            #Otros comandos    
            if msg.startswith('!aperture'):
                c.send('Modo Aperture activado.')

            if msg.startswith('this was a triumph'):
                c.send('I m making a note here: HUGE SUCESS.')

            if msg.startswith('its hard to overstate my satisfaction'):
                c.send('Aperture Science')

            if msg.startswith('aperture science'):
                c.send('-We do what we must, because we can.')

            if msg.startswith('we do what we must'):
                c.send('Because we can.')

            if msg.startswith('for the good of all of us'):
                c.send('Except the ones who are dead.')

            if msg.startswith('but there is no sense crying'):
                c.send('Over every mistake')

            if msg.startswith('you just keep on trying'):
                c.send('Till you run out of cake.')

            if msg.startswith('and the science gets done'):
                c.send('And you make a neat gun')

            if msg.startswith('for the people who are'):
                c.send('Still Alive.')

            if msg.startswith('im not even angry'):
                c.send('Im being so sincere right now.')

            if msg.startswith('even though you broke my heart'):
                c.send('And killed me.')

            if msg.startswith('and tore me to pieces'):
                c.send('And threw every piece')

            if msg.startswith('and threw every piece'):
                c.send('Into a fire.')

            if msg.startswith('as they burned it hurt because'):
                c.send('I was so happy for you.')

            if msg.startswith('now these points of data'):
                c.send('Make a beutiful line.')

            if msg.startswith('we are out of beta'):
                c.send('We are releasing on time.')

            if msg.startswith('so im glad i got burned'):
                c.send('Think of all the things we learned')

#            if msg.startswith('for the people who are'):
#                c.send('Still Alive.')

            if msg.startswith('go ahead and leave me'):
                c.send('I think I prefer to stay inside.')

            if msg.startswith('maybe you will find someone else'):
                c.send('To help you.')

            if msg.startswith('maybe black mesa'):
                c.send('THAT WAS A JOKE. HA HA. FAT CHANCE.')

            if msg.startswith('anyway this cake is great'):
                c.send('Its so delicious and moist.')

            if msg.startswith('look at me still talking'):
                c.send('When there is science to do.')

            if msg.startswith('when i look out there'):
                c.send('It makes me GLaD im not you.')

            if msg.startswith('i have experiments to run'):
                c.send('There is research to be done')

            if msg.startswith('on the people who are'):
                c.send('Still Alive.')

            if msg.startswith('and believe me'):
                c.send('Im still alive!')

            if msg.startswith('im doing science'):
                c.send('And Im still alive!')

            if msg.startswith('i feel fantastic'):
                c.send('And Im still alive!')

            if msg.startswith('while you are dying'):
                c.send('Ill be still alive!')

            if msg.startswith('and when you are dead'):
                c.send('Ill be still alive!')

            if msg.startswith('ill be still alive!'):
                c.send('Still Alive')

            if msg.startswith('still alive'):
                c.send('-Still Alive')

#            if msg.startswith('bot chungo'):
#                c.send('¡Nunca pedí ser creado! D:')

            if msg.startswith('/me mata a eth bot'):
                c.send('/me ni se inmuta')

            if msg.startswith('gemas'):
                c.send('Las [[Gemas de Cristal]]. (idea)')

            if msg.startswith('botencio ese'):
                c.send("{} ese.".format(e.user))
                
            if msg.startswith('/me patea al bot'):
                c.send("/me le devuelve la patada a {}".format(e.user))
                
            if msg.startswith('/me golpea a eth bot'):
                c.send("/me le devuelve el golpe a {}".format(e.user))
                
            if msg.startswith('/me patea a eth bot'):
                c.send("/me le devuelve la patada a {}".format(e.user))
                
            if msg.startswith('/me le tira un ladrillo a eth bot'):
                c.send("/me ni se inmuta.")
                
            if msg.startswith('eth bot, ¿quien es chungo?'):
                c.send("[[Especial:MiPágina|Tú]] eres chungo, [[Usuario:Eth Bot|yo]] soy chungo, [[Usuario:Mamoncho|él]] es chungo, [[Usuario:Connie Maheswaran|ella]] es chunga, [[Especial:ListaUsuarios|todos]] somos chungos! (elmo2)")
                
            if msg.startswith('khá'):
                c.send("KÁH")
                
            if msg.startswith('botencio chungo, ¿cual es el sentido de la vida?'):
                ia4 = random.choice(["No tiene, debido a que la vida es una ilusión. (idea)", "El sentido es ser chungo, todos lo sabemos, ser chungo mola!", "Hay muchas teorías sobre eso, pero el verdadero sentido es alabar a la [[Usuario:Ethereal Rose|Rosa Etérea]].", "El sentido de la vida es editar aquí. (idea)"])
                c.send(ia4)
                
            if msg.startswith('eth bot, quiero combatir contra ti'):
                ia5 = random.choice(["Activado ¿Quieres establecer combate?", "Tú no eres amenaza para mi.", "Será sólo un entrenamiento."])
                c.send(ia5)
                
            if msg.startswith('eth bot, ¿cual es tu propósito?'):
                c.send("Defender la Wikia en honor a los Bots chungos (determined)")
            
            if msg.startswith('eth bot, ¿cual es tu proposito?'):
                c.send("Defender la Wikia en honor a los Bots chungos (determined)")
                
            if msg.startswith('perola'):
                c.send("What we really are... What we really are... (perla:U)")
                
            if msg.startswith('eth bot, ¿de quien es la culpa?'):
                ia6 = random.choice(["#CulpaDeWikia (perla:u)", "#CulpaDelLag (perla:u)", "#CulpaDeLili (perla:u)", "#CulpaDeLadybug \ (ladybug) /", "#CulpaDeLosQueCulpan (perla:u)", "#CulpaDe la [[Usuario:Mamoncho|cosa chunga esta]]"])
                c.send(ia6)
                
            if msg.startswith('mate al chat'):
                c.send("ASESINO!!! D':")

            if msg.startswith('maté al chat'):
                c.send("ASESINO!!! D':")      

            if msg.startswith('(censurado) bot'):
                c.send("Reportado papu!! d1 (?)")
                
            if msg.startswith('who is touching the child'):
                ia2 = random.choice(["Don't touch the child!!! D:<", "He's touching my child! D:"])
                c.send(ia2)
                
            if msg.startswith('/me invoca a eth bot'):
                ia3 = random.choice(["Lo haré después pequeñín :v", "/me aparece entre la neblina"])
                c.send(ia3)

            if msg.startswith('!expulsion'):
                c.send('¡Que cerca estamos, pulsa el botón!')

            if msg.startswith('!kiss'):
                c.send('KE NO')

            if msg.startswith('!extremoduro'):
                c.send('Viva Extremoduro \m/')

            if msg.startswith('!pokimon'):
                pokimon = random.choice(["Bulbasaur. (idea)", "Ivysaur. (idea)", "Venusaur. (idea)", "Charmander. (idea)", "Charmeleon. (idea)", "Charizard. (idea)", "Squirtle. (idea)", "Wartortle. (idea)", "Blastoise. (idea)", "Caterpie. (idea)", "Metapod. (idea)", "Butterfree. (idea)", "Weedle. (idea)", "Kakuna. (idea)", "Beedrill. (idea)", "Pidgey. (idea)", "Pidgeotto. (idea)", "Pidgeot. (idea)", "Rattata. (idea)", "Raticate. (idea)", "Spearow. (idea)", "Fearow. (idea)" "Ekans. (idea)", "Arbok. (idea)", "Pikachu. (idea)", "Raichu. (idea)", "Sandshrew. (idea)", "Sandslash. (idea)", "Nidoran. (idea)", "Nidorina. (idea)", "Nidoqueen. (idea)", "Nidorino. (idea)", "Nidoking. (idea)", "Clefairy. (idea)", "Clefable. (idea)" "Vulpix. (idea)", "Ninetales. (idea)", "Jigglypuff. (idea)", "Wigglytuff. (idea)", "Zubat. (idea)", "Golbat (También conocido como :v). (idea)", "Oddish. (idea)", "Gloom. (idea)", "Vileplume. (idea)", "Paras. (idea)", "Parasect. (idea)", "Venonat. (idea)", "Venomoth. (idea)", "Diglett. (idea)", "Dugtrio. (idea)", "Meowth. (idea)", "Persian. (idea)", "Psyduck. (idea)", "Golduck. (idea)", "Mankey. (idea)", "Primeape. (idea)", "Growlithe. (idea)", "Arcanine. (idea)", "Poliwag. (idea)", "Pokiwhirl. (idea)", "Poliwrath. (idea)", "Abra. (idea)", "Kadabra. (idea)", "Alakazam. (idea)", "Machop. (idea)", "Machoke. (idea)", "Machamp. (idea)", "Bellsprout. (idea)", "Weepinbelt. (idea)"])
                c.send(pokimon)

            if msg.startswith('!emot'):
                c.send('[[MediaWiki:Emoticons|Lista de emoticones]]')
                
            if msg.startswith('!eth'):
                c.send('[[Usuario:Ethereal Rose|Etérea Rosada]] (?)')

            if msg.startswith('!fire'):
                c.send('[[Usuario:Fire Garnet|Granato de Fuego]]')

            if msg.startswith('!perlita'):
                c.send('[[Usuario:Perlita Everdeen|LaRubiaUst]]')
                
            if msg.startswith('!david'):
                c.send('[[Muro:David_a_esmeralda_sayan|Deividades]] (?)')

            if msg.startswith('!hl'):
                c.send('https://www.youtube.com/watch?v=7H0akRFwFWs')

            if msg.startswith('!deletememory'):
                c.send('Water Pearl borr- Espera... ¡NO!')

            if msg.startswith('!help'):
                c.send('[[Usuario:Eth Bot/Manual de uso|Ayuda, comandos e información sobre Eth Bot]].')
                
            if msg.startswith('!reglas'):
                c.send('Lee las reglas dando clic [[Project:Reglas|aquí]].')
                
            if msg.startswith('!panel'):
                c.send('Ve al Panel de Eth Bot, entra aquí: http://ethbot.hol.es y añade lo que gustes.')
                
            if msg.startswith('!guias'):
                c.send('Puedes ver las guías dando clic [[Categoría:Guías|aquí]].')
                
            if msg.startswith('!guides'):
                c.send('Puedes ver las guías dando clic [[Categoría:Guías|aquí]].')
                
            if msg.startswith('!usuario'):
                c.send(self.command.user_command(e.text))
                
            if msg.startswith('!muro'):
                c.send(self.command.wall_command(e.text))
                
            if msg.startswith('!wall'):
                c.send(self.command.wall_command(e.text))
                
            if msg.startswith('!contribuciones'):
                c.send(self.command.contributions_command(e.text))

            if msg.startswith('!contact'):
                c.send('Si necesitas algo, puedes contactar con el Staff de Wikia haciendo clic [[Especial:Contactar|aquí]].')

            if msg.startswith('!info'):
                c.send('Eth Bot versión 2.2. Bot escrito en Python para el chat de Steven Universe Wiki. [[Usuario:Eth Bot/Manual de uso|Manual de uso]] | [[Usuario:Eth Bot/Historial de versiones|Historial de versiones]].')

            if msg.startswith('!set-cmdbot-personal'):
                c.send('Códigos raros NO. Gracias.')

            if msg.startswith('!lasgemasnotienengénero'):
                c.send('Eso sólo es una táctica barata de Azucarada :v')

            if msg.startswith('!ladybug'):
                c.send('/me espera los nuevos episodios de Ladybug. .v.')

            if msg.startswith('bot chungo'):
                c.send("¡Nunca pedí ser creada! ¡Esto es culpa de {}! (amatistatriste)".format(e.user))

            if msg.startswith('/me mata al bot chungo'):
                c.send("/me no se muere y mata a {}".format(e.user))

            #Eth Bot Pokédex

            if msg.startswith('!pokedex bulbasaur'):
                c.send('N.º001: Bulbasaur, el Pokémon Semilla. A Bulbasaur es fácil verle echándose una siesta al sol. La semilla que tiene en el lomo va creciendo cada vez más a medida que absorbe los rayos del sol.')

            if msg.startswith('!pokedex ivysaur'):
                c.send('N.º002: Ivysaur, el Pokémon Semilla. Este Pokémon lleva un bulbo en el lomo y, para poder con su peso, tiene unas patas y un tronco gruesos y fuertes. Si empieza a pasar más tiempo al sol, será porque el bulbo está a punto de hacerse una flor grande.')

            if msg.startswith('!pokedex venusaur'):
                c.send('N.º003: Venusaur, el Pokémon Semilla. Venusaur tiene una flor enorme en el lomo que, según parece, adquiere unos colores muy vivos si está bien nutrido y le da mucho el sol. El aroma delicado de la flor tiene un efecto relajante en el ánimo de las personas.')

            if msg.startswith('!pokedex charmander'):
                c.send('N.º004: Charmander, el Pokémon Lagartija. La llama que tiene en la punta de la cola arde según sus sentimientos. Llamea levemente cuando está alegre y arde vigorosamente cuando está enfadado.')

            if msg.startswith('!pokedex charmeleon'):
                c.send('N.º005: Charmeleon, el Pokémon Llama. Charmeleon no tiene reparo en acabar con su rival usando las afiladas garras que tiene. Si su enemigo es fuerte, se vuelve agresivo, y la llama que tiene en el extremo de la cola empieza a arder con mayor intensidad tornándose azulada.')

            if msg.startswith('!pokedex charizard'):
                c.send('N.º006: Charizard, el Pokémon Llama. Charizard se dedica a volar por los cielos en busca de oponentes fuertes. Echa fuego por la boca y es capaz de derretir cualquier cosa. No obstante, si su rival es más débil que él, no usará este ataque.')

            if msg.startswith('!pokedex squirtle'):
                c.send('N.º007: Squirtle, el Pokémon Tortuguita. El caparazón de Squirtle no le sirve de protección únicamente. Su forma redondeada y las hendiduras que tiene le ayudan a deslizarse en el agua y le permiten nadar a gran velocidad.')

            if msg.startswith('!pokedex wartortle'):
                c.send('N.º008: Wartortle, el Pokémon Tortuga. Tiene una cola larga y cubierta de un pelo abundante y grueso que se torna más oscuro a medida que crece. Los arañazos que tiene en el caparazón dan fe de lo buen guerrero que es.')

            if msg.startswith('!pokedex blastoise'):
                c.send('N.º009: Blastoise, el Pokémon Marisco. Blastoise lanza chorros de agua con gran precisión por los tubos que le salen del caparazón que tiene en la espalda. Puede disparar chorros de agua con tanta puntería que no fallaría al tirar contra una lata pequeña a 50 m.')

            if msg.startswith('!pokedex caterpie'):
                c.send('N.º010: Caterpie, el Pokémon Gusano. Caterpie tiene un apetito voraz. Es capaz de devorar hojas que superen su tamaño en un abrir y cerrar de ojos. Atención a la antena que tiene: libera un hedor realmente fuerte.')

            if msg.startswith('!pokedex metapod'):
                c.send('N.º011: Metapod, el Pokémon Capullo. La capa que recubre el cuerpo de este Pokémon es tan dura como una plancha de hierro. Metapod apenas se mueve. Permanece inmóvil para que las vísceras evolucionen dentro de la coraza que le rodea.')

            if msg.startswith('!pokedex butterfree'):
                c.send('N.º012: Butterfree, el Pokémon Mariposa. Butterfree tiene una habilidad especial para encontrar delicioso polen en las flores. Puede localizar, extraer y transportar polen de flores que estén floreciendo a 10 km de distancia de su nido.')

            if msg.startswith('!pokedex weedle'):
                c.send('N.º013: Weedle, el Pokémon Oruga. Weedle tiene un finísimo sentido del olfato. Es capaz de distinguir las hojas que le gustan de las que no le gustan olisqueando un poco con la gran nariz que tiene.')

            if msg.startswith('!pokedex kakuna'):
                c.send('N.º014: Kakuna, el Pokémon Capullo. Kakuna permanece prácticamente inmóvil al encaramarse a los árboles, aunque la actividad interna de su organismo tiene un ritmo frenético, pues se prepara para su evolución. Prueba de esto es la alta temperatura de su caparazón.')

            if msg.startswith('!pokedex beedrill'):
                c.send('N.º015: Beedrill, el Pokémon Abeja Venenosa. Los Beedrill defienden su territorio a toda costa. No es conveniente acercarse a su colmena, por seguridad. Si se les molesta, todo un enjambre atacará ferozmente.')

            if msg.startswith('!pokedex pidgey'):
                c.send('N.º016: Pidgey, el Pokémon Pajarito. Pidgey tiene un sentido de la orientación muy desarrollado. Es capaz de regresar a su nido, por lejos que se encuentre de las zonas que le resultan familiares.')

            if msg.startswith('!pokedex pidgeotto'):
                c.send('N.º017: Pidgeotto, el Pokémon Pájaro. Pidgeotto se apodera de una zona muy vasta como su territorio y la sobrevuela para controlarla. Si alguien invade su espacio vital, no tendrá ningún reparo en castigarlo con sus afiladas garras.')

            if msg.startswith('!pokedex pidgeot'):
                c.send('N.º018: Pidgeot, el Pokémon Pájaro. El plumaje de este Pokémon es bonito e hipnótico. Muchos Entrenadores se quedan embobados ante la belleza impactante de las plumas que tiene en la cabeza; lo que les lleva a elegir a Pidgeot como su Pokémon.')

            if msg.startswith('!pokedex rattata'):
                c.send('N.º019: Rattata, el Pokémon Ratón. Rattata es cauto como él solo. Hasta cuando duerme mueve las orejas para oír todos los ruidos. No es nada delicado a la hora de elegir su hábitat. Cualquier sitio es bueno para cavar su madriguera.')

            if msg.startswith('!pokedex raticate'):
                c.send('N.º020: Raticate, el Pokémon Ratón. A Raticate le crecen los incisivos firmes y fuertes. Para mantenerlos afilados roe troncos y rocas, e incluso las paredes de las casas.')

            if msg.startswith('!pokedex spearow'):
                c.send('N.º021: Spearow, el Pokémon Pajarito. Spearow pía con tanta fuerza que se le puede oír a 1 km de distancia. Si al agudo chillido le sigue una especie de eco, estaremos oyendo la respuesta de otros Spearow que contestan ante el aviso de peligro.')

            if msg.startswith('!pokedex fearow'):
                c.send('N.º022: Fearow, el Pokémon Pico. A Fearow se le reconoce por tener un pescuezo y un pico largos que le permiten cazar en tierra y agua. Tiene una gran habilidad moviendo el fino pico para atrapar a sus presas.')

            if msg.startswith('!pokedex ekans'):
                c.send('N.º023: Ekans, el Pokémon Serpiente. Ekans se enrosca para descansar. Adoptando esta posición puede responder rápidamente a cualquier amenaza que le aceche desde cualquier lugar, levantando la cabeza con una feroz mirada.')

            if msg.startswith('!pokedex arbok'):
                c.send('N.º024: Arbok, el Pokémon Cobra. Este Pokémon es tremendamente fuerte, puede oprimir cualquier cosa con su cuerpo y hasta es capaz de estrujar un barril de acero. Una vez que Arbok se enrosca a su víctima, no hay forma de escapar de su asfixiante abrazo.')

            if msg.startswith('!pokedex pikachu'):
                c.send('N.º025: Pikachu, el Pokémon Ratón. Cada vez que un Pikachu se encuentra con algo nuevo, le lanza una descarga eléctrica. Cuando se ve alguna baya chamuscada, es muy probable que sea obra de un Pikachu, ya que a veces no controlan la intensidad de la descarga.')

            if msg.startswith('!pokedex raichu'):
                c.send('N.º026: Raichu, el Pokémon Ratón. Si las bolsas de los mofletes se le cargan demasiado, Raichu planta la cola en el suelo para liberar electricidad. Es común encontrar zonas chamuscadas cerca de la madriguera de este Pokémon.')

            if msg.startswith('!pokedex sandshrew'):
                c.send('N.º027: Sandshrew, el Pokémon Ratón. Sandshrew es capaz de absorber agua y no perder ni una gota, algo que le permite sobrevivir en el desierto. Este Pokémon se enrosca para defenderse de los enemigos.')

            if msg.startswith('!pokedex sandslash'):
                c.send('N.º028: Sandslash, el Pokémon Ratón. Sandslash está recubierto de duras púas que son partes endurecidas de la piel. Suele mudarlas una vez al año; debajo de las viejas púas crecen unas nuevas que las sustituyen.')

            if msg.startswith('!pokedex nidoran_hembra'):
                c.send('N.º029: Nidoran♀, el Pokémon Pin Veneno. Nidoran♀ tiene púas que segregan un veneno muy potente. Se piensa que las desarrolló como protección del cuerpo tan pequeño que tiene. Cuando se enfada, libera una horrible sustancia tóxica por el cuerno.')

            if msg.startswith('!pokedex nidorina'):
                c.send('N.º030: Nidorina, el Pokémon Pin Veneno. Cuando están en familia o con sus amigos, esconden las púas para evitar accidentes. Según parece, se alteran bastante si se separan del grupo.')

            if msg.startswith('!pokedex nidoqueen'):
                c.send('N.º031: Nidoqueen, el Pokémon Taladro. Nidoqueen tiene el cuerpo totalmente recubierto de escamas durísimas. Suele lanzar por los aires a sus rivales de los violentos golpes que les propina. Cuando se trata de defender a sus crías, alcanza su nivel máximo de fuerza.')

            if msg.startswith('!pokedex nidoran_macho'):
                c.send('N.º032: Nidoran♂, el Pokémon Pin Veneno. Nidoran♂ ha desarrollado músculos para mover las orejas y orientarlas en cualquier dirección. De este modo, es capaz de captar hasta el sonido más leve.')

            if msg.startswith('!pokedex nidorino'):
                c.send('N.º033: Nidorino, el Pokémon Pin Veneno. Nidorino tiene un cuerno de dureza superior a la del diamante. Si siente una presencia hostil, se le erizan las púas del lomo enseguida y carga contra el enemigo con todas sus fuerzas.')

            if msg.startswith('!pokedex nidoking'):
                c.send('N.º034: Nidoking, el Pokémon Taladro. La gruesa cola de Nidoking encierra una fuerza realmente destructora. Con una vez que la agite, es capaz de tumbar una torre metálica de transmisión. Una vez que este Pokémon se desboca, no hay quien lo pare.')

            if msg.startswith('!pokedex clefairy'):
                c.send('N.º035: Clefairy, el Pokémon Hada. Siempre que hay luna llena, salen en grupo para jugar. Al amanecer, los Clefairy, agotados, regresan a sus refugios de montaña para dormir acurrucados unos con otros.')

            if msg.startswith('!pokedex clefable'):
                c.send('N.º036: Clefable, el Pokémon Hada. Clefable se mueve dando saltitos como si fuera haciendo uso de las alas. Estos pequeños brincos le permiten caminar por el agua. De todos es sabido que le encanta darse paseos por los lagos en tranquilas noches de luna llena.')

            if msg.startswith('!pokedex vulpix'):
                c.send('N.º037: Vulpix, el Pokémon Zorro. Al nacer, Vulpix tiene una cola blanca que se divide en seis si recibe cariño por parte de su Entrenador. Las seis colas se le rizan de forma majestuosa.')

            if msg.startswith('!pokedex ninetales'):
                c.send('N.º038: Ninetales, el Pokémon Zorro. Ninetales emite una siniestra luz a través de los brillantes ojos rojos que tiene, para conseguir controlar del todo la mente de su rival. Dicen que este Pokémon llega a vivir mil años.')

            if msg.startswith('!pokedex jigglypuff'):
                c.send('N.º039: Jigglypuff, el Pokémon Globo. Jigglypuff tiene unas cuerdas vocales que ajustan sin problema la longitud de onda de su voz. Este Pokémon usa la habilidad que tiene para cantar con la longitud de onda necesaria para adormecer a su rival.')

            if msg.startswith('!pokedex wigglytuff'):
                c.send('N.º040: Wigglytuff, el Pokémon Globo. Wigglytuff tiene unos ojos enormes con forma de platillo, que siempre están cubiertos de lágrimas. Si se le metiera algo en el ojo, enseguida se le saldría solo.')

            if msg.startswith('!pokedex zubat'):
                c.send('N.º041: Zubat, el Pokémon Murciélago. Durante el día, Zubat permanece inmóvil y a oscuras. Si este Pokémon pasara mucho tiempo expuesto al sol, correría el peligro de sufrir quemaduras.')

            if msg.startswith('!pokedex golbat'):
                c.send('N.º042: Golbat, el Pokémon Murciélago. A Golbat le encanta chuparles la sangre a los seres vivos. Este Pokémon es más activo en la oscuridad de la noche. Es al caer la noche cuando sale a revolotear y a buscar sangre fresca.')

            if msg.startswith('!pokedex oddish'):
                c.send('N.º043: Oddish, el Pokémon Hierbajo. Durante el día, Oddish se entierra en el suelo para absorber nutrientes valiéndose de todo el cuerpo. Cuanto más fértil sea el suelo, mayor brillo tendrá en las hojas.')

            if msg.startswith('!pokedex gloom'):
                c.send('N.º044: Gloom, el Pokémon Hierbajo. Gloom libera un fétido olor por el pistilo de la flor. Cuando está en peligro, el hedor se intensifica. Si este Pokémon está tranquilo y no se siente amenazado, no libera el desagradable olor.')

            if msg.startswith('!pokedex vileplume'):
                c.send('N.º045: Vileplume, el Pokémon Flor. El polen que contienen las esporas tóxicas de Vileplume causa unos ataques de alergia muy agudos. Por eso, no es aconsejable acercarse a ninguna flor selvática, por muy bonita que sea.')

            if msg.startswith('!pokedex Paras'):
                c.send('N.º046: Paras, el Pokémon Hongo. Paras lleva dos setas parásitas a cuestas llamadas tochukaso. Estas crecen alimentándose de los nutrientes de este Pokémon de tipo Bicho y Planta que les sirve de huésped. Las setas se usan como elixir de vida.')

            if msg.startswith('!pokedex parasect'):
                c.send('N.º047: Parasect, el Pokémon Hongo. Parasect es conocido por destruir en plaga grandes árboles, absorbiendo los nutrientes que tienen en la parte baja del tronco y las raíces. Cuando un árbol azotado por la plaga muere, los Parasect van a por el siguiente al instante.')

            if msg.startswith('!pokedex venonat'):
                c.send('N.º048: Venonat, el Pokémon Insecto. Dicen que durante su evolución Venonat desarrolló una fina capa de espeso pelo alrededor de todo el cuerpo para protegerse. Tiene unos ojos tan grandes que no hay presa que le pase desapercibida.')

            if msg.startswith('!pokedex venomoth'):
                c.send('N.º049: Venomoth, el Pokémon Polilla Venenosa. Venomoth es nocturno, solo actúa en la oscuridad. Su alimento preferido son los pequeños insectos que se concentran cerca de los focos de luz en la oscuridad de la noche.')

            if msg.startswith('!pokedex diglett'):
                c.send('N.º050: Diglett, el Pokémon Topo. En la mayoría de las granjas se suelen criar Diglett por la sencilla razón de que, excaven donde excaven, dejan la tierra perfectamente labrada para sembrar. El terreno queda listo para plantar ricas verduras.')

            if msg.startswith('!pokedex dugtrio'):
                c.send('N.º051: Dugtrio, el Pokémon Topo. Los Dugtrio son trillizos que se originaron a partir de un solo cuerpo, por eso piensan de la misma forma. A la hora de excavar, trabajan en equipo y sin descanso.')

            if msg.startswith('!pokedex meowth'):
                c.send('N.º052: Meowth, el Pokémon Gato Araña. Meowth retrae las afiladas uñas de sus zarpas para caminar a hurtadillas, dando sigilosos pasos para pasar inadvertido. No se sabe muy bien por qué, pero este Pokémon adora las monedas brillantes que resplandecen con la luz.')

            if msg.startswith('!pokedex persian'):
                c.send('N.º053: Persian, el Pokémon Gato Fino. Persian tiene seis llamativos bigotes que le dan un aspecto feroz. Además, le sirven para detectar el movimiento del aire, delator de la presencia cercana de algún Pokémon. Si se le agarra por los bigotes, se vuelve dócil.')

            if msg.startswith('!pokedex psyduck'):
                c.send('N.º054: Psyduck, el Pokémon Pato. Psyduck tiene un extraño poder, que consiste en generar ondas cerebrales iguales a las que se generan cuando se está dormido. Este descubrimiento levantó una gran polémica entre eruditos.')

            if msg.startswith('!pokedex golduck'):
                c.send('N.º055: Golduck, el Pokémon Pato. Golduck alcanza una velocidad de vértigo gracias a las aletas palmípedas de las extremidades y a la forma aerodinámica de su cuerpo. Realmente, la velocidad de este Pokémon supera la de cualquier nadador.')

            if msg.startswith('!pokedex mankey'):
                c.send('N.º056: Mankey, el Pokémon Mono Cerdo. Cuando Mankey empieza a temblar y a respirar con más intensidad, seguro que va a enfadarse. Aunque prever su enfado no sirve de nada porque alcanza un estado de rabia tan rápido que no hay escapatoria.')

            if msg.startswith('!pokedex primeape'):
                c.send('N.º057: Primeape, el Pokémon Mono Cerdo. Cuando Primeape se enfada, se le acelera el ritmo cardíaco y se le fortalecen los músculos. Con todo, pierde en inteligencia.')

            if msg.startswith('!pokedex growlithe'):
                c.send('N.º058: Growlithe, el Pokémon Perrito. Growlithe tiene un sentido del olfato excepcional y una memoria sensitiva tremenda, nunca olvida una esencia. Este Pokémon saca provecho de este don para identificar las sensaciones que tienen otros seres vivos.')

            if msg.startswith('!pokedex arcanine'):
                c.send('N.º059: Arcanine, el Pokémon Legendario. Arcanine es conocido por lo veloz que es. Dicen que es capaz de correr 10 000 km en 24 horas. El fuego que arde con vigor en el interior de este Pokémon constituye su fuente de energía.')

            if msg.startswith('!pokedex poliwag'):
                c.send('N.º060: Poliwag, el Pokémon Renacuajo. Poliwag tiene una piel muy fina. Tanto que es posible entrever a través de la misma las vísceras en espiral que tiene. La piel, aunque fina, tiene la ventaja de ser flexible y hacer rebotar hasta los colmillos más afilados.')

            if msg.startswith('!pokedex poliwhirl'):
                c.send('N.º061: Poliwhirl, el Pokémon Renacuajo. La piel de Poliwhirl está siempre húmeda y lubricada con un fluido viscoso. Gracias a esta película resbaladiza, puede escapar de las garras del enemigo, resbalándosele de las zarpas en pleno combate.')

            if msg.startswith('!pokedex poliwrath'):
                c.send('N.º062: Poliwrath, el Pokémon Renacuajo. Poliwrath tiene unos músculos fornidos y muy desarrollados, por lo que nunca se agota. Es tan fuerte e incansable que cruzar el océano a nado no le supone ningún esfuerzo.')

            if msg.startswith('!pokedex abra'):
                c.send('N.º063: Abra, el Pokémon Psi. Abra duerme 18 horas al día, pero puede detectar a cualquier enemigo que se le acerque mientras duerme. En una situación así, usa Teletransporte para protegerse.')

            if msg.startswith('!pokedex kadabra'):
                c.send('N.º064: Kadabra, el Pokémon Psi. Kadabra emite unas ondas alfa muy particulares que provocan dolores de cabeza a los demás. Solo aquellos que tengan gran poder mental podrán optar a ser Entrenador de este Pokémon.')

            if msg.startswith('!pokedex alakazam'):
                c.send('N.º065: Alakazam, el Pokémon Psi. El cerebro de Alakazam nunca deja de crecer y por eso al cuello le cuesta sostener el peso de la cabeza. Este Pokémon usa sus poderes psicoquinéticos para mantener en alto la cabeza.')

            if msg.startswith('!pokedex machop'):
                c.send('N.º066: Machop, el Pokémon Superpoder. Gracias a su portentosa musculatura, Machop no se agota por mucho esfuerzo que haga. Este Pokémon es tan fuerte que puede derrotar a cien personas adultas de una sola vez.')

            if msg.startswith('!pokedex machoke'):
                c.send('N.º067: Machoke, el Pokémon Superpoder. Los entrenados músculos de Machoke son tan fuertes como el acero. Este Pokémon es tan fuerte que puede levantar con un solo dedo a un luchador de sumo.')

            if msg.startswith('!pokedex machamp'):
                c.send('N.º068: Machamp, el Pokémon Superpoder. Machamp es tan fuerte que puede derribar lo que quiera. Sin embargo, cuando tiene que realizar una tarea que requiere delicadeza y destreza, se le enredan los brazos. Este Pokémon pasa a la acción sin pensar.')

            if msg.startswith('!pokedex bellsprout'):
                c.send('N.º069: Bellsprout, el Pokémon Flor. Bellsprout tiene un cuerpo delgado y flexible que le permite inclinarse y balancearse para esquivar los ataques. Este Pokémon escupe por la boca un fluido corrosivo capaz de hacer que se derrita hasta el hierro.')

            if msg.startswith('!pokedex weepinbell'):
                c.send('N.º070: Weepinbell, el Pokémon Matamoscas. Weepinbell tiene un gancho a modo de extremidad superior trasera, que usa por la noche para colgarse de una rama y echarse a dormir. Si se mueve mientras duerme, puede acabar en el suelo.')

            if msg.startswith('!pokedex victreebell'):
                c.send('N.º071: Victreebell, el Pokémon Matamoscas. Victreebel tiene una enredadera que le sale de la cabeza y que agita a modo de señuelo para atraer a sus presas y así engullirlas por sorpresa cuando estas se aproximan incautas.')

            if msg.startswith('!pokedex tentacool'):
                c.send('N.º072: Tentacool, el Pokémon Medusa. Tentacool está compuesto en su mayor parte por agua. Si se le saca del mar, se secará y se quedará acartonado. Si este Pokémon se deshidrata, hay que echarlo inmediatamente de vuelta al mar.')

            if msg.startswith('!pokedex tentacruel'):
                c.send('N.º073: Tentacruel, el Pokémon Medusa. Tentacruel tiene unas enormes esferas rojas en la cabeza, que brillan antes de lanzar una descarga ultrasónica a lo que le rodea. Este estallido crea unas olas tremendas a su alrededor.')

            if msg.startswith('!pokedex geodude'):
                c.send('N.º074: Geodude, el Pokémon Roca. Cuanto más larga es la vida de Geodude, mayor es el desgaste y la erosión que sufre, y más redondeada la forma que va adquiriendo. Sin embargo, el corazón permanece siempre duro, rocoso y tosco.')

            if msg.startswith('!pokedex graveler'):
                c.send('N.º075: Graveler, el Pokémon Roca. Graveler crece alimentándose a base de piedras. Y, según parece, las prefiere cubiertas de musgo. Cada día se abre camino comiéndose una tonelada de rocas.')

            if msg.startswith('!pokedex golem'):
                c.send('N.º076: Golem, el Pokémon Megatón. Golem vive en las montañas. Si se produce un gran terremoto, estos Pokémon descienden rodando en masa por las laderas.')

            if msg.startswith('!pokedex ponyta'):
                c.send('N.º077: Ponyta, el Pokémon Caballo Fuego. Al nacer, Ponyta es muy débil y apenas puede ponerse en pie. Con todo, se va haciendo más fuerte al tropezarse y caerse en su intento por seguir a sus progenitores.')

            if msg.startswith('!pokedex rapidash'):
                c.send('N.º078: Rapidash, el Pokémon Caballo Fuego. A Rapidash se le suele ver trotando sin rumbo fijo por los campos y llanos. Cuando tiene que ir a algún sitio en concreto, se le aviva el fuego de las melenas y emprende el galope llameante llegando a los 240 km/h.')

            if msg.startswith('!pokedex slowpoke'):
                c.send('N.��079: Slowpoke, el Pokémon Atontado. Slowpoke usa la cola para atrapar a sus presas metiéndola bajo el agua en las riberas de los ríos. Con todo, es olvidadizo, se le puede pasar lo que estaba haciendo y quedarse días enteros holgazaneando en la orilla.')

            if msg.startswith('!pokedex slowbro'):
                c.send('N.º080: Slowbro, el Pokémon Ermitaño. Slowbro lleva en la cola un Shellder enganchado, sujeto por los dientes. Como Slowbro no puede usar la cola para pescar, se mete en el agua de mala gana en busca de sus presas.')

            if msg.startswith('!pokedex magnemite'):
                c.send('N.º081: Magnemite, el Pokémon Imán. Magnemite se engancha a las líneas de tensión para nutrirse de electricidad. Cuando se producen apagones en las casas, es aconsejable revisar el automático y comprobar que no hay Pokémon de este tipo colgados de la caja de fusibles.')

            if msg.startswith('!pokedex magneton'):
                c.send('N.º082: Magneton, el Pokémon Imán. Magneton emite una fuerte energía magnética que causa estragos en los instrumentos mecánicos. Por ello, en las ciudades se avisa con sirenas cuando hay concentraciones de estos Pokémon.')

            if msg.startswith('!pokedex farfetchd'):
                c.send('N.º083: Farfetchd, el Pokémon Pato Salvaje. Al parecer, entre los puerros que suelen llevar los Farfetchd, los hay mejores y peores. A estos Pokémon se les ha visto luchar entre ellos por los mejores puerros.')

            if msg.startswith('!pokedex doduo'):
                c.send('N.º084: Doduo, el Pokémon Ave Gemela. Las dos cabezas de Doduo duermen de forma independiente, siempre por turnos. Mientras una duerme, la otra hace de centinela por si aparecen enemigos.')

            if msg.startswith('!pokedex dodrio'):
                c.send('N.º085: Dodrio, el Pokémon Ave Triple. Según parece, las cabezas no son las únicas partes del cuerpo que tiene triplicadas. Dodrio también tiene tres corazones y tres pares de pulmones. Con esta constitución, puede correr largas distancias sin cansarse.')

            if msg.startswith('!pokedex seel'):
                c.send('N.º086: Seel, el Pokémon León Marino. Seel busca a sus presas en aguas heladas, bajo las capas de hielo. Cuando necesita respirar, abre un agujerito en el hielo con la afilada protuberancia que tiene encima de la cabeza.')

            if msg.startswith('!pokedex dewgong'):
                c.send('N.º087: Dewgong, el Pokémon León Marino. A Dewgong le encanta dormitar sobre la frialdad del hielo. Antiguamente, algún que otro marino lo confundió con una sirena al verlo dormido sobre un glaciar.')

            if msg.startswith('!pokedex grimer'):
                c.send('N.º088: Grimer, el Pokémon Lodo. El elástico cuerpo de lodo de Grimer le permite colarse por cualquier orificio, sea del tamaño que sea. Este Pokémon entra en los bajantes de las cloacas para beberse el agua sucia.')

            if msg.startswith('!pokedex muk'):
                c.send('N.º089: Muk, el Pokémon Lodo. Muk emana por todo el cuerpo un fluido maloliente que obliga a taparse la nariz. Con solo una gota de la sustancia que exuda este Pokémon, se podría contaminar un estanque.')

            if msg.startswith('!pokedex shellder'):
                c.send('N.º090: Shellder, el Pokémon Bivalvo. Por la noche, este Pokémon usa la ancha lengua que tiene para hacer un agujero en el fondo del mar y echarse a dormir. Mientras duerme, Shellder cierra la concha, pero deja la lengua por fuera.')

            if msg.startswith('!pokedex cloyster'):
                c.send('N.º091: Cloyster, el Pokémon Bivalvo. Cloyster es capaz de nadar por el mar. Su técnica consiste en tragar agua y expulsarla por el conducto que tiene en la parte trasera. Este mismo sistema es el que usa para lanzar los pinchos que tiene alrededor de la concha.')

            if msg.startswith('!pokedex gastly'):
                c.send('N.º092: Gastly, el Pokémon Gas. Gastly está compuesto en gran medida de materia gaseosa. Cuando hay viento, el aire arrastra parte de esta materia y el Pokémon mengua. Suelen agruparse bajo los aleros de las casas para resguardarse del viento.')

            if msg.startswith('!pokedex haunter'):
                c.send('N.º093: Haunter, el Pokémon Gas. Haunter es un Pokémon peligroso. Si se ve alguno flotando en la oscuridad y haciendo señas, conviene no acercarse. Este Pokémon intentará robarle la energía a su presa a base de lametazos.')

            if msg.startswith('!pokedex gengar'):
                c.send('N.º094: Gengar, el Pokémon Sombra. Si alguien ve que su sombra le adelanta de repente en una noche oscura, es muy probable que lo que esté viendo no sea su sombra, sino a un Gengar haciéndose pasar por la misma.')

            if msg.startswith('!pokedex onix'):
                c.send('N.º095: Onix, el Pokémon Serpiente Roca. Onix tiene un imán en el cerebro, que actúa como una brújula para no perder la orientación cuando está cavando túneles. A medida que crece, se le redondea y suaviza el cuerpo.')

            if msg.startswith('!pokedex drowzee'):
                c.send('N.º096: Drowzee, el Pokémon Hipnosis. Si a alguien le pica la nariz mientras duerme, seguro que es porque tiene a uno de estos Pokémon cerca de la almohada intentando sacarle los sueños por la nariz para comérselos.')

            if msg.startswith('!pokedex hypno'):
                c.send('N.º097: Hypno, el Pokémon Hipnosis. Hypno lleva un péndulo en la mano. El balanceo y el brillo que tiene sumen al rival en un estado de hipnosis profundo. Mientras busca a su presa, saca brillo al péndulo.')

            if msg.startswith('!pokedex krabby'):
                c.send('N.º098: Krabby, el Pokémon Cangrejo. Krabby vive en la playa, enterrado en agujeros en la arena. Cuando en las playas de arena fina escasea la comida, es común ver a estos Pokémon echando un pulso panza contra panza en defensa de su territorio.')

            if msg.startswith('!pokedex kingler'):
                c.send('N.º099: Kingler, el Pokémon Tenaza. Kingler tiene una pinza enorme y descomunal que usa agitándola en el aire para comunicarse con otros. Lo malo es que, al pesarle tanto, se cansa enseguida.')

            if msg.startswith('!pokedex voltorb'):
                c.send('N.º100: Voltorb, el Pokémon Bola. Voltorb fue visto por primera vez en una empresa encargada de comercializar Poké Balls. La conexión que existe entre aquella primera vez que se le vio y el hecho de que se parece mucho a una Poké Ball sigue siendo un misterio.')

            if msg.startswith('!pokedex electrode'):
                c.send('N.º101: Electrode, el Pokémon Bola. Los Electrode se alimentan de la electricidad de la atmósfera. En días de tormenta con rayos, es fácil verlos explotando por todos lados tras haber consumido demasiada electricidad.')

            if msg.startswith('!pokedex exeggcute'):
                c.send('N.º102: Exeggcute, el Pokémon Huevo. Este Pokémon está compuesto de seis huevos que forman una tupida piña que va girando. Cuando se empiezan a resquebrajar las cáscaras, no hay duda de que Exeggcute está a punto de evolucionar.')

            if msg.startswith('!pokedex exeggutor'):
                c.send('N.º103: Exeggutor, el Pokémon Coco. Exeggutor es originario del trópico. Cuando se expone a un sol intenso, le empiezan a crecer las cabezas. Hay quien dice que, cuando las cabezas caen al suelo, se unen para formar un Exeggcute.')

            if msg.startswith('!pokedex cubone'):
                c.send('N.º104: Cubone, el Pokémon Solitario. A Cubone le ahoga la pena porque no volverá a ver jamás a su madre. La luna le recuerda a veces a ella, y se pone a llorar. Los churretes que tiene en el cráneo que lleva puesto son debidos a las lágrimas que derrama.')

            if msg.startswith('!pokedex marowak'):
                c.send('N.º105: Marowak, el Pokémon Apilahueso. Marowak es la forma evolucionada de Cubone. Es más fuerte porque ha superado la pena por la pérdida de su madre. El ánimo de este Pokémon, ya curtido y fortalecido, no es muy fácil de alterar.')

            if msg.startswith('!pokedex hitmonlee'):
                c.send('N.º106: Hitmonlee, el Pokémon Patada. Hitmonlee tiene la facilidad de encoger y estirar las patas. Con extremidades tan flexibles, propina unas patadas demoledoras. Tras la lucha, se masajea las piernas y relaja los músculos para descansar.')

            if msg.startswith('!pokedex hitmonchan'):
                c.send('N.º107: Hitmonchan, el Pokémon Puñetazo. Dicen que Hitmonchan tiene el mismo ímpetu que un boxeador entrenándose para un campeonato mundial. Este Pokémon tiene un espíritu indomable que nunca se doblega ante la adversidad.')

            if msg.startswith('!pokedex lickitung'):
                c.send('N.º108: Lickitung, el Pokémon Lametazo. Cada vez que Lickitung se encuentra con algo que no conoce, le da un lametazo. Es la forma que tiene de memorizar las cosas, por la textura y el sabor. No soporta los sabores ácidos.')

            if msg.startswith('!pokedex koffing'):
                c.send('N.º109: Koffing, el Pokémon Gas Venenoso. Si Koffing se pone nervioso, aumenta el nivel de toxicidad de los gases que tiene y los expulsa por todo el cuerpo. También suele hincharse mucho hasta llegar a explotar.')

            if msg.startswith('!pokedex weezing'):
                c.send('N.º110: Weezing, el Pokémon Gas Venenoso. A Weezing le encantan los gases que emanan de los desperdicios que quedan en la cocina. Este Pokémon busca casas sucias y descuidadas para crear su hogar. De noche, cuando los habitantes de la casa duermen, va a por la basura.')

            if msg.startswith('!pokedex rhyhorn'):
                c.send('N.º111: Rhyhorn, el Pokémon Clavos. Rhyhorn corre en línea recta arrasando todo lo que encuentra en su camino. Aun estrellándose de cabeza contra un bloque de acero, no se vería afectado; a lo sumo, notaría algo de dolor al día siguiente.')

            if msg.startswith('!pokedex rhydon'):
                c.send('N.º112: Rhydon, el Pokémon Taladro. Rhydon tiene un cuerno capaz de horadar hasta un diamante en bruto y con una sacudida de la cola puede derribar un edificio. La piel de este Pokémon es muy fuerte; ni los disparos de un cañón le arañarían.')

            if msg.startswith('!pokedex chansey'):
                c.send('N.º113: Chansey, el Pokémon Huevo. Chansey pone a diario huevos con un valor nutritivo altísimo. Están tan ricos que hasta quien no tenga hambre se los comerá en un abrir y cerrar de ojos.')

            if msg.startswith('!pokedex tangela'):
                c.send('N.º114: Tangela, el Pokémon Enredadera. A Tangela se le desprenden los tentáculos con facilidad en cuanto se los agarras. Y no solo no le duele, sino que le resulta muy útil para escapar rápido. Además, al día siguiente le crecen otros.')

            if msg.startswith('!pokedex kangaskhan'):
                c.send('N.º115: Kangaskhan, el Pokémon Padres. No es recomendable molestar ni intentar atrapar a crías de Kangaskhan mientras estén jugando, ya que seguro que su madre anda cerca y reaccionará con enfado y violencia.')

            if msg.startswith('!pokedex horsea'):
                c.send('N.º116: Horsea, el Pokémon Dragón. Horsea come insectos pequeños y el musgo de las rocas. Si las corrientes del océano cobran fuerza, este Pokémon se anclará con la cola a rocas o corales para evitar que las aguas lo arrastren.')

            if msg.startswith('!pokedex seadra'):
                c.send('N.º117: Seadra, el Pokémon Dragón. Seadra se echa a dormir tras abrirse un hueco entre las ramas de los corales. Los pescadores de coral suelen pincharse con las púas venenosas de estos Pokémon si no los ven.')

            if msg.startswith('!pokedex goldeen'):
                c.send('N.º118: Goldeen, el Pokémon Pez Color. Goldeen es un bello Pokémon que mueve con elegancia las aletas en el agua. Con todo, no hay que bajar la guardia, en cualquier momento puede embestir con el cuerno.')

            if msg.startswith('!pokedex seaking'):
                c.send('N.º119: Seaking, el Pokémon Pez Color. En otoño, se ven ejemplares de Seaking macho danzando en las riberas de los ríos para cortejar a las hembras. En esta época, la coloración de este Pokémon alcanza sus niveles máximos de belleza.')

            if msg.startswith('!pokedex staryu'):
                c.send('N.º120: Staryu, el Pokémon Estrellada. Staryu posee un órgano central, conocido como su núcleo, que brilla con una luz roja. A finales de verano, pueden verse en la playa los núcleos de estos Pokémon brillando como las estrellas del cielo.')

            if msg.startswith('!pokedex starmie'):
                c.send('N.º121: Starmie, el Pokémon Misterioso. La parte central de Starmie, el núcleo brillante, resplandece con siete colores distintos. Debido a su naturaleza luminosa, a este Pokémon se le ha dado el apelativo de la Gema del Mar.')

            if msg.startswith('!pokedex mr. mime'):
                c.send('N.º122: Mr. Mime, el Pokémon Barrera. Mr. Mime es un experto en pantomima. Con sus gestos y movimientos es capaz de convencer a sus espectadores de que algo existe, cuando en realidad no es así. Pero, cuando el público se lo cree, las ilusiones se hacen realidad.')

            if msg.startswith('!pokedex scyther'):
                c.send('N.º123: Scyther, el Pokémon Mantis. Es espectacular ver lo rápido que es Scyther. Su increíble velocidad refuerza el efecto del par de guadañas que tiene en los brazos, que ya son de por sí contundentes; rebanan gruesos troncos de un tajo.')

            if msg.startswith('!pokedex jynx'):
                c.send('N.º124: Jynx, el Pokémon Forma Humana. Jynx camina con ritmo, balanceándose y moviendo las caderas como si estuviera bailando. Realiza unos movimientos tan vistosos y atractivos que no hay quien pueda resistirse a mover las caderas.')

            if msg.startswith('!pokedex electabuzz'):
                c.send('N.º125: Electabuzz, el Pokémon Eléctrico. Al desatarse una tormenta, bandadas de estos Pokémon se enfrentan entre sí para ver quién alcanza antes sitios altos en los que suelan caer rayos. Hay ciudades que usan Electabuzz en lugar de pararrayos.')

            if msg.startswith('!pokedex magmar'):
                c.send('N.º126: Magmar, el Pokémon Escupefuego. Al luchar, Magmar expulsa violentas llamas por todo el cuerpo para intimidar a su rival. Estos estallidos de fuego crean ondas de calor que abrasan la hierba y los árboles que haya en las proximidades.')

            if msg.startswith('!pokedex pinsir'):
                c.send('N.º127: Pinsir, el Pokémon Escarabajo. Pinsir es sorprendentemente fuerte. Puede agarrar con los cuernos a un rival que pese el doble que él y levantarlo por los aires. En zonas frías, los movimientos de este Pokémon se vuelven lentos.')

            if msg.startswith('!pokedex tauros'):
                c.send('N.º128: Tauros, el Pokémon Toro Bravo. Este Pokémon no está contento a menos que esté continuamente de aquí para allá. Si no hay rival que luche contra Tauros, se estampa contra árboles grandes para calmarse y los embiste para echarlos abajo.')

            if msg.startswith('!pokedex magikarp'):
                c.send('N.º129: Magikarp, el Pokémon Pez. Magikarp es el triste ejemplo de un Pokémon capaz únicamente de saltar y salpicar. Esta conducta llevó a científicos a estudiarlo en profundidad.')

            if msg.startswith('!pokedex gyarados'):
                c.send('N.º130: Gyarados, el Pokémon Atrocidad. Cuando Magikarp evoluciona y se convierte en Gyarados, sufre un cambio estructural en las células del cerebro. Dicen que esa transformación es la causa de la naturaleza violenta y salvaje de este Pokémon.')

            if msg.startswith('!pokedex lapras'):
                c.send('N.º131: Lapras, el Pokémon Transporte. Por culpa de la gente, Lapras está casi en extinción. Dicen que, al anochecer, se pone a cantar quejicoso mientras busca a los miembros de su especie que puedan quedar.')

            if msg.startswith('!pokedex ditto'):
                c.send('N.º132: Ditto, el Pokémon Transformación. Ditto reorganiza la estructura de sus células para adoptar otras formas. Pero, como intente transformarse en algo guiándose por los datos que tenga almacenados en la memoria, habrá detalles que se le escapen.')

            if msg.startswith('!pokedex eevee'):
                c.send('N.º133: Eevee, el Pokémon Evolución. La configuración genética de Eevee le permite mutar y adaptarse enseguida a cualquier medio en el que viva. La evolución de este Pokémon suele ser posible gracias a las radiaciones emitidas por varias piedras.')

            if msg.startswith('!pokedex vaporeon'):
                c.send('N.º134: Vaporeon, el Pokémon Burbuja. Vaporeon sufrió una mutación repentina y desarrolló aletas y branquias que le permiten vivir bajo el agua. Asimismo, este Pokémon tiene la habilidad de controlar las aguas.')

            if msg.startswith('!pokedex jolteon'):
                c.send('N.º135: Jolteon, el Pokémon Relámpago. Las células de Jolteon generan un nivel bajo de electricidad, cuya intensidad aumenta con la electricidad estática que acumula en un pelaje formado por agujas cargadas de electricidad. Esta característica le permite lanzar rayos.')

            if msg.startswith('!pokedex flareon'):
                c.send('N.º136: Flareon, el Pokémon Llama. La suavidad del pelaje de Flareon tiene una función clara: libera calor para que el Pokémon no se asfixie. La temperatura corporal de este Pokémon puede alcanzar los 900 °C.')

            if msg.startswith('!pokedex porygon'):
                c.send('N.º137: Porygon, el Pokémon Virtual. Porygon es capaz de convertirse otra vez en datos informáticos y de entrar en el ciberespacio. Tiene protección anticopia, así que es imposible duplicarlo.')

            if msg.startswith('!pokedex omanyte'):
                c.send('N.º138: Omanyte, el Pokémon Espiral. Omanyte es uno de esos Pokémon ancestrales que se extinguieron hace muchísimo tiempo y que la gente ha recuperado a partir de fósiles. Si un enemigo le ataca, se esconderá dentro de la dura concha que tiene.')

            if msg.startswith('!pokedex omastar'):
                c.send('N.º139: Omastar, el Pokémon Espiral. Omastar usa los tentáculos para atrapar a su presa. Se cree que el motivo de su extinción fue el tamaño y el peso que llegó a alcanzar la concha que lleva a cuestas, lo que le entorpeció y ralentizó los movimientos.')

            if msg.startswith('!pokedex kabuto'):
                c.send('N.º140: Kabuto, el Pokémon Marisco. Kabuto es un Pokémon regenerado a partir de un fósil, aunque, en raras ocasiones, se han encontrado casos de ejemplares vivos en estado salvaje. En 300 millones de años, este Pokémon no ha cambiado en nada.')

            if msg.startswith('!pokedex kabutops'):
                c.send('N.º141: Kabutops, el Pokémon Marisco. Hace mucho tiempo, Kabutops buceaba para atrapar a sus presas. Parece ser que en algún momento cambió de hábitat y se adaptó a vivir en tierra firme. La transformación que se aprecia en las patas y branquias así lo confirma.')

            if msg.startswith('!pokedex aerodactyl'):
                c.send('N.º142: Aerodactyl, el Pokémon Fósil. Los orígenes de Aerodactyl datan de la era de los dinosaurios. Se regeneró a partir de material genético contenido en ámbar. Se supone que fue el amo de los cielos en épocas pasadas.')

            if msg.startswith('!pokedex snorlax'):
                c.send('N.º143: Snorlax, el Pokémon Dormir. Un día cualquiera en la vida de Snorlax consiste en comer y dormir. Es un Pokémon tan dócil que es fácil ver niños usando la gran panza que tiene como lugar de juegos.')

            if msg.startswith('!pokedex articuno'):
                c.send('N.º144: Articuno, el Pokémon Congelar. Articuno es un Pokémon pájaro legendario que puede controlar el hielo. El batir de sus alas congela el aire. Dicen que consigue hacer que nieve cuando vuela.')

            if msg.startswith('!pokedex zapdos'):
                c.send('N.º145: Zapdos, el Pokémon Eléctrico. Zapdos es un Pokémon pájaro legendario que tiene la habilidad de controlar la electricidad. Suele vivir en nubarrones. Este Pokémon gana mucha fuerza si le alcanzan los rayos.')

            if msg.startswith('!pokedex moltres'):
                c.send('N.º146: Moltres, el Pokémon Llama. Moltres es un Pokémon pájaro legendario que tiene la habilidad de controlar el fuego. Dicen que, si resulta herido, se sumerge en el líquido magma de un volcán para arder y curarse.')

            if msg.startswith('!pokedex dratini'):
                c.send('N.º147: Dratini, el Pokémon Dragón. Dratini muda y se despoja de la vieja piel continuamente. Es algo que necesita hacer porque la energía que tiene en su interior no para de alcanzar niveles incontrolables.')

            if msg.startswith('!pokedex dragonair'):
                c.send('N.º148: Dragonair, el Pokémon Dragón. Dragonair acumula grandes cantidades de energía dentro de sí. Dicen que altera el clima de la zona en la que está descargando energía a través de las esferas de cristal que tiene en el cuello y en la cola.')

            if msg.startswith('!pokedex dragonite'):
                c.send('N.º149: Dragonite, el Pokémon Dragón. Dragonite es capaz de dar la vuelta al mundo en solo 16 horas. Es un Pokémon de buen corazón que guía hasta tierra a los barcos que se encuentran perdidos en plena tormenta y a punto de zozobrar.')

            if msg.startswith('!pokedex mewtwo'):
                c.send('N.º150: Mewtwo, el Pokémon Genético. Mewtwo fue creado por manipulación genética. Pero, a pesar de que el hombre creó su cuerpo, dotar a Mewtwo de un corazón compasivo quedó en el olvido.')

            if msg.startswith('!pokedex mew'):
                c.send('N.º151: Mew, el Pokémon Nueva Especie. Dicen que Mew posee el mapa genético de todos los Pokémon. Puede hacerse invisible cuando quiere, así que pasa desapercibido cada vez que se le acerca alguien.')
                

            #Comando !restart. Actualiza los registros y luego reinicia el bot.
            if msg.startswith('!restart') and (wikibot.userrights(e.user)):
                self.th.cancel()
                c.send(self.command.update_command(e.user))
                self.updated = True
                c.send("{}: Reiniciando Eth Bot...".format(e.user))
                c.restart()


            #Comando !bot_off. Apaga el bot. Luego de haberse usado, sólo puede volver a encenderse mediante SSH.
            if msg.startswith('!bot_off') and (wikibot.userrights(e.user)):
                self.th.cancel()
                c.send(self.command.update_command(e.user))
                self.updated = True
                c.send("{}: Apagando Eth Bot...".format(e.user))
                c.disconnect()

            #Comando !updated. Muestra la última vez que los registros del chat fueron actualizados
            if msg.startswith('!updated') and (wikibot.userrights(e.user)):
                c.send(self.command.updated_command(e.user))

            #Comando !logs. Muestra la página de registros del chat
            if msg.startswith('!logs'):
                c.send(self.command.log_command(e.user))

            #Comando !clearreg. Vacía los registros del chat
            if msg.startswith('!clearlogs') and (wikibot.userrights(e.user)):
                c.send(self.command.dump_buffer_command())

            #Información de YouTube
            if ('http' and 'youtu' in msg) and (e.user not in ["Pokimon Bot",  config_file['user']]) and self.youtubeinfo:
                c.send(self.command.youtube_info(e.text))

            #Comando !seen
            if msg.startswith('!seen '):
                if self.seen:
                    if e.user not in userdict:
                        userdict[e.user] = time.time()
                    c.send(self.command.seen_command(e.user, e.text, userdict, time.time()))
                else:
                    pass

            #Comando !kick (Expulsar usuarios)
            if msg.startswith('!kick') and (wikibot.userrights(e.user)):
                try:
                    user = e.text.split(' ', 1)[1]
                    if (wikibot.userrights(user)):
                        pass
                    else:
                        c.kick_user(user)
                except IndexError:
                    pass

            #Filtro de groserías (Desactivado por defecto)
            #if self.command.swear_filter(msg) and not (wikibot.userrights(e.user)):
            #    c.kick_user(e.user)

            #Comando !updatelogs. Actualiza los registros de chat
            if msg.startswith('!updatelogs') and (wikibot.userrights(e.user)) and self.logger_on:
                self.th.cancel()
                c.send(self.command.update_command(e.user))
                self.updated = True

            if e.user not in userdict or e.user in userdict:
                userdict[e.user] = time.time()

            if msg.startswith('!gauss '):
                cond = e.text.replace("!gauss ", "")
                cond = cond.split(", ")
                try:
                    x = cond[0]
                    y = cond[1]
                    z = cond[2]
                    c.send(self.command.gauss_progression(int(x), int(y), int(z)))
                except IndexError or ValueError:
                    pass

            if ('https://twitter.com/' in msg) and self.twitterinfo:
                c.send(self.command.twitter_info(e.text))

            if msg.startswith('!ignore ') and (wikibot.userrights(e.user)):
                ignore_user = e.text.split(' ', 1)[1]
                if e.user == ignore_user:
                    c.send("{}: No puedes ignorarte a tí mismo (herpderp)".format(e.user))
                elif ignore_user in ignored:
                    c.send("{}: {} ya está en la lista de ignorados.".format(e.user, ignore_user))
                elif wikibot.userrights(ignore_user):
                    c.send("{}: Imposible ignorar a {} debido a que es un moderador de chat.".format(e.user, ignore_user))
                else:
                    ignored.append(ignore_user)
                    c.send("{}: {} ha sido agregado a la lista de ignorados.".format(e.user, ignore_user))

            if msg.startswith('!unignore ') and (wikibot.userrights(e.user)):
                ignore_user = e.text.split(' ', 1)[1]
                if ignore_user not in ignored:
                    c.send("{}: {} no está en la lista de ignorados.".format(e.user, ignore_user))
                else:
                    ignored.remove(ignore_user)
                    c.send("{}: {} ha sido removido de la lista de ignorados.".format(e.user, ignore_user))

            #Tell command
            if msg.startswith('!tell ') and self.tell:
                split_text = e.text.split(' ', 2)
                tell_user = split_text[1].replace('_', ' ')
                message = split_text[2]
                if tell_user == e.user:
                    c.send('{}: No puedes enviarte un mensaje a tí mismo (herpderp)'.format(e.user))
                elif tell_user == config_file['user']:
                    c.send('{}: Oc. :v'.format(e.user))
                else:
                    if tell_user in tell.keys():
                        tell[tell_user].append({'user': e.user, 'text': message})
                    else:
                        tell[tell_user] = [{'user': e.user, 'text': message}]
                    codecs.open('tell.json', 'w').write(json.dumps(tell))
                    c.send('{}: Le diré eso a {} cuando le vea en el chat.'.format(e.user, tell_user))
            
            if msg.startswith('!rps '):
                user_choice = e.text.split(' ')[1]
                print user_choice
                c.send(e.user + ": " + self.command.rock_paper_scissors(user_choice))
        else:
            pass

    def format_message(self, **kwargs):
        f = codecs.open('ChatBot.txt', 'a', encoding='utf-8')
        time = '[{}-{:02}-{:02} {:02}:{:02}:{:02}]'.format(datetime.utcnow().year, datetime.utcnow().month, datetime.utcnow().day, datetime.utcnow().hour, datetime.utcnow().minute, datetime.utcnow().second)
        if kwargs['event'] == 'join':
            f.write(time + ' ~ ' + kwargs['user'] + ' ha entrado al chat.\n')
        elif kwargs['event'] == 'leave':
            f.write(time + ' ~ ' + kwargs['user'] + ' ha salido del chat.\n')
        elif kwargs['event'] == 'message':
            f.write(time + ' <' + kwargs['user'] + '> ' + kwargs['text'] + '\n')
        elif kwargs['event'] == 'kick':
            f.write(time + '~ ' + kwargs['user'] + ' ha sido expulsado del chat por ' + kwargs['mod'] + '\n')
        elif kwargs['event'] == 'ban':
            f.write(time + ' ~ ' + kwargs['user'] + ' ha sido baneado del chat durante ' + str(kwargs['time']) + ' segundos por ' + kwargs['mod'] + '.\n')
        elif kwargs['event'] == 'unban':
            f.write(time + ' ~ ' + kwargs['user'] + ' ha sido desbaneado del chat por ' + kwargs['mod'] + '.\n')
        f.close()

    def log_thread(self):
        self.th = threading.Timer(300, self.command.update_logs)
        self.th.daemon = True
        self.th.start()

if __name__ == '__main__':
    bot = EthBot()
    bot.start()
