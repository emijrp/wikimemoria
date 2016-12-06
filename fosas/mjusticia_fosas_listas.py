#!/usr/bin/python
# -*- coding: utf-8 -*-

import pywikibot

def main():
    site = pywikibot.Site('wikimemoria', 'wikimemoria')
    overwrite = True
    ccaa = {
        "Andalucía": ["Almería", "Cádiz", "Córdoba", "Granada", "Huelva", "Jaén", "Málaga", "Sevilla"], 
        "Aragón": ["Huesca", "Teruel", "Zaragoza"], 
        "Canarias": ["Las Palmas", "Santa Cruz de Tenerife"], 
        "Cantabria": ["Cantabria"], 
        "Castilla-La Mancha": ["Albacete", "Ciudad Real", "Cuenca", "Guadalajara", "Toledo"], 
        "Castilla y León": ["Ávila", "Burgos", "León", "Palencia", "Salamanca", "Segovia", "Soria", "Valladolid", "Zamora"], 
        "Cataluña": ["Barcelona", "Girona", "Lleida", "Tarragona"], 
        "Comunidad de Madrid": ["Madrid"], 
        "Comunidad Foral de Navarra": ["Navarra"], 
        "Comunidad Valenciana": ["Alicante", "Castellón", "Valencia"], 
        "Extremadura": ["Badajoz", "Cáceres"], 
        "Galicia": ["A Coruña", "Lugo", "Ourense", "Pontevedra"], 
        "Islas Baleares": ["Baleares"], 
        "La Rioja": ["La Rioja"], 
        "País Vasco": ["Álava", "Gipuzkoa", "Vizcaya"], 
        "Principado de Asturias": ["Asturias"], 
        "Región de Murcia": ["Murcia"], 
    }
    
    for comunidad, provincias in ccaa.items():
        de = 'de'
        if comunidad == 'Islas Baleares':
            de = 'de las'
        elif comunidad in ['País Vasco', 'Principado de Asturias']:
            de = 'del'
        elif comunidad in ['Comunidad Foral de Navarra', 'Comunidad de Madrid', 'Comunidad Valenciana', 'Región de Murcia']:
            de = 'de la'
        en = 'en'
        if comunidad == 'Islas Baleares':
            en = 'en las'
        elif comunidad in ['País Vasco', 'Principado de Asturias']:
            en = 'en el'
        elif comunidad in ['Comunidad Foral de Navarra', 'Comunidad de Madrid', 'Comunidad Valenciana', 'Región de Murcia']:
            en = 'en la'
        
        if len(provincias) > 1: #ccaa no uniprovinciales
            title = "Fosas %s %s" % (en, comunidad)
            page = pywikibot.Page(site, title)
            if not page.exists() or (page.exists() and overwrite):
                page.text = "{{Lista de fosas por lugar|país=España|comunidad autónoma=%s}}" % (comunidad)
                page.save("BOT - Creando página")
            
            #redirects
            for redtitle in [
                "Lista de fosas %s %s" % (en, comunidad), 
                "Fosas %s %s" % (de, comunidad), 
                "Lista de fosas %s %s" % (de, comunidad), 
                ]:
                red = pywikibot.Page(site, redtitle)
                if not page.exists() or (page.exists() and overwrite):
                    red.text = "#REDIRECCIÓN [[%s]]" % (title)
                    red.save("BOT - Creando redirección")
            
            for provincia in provincias:
                title = "Fosas en la provincia de %s" % (provincia)
                page = pywikibot.Page(site, title)
                if not page.exists() or (page.exists() and overwrite):
                    page.text = "{{Lista de fosas por lugar|país=España|comunidad autónoma=%s|provincia=Provincia de %s}}" % (comunidad, provincia)
                    page.save("BOT - Creando página")
                
                #redirects
                for redtitle in [
                    "Lista de fosas en la provincia de %s" % (provincia), 
                    "Lista de fosas de la provincia de %s" % (provincia), 
                    "Fosas de la provincia de %s" % (provincia), 
                    ]:
                    red = pywikibot.Page(site, redtitle)
                    if not page.exists() or (page.exists() and overwrite):
                        red.text = "#REDIRECCIÓN [[%s]]" % (title)
                        red.save("BOT - Creando redirección")
        else: #ccaa uniprovinciales
            title = "Fosas %s %s" % (en, comunidad)
            page = pywikibot.Page(site, title)
            if not page.exists() or (page.exists() and overwrite):
                page.text = "{{Lista de fosas por lugar|país=España|comunidad autónoma=%s}}" % (comunidad)
                page.save("BOT - Creando página")
            
            #redirects
            for redtitle in [
                "Lista de fosas %s %s" % (en, comunidad), 
                "Fosas %s %s" % (de, comunidad), 
                "Lista de fosas %s %s" % (de, comunidad), 
                "Lista de fosas en la provincia de %s" % (provincias[0]), 
                "Lista de fosas de la provincia de %s" % (provincias[0]), 
                "Fosas en la provincia de %s" % (provincias[0]), 
                "Fosas de la provincia de %s" % (provincias[0]), 
                ]:
                red = pywikibot.Page(site, redtitle)
                if not page.exists() or (page.exists() and overwrite):
                    red.text = "#REDIRECCIÓN [[%s]]" % (title)
                    red.save("BOT - Creando redirección")

if __name__ == "__main__":
    main()
