#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import time
import youtube
import urllib2
from timer import GetInHMS, seen
import wikibot
import codecs
import twitter
import random

class command(object):
    def __init__(self, vicbot, username, password):
        self.c = vicbot
        self.username = username
        self.password = password
        wikibot.login(self.username, self.password)

    #Comando !updated. Muestra la última vez que los registros de chat fueron actualizados.
    def updated_command(self, user):
        desired_time = int(time.time() - self.c.last_updated)
        with open('ChatBot.txt') as f:
            if self.c.updated:
                return '{}: El registro del chat se ha actualizado hace {}. Actualmente contienen ~{} líneas.'.format(user, GetInHMS(desired_time, '%02d:%02d', 2), len(f.readlines()))
            else:
                return "{}: Los registros del chat no se han actualizado desde mi último inicio. El registro contiene actualmente ~{} líneas.".format(user, len(f.readlines()))

    #Comando !clearreg. Vacía el registro
    def dump_buffer_command(self):
        open('ChatBot.txt', 'w').close()
        return 'Registros vaciados'
        
    #Comando !welcome. Da la bienvenida al chat a un usuario
    def welcome_command(self, message):
        if message[8:] == '':
            return 'Error de sintaxis. La sintaxis correcta es !welcome Usuario'
        else:
            return 'Bienvenido al chat de Steven Universe Wiki, %s. Lee las [[Project:Reglas|reglas]] para evitarte problemas. Aquí tienes la [[MediaWiki:Emoticons|lista de emoticones]] y las [[Categoría:Guías|guías]].' % message[9:]

    def invoke_command(self, message):
        if message[7:] == '':
            return 'Parece que falta un argumento.'
        else:
            return '/me usa MAGIA NEGRA para invocar a %s.' % message[8:]
            
    def user_command(self, message):
        if message[8:] == '':
            return 'Parece que falta un argumento.'
        else:
            return '[[Usuario:%s]].' % message[9:]
            
            
    def wall_command(self, message):
        if message[5:] == '':
            return 'Parece que falta un argumento.'
        else:
            return '[[Muro:%s]].' % message[6:]
            
    def contributions_command(self, message):
        if message[14:] == '':
            return 'Parece que falta un argumento.'
        else:
            return '[[Especial:Contribuciones/%s]].' % message[15:]
            
    #Comando !logs. Envía un enlace a la página con los registros del chat.
    def log_command(self, user):
        return "{}: Los registros de chat se encuentran [[Category:Registros del chat|aquí]].".format(user)

    #Comando de información de YouTube. Cuando se envía un enlace de YouTube, Eth Bot responde con información del vídeo.
    def youtube_info(self, message):
        try:
            url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
            url2 = url[0]
            if ('youtube.com' in url2 and 'watch?v=' in url2) or ('youtu.be' in url2):
                yt = youtube.YouTube(url2)
                return yt.video_information
            else:
                pass
        except urllib2.HTTPError as err:
            if err.code == 404 or err.code == 403:
                pass
        except IndexError or TypeError:
            pass

    #Comando !updatelogs. Actualiza los registros de chat.
    def update_command(self, user):
        with open('ChatBot.txt') as f:
            log_file = len(f.readlines())
            self.update_logs(user)
            return '{}: [[Project:Chat/Registros/{}|Registro del chat]] actualizado (agregadas {} líneas).'.format(user, time.strftime('%d %B %Y', time.gmtime()), log_file)

    #Comando !seen. Informa la última vez que un usuario ha visto la ventana del chat
    def seen_command(self, user, message, dictionary, time):
        seen_user = message.split(' ', 1)[1]
        if seen_user in dictionary:
            seen_time = int(time - dictionary[seen_user])
            if seen_time == 0 or user == seen_user or seen_user == self.username:
                return '%s está en el chat en este momento.' % seen_user
            else:
                return seen(seen_user, seen_time)
        else:
            return "No he visto a %s desde mi último inicio." % seen_user

    #Grabar los registros en una página wiki utilizando la API de MediaWiki
    def update_logs(self, user=None):
        f = codecs.open('ChatBot.txt', 'r', encoding='utf-8')
        a = f.read()
        f.close()
        logger_page = 'Project:Chat/Registros/' + time.strftime('%d %B %Y', time.gmtime())
        if user is not None:
            summary = 'Actualizando registro del chat (Solicitado por [[Usuario:' + user + '|' + user + ']])'
        else:
            summary = 'Actualizando registro del chat'
        try:
            cut = wikibot.edit(logger_page)
            text = re.findall('(.*)\</pre\>', cut, re.DOTALL)[0]
        except:
            text = ''
        if text:
            new_text = text + a.replace('<', '&lt;').replace('>', '&gt;') + '</pre>\n[[Categoría:Registros del chat|{0}]]'.format(time.strftime('%Y %m %d', time.gmtime()))
            wikibot.save(logger_page, new_text, summary=summary)
        else:
            new_text = '<pre class="ChatLog">\n' + a.replace('<', '&lt;').replace('>', '&gt;') + '</pre>\n[[Categoría:Registros del chat|{0}]]'.format(time.strftime('%Y %m %d', time.gmtime()))
            wikibot.save(logger_page, new_text, summary=summary)

        #Limpiar el archivo de registros una vez que estos fueron grabados
        open('ChatBot.txt', 'w').close()

        self.c.updated = True
        self.c.last_updated = time.time()
        self.c.log_thread()

    #Información de Twitter. AL enviar un enlace de Twitter, Eth Bot responde con información del tweet.
    def twitter_info(self, message):
        try:
            url = re.findall('twitter\.com/(?:#!/)?[^/]+/status(?:es)?/(\d+)', message)
            URL = url[0]
            t = twitter.Twitter(URL)
            return t.tweet_info
        except urllib2.HTTPError as err:
            if err.code == 404 or err.code == 403:
                pass
        except IndexError:
            pass

    
    def tell_say(self, user, tell):
        return "{0}, {1} te ha dicho: {2}".format(user, tell['user'], tell['text'])
